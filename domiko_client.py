import os
import discord
#  http://discordpy.readthedocs.io/en/latest/

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


async def test_speech(c):
    for v in c.voice_clients:
        if v.channel.id == VOICE_CHATROOM_ID:
            print('player started')
            player = v.create_ffmpeg_player('audios/tes.mp3')
            player.start()
            print('player finished')


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content == ("voice/test"):
        test_speech(client)
        
client.run(DISCORD_TOKEN)