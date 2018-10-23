import discord
from discord.ext import commands
import random
class BAfun():

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="8ball")
    async def _ball(self, ctx, *, question):
            ': Ask me a question'
            question = question
            answers = random.randint(1, 20)

            if question == "":
                return

            elif answers == 1:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` It is certain```""")

            elif answers == 2:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  It is decidedly so```""")

            elif answers == 3:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Without a doubt```""")

            elif answers == 4:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` Yes definitely```""")

            elif answers == 5:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  You may rely on it```""")

            elif answers == 6:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  As i see it, yes```""")

            elif answers == 7:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Most likely```""")

            elif answers == 8:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Outlook good```""")

            elif answers == 9:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Yes```""")

            elif answers == 10:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Signs point to yes```""")

            elif answers == 11:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Reply hazy try again```""")

            elif answers == 12:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Ask again later```""")

            elif answers == 13:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Better not to tell you now```""")

            elif answers == 14:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}``` Cannot predict now```""")

            elif answers == 15:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Concentrate and ask again```""")

            elif answers == 16:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Don't count on it```""")

            elif answers == 17:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  My reply is no```""")

            elif answers == 18:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  My sources say no```""")

            elif answers == 19:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Outlook not so good```""")

            elif answers == 20:
                await ctx.send(f"""\U0001f3b1 Question by {ctx.author.name}: {question}```  Very doubtful```""")


    @commands.command(name="pepe")
    async def pepe(,selfctx, user: discord.Member = None):
        """kiss someone!"""
        user = user or ctx.message.author

        pepe = "**  kissed you.{1}!**"

        choices = ["http://i.imgur.com/vpIyEue.png",
                   "http://i.imgur.com/0koMC0v.jpg",
                   "http://i.imgur.com/9Q6KMZa.png",
                   "http://i.imgur.com/54xy6jr.png",
                   "http://i.imgur.com/QvCngiJ.jpg",
                   "http://i.imgur.com/ftWgrOE.jpg",
                   "http://i.imgur.com/rhDSqRv.jpg",
                   "http://i.imgur.com/89NZ3zM.jpg",
                   "http://i.imgur.com/I4cIH5b.png",
                   "http://i.imgur.com/GIFc4uX.png",
                   "http://i.imgur.com/bgShJpZ.png",
                   "http://i.imgur.com/jpfPLyn.png",
                   "http://i.imgur.com/pZeYoej.png",
                   "http://i.imgur.com/M8V9WKB.jpg",
                   "http://i.imgur.com/ZBzHxNk.jpg",
                   "http://i.imgur.com/xTyJ6xa.png",
                   "http://i.imgur.com/TOozxRQ.png",
                   "http://i.imgur.com/Eli5HdZ.png",
                   "http://i.imgur.com/pkikqcA.jpg",
                   "http://i.imgur.com/gMF8eo5.png",
                   "http://i.imgur.com/HYh8BUm.jpg",
                   "http://i.imgur.com/ZGVrRye.jpg",
                   "http://i.imgur.com/Au4F1px.jpg",
                   "http://i.imgur.com/gh36k9y.jpg",
                   "http://i.imgur.com/MHDoRuN.png",
                   "http://i.imgur.com/V3MJfyK.png",
                   "http://i.imgur.com/QGGTipc.jpg",
                   "http://i.imgur.com/PRFrTgz.png",
                   "http://i.imgur.com/9UBJrwM.jpg",
                   "http://i.imgur.com/WQY9Vhb.jpg",
                   "http://i.imgur.com/sIbQdou.jpg",
                   "http://i.imgur.com/LlUMg00.jpg",
                   "http://i.imgur.com/MmijlWa.png",
                   "http://i.imgur.com/i0CrtrX.png",
                   "http://i.imgur.com/Dfpudwp.jpg",
                   "http://i.imgur.com/hhg0wVF.gif",
                   "http://i.imgur.com/7VDiIHN.jpg",
                   "http://i.imgur.com/nxvXpNV.jpg",
                   "http://i.imgur.com/DZYEjrW.gif",
                   "http://i.imgur.com/mnyQ0Rh.jpg",
                   "http://i.imgur.com/aHawbbs.jpg",
                   "http://i.imgur.com/g8cCHV7.jpg",
                   "http://i.imgur.com/E2cMU7Y.jpg",
                   "http://i.imgur.com/PkmcgGF.jpg",
                   "http://i.imgur.com/7qLQ1xl.jpg",
                   "http://i.imgur.com/7qLQ1xl.jpg",
                   "http://i.imgur.com/arSsPwf.png",
                   "http://i.imgur.com/xcYh4iC.png",
                   "http://i.imgur.com/9692WND.jpg",
                   "http://i.imgur.com/diAK5Nu.jpg",
                   "http://i.imgur.com/zDs0tRW.jpg",
                   "http://i.imgur.com/PEM87nV.jpg",
                   "http://i.imgur.com/zlCzlND.jpg",
                   "http://i.imgur.com/n0OHxDl.jpg",
                   "http://i.imgur.com/TQRf1WH.png",
                   "http://i.imgur.com/zi9ad15.jpg",
                   "http://i.imgur.com/b8A6Qke.jpg",
                   "http://i.imgur.com/YuLapEu.png",
                   "http://i.imgur.com/fWFXkY1.jpg",
                   "http://i.imgur.com/i5vNvWU.png",
                   "http://i.imgur.com/oXwUwtJ.jpg",
                   "http://i.imgur.com/hadm4jV.jpg",
                   "http://i.imgur.com/gbCvkqo.png",
                   "http://i.imgur.com/wDiiWBG.jpg",
                   "http://i.imgur.com/Mvghx4V.jpg",
                   "http://i.imgur.com/SnTAjiJ.jpg",
                   "http://i.imgur.com/QvMYBnu.png",
                   "http://i.imgur.com/WkzPvfB.jpg",
                   "http://i.imgur.com/PfAm4ot.png",
                   "http://i.imgur.com/SIk4a45.png",
                   "http://i.imgur.com/aISFmQq.jpg",
                   "http://i.imgur.com/sMQkToE.png",
                   "http://i.imgur.com/7i3cBrP.png",
                   "http://i.imgur.com/1oMSz6e.png",
                   "http://i.imgur.com/nVCRnRv.png",
                   "http://i.imgur.com/FzWmxmi.jpg",
                   "http://i.imgur.com/rpUI20F.jpg",
                   "http://i.imgur.com/FDmnFDZ.jpg",
                   "http://i.imgur.com/40Z1Yyg.jpg",
                   "http://i.imgur.com/osy5Nu4.png",
                   "http://i.imgur.com/4w81MSS.jpg",
                   "http://i.imgur.com/qRXQFYa.png",
                   "http://i.imgur.com/A1af62j.jpg",
                   "http://i.imgur.com/wOc6fUe.jpg",
                   "http://i.imgur.com/Z6ILiJ4.jpg",
                   "http://i.imgur.com/537UpEJ.jpg",
                   "http://i.imgur.com/HDc6kko.png",
                   "http://i.imgur.com/oyLpuXq.jpg",
                   "http://i.imgur.com/iCmGtJS.jpg",
                   "http://i.imgur.com/MjpnlQm.png",
                   "http://i.imgur.com/c6MWRQ9.jpg"]


        image = random.choice(choices)

        embed = discord.Embed(description=f"""{user.name}""", colour=discord.Colour(0xba4b5b))
        embed.add_field(name=' Random', value=f''' ~~pepe~~''', inline=False)
        embed.set_image(url=image)


        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(BAfun(bot))