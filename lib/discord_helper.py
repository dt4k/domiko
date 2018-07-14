import os
from lib import audio

class DiscordHelper(object):
    def __init__(self, client, roomid):
        self._client = client
        self._roomid = roomid

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

    async def handle_message(self, message):
        if message.author.bot:
            return

        if message.content == ("test"):
            await self.speech('テストです')

        if message.content.startswith("say "):
            text = message.content.split(' ')[-1]
            await self.speech(text)



