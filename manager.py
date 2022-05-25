from typing_extensions import Self
from discord.ext import commands
from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound

class Manager(commands.Cog):
    """Manager the bot"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()#So entra quando o bot estiver realmente pronto   
    async def on_ready(self):
        print(f"Vamo nessa! Estou conectado como {self.bot.user}")

    @commands.Cog.listener()# sempre que a pessoa falar 'palavrão'  o bot vai falar para ele para com isso e excluir a mensagem
    async def on_message(self,message):
        if message.author == self.bot.user:
            return
        
        if "palavrão" in message.content:
            await message.channel.send(f"Por favor, {message.author.name}, não ofenda os demais usuários!")
            await message.delete()
    
    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error,MissingRequiredArgument):
            await ctx.send("Favor enviar todos os argumentos. Digite !help para ver os parâmetros de cada comando.")
        if isinstance(error,CommandNotFound):
            await ctx.send("O comando não existe. Digite help para ver todos os comandos.")
        else:
            raise error

def setup(bot):
    bot.add_cog(Manager(bot))

