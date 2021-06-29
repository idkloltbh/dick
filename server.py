import discord
from discord.ext import commands
import requests
import json
import os
import time
#читаем переменные из .env
settings={"token":(os.getenv("ODE5ODc4MTY4NDg3OTE5NjI2.YEtBCw.fSntywwKfVmkwV97MaVRguqFHK4")),"name":(os.getenv("BOTNAME")),"id":int((os.getenv("ID"))),"prefix":(os.getenv("PREFIX"))}
proxy=os.getenv("PROXY")
#делаем самого бота с префиксом
client=commands.Bot(command_prefix=settings['prefix'])
#команды от бота
@client.command() 
#команда commands (список команд)
async def commands(ctx):
    embed=discord.Embed(title="Commands list")
    embed.add_field(name="Just Dance Unlimited", value="!getnohuds <codename>\n!getsku <codename>\n!gettextures <codename>", inline=False)
    embed.add_field(name="Checking", value="!checkjdu <codename>\n!checkjdchn <codename>", inline=False)
    embed.add_field(name="Decryption", value="!decjd14 <timeline.tpl.ckd>\n!decjd15tapes <tape>\n!decjd15musictrack <musictrack>", inline=False)
    await ctx.send(embed=embed)
    print("[LOG] Command !commands, time: " + str((time.time())))
@client.command() 
#команда getnohuds (получить nohuds из jdu)
async def getnohuds(ctx, codename):
    response = requests.get('https://heyimyunyl.tk/jdu/nohud/' + codename)
    try:
      json_data = json.loads(response.text)
      try:
        embed=discord.Embed(title=codename + " no-huds")
        embed.add_field(name="ULTRA webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_ULTRA.webm']), inline=False)
        embed.add_field(name="ULTRA.hd webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_ULTRA.hd.webm']), inline=True)
        embed.add_field(name="MID webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_MID.webm']), inline=True)
        embed.add_field(name="MID.hd webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_MID.hd.webm']), inline=True)
        embed.add_field(name="LOW webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_LOW.webm']), inline=True)
        embed.add_field(name="LOW.hd webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_LOW.hd.webm']), inline=True)
        embed.add_field(name="HIGH webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_HIGH.webm']), inline=True)
        embed.add_field(name="HIGH.hd webm", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '_HIGH.hd.webm']), inline=True)
        embed.add_field(name="Audio", value=str(json_data['urls']['jmcs://jd-contents/' + codename + '/' + codename + '.ogg']), inline=True)
        embed.set_footer(text="Thanks for using!")
        await ctx.send(embed=embed)
        print("[LOG] Command !getnohuds, time: " + str((time.time())))
      except KeyError:
        await ctx.send("Bot can't find NO-HUDs")
    except json.decoder.JSONDecodeError:
      await ctx.send("Bot can't find NO-HUDs")
@client.command() 
#команда getsku (получить sku)
async def getsku(ctx, codename):
    orbis=json.load((open("public/skupackages/orbis.json")))
    pc=json.load((open("public/skupackages/pc.json")))
    nx=json.load((open("public/skupackages/nx.json")))
    ggp=json.load((open("public/skupackages/ggp.json")))
    try:
      skuorbis = orbis[codename + '_mapContent']['url']
    except KeyError:
      skuorbis = "Bot haven't found ORBIS SKU!"
    try:
      skupc = pc[codename + '_mapContent']['url']
    except KeyError:
      skupc = "Bot haven't found PC SKU!"
    try:
      skunx = nx[codename + '_mapContent']['url']
    except KeyError:
      skunx = "Bot haven't found NX SKU!"
    try:
      skuggp = ggp[codename + '_mapContent']['url']
    except KeyError:
      skuggp = "Bot haven't found GGP SKU!"
    embed=discord.Embed(title=codename + " skus")
    embed.add_field(name="GGP", value=str(skuggp), inline=False)
    embed.add_field(name="NX", value=str(skunx), inline=False)  
    embed.add_field(name="ORBIS", value=str(skuorbis), inline=True)
    embed.add_field(name="PC", value=str(skupc), inline=False)
    embed.set_footer(text="Thanks for using!")
    await ctx.send(embed=embed)
    print("[LOG] Command !getsku, time: " + str((time.time())))
@client.command() 
#команда gettextures (получить текстурки из jdu)
async def gettextures(ctx, codename):
    try:
      songdb=json.load((open("public/songdb.json")))
      try:
        embed=discord.Embed(title=codename + " textures")
        try:
          embed.add_field(name=codename + "_banner_bkg.tga.ckd", value=str(songdb[codename]["assets"]["phoneCoach1ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_map_bkg.tga.ckd", value=str(songdb[codename]["assets"]["map_bkgImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_coach_1.tga.ckd", value=str(songdb[codename]["assets"]["coach1ImageUrl"]), inline=False)
          embed.add_field(name=codename + "_coach_1_phone.png", value=str(songdb[codename]["assets"]["phoneCoach1ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_coach_2.tga.ckd", value=str(songdb[codename]["assets"]["coach2ImageUrl"]), inline=False)
          embed.add_field(name=codename + "_coach_2_phone.png", value=str(songdb[codename]["assets"]["phoneCoach2ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_coach_3.tga.ckd", value=str(songdb[codename]["assets"]["coach3ImageUrl"]), inline=False)
          embed.add_field(name=codename + "_coach_3_phone.png", value=str(songdb[codename]["assets"]["phoneCoach3ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_coach_4.tga.ckd", value=str(songdb[codename]["assets"]["coach4ImageUrl"]), inline=False)
          embed.add_field(name=codename + "_coach_4_phone.png", value=str(songdb[codename]["assets"]["phoneCoach4ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_generic.tga.ckd", value=str(songdb[codename]["assets"]["coverImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_online.tga.ckd", value=str(songdb[codename]["assets"]["cover_smallImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_phone.jpg", value=str(songdb[codename]["assets"]["phoneCoverImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_1024.png", value=str(songdb[codename]["assets"]["cover_1024ImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_albumbkg.tga.ckd", value=str(songdb[codename]["assets"]["expandBkgImageUrl"]), inline=False)
        except KeyError:
          pass
        try:
          embed.add_field(name=codename + "_cover_albumcoach.tga.ckd", value=str(songdb[codename]["assets"]["expandCoachImageUrl"]), inline=False)
        except KeyError:
          pass
        embed.set_footer(text="Thanks for using!")
        await ctx.send(embed=embed)
        print("[LOG] Command !gettextures, time: " + str((time.time())))
      except KeyError:
        embed=discord.Embed(description="Bot haven't found NO-HUDs")
        await ctx.send(embed=embed)
    except json.decoder.JSONDecodeError:
      embed=discord.Embed(description="Bot haven't found NO-HUDs")
      await ctx.send(embed=embed)
@client.command() 
#команда checkjdu (получить placeholder)
async def checkjdu(ctx, codename):
    songdb=json.load(open("public/songdb.json"))
    try:
      songinfo=songdb[codename]
      embed=discord.Embed(title="Result", url=songinfo["assets"]["phoneCoverImageUrl"], description=codename + ' exists on JDU server')
      embed.set_footer(text="Thanks for using!")
      await ctx.send(embed=embed)
    except KeyError:
      response = requests.get('http://jd-s3.akamaized.net/public/map/' + codename + '/' + codename + '_banner_bkg.jpg/a69d3bd23a3bdbf04f4726ab8dd4771f.jpg')
      if response.status_code == 200:
        embed=discord.Embed(title="Result", url='http://jd-s3.akamaized.net/' + codename + '/' + codename + '_banner_bkg.jpg/a69d3bd23a3bdbf04f4726ab8dd4771f.jpg', description=codename + ' exists on JDU server')
        embed.set_footer(text="Thanks for using!")
        await ctx.send(embed=embed)
      else:
        embed=discord.Embed(description=codename + ' does not exist on JDU servers')
        await ctx.send(embed=embed)
@client.command() 
#команда checkjdchn (получить placeholder)
async def checkjdchn(ctx, codename):
    response = requests.get('https://jd.ubicdn.com/assets/maps/' + codename + '/cover.jpg')
    jsonfile=json.loads(requests.get('https://jd.ubicdn.com/assets/mapsconf/' + codename + '.json').text)
    if response.status_code == 200:
      embed=discord.Embed(title="Result", url='https://jd.ubicdn.com/assets/mapsconf/' + codename + '.json', description=jsonfile["title"] + ' by ' + jsonfile["artist"]  + ' exists on JDCHN confguration server')
      embed.set_footer(text="Thanks for using!")
      await ctx.send(embed=embed)
    else:
      embed=discord.Embed(description=codename + ' does not exist on JDCHN confguration server')
      await ctx.send(embed=embed)
@client.command() 
#команда decjd14
async def decjd14(ctx, codename):
    pass
#запускаем бота
print("[LOG] Bot started!")
client.run(settings['token'])
