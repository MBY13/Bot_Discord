from discord.ext import commands,tasks
from decouple import config
import os

bot = commands.Bot("!") # Definimos o que o usuario deve digitar pra chamar um evento no bot

def load_cogs(bot):#aqui temos um maneira de exercutar o codigo que esta nas pastas para ficar mais organizado quando for fazer a manutenção
    bot.load_extension("manager")
    bot.load_extension("Tasks.dates")
    for file in os.listdir("Commands"):
        if file.endswith(".py"):
            cog = file[:-3:]
            bot.load_extension(f"Commands.{cog}")
load_cogs(bot)

TOKEN = config("TOKEN")
bot.run(TOKEN) #URL do vinculo discord com o bot 