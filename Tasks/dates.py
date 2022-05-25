from discord.ext import commands,tasks
import datetime

class Dates(commands.Cog):
    """Work with Dates"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.current_time.start()
    
    @tasks.loop(hours=1)#a cada 1h o bot manda uma mensagem de quando entrou no canal
    async def current_time(self):
        now = datetime.datetime.now()

        now = now.strftime("%d/%m/%Y  ás %H:%M:%S")

        channel = self.bot.get_channel(938217194213478402)

        await channel.send("Data atual: " + now )



def setup(bot):
    bot.add_cog(Dates(bot))

