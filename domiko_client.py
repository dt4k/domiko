import os
import discord 
#  http://discordpy.readthedocs.io/en/latest/
from lib import audio


client = discord.Client()
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
VOICE_CHATROOM_ID = os.environ['VOICE_CHATROOM_ID']

async def join_voice_channel(channel_id):
    print('joined to %s' % channel_id)
    voice = await client.join_voice_channel(client.get_channel(channel_id))
    return voice

@client.event
async def on_ready():
    print('Process is launched. Logged in as %s(%s)' %(client.user.name, client.user.id))
    await join_voice_channel(VOICE_CHATROOM_ID)
    await test_speech(client)


async def test_speech(c, text='こんにちは!'):
    for v in c.voice_clients:
        if v.channel.id == VOICE_CHATROOM_ID:
            print('player started')
            fpath = audio.generate_wav(text)
            print(text)

            player = v.create_ffmpeg_player(fpath, after=lambda : os.remove(fpath))
            player.start()
            print('player finished')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == ("test"):
        await test_speech(client)

    if message.content.startswith("say "):
        text = message.content.split(' ')[-1]
        await test_speech(client, text)

client.run(DISCORD_TOKEN)