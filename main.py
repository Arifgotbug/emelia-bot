from heart import start_beating

import os 
import platform 
import random 
import sys 
import discord 
from discord.ext import tasks 
from discord.ext.commands import Bot 
from discord_slash import SlashCommand, SlashContext

token = 
intents = discord.Intents.default()
prefix = ".e"
bot = Bot(command_prefix=prefix, intents=intents)
slash = SlashCommand(bot, sync_commands=True)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}")
    print(f"Running on: {platform.system()} {platform.release} ({os.name})")
    print("-----------------------------")
    status_task.start()

@tasks.loop(seconds=5)
async def status_task():
    st = ["Watching this Server!", "with Shrimp", f"{prefix}help"]
    await bot.change_presence(activity=discord.Game(random.choice(st)))

bot.remove_command("help")

if __name__ == "__main__":
    for file in os.listdir("./cogs"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                bot.load_extension(f"cogs.{extension}")
                print(f"Loaded extension \'{extension}\'")
            except Exception as e:
                exception = f"{type(e).__name__} : {e}"

                print(f"Failed to load Extension {extension}")
                print(f"Problem: {exception}")

@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return 
    await bot.process_commands(message)

@bot.event 
async def on_slash_command(ctx: SlashContext):
    fullCommandName = ctx.name 
    split = fullCommandName.split(" ")
    executeCommand = str(split[0])
    print(f"Excecuted {executeCommand} command in {ctx.guild.name} (ID:{ctx.guild.id}) by {ctx.author} (ID: {ctx.author.id})")


@bot.event
async def on_command_error(context, error):
    raise error 
start_beating()
bot.run(token)