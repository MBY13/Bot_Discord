#Cada reação retorna um cargo diferente para poder fazer autentificações
from discord.ext import commands

class Reactions(commands.Cog):
    """Works with Reactions"""
    
    def __init__(self, bot):
        self.bot = bot
    #Events = commands.Cog.listener()
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        print(reaction.emoji)
        if reaction.emoji == "🐬":
            role = user.guild.get_role(974080691061022730)
            await user.add_roles(role)
        elif reaction.emoji == "🥵":
            role = user.guild.get_role(974080741992435793)
            await user.add_roles(role)
            
def setup(bot):
    bot.add_cog(Reactions(bot))

