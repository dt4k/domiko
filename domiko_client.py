import os
import discord
#  http://discordpy.readthedocs.io/en/latest/
from lib import discord_helper

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
VOICE_CHATROOM_ID = os.environ['VOICE_CHATROOM_ID']

client = discord.Client()
helper = discord_helper.DiscordHelper(client, VOICE_CHATROOM_ID)

@client.event
async def on_ready():
    print('Process is launched. Logged in as %s(%s)' %
          (client.user.name, client.user.id))

    # join to the voice channel
    await client.join_voice_channel(client.get_channel(VOICE_CHATROOM_ID))
    print('joined to %s' % VOICE_CHATROOM_ID)
    await helper.speech('こんにちは！')


@client.event
async def on_message(message):
    await helper.handle_message(message)

client.run(DISCORD_TOKEN)
