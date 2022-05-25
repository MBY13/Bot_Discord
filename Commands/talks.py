#Arquivo de conversa com o usuario
from discord.ext import commands
import discord

class Talks(commands.Cog):
    """ Talks with user"""
    
    def __init__(self, bot):
        self.bot = bot
    
    #bot.command = commands.command
    @commands.command(name='oi', help = "Envia um oi (Não precisa de argumentos)")# primeiro comando, sempre que digitar !oi vai acontecer alguma coisa
    async def send_hello(self, ctx):
        name = ctx.author.name
        response = "Olá, Fui criado em python pelo " + name

        await ctx.send(response)

    @commands.command(name = "Segredo", help = "Envia um segredo no privado")
    async def secret(self, ctx):
        try:
            await ctx.author.send("Testando mensagens com o await")
            await ctx.author.send("Aqui vai ir somente para o autor")

        except discord.errors.Forbidden:
            await ctx.send("Não posso contar o segredo")


def setup(bot):
    bot.add_cog(Talks(bot))

