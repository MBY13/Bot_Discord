#Aqui utilizamos uma api para fazer uma consulta de moedas
from discord.ext import commands
import requests

class Cryptos(commands.Cog):
    """Work with Cryptos"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help = "Traz o valor de uma moeda sobre a outra (Precisa passar 3 Caracteres de cada tipo de moeda pesquisada Exemplo: EUR BRL)")# se deixar vazio pega o nome do def
    async def binance(self,ctx, coin, base):
        try:
            response = requests.get(f"https://economia.awesomeapi.com.br/all/{coin.upper()}-{base.upper()}")
            
            data = response.json()
            price = data[coin.upper()]['bid']
            
            if price:
                await ctx.send(f"O valor do par {coin}/{base} é {price}")
            else:
                await ctx.send(f"O par {coin}/{base} é inválido")
        except:
            await ctx.send(f"Ops... Ocorreu um erro")

        # https://economia.awesomeapi.com.br/all/Moeda que quero a conversão (1 dolar) - em relação a essa (quantos reais)

def setup(bot):
    bot.add_cog(Cryptos(bot))

