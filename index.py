import discord
from discord.ext import commands
from datetime import timedelta
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

intents.members = True 

brainrot = ["skibidi", "gyatt", "sigma", "rizz", "mangos", "mango", "lunchly", "thick of it", "prime", "phonk", "aura", "tuff", "fein", "fe!n", "skibid", "skbidi", "skbid", "toilet", "noradrenaline", "alvin", "💀","bomboclat","gyat","packgod"]


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if any(word in message.content.lower() for word in brainrot):
        print("brainrotted")
        
        duration = timedelta(minutes=5)

        try:
            await message.author.edit(timed_out_until=discord.utils.utcnow() + duration)
            print(brainrot)
            await message.channel.send(
                f"'{message.content}' <@{message.author.id}> Terminated"
            )
        except discord.Forbidden:
            await message.channel.send("I do not have permission to timeout this user.")
        except discord.HTTPException as e:
            await message.channel.send(f"An error occurred: {e}")
client.run('token here')