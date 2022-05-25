from discord.ext import commands

class Smarts(commands.Cog):
    """work with Smarts"""
    
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='calcular', help = "Calcula uma expressão (Precisa passar uma expressão como argumento)")
    async def calculate_expression(self, ctx, *expression):#Sempre deve colocar o ctx antes dde qualquer parametro * significa que você vai passar varios argumentos
        expression = "".join(expression)#join transforma um tupla("a","a","a") em uma unica string
        response = eval(expression)# pega o valor do que você passar independente se passar string ou não tomar muito cuidado para utilizar 

        await ctx.send("A resposta é: " + str(response))#trazer o valor na tela


def setup(bot):
    bot.add_cog(Smarts(bot))

