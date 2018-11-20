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

bot = commands.Bot(description='Isse can do a lot more.....', command_prefix=commands.when_mentioned_or('p?'))


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
@commands.cooldown(1, 3, commands.BucketType.user)
async def spawn(ctx, val1):
     if ctx.author.permissions_in(ctx.channel).manage_roles:
        channel = ctx.channel
        val = val1.lower() 
        url = "https://img.pokemondb.net/artwork/vector/large/" + val + ".png"
        embed = discord.Embed(title="Sausage!", color=0xffb6c1)
        embed.set_image(url=url)
        await channel.send(embed=embed)
        
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
        
        

@bot.listen()
async def on_member_join(member):
    await member.send(f"{member.name}Welcome to {member.guild.name}")       
        

@bot.event
async def on_command_error(ctx, err):
    if ctx.guild.id == 490190146843443201:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')
        
    if ctx.guild.id == 494725137476616202:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')
    if ctx.guild.id == 453472827526479874:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')
    if ctx.guild.id == 457729395122241537:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')
    if ctx.guild.id == 509434069319155712:
        await ctx.channel.send(f'''```py\n{type(err).__name__}: {err!s}```''')   
    else:
        return
    



@bot.event
async def on_ready():
    bot.load_extension("fun")
    bot.load_extension("search")
    bot.load_extension('ExampleRepl')
    options = ('help via p?help', 'to Garry#2508', f'on {len(bot.guilds)} servers')
    while True:
        await bot.change_presence(activity=discord.Streaming(name=random.choice(options), url='https://www.twitch.tv/cohhcarnage'))
        await asyncio.sleep(10)


bot.add_cog(BAdmin())
bot.add_cog(BAmath())
bot.add_cog(BAsics())
bot.run(os.getenv('TOKEN'))
