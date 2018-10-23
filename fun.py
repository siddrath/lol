import discord
from discord.ext import commands
import random
class BAfun():

    def __init__(self, bot):
        self.bot = bot
        
        
     @commands.command()
     async def neko(ctx):
         ''''sends cute dog pics'''
         r = requests.get("https://nekos.life/api/neko").json()

         colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
         col = int(random.random() * len(colours))
         content = [":neko: Don't be sad! This neko wants to play with you!", "You seem lonely, {0.mention}. Here, have a neko. They're not as nice , but enjoy!".format(ctx.message.author), "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait its neko."]
         con = int(random.random() * len(content))
         embed=discord.Embed()
         embed.set_image(url=r["neko"])
         await ctx.send(content=content[con],embed=embed)   
        
        
        
        
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
          
    
    

def setup(bot):
    bot.add_cog(BAfun(bot))
