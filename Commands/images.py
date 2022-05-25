# aqui colocamos reports com imagens e tudo mais para ter algo "Bonito" para o usuario
from discord.ext import commands
import discord

class Images(commands.Cog):
    """Work with Images"""
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = "foto",help= "Traz uma foto com um formato de report na sala" )
    async def get_random_image(self, ctx):
        url_image = "https://picsum.photos/1920/1080"

        embed = discord.Embed(
            title = "Resultado da Busca",
            description = "PS: A busca é totalmente aleatória",
            color = 0x0000FF
        )
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.set_footer(text="Feito por " + self.bot.user.name, icon_url=self.bot.user.avatar_url)

        embed.add_field(name="API", value="Usamos a API do https://picsum.photos")
        embed.add_field(name="Parâmetros", value="{largura}/{altura}")

        embed.add_field(name="Exemplo", value=url_image, inline=False)

        embed.set_image(url=url_image)

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Images(bot))

