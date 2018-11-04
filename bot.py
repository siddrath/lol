import discord
import aiohttp
import datetime
import inspect
import os
import io
import re
import asyncio
import random
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import psutil
import json



bot = commands.Bot(description='BAsics can do a lot more.....', command_prefix=commands.when_mentioned_or('p?'))


class BAsics():

    @commands.command()
    async def owner(self, ctx):
        ': Name of my creator'
        await ctx.send('My owner is <@411496838550781972> ')
        await ctx.message.delete()

    @commands.command()
    async def ping(self, ctx):
        ': Check your connection '
        t1 = ctx.message.created_at
        m = await ctx.send('**Pong!**')
        time = (m.created_at - t1).total_seconds() * 1000
        await m.edit(content='**Pong! Took: {}ms**'.format(int(time)))
        await ctx.message.delete()

    @commands.command(pass_contex=True)
    async def invite(self, ctx):
        ': Invite me '
        await ctx.send('https://discordapp.com/oauth2/authorize?client_id=486093523024609292&scope=bot&permissions=2146958591')

    @commands.command()
    async def uptime(self,ctx):
        res = os.popen("uptime").read()
        matches = re.findall(r"up (\d+) days, (\d+):(\d+)", res)
        time = matches[0]
        fmtime = "{0[0]} days, {0[1]} hours {0[2]} minutes".format(time)
        await ctx.send(f'''```py\n{fmtime}```''')

    @commands.command()
    async def serverinfo(self, ctx):
        ': Get the server info'
        guild = ctx.guild
        embed = discord.Embed(title=f'''{guild}''', colour=discord.Colour.dark_purple(), description='More Info Below', timestamp=datetime.datetime.utcnow())
        embed.set_thumbnail(url=f'''{guild.icon_url}''')
        embed.add_field(name='Server Created At :', value=f'''  {guild.created_at}''', inline=False)
        embed.add_field(name='Created by :', value=f'''{guild.owner.mention}''', inline=False)
        embed.add_field(name='Region :', value=f'''  {guild.region}''', inline=False)
        embed.add_field(name='Server ID :', value=f'''{guild.id}''', inline=False)
        embed.add_field(name='Server Members :', value=f'''  {len(guild.members)}''', inline=False)
        embed.add_field(name='Online Members :',
                        value=f'''{len([I for I in guild.members if I.status is discord.Status.online])}''',inline=False)
        embed.add_field(name='Server Channel :', value=f'''  {len(guild.channels)}''', inline=False)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def avatar(self, ctx, user: discord.Member = None):
        """: Check AVATARS"""
        user = user or ctx.message.author
        embed = discord.Embed(title=f'''{user.name}'s Avatar''', description=f'''{user.name} looks like.....''',color=discord.Colour.dark_purple())
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def count(self, ctx):
        ''': Get the info about my servers'''
        total = sum(1 for m in set(ctx.bot.get_all_members()) if m.status != discord.Status.offline)
        embed = discord.Embed(title=f'''Count''', colour=discord.Colour.dark_purple(),description=f'''I am in **{len(bot.guilds)}** servers \nI am used by **{len(bot.users)}** users \nI am currently entertaining **{total}** users''')

        embed.set_thumbnail(url=f'''{bot.user.avatar_url}''')
        await ctx.send(embed=embed)

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        ''': See your profile'''
        member = member or ctx.message.author
        x = Image.open("pngs/FBI.png")
        x.load()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(member.avatar_url_as(format='png')) as r:
                b = io.BytesIO(await r.read())
        x1 = Image.open(b)
        x1.load()
        font_type = ImageFont.truetype('arialbd.ttf', 15)
        font_type1 = ImageFont.truetype('arialbd.ttf', 14)
        draw = ImageDraw.Draw(x)
        x.paste(x1.resize((75, 75)), (195, 55))
        draw.text(xy=(80, 166), text=member.name, fill=(0, 0, 0), font=font_type)
        draw.text(xy=(75, 204), text=ctx.guild.name, fill=(0, 0, 0), font=font_type1)
        draw.text(xy=(68, 223), text=member.top_role.name, fill=(0, 0, 0), font=font_type1)
        x.save("profile.png")
        await ctx.send(file=discord.File("profile.png"))
        os.system("rm profile.png")

    @commands.command()
    async def wanted(self, ctx, member: discord.Member = None):
        ''': Hunt someone'''
        member = member or ctx.message.author
        x = Image.open("pngs/Wanted.png")
        x.load()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(member.avatar_url_as(format='png')) as r:
                b = io.BytesIO(await r.read())
        x1 = Image.open(b)
        x3 = x.resize((400, 600))
        x3.paste(x1.resize((300, 250)), (50, 160))
        x3.save("wanted.png")
        await ctx.send(file=discord.File("wanted.png"))
        os.system("rm wanted.png")

    @commands.command()
    async def shit(self,ctx, member: discord.Member):
        ''': Show em how shitty they are'''
        x = Image.open("pngs/shit.png")
        async with aiohttp.ClientSession() as cs:
            async with cs.get(member.avatar_url_as(format='png')) as r:
                b = io.BytesIO(await r.read())
        # open the pic and give it an alpha channel so it's transparent
        im1 = Image.open(b).convert('RGBA')
        im4 = im1.resize((120, 200))
        # rotate it and expand it's canvas so the corners don't get cut off:
        im2 = im4.rotate(-45, expand=1)

        # note the second appearance of im2, that's necessary to paste without a bg
        x.paste(im2, (200, 655), im2)
        x.save("SHIT.png")
        await ctx.send(file=discord.File("SHIT.png"))
        os.system("rm SHIT.png")



class BAmath():

    @commands.command()
    async def fact(self, ctx, num: int):
        ': Get factorial of any number '
        if num < 0:
            await ctx.send('Sorry, factorial does not exist for negative numbers')
        elif num == 0:
            await ctx.send('The factorial of 0 is 1')
        else:
            from math import factorial
            await ctx.send(f'''The factorial of {num} is : ```{factorial(num)}```''')
    @commands.command()
    async def add(self, ctx, num: int, num2: int):
        ': Add two numbers'
        await ctx.send(num + num2)

    @commands.command()
    async def factor(self, ctx, num: int):
        ': Find prime factors '
        await ctx.send('Factors are:')
        i = 1
        while i <= num:
            k = 0
            if (num % i) == 0:
                j = 1
                while j <= i:
                    if (i % j) == 0:
                        k = k + 1
                    j = j + 1
                if k == 2:
                    await ctx.send('`1`')
                    await ctx.send(f'''`{i}`''')
            i = i + 1


class BAdmin():

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason):
        ': Kick the member if you have authority '
        if ctx.author.permissions_in(ctx.channel).kick_members:
            if reason is None:
                await member.send(f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
                em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                                description=f'''{member} has been kicked''', timestamp= datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culpret', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for kicking', value=f'''_No reason provided_''', inline=False)
                await ctx.send(embed=em)
                await member.kick()
            else:
                await member.send(f'''You have been kicked by {ctx.author.name} from {ctx.guild.name} due to {reason} ''')
                em = discord.Embed(title='Kicked', colour=discord.Colour.dark_red(),
                                   description=f'''{member} has been kicked''', timestamp=datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for kicking', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
                await member.kick()
        else:
            message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after= 3)
            await message.add_reaction('\u2623')

    @commands.command()
    async def perms(self, ctx, user: discord.Member = None):
        ': Find what you can do on this server'
        user = ctx.message.author if user is None else user
        if not user:
            user = ctx.author
        mess = []
        for i in user.guild_permissions:
            if i[1]:
                mess.append("\u2705 {}".format(i[0]))
            else:
                mess.append("\u274C {}".format(i[0]))
        embed = discord.Embed(title = f'''{user.name} 's permissions in the server are: ''',description ="\n".join(mess), color = discord.Colour.dark_purple())
        await ctx.send(embed=embed)

    @commands.command()
    async def purge(self, ctx, limit: int):
        ': Delete messages'
        if ctx.author.permissions_in(ctx.channel).manage_messages:
            await ctx.channel.purge(limit=limit)
            await ctx.send(f'''Deleted {limit} message(s)''')
        else:
            return

    @commands.command()
    async def prune(self, ctx, days: int):
        ': Prune the inactive members'
        if ctx.author.permissions_in(ctx.channel).ban_members:
         await ctx.guild.prune_members(days=days)
        else:
            await ctx.send(f'''{ctx.author.mention} you are not Eligible for this''',delete_after = 3)

    @commands.command()
    async def estimatedprune(self, ctx, days: int):
        ': Estimate the inactive members to prune'
        await ctx.send(await ctx.guild.estimate_pruned_members(days=days))

    @commands.command()
    async def warn(self, ctx, member: discord.Member , *, reason = None):
        ''': SoftWarn a person'''
        if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
            if reason is None:
                await ctx.send(f'''{ctx.author.mention} \n ```A reason needed to warn``` ''')
            else:
                embed = discord.Embed(title='Warning', colour=discord.Colour.gold(),
                                      description =f'''You have been warned by {ctx.author.name} for {reason}''', timestamp=datetime.datetime.utcnow())
                await member.send(embed=embed)
                em = discord.Embed(title='Warned', colour=discord.Colour.gold(),
                                   description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow())
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
        else:
            await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after= 3)

    @commands.command()
    async def swarn(self, ctx, member: discord.Member , *, reason = None):
        ': Warn a person seriously'
        if ctx.author.permissions_in(ctx.channel).kick_members or ctx.author.permissions_in(ctx.channel).manage_messages:
            if reason is None:
                await ctx.send(f'''{ctx.author.mention} \n ```A serious reason needed to warn``` ''')
            else:
                embed = discord.Embed(title='Warning', colour=discord.Colour.red(),
                                      description=f'''You have been warned by {ctx.author.name} for {reason}''', timestamp=datetime.datetime.utcnow())
                await member.send(embed=embed)
                em = discord.Embed(title= 'Seriously Warned', colour= discord.Colour.red(),
                                   description=f'''{member} has been warned''', timestamp=datetime.datetime.utcnow() )
                em.set_thumbnail(url=member.avatar_url)
                em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
                em.add_field(name='Culprit', value=f'''{member}''', inline=False)
                em.add_field(name='Reason for warning', value=f'''{reason}''', inline=False)
                await ctx.send(embed=em)
        else:
            await ctx.send(f'''{ctx.author.mention} you aren't eligible for this''', delete_after=3)
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)
async def botinfo(ctx):
    embed = discord.Embed(title="Team Rocket", description="Bot information", color=0xeee657)

    # give info about you here
    embed.add_field(name="isse#2508", value="Developer", inline=False)

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")

    embed.add_field(name="User Count", value=f"{len(bot.users)}")

    embed.add_field(name="Discord Version", value=discord.__version__)
    mem = psutil.virtual_memory()
    cmem = (mem.available/10000000000)

    embed.add_field(name="CPU Statistics", value=f"\nCPU Count **{psutil.cpu_count()}**\nRAM **{cmem} GB**")
    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="[Invite Me](https://discordapp.com/oauth2/authorize?client_id=486093523024609292&scope=bot&permissions=2146958591)")

    await ctx.send(embed=embed)
    
@bot.command()
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

           

@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.message.delete()

    return await ctx.send(mesg)

@bot.command(name="start")
@commands.cooldown(1, 3, commands.BucketType.user)
async def start_journey(ctx):
    embed = discord.Embed(title="Select a Starter!", description="Choose any of the Starters!", color=0xffb6c1)
    embed.add_field(name="...", value="You've been hypnotized by pokemons, and instead of the normal starters, you are forced to pick between \n-Flowin, the Grass type fakemon, \n-Flire the fire type fakemon and \n-Aquino, the water type.")
    embed.set_thumbnail(url="https://i.pinimg.com/736x/22/b9/59/22b959c3650bed0fff0decef732371c0--pokemon-tattoo-pokemon-special.jpg")
    embed.set_image(url="https://oyster.ignimgs.com/wordpress/stg.ign.com/2013/01/Pokemon-G3-610x325.jpg")
    embed.add_field(name="__React__ to Pick a Starter!", value="...")
    start_msg = await ctx.send(embed=embed)



@bot.command(hidden = True)
async def code(ctx, command):
        ''': getting the code for command'''

        a = inspect.getsource(bot.get_command(command).callback)
        embed = discord.Embed(title='Code', description="```py\n"+a+"```",color=discord.Colour.dark_purple())
        embed.set_thumbnail(url='https://scontent.fdel3-1.fna.fbcdn.net/v/t1.0-9/20155639_1952222755056855_6450365686627691750_n.png?oh=0b2c4ecd1409396b05f71c31dd07dd2d&oe=5AE7B998')
        await ctx.send(embed=embed)


@bot.command(hidden=True)
async def reload(ctx, extension):
    if ctx.author.id == 411496838550781972:
       try:
            bot.unload_extension(extension)
            bot.load_extension(extension)
            embed = discord.Embed(title="Reload", description=f'''Reloaded {extension}''',
                                  color=discord.Colour.dark_purple())
            await ctx.send(embed=embed)
       except ModuleNotFoundError:
            await ctx.send("```No such extention exists```")
    else:
        await ctx.send("```You can't do it buddy you better know it```")
        
@bot.listen()
async def on_member_join(member):
    await member.send(f"{member.name}Welcome to {member.guild.name}")



@bot.event
async def on_command_error(ctx, err):
    if ctx.guild.id == 494725137476616202:

        await ctx.channel.send(f'''_\n{type(err).__name__}: {err!s}_''')

    if ctx.guild.id == 490190146843443201:
        await ctx.channel.send(f'''_\n{type(err).__name__}: {err!s}_''')

    if ctx.guild.id == 453472827526479874:
        await ctx.channel.send(f'''_\n{type(err).__name__}: {err!s}_''')

    if ctx.guild.id == 457729395122241537:
        await ctx.channel.send(f'''_\n{type(err).__name__}: {err!s}_''')
    else:
        return








@bot.event
async def on_ready():
    bot.load_extension("fun")
    bot.load_extension("search")
    bot.load_extension('ExampleRepl')
    options = ('help via p?help', 'to ! Garry#2508', f'on {len(bot.guilds)} servers')
    while True:
        await bot.change_presence(activity=discord.Streaming(name=random.choice(options), url='https://www.twitch.tv/cohhcarnage'))
        await asyncio.sleep(10)


bot.add_cog(BAdmin())
bot.add_cog(BAmath())
bot.add_cog(BAsics())
bot.run(os.getenv('TOKEN'))
