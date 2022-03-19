import discord
from config import Config
config = Config()
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

def count_messages(message):
    print('Add message to author id')
    # print(message.author.name)
    # print('{}---{}'.format(message.author.id,'-------------------'))
    # print('Add message to guild id')
    # print(message.guild.name)
    # print('{}---{}'.format(message.guild.id,'-------------------'))
    ## Global:
    # db.add(`globalMessages_${message.author.id}`, 1)
    ## Guild:
    # db.add(`guildMessages_${message.guild.id}_${message.author.id}`);

def handle_thread(message):
    print(message.content)

async def get_all_users_by_role(role):
    print(role)

@client.event
async def on_message(message):
    count_messages(message)
    handle_thread(message)

    channel = client.get_channel(int(config.WELCOME_CHANNEL_ID))
    for thread in channel.threads:
        async for msg in thread.history():
            print(msg.content)

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(config.BOT_TOKEN)