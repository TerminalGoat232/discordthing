import discord
from discord import Member
from discord.ext import commands, tasks
import os
from io import BytesIO
import random as rd
import codecs
import webbrowser as w 
from PIL import Image
import PIL.ImageOps
from discord.voice_client import VoiceClient
import asyncio as asc
import json as js
from math import *
from amogus import *
from numpy import *
import youtube_dl as dl
from discord.ext.commands import has_permissions, bot_has_permissions
from FLIB import *
import datetime as dt
from datetime import date
import time
try: import serial 
except: print("the serial library is optional")
dl.utils.bug_reports_message = lambda: 'OOOoOOOoooOOOooooOoo'
def getprf(cl,message):
	with open("prefix.json", "r") as c:
		prx = js.load(c)
	return prx[str(message.guild.id)]
cl = commands.Bot(command_prefix=getprf)
cl2 = discord.Client()
formatoptun = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0', 
    "preferredcodec": "mp3",
    "preferredquality" : "192",
}

ffmpeg_options = {
    'options': '-vn',


}
ydl = dl.YoutubeDL(formatoptun)
k = 0
volume1 = 1
StBd = []
exc = 1
Q = []
lnk2 = ''
with codecs.open('badwords.txt', 'r', 'utf8') as F:
    for conchos in F:
        b = conchos.strip(',').split(',')


# thing

class MainPlay(discord.PCMVolumeTransformer):
	def __init__(self, src,*, data, vol=0.5):
		super().__init__(src, vol)
		self.data = data
		self.tit = data.get('title')
		self.url = data.get('url')
	@classmethod
	async def furl(cls, url, *, loop=None, Strm = None):
		loop = loop or asc.get_event_loop()
		data = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download = not Strm))
		if "entries" in data:
			data = data['entries'][0]
		fname = data['url'] if Strm else ydl.prepare_filename(data)
		return cls(discord.FFmpegPCMAudio(fname, **ffmpeg_options), data=data)

a = ["deek"]
ngu = ['abczyx09324930j24094']

@cl.event
async def on_ready():
    print('i have login as {0.user}'.format(cl))
    print("console.log")
    doingstuff.start()
    await CheckEvents()
    # with open("evt.json","r") as m:
    # 	mn = js.load(m)
    # dtt = date.today()
    # xk = dtt.strftime("%m/%d")
    # for fh in range(0,len(mn["Events"])):
    # 	# print(list(mn["Events"])[fh])
    # 	if xk == list(mn["Events"])[fh]:
    # 		g = ''.join(list(mn['Events'][xk]))
    		
    # 		emb = discord.Embed(title = f"\ud83c\udf82 EVENT TODAY: {xk}", description=f"\ud83c\udf81 {g} \ud83c\udf82",color=0xfbf8b7)
    # 		await cl.get_channel(id = 887513361791717426).send("@everyone")
    # 		await cl.get_channel(id = 887513361791717426).send(embed=emb)
    # 	else: pass
medvar = 1
fff=''
async def CheckEvents():
	global medvar
	swday = [28,30,31]
	while 1:
		# print(">_", medvar)
		with open("evt.json","r") as m: mn = js.load(m)
		dtt = date.today()
		xk = dtt.strftime("%m/%d")
		ff = list(xk)
		# print(ff)
		# print(xk)
		for fh in range(0,len(mn["Events"])):   
			gg = list(list(mn["Events"])[fh])
			if xk == list(mn["Events"])[fh] and medvar == 1 : #str
				g = ''.join(list(mn['Events'][xk]))
				emb = discord.Embed(
					title = f"\ud83c\udf82 EVENT TODAY: {xk}", 
					description=f"\ud83c\udf81 {g} \ud83c\udf82",
					color=0xfbf8b7)
    			# await cl.get_channel(id = 887513361791717426).send("@everyone")
				await cl.get_channel(id = 887513361791717426).send(embed=emb)
				for x in range(0, len(ff)):
					try: 
						mc = int(ff[4])+1
						ff[4] = str(mc)
						break
					except:pass
				cac = int(str(xk)[::-1][1]+str(xk)[::-1][0])
				for kk in range(0,cac):
					if kk in swday or (kk == 29 and dt.today().year % 4 == 0):
						fff = str(int(ff[2])+1) + '/' + '01'
						ff=list(fff)

					# for j in range(0,9):
					# 	if ff[0] == j:
					# 		ff = 0 + fff
					# 	else:
					# 		pass 
				if xk == "12/31":
					ff == "01/01"
			else: pass
		if xk != ''.join(ff):medvar = 0
		elif xk == ff: medvar = 1
		# print(''.join(ff))
		await asc.sleep(5)

cl.remove_command("help")
@cl.command(name="help")
async def help(ctx):
	emb = discord.Embed(
		title="_*Bot commands*_ :", color=0xfbf8b7, 
		description= f"[[{dt.datetime.utcnow()}]]",
		)
	emb.set_image(url='')
	emb.add_field(
		name="**Moderation:**",
		value=f"```re\n> mute\n> unmute\n> kick\n> AddBadw\n> Prefix [new prfx]```\n **Event [Still working on]:**\n ```re\n> AddEvent[datetime][event]\n> EventToday\n```\n**Math:**\n```re\n> Math[Eq]\n> STR2ASCII[texts]\n> STR2BIN[texts]\n> ASCII2STR[ASCII]\n> BIN2STR[Binary]\n```\n ")
	emb.add_field(
		name="**Music:**",
		value=f"```re\n> Plug[it's trash now]\n> Pmus[song name]\n> List[song name]\n> Plist\n> var[song name]\n> Pvar\n> StopP\n> Loop[inf/brk]\n> Resp\n> PauseM\n> ReplaceIn[pos][new song]\n> PSlist[pos]\n> WatchLs\n```")
	emb.add_field(
		name="**Misc:**",
		value="```re\n> RNG [min][max]\n> EC  [messages]\n> TicB\n> Reverse [texts]\n>TmdEC [time] [texts]\n> Avt\n> Susify [texts]```"  
		)
	emb.add_field(
		name="Info",
		value="```re\n> help [show this commands board]\n> ?SPrefix ( show SERVERS prefixs >;] ) \n```"
		)
	emb.set_footer(text=f"_Bot Made By TerminalGoat#0948_",icon_url="https://cdn.discordapp.com/app-icons/875286348951592981/682a085c987b8f66c9cabb68822e593d.png")
	await ctx.send(embed=emb)
@cl.command(name="AddEvent")
async def AddEvent(ctx,date,*,event):
	with open("evt.json","r") as wt:
		mn = js.load(wt)
		dr = f"{date}"
		# evt2 = FindRplChar(event,"-"," ")
		cx = f"{event}"
	mn["Events"].update({dr:cx})
	await ctx.send(embed = discord.Embed(
		title="** ADDED NEW EVENT:**",
		description=f"```\n {event} \n```"))
	with open("evt.json","w") as wr:
		js.dump(mn,wr,indent=4)
@cl.command(name="EventToday")
async def EventToday(ctx):
	with open("evt.json","r") as m:
		mn = js.load(m)
	dtt = date.today()
	xk = dtt.strftime("%m/%d")
	for fh in range(0,len(mn["Events"])):
		print(list(mn["Events"])[fh])
		if xk == list(mn["Events"])[fh]:
			g = ''.join(list(mn['Events'][xk]))
			chl = cl.get_channel('887513361791717426')
			emb = discord.Embed(
				title = "*EVENT TODAY :*", 
				description=f"```\n\n\n  {g} \n\n\n ```", 
				color=0xfbf8b7)
			await ctx.send( embed = emb )
@cl.command(name='unmute')
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="BONKED")

   await member.remove_roles(mutedRole)
   await member.send(f" you have been unmuted from: - {ctx.guild.name}")
   emb = discord.Embed(title="*UNMUTE*", description=f" unmuted: {member.mention}",colour=discord.Colour.green())
   await ctx.send(embed=emb)
@cl.command(name="mute")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="BONKED")

    if not mutedRole:
        mutedRole = await guild.create_role(name="BONKED")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole,
             speak=False,
             send_messages=False, 
             read_message_history=True,
             read_messages=False)
    embed = discord.Embed(title="*ANNOUNCEMENT!*",
     description=f"{member.mention} has been muted ",
     colour=discord.Colour.red())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f"muted by: {guild.name} reason: {reason}")
@cl.command(name="AddBadw")
async def AddBadw(ctx,*,badw:str):
	global StBd
	StBd.append(badw)
	print(StBd)
	c= ""

	with codecs.open('badwords.txt', 'r', 'utf8') as F:
	    for conchos in F:
	        b = conchos.strip(',').split(',')
	        b.append(badw)
	        m = JNL2Str(",", b)
	        c = m
	        print(m)
	        await ctx.send("added no no word to the list")
	with codecs.open("badwords.txt","w",'utf8') as F: 
		F.write(c)
	
@cl.command(name="Plug")
async def Plug(ctx):
	if not ctx.message.author.voice:
			await ctx.send("connect to voice channel first")
			return
	else:
		vc = ctx.message.author.voice.channel
		await vc.connect()

@cl.command(name ="Pmus", pass_context=True)
async def Pmus(ctx,*,lnk:str): 
	global volume1, lnk2
	lnk2 = lnk
	async def Pmus():
		server = ctx.message.guild
		voice_channel = server.voice_client
		async with ctx.typing():
			player = await MainPlay.furl(lnk, loop=cl.loop)
			voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('** Now playing:** {} :musical_note:  '.format(player.tit))
	try:
		if not ctx.message.author.voice:
			
			await ctx.send("connect to voice channel first [Use <Prefix>Plug to connect da bot]")
			return
		else:
			try:
				vc = ctx.message.author.voice.channel
				await vc.connect()
				await Pmus()

			except:
				await Pmus()
	except: pass

@cl.command(name ="PSList", pass_context=True)
async def PSList(ctx, pos:int):
	global Q,lnk2
	pos -= 1
	print(Q[pos])
	try:
		if not ctx.message.author.voice:
			await ctx.send("connect to voice channel first [Use <Prefix>Plug to connect da bot]")
			return
		else:
			server = ctx.message.guild
			voice_channel = server.voice_client		
			async with ctx.typing():
				lnk2 = Q[pos]
				player = await MainPlay.furl(Q[pos], loop=cl.loop)
				voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send('**Now playing:** {}'.format(player.tit))
	except: pass
	finally: return
pos = -1

@cl.command(name="Plist")
async def Plist(ctx):
	global Q,pos,exc
	try:
		if not ctx.message.author.voice:
			await ctx.send("connect to voice channel first [Use <Prefix>Plug to connect da bot]")
			return
		else:
			while exc:
				try:
				
					pos += 1
					server = ctx.message.guild
					voice_channel = server.voice_client		
					# async with ctx.typing():
					player = await MainPlay.furl(Q[pos], loop=cl.loop)
					voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
					# await ctx.send('**Now playing:** {}'.format(player.tit))
					print(pos)
					print("playing: {} ".format(player.tit))
					print(len(Q))
					
					if pos > len(Q):
						await ctx.send("OUT OF SONG")
						pos = -1

						break
				except: 
					pos -= 1
					pass
					# print(pos) 
				await asc.sleep(.5)
				
	except: pass
	finally: return

@cl.command(name="kick")
@commands.has_permissions(kick_members=True)
async def kick(ctx, name:Member, *, reason:str):
	if ctx.message.author.guild_permissions.kick_members:
		if reason == None:
			ctx.send(f"gimme da reason why u wanna kik {name}")
		else:
			await name.kick(reason=reason)
			emb = discord.Embed(title="**!!ANOUNCEMENT!!**", description=f"```{name} has been kicked, reason: {reason}````",color=0xff5b00)
			await ctx.send(embed=emb)

@cl.command(name="Prefix")
#Coiashdoidhoioiscoiscsndnclkdmclkcmlmcccccccccccccccccccccccccccccccccccccc
async def Prefix(ctx, prf:str):
	
	if len(prf) == 1:
		with open("prefix.json", "r") as c:
			prefx = js.load(c)
		prefx[str(ctx.guild.id)] = prf
		with open("prefix.json", "w") as c:
			js.dump(prefx,c,indent=5)
		await ctx.send(f"*changed prefix to {prf}*")
	else:
		await ctx.send("**only accept prefix as a symbol or character**")
#Coiashdoidhoioiscoiscsndnclkdmclkcmlmcccccccccccccccccccccccccccccccccccccc
@cl.event
async def on_guild_join(guild):
	with open("prefix.json", "r") as c:
		prx = js.load(c)
	prx[str(guild.id)] = "-"
	with open("prefix.json", "w") as c:
		js.dump(prx,c,indent=5)

@cl.command(name ="Pagain", pass_context=True)
async def Pagain(ctx):
	global lnk2
	server = ctx.message.guild
	voice_channel = server.voice_client
	try:
		async with ctx.typing():
			player = await MainPlay.furl(lnk2, loop=cl.loop)
			voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
		await ctx.send("*Playing {}".format(player.tit)+ " again* :repeat: ")
	except:pass
@cl.command(name="var")
async def var(ctx, *,lnk11:str):
	global lnk12
	await ctx.message.delete()
	lnk12 = lnk11
lnk12 =""
@cl.command(name="Pvar")
async def Pvar(ctx):
	global lnk12
	print(lnk12)
	await ctx.message.delete()
	server = ctx.message.guild
	voice_channel = server.voice_client
	async with ctx.typing():
		player = await MainPlay.furl(lnk12, loop=cl.loop)
		voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
f = 0
v = 0
@cl.command(name="Loop")

async def Loop(ctx, t:str):
	global lnk2, f,v,exc
	sound = cl.voice_clients
	if t.lower() == "inf":
		f = 1
		emb = discord.Embed(description=f"LOOPING the current song ", color= 0xc6fea0)	
		await ctx.send(embed=emb)
		v = 0
	if t.lower() == "brk":
		v = 1
		f = 0
		emb1 = discord.Embed(description=f"```diff\n The loop has been broken ```", color= 0xc6fea0)	
		await ctx.send(embed=emb1)
		print(f)
		print(v)

	
	while f:
		try:
			server = ctx.message.guild
			vc = server.voice_client
			player = await MainPlay.furl(lnk2, loop=cl.loop)
			# player = await MainPlay.furl(lnk2, loop=cl.loop)
			vc.play(player, after=lambda e: print('Loop: %s' % f) if f else None)
			if v == 1:
				# await ctx.send('the loop has been broken')
				break
		except: pass
		await asc.sleep(.1)
@cl.command(name="List")
async def List(ctx,*,lnk11):
	global Q
	server = ctx.message.guild
	voice_channel = server.voice_client
	Q.append(lnk11) 
	print(Q)
	print(len(Q))
	await ctx.send(f"added {lnk11} to the song list")
	
@cl.command(name="ReplaceIn")
async def ReplaceIn(ctx, pos1:int, *,lnk33:str):
	global Q
	Q[pos1] = lnk33
	await ctx.send(f"``` Replaced { Q[pos1] } with { lnk33} ")

@cl.command(name="WatchLs")
async def  WatchLs(ctx):
	global Q
	for xh in range(0, len(Q)):
		await ctx.send(f"```\n song {xh+1}: { Q[xh] }, indx = {xh+1} \n```") 

@cl.command(name="PauseM")
async def PauseM(ctx):
	global exc
	abc = ctx.message.guild
	vc = abc.voice_client
	exc = 0
	print(exc)
	vc.pause()
sttcolor = 0
@cl.command(name="TicB")
async def TicB(ctx):
	global sttcolor
	stt = time.monotonic()

	msg = await ctx.send("[0]Pinging...")
	send = time.monotonic() - stt

	rac = time.monotonic()
	await msg.add_reaction("\U0001f44d")
	ract = time.monotonic() - rac 

	edtt = time.monotonic()
	await msg.edit(content="[1]Pinging...")
	edt = time.monotonic() - edtt

	delt = time.monotonic()
	await msg.delete()
	deltt = time.monotonic() - delt
	a = int(cl.latency * 1000)
	nw = dt.datetime.utcnow()
	ave = round((1000*(send+deltt+ract+edt)+a)/5)
	print("average ping >_ ", ave)
	if ave <= 500: sttcolor = 0xbff9d2 #stronk
	elif ave > 500 and ave <= 1500: sttcolor = 0xffffd7 #nỏm
	elif ave > 1500: sttcolor = 0xff8c8c #weamk 
	await ctx.send(
		embed = discord.Embed(
			title="BONK! :l ", description=(
				f"**Send:** ```>_ { send*1000:.1f}ms ``` \n"
				f"**Bot Latency:** ```>_ { a}ms ``` \n"
				f"**Delete:** ```>_ { deltt*1000:.1f}ms ```\n"
				f"**React:** ```>_ { ract*1000:.1f}ms ```\n"
				f"**Edit:** ```>_ { edt*1000:.1f}ms ```\n"
				f"_Finished: {nw}_"
				),color=sttcolor))
@commands.has_permissions(manage_messages=True)
@cl.command(name="EC", pass_context=True)
async def EC(ctx, *, rep):
	await ctx.message.delete()
	await ctx.send(rep)
	
@cl.command(name="ResP")
async def ResP(ctx):
	global exc
	exc = 1
	abc1 = ctx.message.guild
	vc = abc1.voice_client
	vc.resume()

@cl.command(name="Kill", pass_context=True)
async def Kill(ctx):
	await ctx.message.delete()
	try:
		vc =  ctx.message.guild.voice_client
		await vc.disconnect()
	except: pass
	# await ctx.send('*OOF*')
	quit()
@cl.command(name="StopP")
async def StopP(ctx):
	try:
		await ctx.send("*stopped playing music*")
		vc =  ctx.message.guild.voice_client
		await vc.disconnect()
	except: return
# <Still working on....
# @cl.command(name="Vol")
# async def Vol(ctx, *,volum:float):
# 	global volume1
# 	volume1 = volum
# 	ctx.send(" Volume set: {volume1}%")
# 	if 0 <= volume1 <= 100:
# 		volume1 = volume1 / 100
# 	else:
# 		await ctx.send("limited volume unit is 100 and 0 ")
@cl.command(name="SaveList")
async def SaveList(ctx):                                                                                                          
	pass
#/>

''' phân [fun] '''
#convert thingy
@cl.command(name="STR2ASCII")
async def STR2ASCII(ctx,opt=None,*, txt:str):
	c = ''
	for chim in txt:
		v = str(ord(chim))
		c += v+' '
	if opt ==None:
		await ctx.send(embed=discord.Embed(title="Here's your output [TEXT --> ASCII]:", 
			description=f"```py\n >_ {c}```",
			color=0xfbf8b7))
	elif opt.lower() == "--rm-spc":
		c = c.replace(' ','')
		await ctx.send(embed=discord.Embed(title="Here's your output [TEXT --> ASCII]:", 
			description=f"```py\n >_ {c}```",
			color=0xfbf8b7))
@cl.command(name="ASCII2STR")
async def ASCII2STR(ctx,*,ASCII:str):
	cc=''
	ASCII11 = ASCII.replace(' ',',')
	ASCII1 = ASCII11.split(',')
	for ASCII2 in ASCII1:
		cvrt = chr(int(ASCII2))
		cc += cvrt
	await ctx.send(embed=discord.Embed(title="Here's your output [ASCII --> TEXT]:", 
		description=f"```py\n >_ {cc}```",
		color=0xfbf8b7))
@cl.command(name="STR2BIN")
async def STR2BIN(ctx,opt=None,*,txt1):
	cc2 = ''
	for ch in txt1:
		vv  = str(bin(ord(ch)))
		vv1  = list(vv)
		for x in range(0,2):
			vv1[x] = ''
		vvx = ''.join(vv1)
		cc2 += vvx+' '
	if opt == None:
		await ctx.send(embed=discord.Embed(title="Here's your output [TEXT --> BINARY]:", 
			description=f"```py\n >_ {cc2}```",
			color=0xfbf8b7))
	elif opt.lower() == "--rm-spc":
		cc2 = cc2.replace(" ",'')
		await ctx.send(embed=discord.Embed(title="Here's your output [TEXT --> BINARY]:", 
			description= f"```py\n >_ {cc2}```",
			color=0xfbf8b7))
@cl.command(name="BIN2STR")
async def BIN2STR(ctx,*,bi,opt=None):
	cc3=''
	result=''
	b1 = bi.replace(' ',',').split(',')
	for k in b1:
		c1 = "0b"+k
		cc3 += c1+','
	ub = cc3.split(',')
	for bb in ub:
		try:
			fx = ''.join(bb)
			cvbt = chr(int(fx[:0xFF].encode("UTF-8"),2))
			result += cvbt
		except:pass
	await ctx.send(embed=discord.Embed(title="Here's your output [BINARY --> TEXT]:", 
		description=f" ```py\n >_ {result}```",
		color=0xfbf8b7))

ans=0
calc =0
a = 1
@cl.command(name="Math")
async def Math(ctx,*,val:str):
	global ans,calc
	try:
		calc = eval(val)
		ans = calc
		a = 1
	except ZeroDivisionError:
		await ctx.send(embed=discord.Embed(title="ERROR! ;/", 
		description=f"```Cannot divide by zero!```",
		color=0xff8c8c))
		a = 0
	except ValueError:
		await ctx.send(embed=discord.Embed(title="ERROR! ;/", 
		description=f"```Bad Value!```",
		color=0xff8c8c))
		a = 0
	except SyntaxError:
		await ctx.send(embed=discord.Embed(title="ERROR! ;/", 
		description=f"```Syntax Error!```",
		color=0xff8c8c))
		a = 0
	except Exception:
		cc = val.lower().replace(' ',',').split(',')
		for x in range(0,len(cc)):
			if cc[x].lower() == "ans":
				cc[x] = ans
		vb = ''.join(cc)
		calc = eval(vb)
	if a == 1:
		await ctx.send(embed=discord.Embed(title="Here's your calculation result:", 
			description=f"```py\n >_ {calc}```",
			color=0x48f898))
# cvt1=0
# cvt2=0
# @cl.command(name="ConvertU")
# async def ConvertU(ctx, para,*,un:float ):
# 	global cvt1,cvt2
# 	a1 = ["km->m","kg->g",'kw->w','kj->j','m->mm','g->mg']
# 	a2 = ["m->km","g->kg",'w->kw','j->kj','mm->m','mg->g']
# 	for x in a1:
# 		if para.lower() == x:
# 			cvt1 = un*1000
# 		break
# 		await ctx.send(embed=discord.Embed(title=f"{para.lower()}", 
# 			description=f"{cvt1}{para[3]+para[4]}",
# 			color=0xfbf8b7))
# 	for x1 in a2:
# 		if para.lower() == x1:
# 			cvt2 = un/1000
# 		break
# 	await ctx.send(embed=discord.Embed(title=f"{para.lower()}", 
# 		description=f"{cvt2}{para[3]+para[4]}",
# 		color=0xfbf8b7))
@cl.command(name="TmdEC")
async def TmdEC(ctx,dly=0.5,*,tc):
	await ctx.message.delete()
	msg = await ctx.send("‎")
	xs = ''
	for bb in tc:
		xs += bb
		await msg.edit(content=f"{xs}")
		await asc.sleep(dly)
@cl.command(name="Susify")
async def Susify(ctx, *, wd2):
	sus = amogusify(wd2,True)
	if wd2.lower() == "your self" or wd2.lower() == "ur self":
		
		cus =["Im already sus ig", "RetardGus","you sus",'im sus']
		sus = rd.choice(cus) 
	await ctx.send(sus)
@cl.command(name="Reverse")
async def Reverse(ctx,*,wd):
	await ctx.send(f"{wd[::-1]}")
@cl.command(name="RNG")
async def RNG(ctx,fro:int,to:int):
	RNG = rd.randint(fro,to)
	cc = await ctx.send(embed=discord.Embed(title=f"Here's your random number [FROM {fro} to {to}]:", 
		description=f" ```py\n >_ {RNG}```",
		color=0xfbf8b7))
	await cc.add_reaction("🔁")
	def refresh(rec,u):
		return u != cl.user and str(rec.emoji) == "🔁"
	while 1:
		try:
			rec, u = await cl.wait_for("reaction_add", check=refresh, timeout=1)
			if str(rec.emoji) == '🔁':
				RNG = rd.randint(fro,to)
				emb = discord.Embed(title=f"Here's your random number [FROM {fro} to {to}]:", 
				description=f" ```py\n >_ {RNG}```",
				color=0xfbf8b7)
				await cc.edit(embed = emb)
				await cc.remove_reaction("🔁",u)

		except asc.TimeoutError:
			await cc.remove_reaction("🔁",ctx.author)
		except: pass
#process image thingy
@cl.command(name="InvertUsr")
async def InvertUsr(ctx, usr:Member = None):
	if usr == None:
		usr = ctx.author
	cc = usr.avatar_url 
	g = Image.open(BytesIO(await cc.read()))
	res = Image.open(g).convert("RGBA")
	res.save("cc.png")
	await ctx.send(file=discord.File("cc.png"))
	await ctx.message.delete()
@cl.command(name="Avt")
async def Avt(ctx,usr:Member = None):
	if usr == None:
		usr = ctx.author
	get = usr.avatar_url
	await ctx.send(get)
@cl.command(name="Tutel")
async def Tutel(ctx,*,inp):
	comm = ["right:","turnbott:"]
	pass

@cl.event 
@has_permissions(kick_members = True)
@commands.has_permissions(manage_messages=True)
async def on_message(message):
	global  k,b, StBd
	  
	inp = message.content 
	d = list(inp.strip().lower().split(' '))
	for i in range(0,len(d)):
		try:
			print(d[i])
			for j in range(0,len(b)):
				if d[i] == b[j]:
					k += 1
					await message.delete()
					await message.channel.send(f" {message.author.mention} NO BAD WORDS!!!!!!!, CAUTION(s):{k}")
			for jk in range(0,len(StBd)):
				if d[i] == StBd[jk]:
					k += 1
					await message.delete()
					await message.channel.send(f" {message.author.mention} NO BAD WORDS!!!!!!!, CAUTION(s):{k}")
		except: return
		if k >= 10:
			g = message.guild
			mtdRole = discord.utils.get(g.roles, name="eats shit")
			if not mtdRole:
				mtdRole = await g.create_role(name="eats shit")
			for gc in g.channels:
				await gc.set_permissions(mtdRole, speak=True, send_messages=False, read_message_history=True, read_messages=True)
			await message.channel.send(f'User {message.author} has been muted, reason: swearing abuse')
			# await message.channel.send(embed=emb)
			await member.add_roles(mutedRole, reason=None)
			k = 0
	else: 
		try: await cl.process_commands(message)
		except: pass 
	if message.author == cl.user:
	    return
	if message.content.lower() == 'hello' or message.content.lower() == 'hi' or message.content.lower() == 'lô':
	    await message.channel.send(rd.choice(a))
	if message.content.lower() == "!wake":
		await message.delete()
		quit()
	if message.content.startswith('~RunLk='):
		w.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(message.content[len('~RunLk')+1:].format(message))
		#print(message.content[len('~RunLk')+1:].format(message))
	if message.content.startswith('?SearchYT='):
		p = message.content[len('?SearchYT')+1:].format(message)
		w.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(f'https://www.youtube.com/results?search_query={p}')
	if message.content.startswith('?SearchGG='):
		p1 = message.content[len('?SearchGG')+1:].format(message)
		w.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open(f'https://www.google.com/search?q={p1}')
	if message.content.startswith('~ShutdownC'):
		try:
			os.system('shutdown /s /t 10')
		except:
			os.system('shutdown now -h')
		await message.delete()
		await message.channel.send("i shat myself and i'm dying...")
		print(message.content[len('~RunLk')+1:].format(message))
	if message.content.startswith("?SPrefix"):
		with open("prefix.json", "r") as c:
			prefx = js.load(c)
		emb = discord.Embed(title = "*CHECKING SERVER(S) PREFIX*", description=f"```Server Prefix (JSON): {prefx} ```", color=0xfbf8b7)
		await message.channel.send(embed=emb)
	if message.content.startswith("birthday"):
		with open("evt.json","r") as wt:
			mn = js.load(wt)
			dr = f"{message.content[len('birthday')+1:].format(message)}"
			cx = f"{message.author}"
		mn["birthday"].update({dr:cx})
		with open("evt.json","w") as wr:
			js.dump(mn,wr,indent=4)
		emb = discord.Embed(title = f"*ADDED {message.author} BIRTHDAY!*", description=f"``` {message.author} birthday is {message.content[len('birthday')+1:].format(message)} \ud83c\udf82 \ud83c\udf81 !!! ```", color=0xbcbcfc)
		await message.channel.send(embed=emb)
		# print(message.content[len('birthday')+1:].format(message))
	

sec = 60		
@tasks.loop(seconds=sec)
async def doingstuff():
	global ngu
	global sec 
	with open("evt.json","r") as m:
		mn = js.load(m)
	dtt = date.today()
	xk = dtt.strftime("%m/%d")
	for fh in range(0,len(mn["Events"])):
		# print(list(mn["Events"])[fh])
		if xk == list(mn["Events"])[fh]:
			g = ''.join(list(mn['Events'][xk]))
			# print(g)
			await cl.change_presence(activity=discord.Game(f' \ud83c\udf82 !!EVENT TODAY!!: {g} '))
		elif xk != list(mn["Events"])[fh] : await cl.change_presence(activity=discord.Game(rd.choice(ngu)))


with open("tok.txt","r") as t:
	for x in t: tok = x
cl.run(tok)
