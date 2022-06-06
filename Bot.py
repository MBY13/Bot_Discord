from discord.ext import commands
from decouple import config # comentato linha 16 para fazer o teste com variaveis ambiente no linux 
import token_secret

bot = commands.Bot("!") # Definimos o que o usuario deve digitar pra chamar um evento no bot

def load_cogs(bot):#aqui temos um maneira de exercutar o codigo que esta nas pastas para ficar mais organizado quando for fazer a manutenção
    bot.load_extension("manager")
    bot.load_extension("Tasks.dates")
    bot.load_extension("Commands.cryptos")
    bot.load_extension("Commands.images")
    bot.load_extension("Commands.reactions")
    bot.load_extension("Commands.smarts")
    bot.load_extension("Commands.talks")
load_cogs(bot)

TOKEN = token_secret.get_secret()
bot.run(TOKEN) #URL do vinculo discord com o bot 

#!segredo