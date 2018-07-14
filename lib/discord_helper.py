import os
import time
import asyncio
from lib import audio, game_client

class DiscordHelper(object):
    def __init__(self, client, roomid):
        self._client = client
        self._roomid = roomid
        self.game = game_client.GameClient()

    async def speech(self,text):
        for v in self._client.voice_clients:
            if v.channel.id == self._roomid:
                print('player started')
                fpath = audio.generate_wav(text)
                print(text)

                player = v.create_ffmpeg_player(
                    fpath, after=lambda: os.remove(fpath))
                player.start()
                print('player finished')

    def _parse_timer(self, timer):
        t = time.strptime(timer, '%M:%S')
        m = t.tm_min
        s = t.tm_sec
        if m < 1:
            return '%d秒' % s
        else:
            return '%d分%d秒' % (m, s)



    async def sitrep(self, message):
        timer = await self.game.timer()
        red_score = await self.game.red_score()
        yellow_score = await self.game.yellow_score()
        text = "残り時間は，{}。レッドチームは{}点，イエロチームは{}点です。".format(self._parse_timer(timer), red_score, yellow_score)

        await self._client.send_message(message.channel, text)
        await self.speech(text)

    async def game_start(self, message):
        # TODO: fix these messy synchronous procedure
        await self.speech('ゲームを開始します。開始5秒前')
        await asyncio.sleep(3)
        await self.speech('5')
        await asyncio.sleep(1)
        await self.speech('4')
        await asyncio.sleep(1)
        await self.speech('3')
        await asyncio.sleep(1)
        await self.speech('2')
        await asyncio.sleep(1)
        await self.speech('1')
        await asyncio.sleep(1)
        await self.speech('ゲームスタート!')
        await self._client.send_message(message.channel, 'ゲームスタート!')
        return await self.game.start()


    async def handle_message(self, message):
        if message.author.bot:
            return

        # debug command
        if message.content.startswith("say "):
            text = message.content.split(' ')[-1]
            await self.speech(text)

        elif message.content.startswith("command "):
            command = message.content.split(' ')[-1]
            if command == 'start':
                await self.game_start(message)
            elif command == 'pause':
                text = 'ゲームを中断します'
                await self.speech(text)
                await self._client.send_message(message.channel, text)
                await asyncio.sleep(3)
                return await self.game.pause()
            elif command == 'reset':
                text = 'ゲームをリセットします'
                await self.speech(text)
                await self._client.send_message(message.channel, text)
                await asyncio.sleep(3)
                return await self.game.reset()
            elif command == 'sitrep':
                await self.sitrep(message)
            else:
                print('unknown command given: %s' % command)
