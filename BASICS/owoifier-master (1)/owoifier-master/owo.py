import discord
import random



users = {}

client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    print('Servers connected to:')
    for server in client.servers:
        print(server.name)

        
        
@client.event
async def on_guild_join(guild):
    allowedID = [536447514447183892]
    if guild.id not in allowedID:
        await guild.leave()
    
    name = "OwOifiew"
    command1 = "**~OwO** *your message here*"
    command2 = "~Hewp"
    
    join_message = """H-hewwo {}
I'm {} (。U⁄ ⁄ω⁄ ⁄ U。) cweated by b9king#6857
My commands awe:
{}
{}
You can suppowt my cweatow hewe:  ( °꒳° ) https://www.patreon.com/b9king
    """.format(guild.name,name,command1,command2)    
    
    x = guild.channels
    y = False
    
    for i in x:
        if i.permissions_for(guild.me).send_messages and not y:
            print(i)
            x = i
            break
    await x.send(join_message)

  
@client.event
async def on_message(message):
    
    
    
    if message.content.startswith("~Hewp"):
        help = """T-thanks fow downwoading the OwO-oifiew
To use this bot pwease type +AH4-OwO Youw message hewe
To suppowt futuwe pwojects and weawn how to make something wike this pwease visit:
https://www.patreon.com/b9king
"""
         #_________________________________________________________________
#________________Help Command_____________________________________



    elif message.content.startswith("(debug 124 owo)"):
        x = message.content.replace("(debug 124 owo)","")
        await client.change_presence(status=discord.Status.online, activity=discord.Game(x))
    
    
    elif message.content == "~Help OwO":
        name = "**OwOifier**"
        command1 = "**~OwO (your message here)**"
        command2 = "**~Conditions** (us zipcode)"
        command3 = "**~Forecast** (us zipcode)"
        command4 = "**~Alerts** (us zipcode)"
        
        Helpmessage = """
        **Thanks for adding me to {}**!
        I-i take any message you give me and tuwn it into an OwO message
        I-i am abwe to intewact with othew bots who output ~OwO the at the stawts of theiw message (⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡

        My commands are:
        {}
        **Click the embed to support my creator**
        """.format(message.guild.name,command1)
        
        embed=discord.Embed(title="OwOifier Help", url="https://www.patreon.com/b9king", description= Helpmessage, color=0x00ffff)
        embed.set_thumbnail(url="https://files.catbox.moe/g2i27n.png")
        await message.channel.send(embed=embed)   
        
        await message.channel.send(help)
    if message.content.startswith("~OwO") and message.author.id != "589675076945969152":
        jesus = message.channel
        message = message.content.replace("~OwO ", "" )
        message = message.replace("~OwO","")
        message = message.replace("OwO","")
        faces = ['(ᵘʷᵘ)',
 '(ᵘﻌᵘ)',
 '(◡ ω ◡)',
 '(◡ ꒳ ◡)',
 '(◡ w ◡)',
 '(◡ ሠ ◡)',
 '(˘ω˘)',
 '(⑅˘꒳˘)',
 '(˘ᵕ˘)',
 '(˘ሠ˘)',
 '(˘³˘)',
 '(˘ε˘)',
 '(´˘`)',
 '(´꒳`)',
 '(˘˘˘)',
 '( ᴜ ω ᴜ )',
 '( ´ω` )۶',
 '(„ᵕᴗᵕ„)',
 '(*ฅ́˘ฅ̀*)',
 '(ㅅꈍ ˘ ꈍ)',
 '(⑅˘꒳˘)',
 '( ˘ᴗ˘ )',
 '(ᵕᴗ ᵕ⁎)',
 ' *:･ﾟ✧(ꈍᴗꈍ)✧･ﾟ:* *˚*',
 '(ꈍ ω ꈍ).₊̣̇.',
 ' (。U ω U。) ',
 '(。U⁄ ⁄ω⁄ ⁄ U。)',
 ' (U ᵕ U❁) ',
 '(U ﹏ U)',
 ' (◦ᵕ ˘ ᵕ◦)',
 ' ღ(U꒳Uღ)',
 ' ♥(。U ω U。)',
 ' – ̗̀ (ᵕ꒳ᵕ) ̖́- ',
 ' ಇ( ꈍᴗꈍ)ಇ ',
 'ᕦ( ˘ᴗ˘ )ᕤ ',
 '(⁄˘⁄ ⁄ ω⁄ ⁄ ˘⁄)♡ ',
 '( ͡U ω ͡U )',
 ' ( ͡o ᵕ ͡o ) ',
 '( ͡o ꒳ ͡o )',
 ' (❀˘꒳˘)♡',
 '(˘꒳˘❀)',
 ' ( ˊ.ᴗˋ )',
 ' (灬´ᴗ`灬)',
 ' [̲̅$̲̅(̲̅ ᵕ꒳ᵕ)̲̅$̲̅]',
 ' ★⌒ヽ(˘꒳˘ *) ',
 '( ˶˘ ³˘',
 '(ᵕ꒳ᵕ)*₊˚♡',
 'OwO',
 ' Owo',
 ' owO',
 ' ÓwÓ ',
 'ÕwÕ ',
 '@w@ ',
 'ØwØ',
 ' øwø ',
 'uwu',
 ' ☆w☆ ',
 '✧w✧ ',
 ' ♥w♥',
 ' ゜w゜',
 ' ◕w◕ ',
 'ᅌwᅌ',
 ' ◔w◔',
 ' ʘwʘ ',
 '⓪w⓪ ',
 '︠ʘw ʘ ',
 '(owo)',
 '𝕠𝕨𝕠',
 ' 𝕆𝕨𝕆 ',
 '𝔬𝔴𝔬',
 ' 𝖔𝖜𝖔 ',
 '𝓞𝔀𝓞',
 ' 𝒪𝓌𝒪',
 ' 𝐨𝐰𝐨 ',
 '𝐎𝐰𝐎 ',
 '𝘰𝘸𝘰 ',
 '𝙤𝙬𝙤 ',
 '𝙊𝙬𝙊 ',
 '𝚘𝚠𝚘 ',
 'σωσ ',
 'OɯO',
 ' oʍo',
 ' oᗯo',
 ' ๏w๏',
 ' o̲wo',
 '̲ ᎧᏇᎧ',
 ' օաօ',
 '(。O ω O。)',
 ' (。O⁄ ⁄ω⁄ ⁄ O。) ',
 '(O ᵕ O)',
 ' (O꒳O) ',
 'ღ(O꒳Oღ)',
 ' ♥(。ᅌ ω ᅌ。)',
 ' (ʘωʘ) ',
 '(⁄ʘ⁄ ⁄ ω⁄ ⁄ ʘ⁄)♡',
 ' ( ͡o ω ͡o )',
 ' ( ͡o ᵕ ͡o )',
 ' ( ͡o ꒳ ͡o ) ',
 '( o͡ ꒳ o͡ )',
 ' ( °꒳° ) ',
 '( °ᵕ° ) ',
 '( °﹏° )',
 ' ( °ω° )',
 ' ̷(ⓞ̷ ̷꒳̷ ̷ⓞ̷) ',
 '（ ゜ω 。）']
        
        message = message.replace("l","w")
        message = message.replace("r","w")
        message = message.replace("L","W")
        message = message.replace("R","W")
        message = message.replace("ove","uv")
        message = message.replace("your","yow")
        message = message.replace("Your","Yow")     
        message = message.replace("hey","haiii")
        message = message.replace("Hey","Haiii")
        
        x = ['!', ',', '.']
        
        y = ""
        
        end = False
        
        if message[-1] in x:
            end = True
        
        for i in message:
            if i in x:
                y += " " + random.choice(faces)
            elif i.isupper():
                if random.randint(1,10) in [1,2,3]:
                    y += "{}-{}".format(i,i.lower())
                else:
                    y += i
            else:
                y += i
                    
    
        
        
        if not end:
            y+= " " + random.choice(faces)
        
        
        await jesus.send(y)
                
   
client.run('NTg5Njc1MDc2OTQ1OTY5MTUy.XQXIWg.4ZFKB3J-xjHWrGbfhvbiJ_FoMFo') 
