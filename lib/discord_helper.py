import os
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

    async def sitrep(self):
        timer = await self.game.timer()
        red_score = await self.game.red_score()
        yellow_score = await self.game.yellow_score()
        text = "残り時間{}。レッドチームは{}点，イエロチームは{}点です。".format(timer, red_score, yellow_score)
        await self.speech(text)

    async def handle_message(self, message):
        if message.author.bot:
            return

        # debug command
        if message.content.startswith("say "):
            text = message.content.split(' ')[-1]
            await self.speech(text)

        elif message.content.startswith("command "):
            cmd = message.content.split(' ')[-1]
            commands = {
                'start': self.game.start,
                'pause': self.game.pause,
                'reset': self.game.reset,
                'sitrep': self.sitrep
             }
            if cmd in commands:
                return await commands[cmd]()
            else:
                print('unknown command given: %s' % cmd)

