import discord
import aiohttp
import datetime
import inspect
import os
import io
import re
import requests
import asyncio
import random
import psutil
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont
import json
import ast
from urllib import parse
import secrets
from bs4 import BeautifulSoup





bot = commands.Bot(description='utlity can do a lot more.....', command_prefix=commands.when_mentioned_or('?'))
bot.remove_command('help')


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


@bot.command(hidden = True)
async def code(ctx, command):
        ''': getting the code for command'''

        a = inspect.getsource(bot.get_command(command).callback)
        embed = discord.Embed(title='Code', description="```py\n"+a+"```",color=discord.Colour.dark_purple())
        embed.set_thumbnail(url='https://scontent.fdel3-1.fna.fbcdn.net/v/t1.0-9/20155639_1952222755056855_6450365686627691750_n.png?oh=0b2c4ecd1409396b05f71c31dd07dd2d&oe=5AE7B998')
        await ctx.send(embed=embed)


@bot.command(pass_context = True)
async def say(ctx, *args):
    mesg = ' '.join(args)
    await ctx.message.delete()

    return await ctx.send(mesg)


@bot.command(pass_context=True)
async def pepe(ctx, user: discord.Member = None):
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
@bot.command(pass_context=True, name='wikipedia', aliases=['wiki', 'w'])
async def wikipedia(ctx, *, query: str):
    """
    Get information from Wikipedia
    """
    try:
        url = 'https://en.wikipedia.org/w/api.php?'
        payload = {}
        payload['action'] = 'query'
        payload['format'] = 'json'
        payload['prop'] = 'extracts'
        payload['titles'] = ''.join(query).replace(' ', '_')
        payload['exsentences'] = '5'
        payload['redirects'] = '1'
        payload['explaintext'] = '1'
        headers = {'user-agent': 'Red-cog/1.0'}
        conn = aiohttp.TCPConnector(verify_ssl=False)
        session = aiohttp.ClientSession(connector=conn)
        async with session.get(url, params=payload, headers=headers) as r:
            result = await r.json()
        session.close()
        if '-1' not in result['query']['pages']:
            for page in result['query']['pages']:
                title = result['query']['pages'][page]['title']
                description = result['query']['pages'][page]['extract'].replace('\n', '\n\n')
            em = discord.Embed(title='Wikipedia: {}'.format(title), description=u'\u2063\n{}...\n\u2063'.format(description[:-3]), color=discord.Color.blue(), url='https://en.wikipedia.org/wiki/{}'.format(title.replace(' ', '_')))
            em.set_footer(text='Information provided by Wikimedia', icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Wikimedia-logo.png/600px-Wikimedia-logo.png')
            await ctx.send(embed=em)
        else:
            message = 'I\'m sorry, I can\'t find {}'.format(''.join(query))
            await ctx.send('```{}```'.format(message))
    except Exception as e:
        message = 'Something went terribly wrong! [{}]'.format(e)
        await ctx.send('```{}```'.format(message))
        
            
@bot.command(pass_context=True, aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):

    name="user",
    if member is None:
        member = ctx.author

    e = discord.Embed(title=f"User: {member.name}",description=f"This is all the information I could find on {member.name}...",)
    e.set_thumbnail(url=member.avatar_url_as(static_format="png"))
    e.add_field(name="Name",value=member.name)
    e.add_field(name="Discriminator",value=f"#{member.discriminator}")
    e.add_field(name="ID",value=str(member.id))
    e.add_field(name="Bot",value=str(member.bot).capitalize())
    e.add_field(name="Highest Role",value=member.top_role.mention)
    e.add_field(name="Join Position",value=f"#{sorted(member.guild.members, key=lambda m: m.joined_at).index(member) + 1}")
    e.add_field(name="Created Account",value=member.created_at.strftime("%c"))
    e.add_field(name="Joined This Server",value=member.joined_at.strftime("%c"))
    e.add_field(name="Roles",value=f"{len(member.roles)-1} Roles: {', '.join([r.mention for r in member.roles if not r.is_default()])}")
    await ctx.send(embed=e)
    

@bot.command()
async def feedback(ctx, * , feedback):
    channel = bot.get_channel(519136306853314560)
    embed = discord.Embed(title="Feedback Submission :robot:", colour=discord.Colour.red(), description=f'''Submitted by- {ctx.author}''')
    embed.add_field(name="Feedback", value=feedback, inline=False)
    embed.set_footer(text=f"From {ctx.guild.name} ({ctx.guild.id})")
    await channel.send(embed=embed)
    await ctx.send("Your Feedback Has Been Submitted")


@bot.command()
async def poll(ctx, *, poll_message):
        embed = discord.Embed(title=f'''{ctx.author}'s new poll''', colour=discord.Colour.red(), description=poll_message)
        try:
            await ctx.message.delete()
        except:
            pass
        msg = await ctx.send(embed=embed)        
        try:
            await msg.add_reaction("\N{THUMBS UP SIGN}")
            await msg.add_reaction("\N{THUMBS DOWN SIGN}")
        except:
            await msg.delete()
            await ctx.send("Make sure i can add reactions to the poll")
        






@bot.command(pass_context=True)
async def bite(ctx, member: discord.Member):
    """bites  someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    bite = "**{0}bites you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466571069973856256/bite-HkutgeXob.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466571762339938304/bite-ry00lxmob.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466572007258193920/bite-H1_Jbemjb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572188372434964/bite-H1hige7sZ.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466572377233293322/bite-Hk1sxlQjZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572552739880961/bite-rkakblmiZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466572804385669120/bite-BJXRmfr6-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466573024078987284/bite-ry3pQGraW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=bite.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def cuddle(ctx, member: discord.Member):
    """cuddle  someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    cuddle = "**cuddles you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466573538841591809/cuddle-SJn18IXP-.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466573996201082900/cuddle-r1s9RqB7G.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466574139805794306/cuddle-SJceIU7wZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574279127859200/cuddle-r1XEOymib.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466574467070427156/cuddle-S1T91Att-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574644577697792/cuddle-BkZCSI7Pb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466574850375548939/cuddle-Byd1IUmP-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466575399862665216/cuddle-BkN0rIQDZ.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=cuddle.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)


@bot.command(pass_context=True)
async def pat(ctx, member: discord.Member):
    """pat someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    pat = "**you have been patted .{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466577618771378176/pat-rktsca40-.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466577986209185812/pat-rkZbJAYKW.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466578464619626496/pat-SJva1kFv-.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466578677090484224/pat-BkJBQlckz.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466578825468182538/pat-H1s5hx0Bf.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579159435706380/pat-rJMskkFvb.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579338490544128/pat-rkBZkRttW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466579500117917727/pat-Sk2FyQHpZ.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=pat.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def kiss(ctx, member: discord.Member):
    """kiss someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    kiss = "**  kissed you.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/456701536912015361/466579840070582284/kiss-B1MJ2aODb.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466580423116324874/kiss-Hkt-nTOwW.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466581686591946763/kiss-r1VWnTuPW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466582897755947017/kiss-BkUJNec1M.gif',
               'https://cdn.discordapp.com/attachments/456701536912015361/466583102047780914/kiss-Sk1k3TdPW.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583257341755392/kiss-BJv0o6uDZ.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583404222087168/kiss-S1PCJWASf.gif'
               'https://cdn.discordapp.com/attachments/456701536912015361/466583780736499712/kiss-SJ3dXCKtW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)
@bot.command(pass_context=True)
async def poke(ctx, member: discord.Member):
    """poke someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    poke = "**{0} poked {1}!**"

    choices = ['https://pa1.narvii.com/6021/b50b8078fa1d8e8f6d2ebfb085f106c642141723_hq.gif',
               'https://media1.tenor.com/images/8fe23ec8e2c5e44964e5c11983ff6f41/tenor.gif',
               'https://media.giphy.com/media/WvVzZ9mCyMjsc/giphy.gif',
               'https://media.giphy.com/media/pWd3gD577gOqs/giphy.gif',
               'http://gifimage.net/wp-content/uploads/2017/09/anime-poke-gif-12.gif', 'https://i.gifer.com/S00v.gif',
               'https://i.imgur.com/1NMqz0i.gif']

    image = random.choice(choices)

    embed = discord.Embed(description=poke.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def hug(ctx, member: discord.Member):
    """hug someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    hug = "**{0}Aww, I see you are lonely, take a hug <3{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/447337220895145998/466226631778893824/hug-rk_6GyncG.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466227315110576129/hug-ry6o__7D-.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466227511165190175/hug-Bk5haAocG.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466228974326906891/hug-BkBs2uk_b.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229286966394881/hug-HkfgF_QvW.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230001872666635/hug-BkZngAYtb.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230123209687040/hug-Bk5T2_1Ob.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466230234795212802/hug-Hy4hxRKtW.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=hug.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)

@bot.command(pass_context=True)
async def slap(ctx, member: discord.Member):
    """Slap someone!"""
    author = ctx.message.author.mention
    mention = member.mention

    slap = "**{0}Hmm, why do you want this?Slaps.{1}!**"

    choices = ['https://cdn.discordapp.com/attachments/447337220895145998/466229677300908042/slap-rJYqQyKv-.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229535059345408/slap-r1PXzRYtZ.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466229453236731904/slap-SkSCyl5yz.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466231429337055242/slap-B1-nQyFDb.gif',
               'https://cdn.discordapp.com/attachments/447337220895145998/466231614352130048/slap-HkskD56OG.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466231875120267284/slap-By2iXyFw-.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466232154112917504/slap-SkKn-xc1f.gif'
               'https://cdn.discordapp.com/attachments/447337220895145998/466232493889290241/slap-rJrnXJYPb.gif']


    image = random.choice(choices)

    embed = discord.Embed(description=slap.format(author, mention), colour=discord.Colour(0xba4b5b))
    embed.set_image(url=image)

    await ctx.send(embed=embed)
    

        
@bot.command()
async def dog(ctx):
    ''''sends cute dog pics'''
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    embed=discord.Embed()
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed)
    

 
@bot.command()
async def neko(ctx):
    ''''sends cute nekos'''
    r = requests.get("https://nekos.life/api/neko").json()

    colours = [0x1abc9c, 0x11806a, 0x2ecc71, 0x1f8b4c, 0x3498db, 0x206694, 0x9b59b6, 0x71368a, 0xe91e63, 0xad1457, 0xf1c40f, 0xc27c0e, 0xa84300, 0xe74c3c, 0x992d22, 0x95a5a6, 0x607d8b, 0x979c9f, 0x546e7a]
    col = int(random.random() * len(colours))
    content = [":neko: Don't be sad! This neko wants to play with you!", "You seem lonely, {0.mention}. Here, have a neko. They're not as nice , but enjoy!".format(ctx.message.author), "Weuf, woof, woooooooooof. Woof you.", "Pupper!", "Meow... wait its neko."]
    con = int(random.random() * len(content))
    embed=discord.Embed()
    embed.set_image(url=r["neko"])
    await ctx.send(content=content[con],embed=embed)


@bot.command(pass_context=True, no_pm=True, name='kill')
async def _kill(ctx, victim: discord.Member):
    """Randomly chooses a kill."""
    author = ctx.message.author
    if victim.id == author.id:
        await ctx.send('I won\'t let you kill yourself!')
    elif victim.id == ctx.bot.user.id:
        await ctx.send('I refuse to kill myself!')
    else:
        choices =["{killer} shoves a double barreled shotgun into {victim}\'s mouth and squeezes the trigger of the gun, causing {victim}\'s head to horrifically explode like a ripe pimple, splattering the young person\'s brain matter, gore, and bone fragments all over the walls and painting it a crimson red.",
                  "Screaming in sheer terror and agony, {victim} is horrifically dragged into the darkness by unseen forces, leaving nothing but bloody fingernails and a trail of scratch marks in the ground from which the young person had attempted to halt the dragging process.",
                  "{killer} takes a machette and starts hacking away on {victim}, chopping {victim} into dozens of pieces'.",
                  "{killer} pours acid over {victim}. Well don\'t you look pretty right now?",
                  "{victim} screams in terror as a giant creature with huge muscular arms grab {victim}\'s head; {victim}\'s screams of terror are cut off as the creature tears off the head with a sickening crunching sound. {victim}\'s spinal cord, which is still attached to the dismembered head, is used by the creature as a makeshift sword to slice a perfect asymmetrical line down {victim}\'s body, causing the organs to spill out as the two halves fall to their) respective sides.",
                  "{killer} grabs {victim}\'s head and tears it off with superhuman speed and efficiency. Using {victim}\'s head as a makeshift basketball, {killer} expertly slams dunk it into the basketball hoop, much to the applause of the audience watching the gruesome scene.",
                  "{killer} uses a shiv to horrifically stab {victim} multiple times in the chest and throat, causing {victim} to gurgle up blood as the young person horrifically dies.",
                  "{victim} screams as {killer} lifts {victim} up using his superhuman strength. Before {victim} can even utter a scream of terror, {killer} uses his superhuman strength to horrifically tear {victim} into two halves; {victim} stares at the monstrosity in shock and disbelief as {victim} gurgles up blood, the upper body organs spilling out of the dismembered torso, before the eyes roll backward into the skull.",
                  "{victim} steps on a land mine and is horrifically blown to multiple pieces as the device explodes, the {victim}\'s entrails and gore flying up and splattering all around as if someone had thrown a watermelon onto the ground from the top of a multiple story building.",
                  "{victim} is killed instantly as the top half of his head is blown off by a Red Army sniper armed with a Mosin Nagant, {victim}\'s brains splattering everywhere in a horrific fashion."]
        
        message = str(random.choice(choices)).format(victim=victim.display_name, killer=author.display_name)
        await ctx.send(message)

@bot.command()
async def ban(ctx, member: discord.Member, *, reason):
    if ctx.author.permissions_in(ctx.channel).ban_members:
        if reason is None:
            await member.send(f'''You have been banned by {ctx.author.name} from {ctx.guild.name} due to __No reason given__ ''')
            em = discord.Embed(title='Banned', colour=discord.Colour.dark_red(),
                            description=f'''{member} has been banned''', timestamp= datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culpret', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for Banning', value=f'''_No reason provided_''', inline=False)
            await ctx.send(embed=em)
            await member.ban()
        else:
            await member.send(f'''You have been Banned by {ctx.author.name} from {ctx.guild.name} due to {reason} ''')
            em = discord.Embed(title='Banned', colour=discord.Colour.dark_red(),
                                description=f'''{member} has been banned''', timestamp=datetime.datetime.utcnow())
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Moderator', value=f'''{ctx.author.name}''', inline=False)
            em.add_field(name='Culprit', value=f'''{member}''', inline=False)
            em.add_field(name='Reason for Banning', value=f'''{reason}''', inline=False)
            await ctx.send(embed=em)
            await member.ban()
    else:
        message = await ctx.send(f'''{ctx.author.mention} you are not eligible for this''', delete_after= 3)
        await message.add_reaction('\u2623') 
        
@bot.command()
async def unban(ctx, userid: int):
    """:unban member using userid"""
    if ctx.author.permissions_in(ctx.channel).ban_members:
        banlist = await ctx.guild.bans()
        for bans in banlist:
            if(bans.user.id == userid):
                await ctx.guild.unban(bans.user)
                await ctx.send("successfully unbanned")
        
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



@bot.command(pass_context=True)
async def joined_at(ctx, member: discord.Member = None):
    if member is None:
        member = ctx.message.author
        em = discord.Embed(title='Join', colour=discord.Colour.dark_red(),
                            description=f'''{member} has been Joinned''', timestamp=datetime.datetime.utcnow())
        em.set_thumbnail(url=member.avatar_url)
        em.add_field(name='Member', value=f'''{member} joined at {member.joined_at}''', inline=False)
        await ctx.send(embed=em)
        
@bot.command(pass_context=True)
async def rps(ctx, choice):
    """"""
    choices = ["rock", "paper", "scissors"]
    await ctx.send("You chose {} | CPU chose {}".format(choice, random.choice(choices)))
    
@bot.command(pass_context=True)
async def ud(ctx, *, msg):
    """Pull data from Urban Dictionary. Use >help ud for more information.
    Usage: >ud <term> - Search for a term on Urban Dictionary.
    You can pick a specific result to use with >ud <term> | <result>.
    If no result is specified, the first result will be used.
        """
    await ctx.message.delete()
    number = 1
    if " | " in msg:
        msg, number = msg.rsplit(" | ", 1)
    search = parse.quote(msg)
    response = requests.get("http://api.urbandictionary.com/v0/define?term={}".format(search)).text
    result = json.loads(response)
    if result == "no_results":
        await ctx.send( "{} couldn't be found on Urban Dictionary.".format(msg))
    else:
        try:
            top_result = result["list"][int(number) - 1]
            embed = discord.Embed(title=top_result["word"], description=top_result["definition"],
                                    url=top_result["permalink"])
            if top_result["example"]:
                embed.add_field(name="Example:", value=top_result["example"])
            if result == "tags":
                embed.add_field(name="Tags:", value=" ".join(result["tags"]))
            embed.set_author(name=top_result["author"],
                                icon_url="https://lh5.ggpht.com/oJ67p2f1o35dzQQ9fVMdGRtA7jKQdxUFSQ7vYstyqTp-Xh-H5BAN4T5_abmev3kz55GH=w300")
            number = str(int(number) + 1)
            embed.set_footer(text="{} results were found. To see a different result, use ?ud {} {}.".format(
                len(result["list"]), msg, number))
            await ctx.send("", embed=embed)
        except IndexError:
            await ctx.send( "That result doesn't exist! Try ?ud {}.".format(msg))
            
@bot.command(pass_context=True, name='youtube', no_pm=True)
async def youtube(ctx, *, query: str):
    """Search on Youtube"""
    try:
        url = 'https://www.youtube.com/results?'
        payload = {'search_query': ''.join(query)}
        headers = {'user-agent': 'Red-cog/1.0'}
        conn = aiohttp.TCPConnector()
        session = aiohttp.ClientSession(connector=conn)
        async with session.get(url, params=payload, headers=headers) as r:
            result = await r.text()
        session.close()
        yt_find = re.findall(r'href=\"\/watch\?v=(.{11})', result)
        url = 'https://www.youtube.com/watch?v={}'.format(yt_find[0])
        await ctx.send (url)
    except Exception as e:
        message = 'Something went terribly wrong! [{}]'.format(e)
        await  ctx.send(message)
        
@bot.command(aliases=['slots', 'bet'])
@commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
async def slot(ctx):
    """ Roll the slot machine """
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)

    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

    if (a == b == c):
        await ctx.send(f"{slotmachine} All matching, you won! 🎉")
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
    else:
        await ctx.send(f"{slotmachine} No match, you lost 😢")


@bot.command(aliases=['howhot', 'hot'])
async def hotcalc(ctx, *, user: discord.Member = None):
    """ Returns a random percent for how hot is a discord user """
    if user is None:
        user = ctx.author

    random.seed(user.id)
    r = random.randint(1, 100)
    hot = r / 1.17

    emoji = "💔"
    if hot > 25:
        emoji = "❤"
    if hot > 50:
        emoji = "💖"
    if hot > 75:
        emoji = "💞"

    await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")

@bot.command()
async def password(ctx):
    """ Generates a random password string for you """
    if hasattr(ctx, 'guild') and ctx.guild is not None:
        await ctx.send(f"Sending you a private message with your random generated password **{ctx.author.name}**")
    await ctx.author.send(f"🎁 **Here is your password:**\n{secrets.token_urlsafe(18)}")

@bot.command()
async def reverse(ctx, *, text: str):
    """ !poow ,ffuts esreveR
    Everything you type after reverse will of course, be reversed
    """
    t_rev = text[::-1].replace("@", "@\u200B").replace("&", "&\u200B")
    await ctx.send(f"🔁 {t_rev}")

@bot.command(aliases=['joinme', 'join', 'botinvite'])
async def invite(ctx):
    """ Invite me to your server """
    await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n<{discord.utils.oauth_url(ctx.bot.user.id)}>")
    
@bot.command(name="username")
async def change_username(ctx, *,name: str):
    """ Change username. """
    try:
        await ctx.bot.user.edit(username=name)
        await ctx.send(f"Successfully changed username to **{name}**")
    except discord.HTTPException as err:
        await ctx.send(err)

@bot.command(aliases=["nk"])
async def nicknames(ctx, member: discord.Member, *, name: str = None):
    """ Nicknames a user from the current server. """
    if ctx.author.permissions_in(ctx.channel).manage_nicknames:
        try:
            await member.edit(nick=name, reason= f'''{ctx.author.name} from {ctx.guild.name} Changed by command''')
            message = f"Changed **{member.name}'s** nickname to **{name}**"
            if name is None:
                message = f"Reset **{member.name}'s** nickname"
            await ctx.send(message)
        except Exception as e:
            await ctx.send(e)
   

@bot.command(pass_context = True)
async def mute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == '411496838550781972':
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send("please specify a user")
            return
        await member.add_roles(role)
        await ctx.send("member is muted")

@bot.command(pass_context = True)
async def unmute(ctx, member: discord.Member):
     if ctx.message.author.guild_permissions.administrator or ctx.message.author.id == '411496838550781972':
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        if not member:
            await ctx.send("please specify a user")
            return
        await member.remove_roles(role)
        
        
@bot.command(hidden=True)
async def editmessage(ctx, id:int, *, newmsg:str):
    """Edits a message sent by the bot"""
    try:
        msg = await ctx.channel.get_message(id)
    except discord.errors.NotFound:
        await ctx.send("Couldn't find a message with an ID of `{}` in this channel".format(id))
        return
    if msg.author != ctx.guild.me:
        await ctx.send("That message was not sent by me")
        return
    await msg.edit(content=newmsg)
    await ctx.send("edit af")
  
@bot.command(name='ceinfo')
async def customemojiinfo(ctx, *, emoji: discord.Emoji):
    """Display information for a custom emoji.

    * emoji - The emoji to get information about."""

    embed = discord.Embed(title=emoji.name)
    embed.description = f"{emoji.id} | [Full image]({emoji.url})"

    embed.add_field(name="Guild", value=f"{emoji.guild.name} ({emoji.guild.id})")
    embed.add_field(name="Managed", value=emoji.managed)
    embed.add_field(name="Created at", value=emoji.created_at.ctime())
    url = emoji.url.replace('discordapp.com/api', 'cdn.discordapp.com')
    embed.set_thumbnail(url=url)

    await ctx.send(embed=embed) 

    
@bot.command(pass_context=True,name='ademote')
async def addemote(ctx, name, url):
    if ctx.message.author.guild_permissions.manage_emojis:

    
        await ctx.message.delete()
        try:
            response = requests.get(url)
        except (requests.errors.MissingSchema, requests.errors.InvalidURL, requests.errors.InvalidSchema):
            return await ctx.send("The URL you have provided is invalid.")
        if response.status_code == 404:
            return await ctx.send("The URL you have provided leads to a 404.")
        elif url[-3:] not in ("png", "jpg") and url[-4:] != "jpeg":
            return await ctx.send("Only PNG and JPEG format images work to add as emoji.")
        emoji = await ctx.guild.create_custom_emoji(name=name, image=response.content)
        await ctx.send("Successfully added the emoji {0.name} <:{0.name}:{0.id}>!".format(emoji))

@bot.command(pass_context=True,name='remote')
async def removeemote(ctx, name, url):
    if ctx.message.author.guild_permissions.manage_emojis:

        await ctx.message.delete()
        emotes = [x for x in ctx.guild.emojis if x.name == name]
        emote_length = len(emotes)
        if not emotes:
            return await ctx.send("No emotes with that name could be found on this server.")
        for emote in emotes:
            await emote.delete()
        if emote_length == 1:
            await ctx.send("Successfully removed the {} emoji!".format(name))
        else:
            await ctx.send("Successfully removed {} emoji with the name {}.".format(emote_length, name))
            
@bot.command(pass_context=True)
async def comic(ctx, *, comic=""):
    """Pull comics from xkcd."""
    if comic == "random":
        randcomic = requests.get("https://c.xkcd.com/random/comic/".format(comic))
        comic = randcomic.url.split("/")[-2]
    site = requests.get("https://xkcd.com/{}/info.0.json".format(comic))
    if site.status_code == 404:
        site = None
        found = None
        search = parse.quote(comic)
        result = requests.get("https://www.google.co.nz/search?&q={}+site:xkcd.com".format(search)).text
        soup = BeautifulSoup(result, "html.parser")
        links = soup.find_all("cite")
        for link in links:
            if link.text.startswith("https://xkcd.com/"):
                found = link.text.split("/")[3]
                break
        if not found:
            await ctx.send("That comic doesn't exist!")
        else:
            site = requests.get("https://xkcd.com/{}/info.0.json".format(found))
            comic = found
    if site:
        json = site.json()
        embed = discord.Embed(title="xkcd {}: {}".format(json["num"], json["title"]), url="https://xkcd.com/{}".format(comic))
        embed.set_image(url=json["img"])
        embed.set_footer(text="{}".format(json["alt"]))
        await ctx.send("", embed=embed)

       
@bot.command(aliases=['hban'], pass_context=True)
async def hackban(ctx, user_id: int):
    """Bans a user outside of the server."""
    if ctx.author.permissions_in(ctx.channel).ban_members:
        author = ctx.message.author
        guild = author.guild

        user = guild.get_member(user_id)
        if user is not None:
            await ctx.invoke(ctx.ban, user=user)
            return


        try:
            await ctx.bot.http.ban(user_id, guild.id, 0)
            await ctx.send("Done")
        except discord.NotFound:
            await ctx.message.edit('Invalid user ID was provided.')
        except discord.errors.Forbidden:
            await ctx.message.edit('Not enough permissions.')
             
@bot.command(aliases=["vote", "daily"])
@commands.cooldown(1, 3, commands.BucketType.user)
async def upvote(ctx):
    embed = discord.Embed(title="Upvote the Bot Here!")
    embed.add_field(name="You haven't upvoted?", value="If you have not upvoted")
    embed.add_field(name="Upvote Touka Here! ", value="[Upvote Touka](https://discordbots.org/bot/486093523024609292/vote)")
    embed.set_footer(text = "Made by garry#2508", icon_url = 'https://cdn.discordapp.com/avatars/486093523024609292/3473b7f51092af6f4656bf9abed80d6c.webp?size=1024')
    await ctx.send(embed=embed)
    
@bot.command(name="pg")
async def pingrole(ctx, role: discord.Role, *, message):
    """
    Temporarily edits a role to be pingable, sends a message mentioning said role, then edits it to be
    unpingable.

    The role must be below my highest role.
    """
    if role.position >= ctx.guild.me.top_role.position:
        return await ctx.send("I can't edit that role because it's above my highest role.")

    try:
        await role.edit(mentionable=True, reason=f'Pingrole by{ctx.author}')
        await ctx.send(f'{role.mention}: {message}')
    finally:
        try:
            await role.edit(mentionable=False, reason=f'Pingrole by {ctx.author}')
        except discord.HTTPException:
            pass 
        
@bot.command(pass_context=True)
async def mods(ctx):
    """
    Shows mods in this server.

    A mod is defined as a human in this server with the "Kick Members" permission, or is a Dogbot Moderator.
    """
    is_mod = lambda m: (m.guild_permissions.kick_members) and not m.bot
    mods = [m for m in ctx.guild.members if is_mod(m)]

    embed = discord.Embed(title='Moderators in ' + ctx.guild.name, color=discord.Color.blurple(),
                            description=f'There are {len(mods)} mod(s) total in {ctx.guild.name}.')

    for status in discord.Status:
        those_mods = [m for m in mods if m.status is status]
        if not those_mods:
                continue
        embed.add_field(name=str(status).title(), value='\n'.join(str(m) for m in those_mods))

    await ctx.send(embed=embed) 
    
@bot.command(pass_context=True)
async def online(ctx: commands.Context):
    """
    Show total online users on sever
    """
    guild = ctx.message.guild
    online = [1 if m.status != discord.Status.offline else 0 for m in guild.members]
    await ctx.send('{} users online'.format(sum(online)))
    
@bot.command()
async def website(ctx):
    """ Check out my source code <3 """
    await ctx.send(f"**{ctx.author.name}** check me out:\nhttps://balasaikumardon.wixsite.com/website")
    
@bot.command()
async def servers(ctx):
    a = []
    for i in bot.guilds:
        a.append(i.name)
        await ctx.send(", ".join(a))
        
@bot.command(aliases=['roleinfo'])
async def role(ctx, *, role: discord.Role):
    """Retrieves information about a role in this guild."""
    e = discord.Embed(color=role.color)
    e.add_field(name='Name', value=role.name)
    e.add_field(name='ID', value=role.id)
    e.add_field(name='Role created', value=role.created_at.ctime())
    e.add_field(name='Color', value=str(role.color).upper())
    e.add_field(name='Properties', value='{}, {}'.format('Mentionable' if role.mentionable else 'Not mentionable', 'hoisted' if role.hoist else 'not hoisted'))
    e.add_field(name='Members', value=len(role.members))
    await ctx.send(embed=e)
    

        

@bot.command(pass_context=True)
async def help(ctx, val =None):
    """: help commands"""
    if val is None:
        embed = discord.Embed(title=f'''commands''', description=f'''bot prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.add_field(name='Fun Commands :', value=f'''howhot\n hot\n bet\n  neko\n cat\n pepe\n rps\n 8ball\n bite\n cuddle\n poke \n  kiss\n love\n pat\n slap \n wanted\n profile\n ''', inline=False)
        embed.add_field(name='search :', value=f''' youtube: usage ?youtube <search,url>\n wikipedia:usage ?wiki <query>\n UrbanDictionary: usage ?ud <search>\n comic:usage ?comic <search>\n''', inline=False)
        embed.add_field(name=' server :', value=f'''Serverinfo \n invite\n server\n avatar\n userinfo\n poll\n online: check online count of server\n mods : check list of mods of server''', inline=False)
        embed.add_field(name=' Emotes :', value=f'''addemote : usage ?addemote <name> <url>\n removeemote : usage ?removeemote <name> <url>\n''', inline=False)
        embed.add_field(name=' moderation:', value=f''' Ban :bans user\n hackban : bans user outside the server\n Unban : unbans user\n Kick : kick member\n Warn : warns a person\n prune :Prune the inactive members\npurge : Delete messages\n estimatedprune :Estimate the inactive members to prune\n pg : pings a role usage ?pg @ admin<text>\n''', inline=False)
        embed.add_field(name='Extra:', value=f''' feedback: report me bugs\n say : ecos you\n botinvite : invite me to your server\n password: generates random password\n reverse: reverse's the word u entred\n website \n upvote ''', inline=False)
        embed.set_footer(text = "Made by Garry#2508", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        send = await ctx.send(embed=embed)


    elif val == 'ban':
        embed = discord.Embed(title=f'''Ban command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?ban <user or user.id> <reason>", inline=False)
        embed.add_field(name="Example", value="?ban @garry#2508 hi\n ?ban 411496838550781972 hi", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'unban':
        embed = discord.Embed(title=f'''Unban command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?unban <user.id> ", inline=False)
        embed.add_field(name="Example", value="?unban 411496838550781972 ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'hackban':
        embed = discord.Embed(title=f'''Hackban command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?hban <user.id> ", inline=False)
        embed.add_field(name="Example", value="?hban 411496838550781972 ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'kick':
        embed = discord.Embed(title=f'''kick command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?kick <user.id or user> ", inline=False)
        embed.add_field(name="Example", value="?kick 411496838550781972 hi\n ?kick @garry#2508 hi ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'warn':
        embed = discord.Embed(title=f'''Warn command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?warn <user> ", inline=False)
        embed.add_field(name="Example", value="?warn @garry#2508 hi ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'youtube':
        embed = discord.Embed(title=f'''Youtube command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?youtube <search or url> ", inline=False)
        embed.add_field(name="Example", value="?youtube shape of you\n ?youtube https://youtu.be/hA6hldpSTF8 ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'wikipedia':
        embed = discord.Embed(title=f'''Wiki command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="Allias", value="wiki or wikipedia ", inline=False)
        embed.add_field(name="usage", value="?wiki <search> ", inline=False)
        embed.add_field(name="Example", value="?wiki pokemon ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'urbandictionary':
        embed = discord.Embed(title=f'''Urbandictionary command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="Allias", value="ud or urbandictionary ", inline=False)
        embed.add_field(name="usage", value="?ud <word> ", inline=False)
        embed.add_field(name="Example", value="?ud flower\n ?urbandictionary flower ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)

    elif val == 'comic':
        embed = discord.Embed(title=f'''Comic command''', description=f'''prefix : ?''',color=discord.Colour(0xba4b5b))
        embed.add_field(name="usage", value="?comic <search> ", inline=False)
        embed.add_field(name="Example", value="?comic die ", inline=False)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/494722737420500993/521947092625915948/neko292.jpg')
        embed.set_footer(text = "?help <command>to get more help", icon_url = 'https://images-ext-1.discordapp.net/external/LVSBex7pO3PGD7jRP42QT80UTPANLaYV-eEcy3gL-wY/https/cdn.nekos.life/neko/neko_004.png?width=334&height=473')
        await ctx.send(embed=embed)


    
    
@bot.command(hidden=True)
async def reload(ctx, extension):
    if ctx.author.id == 411496838550781972 or 293800689266851850:
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

        

 
    
    
@bot.event
async def on_guild_join(guild):
    general = find(lambda x: x.name == 'general',  guild.text_channels)
    if general and general.permissions_for(guild.me).send_messages:
        if general and general.permissions_for(guild.me).send_messages:
            await general.send('Hello {}!'.format(guild.name))
    
    
        

@bot.event
async def on_command_error(ctx, err):
    if ctx.guild.id == 453472827526479874 or 453583048504639505 or 457318783951044609 or 457487658374135808 or 457729395122241537 or 468908507782053899 or 474735368273395713 or 475961215168806923 or 480246586279067650 or 486461298805178368 or 490190146843443201 or 494725137476616202 or 498284867868557313 or 500572118396698624 or 507703335017512962 or 509434069319155712 or 513715362920005632 or 513900235391762446 or 515059024098754564 or 515473815560781824 or 517031325056761866 or 518083297650147329 or 518526295055794186 or 520144444050374657 or 520203621485379584 or 521287749236686848 or 521314129735188490:
        

        send_help = (commands.MissingRequiredArgument, commands.BadArgument, commands.TooManyArguments, commands.UserInputError, commands.CommandNotFound, commands.CommandInvokeError)


    if isinstance(err, commands.CommandNotFound):
        await ctx.send('No commands found. Check help for list of my commands ')

    elif isinstance(err, commands.MissingRequiredArgument):
        pass
    
    elif isinstance(err, commands.CommandOnCooldown):
        await ctx.send(f'Please wait {err.retry_after:.2f}s')

    elif isinstance(err, commands.MissingPermissions):
        pass 
            
    else:
        print(''.join(traceback.format_exception(type(err), err, err.__traceback__)))


    
    
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="playing ?help",type=1))

    print ("Started")

    





bot.add_cog(BAdmin())
bot.add_cog(BAmath())
bot.add_cog(BAsics())
bot.run(os.getenv('TOKEN'))
