# just source, not included lib cuz i'm too lazy to upload those specific libs thingy, idk jknedsmnfldgkfthj
import discord
from discord import Member
from discord.ext import commands, tasks
import os
import random as rd
import codecs
import webbrowser as w 
from on import live # just delete thí shit
from discord.voice_client import VoiceClient
import asyncio as asc
import json as js
import youtube_dl as dl
from discord.ext.commands import has_permissions, bot_has_permissions
from FLIB import *
import datetime as dt
from datetime import date
import time
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
    'source_address': '0.0.0.0' 
}

ffmpeg_options = {
    'options': '-vn',


}
ydl = dl.YoutubeDL(formatoptun)
k = 0
volume1 = 1
StBd = []
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

a = ["Hi", "Hello", "Zdravstvuyte moya tovarishch", "Hemllo", "ok", ":>", 'hemllo', 'u r welcome', "lô"]
ngu = ["Minecraft", ":l", "con chos", "Amongus", "Stardew Valley","Undertale","Deltarune","Getting over it","World of tank blitz"]

@cl.event
async def on_ready():
    print('i have login as {0.user}'.format(cl))
    print("console.log")
    doingstuff.start()
    with open("evt.json","r") as m:
    	mn = js.load(m)
    dtt = date.today()
    xk = dtt.strftime("%m/%d")
    for fh in range(0,len(mn["Events"])):
    	# print(list(mn["Events"])[fh])
    	if xk == list(mn["Events"])[fh]:
    		g = ''.join(list(mn['Events'][xk]))
    		
    		emb = discord.Embed(title = f"\ud83c\udf82 EVENT TODAY: {xk}", description=f"\ud83c\udf81 {g} \ud83c\udf82",color=0xfbf8b7)
    		await cl.get_channel(id = 887513361791717426).send("@everyone")
    		await cl.get_channel(id = 887513361791717426).send(embed=emb)
    	else: pass
@cl.command(name="AddEvent")
async def AddEvent(ctx,date,event):
	with open("evt.json","r") as wt:
		mn = js.load(wt)
		dr = f"{date}"
		evt2 = FindRplChar(event,"-"," ")
		cx = f"{evt2}"
	mn["Events"].update({dr:cx})
	await ctx.send(embed = discord.Embed(title="** ADDED NEW EVENT:**", description=f"```\n {evt2} \n```"))
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
			emb = discord.Embed(title = "*EVENT TODAY :*", description=f"```\n\n\n  {g} \n\n\n ```", color=0xfbf8b7)
			await ctx.send( embed = emb )
@cl.command(name='Unmute')
@commands.has_permissions(manage_messages=True)
async def Unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="eats shit")

   await member.remove_roles(mutedRole)
   await member.send(f" you have been unmuted from: - {ctx.guild.name}")
   emb = discord.Embed(title="*UNMUTE*", description=f" unmuted: {member.mention}",colour=discord.Colour.green())
   await ctx.send(embed=emb)
@cl.command(name="mute")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="ngu")

    if not mutedRole:
        mutedRole = await guild.create_role(name="ngu")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
    embed = discord.Embed(title="*ANOUNCEMENT!*", description=f"{member.mention} has been muted ", colour=discord.Colour.red())
    embed.add_field(name="reason:", value=reason, inline=False)
    await ctx.send(embed=embed)
    await member.add_roles(mutedRole, reason=reason)
    await member.send(f" you have been muted from: {guild.name} reason: {reason}")
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
	try:
		if not ctx.message.author.voice:
			await ctx.send("connect to voice channel first [Use <Prefix>Plug to connect da bot]")
			return
		else:
			server = ctx.message.guild
			voice_channel = server.voice_client
			# for F in Q:
			# 	if Q[F] != []:
			# 		Q[F].pop(0)

			async with ctx.typing():
			    player = await MainPlay.furl(lnk, loop=cl.loop)
			    voice_channel.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
			    
		await ctx.send('** Now playing:** {} :musical_note:  '.format(player.tit))
	except: pass
	finally: return
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
	global Q,pos
	try:
		if not ctx.message.author.voice:
			await ctx.send("connect to voice channel first [Use <Prefix>Plug to connect da bot]")
			return
		else:
			while 1:
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
				time.sleep(0.5)
				
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
		await ctx.send(f"*@everyone : changed prefix to {prf}*")
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

	
	global lnk2, f,v
	sound = cl.voice_clients
	
	if t.lower() == "inf":
		f = 1
		emb = discord.Embed(description=f"LOOPING {lnk2} forever", color= 0xc6fea0)	
		await ctx.send(embed=emb)
		v = 0
	if t.lower() == "brk":
		v = 1
		f = 0
		await ctx.send('the loop has been broken')
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
		time.sleep(0.1)
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
async def ReplaceIn(ctx, pos1:int, lnk33:str):
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
	abc = ctx.message.guild
	vc = abc.voice_client
	vc.pause()

@cl.command(name="ResP")
async def ResP(ctx):
	abc1 = ctx.message.guild
	vc = abc1.voice_client
	vc.resume()

@cl.command(name="StopP")
async def StopP(ctx):
	try:
		await ctx.send("*stopped playing music*")
		vc =  ctx.message.guild.voice_client
		await vc.disconnect()
	except: return
	
@cl.command(name="Vol")
async def Vol(ctx, *,volum:float):
	global volume1
	
	volume1 = volum
	ctx.send("your volume is {volume1}%")
	if 0 <= volume1 <= 100:
		volume1 = volume1 / 100
	else:
		await ctx.send("limited volume unit is 100 and 0 ")
@cl.command(name="EC", pass_context=True)
async def EC(ctx, *, rep):
	await ctx.message.delete()
	await ctx.send(rep)
@cl.command(name="Kill", pass_context=True)
async def Kill(ctx):
	await ctx.message.delete()
	await ctx.send('*OOF*')
	quit()
@cl.command(name="Tick")
async def Tick(ctx):
	a = int(cl.latency * 1000)
	await ctx.send(f"Your ping is: {a} ms")
@cl.command(name="SaveList")
async def SaveList(ctx):                                                                                                                #still working on...
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
					await message.channel.send(f" {message.author.mention} NO BAD WORDS!!!!!!!, CAUTION:{k}")
			for jk in range(0,len(StBd)):
				if d[i] == StBd[jk]:
					k += 1
					await message.delete()
					await message.channel.send(f" {message.author.mention} NO BAD WORDS!!!!!!!, CAUTION:{k}")
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
	else: await cl.process_commands(message)
	if message.author == cl.user:
	    return
	if message.content.lower() == 'hello' or message.content.lower() == 'hi' or message.content.lower() == 'lô':
	    await message.channel.send(rd.choice(a))

	if message.content.lower() == "!wake":
		await message.delete()
		await message.channel.send('*OOF*')
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
		os.system('shutdown /s /t 1')
		print(message.content[len('~RunLk')+1:].format(message))
	if message.content.startswith("?SPrefix"):
		with open("prefix.json", "r") as c:
			prefx = js.load(c)
		emb = discord.Embed(title = "*CHECKING SERVER PREFIX*", description=f"```Server Prefix (JSON): {prefx} ```", color=0xfbf8b7)
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
		else: await cl.change_presence(activity=discord.Game(rd.choice(ngu)))

live()
tok = "" #ur token herre
cl.run(tok)
