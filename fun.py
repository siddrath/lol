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
        
        
        
        
   
    

def setup(bot):
    bot.add_cog(BAfun(bot))
