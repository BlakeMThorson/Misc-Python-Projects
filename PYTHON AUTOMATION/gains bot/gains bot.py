import pyautogui
import time
import os


#_______________________________updating sheet____________________________________________
#_________________________________________________________________________________________
def updateSheet():
    #open program
    os.startfile('a.exe')
    #wait
    print("OPENING WINDOW")
    time.sleep(3)
    print("waiting for USB DETECTION")
    time.sleep(5)
    print("starting")
    #enter right right right enter left enter
    pyautogui.typewrite(['right', 'right', 'enter', 'enter','right', 'right',  'enter', 'right', 'enter', 'right', 'right', 'enter','left','enter'], interval=.25)
    pyautogui.hotkey('alt', 'f4')
    #close program

#_____________________________READING SHEET_______________________________________________
#_________________________________________________________________________________________
def getLastWorkout():
    import csv
    with open('LogBook.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        rows = list(csv_reader)
    
    toReturn = {}
    
    for i in range(len(rows[5])):
        toReturn[rows[3][i]] = rows[5][i]
        
        if rows[6][i] != "":
            toReturn[rows[3][i]] = rows[6][i]
            
    
    meters = 0
    #updating meters
    print(len(rows))
    for i in range(len(rows)):
        print(i)
        if i >= 6:
            if len(rows[i]) == 0:
                break
                
            else:
                meters += int(rows[i][10])
    
    
    
    toReturn["Meters"] = str(meters)
            
        
            
    
        
    return toReturn


#_______________________EMBED MAKER______________________________________________________
#________________________________________________________________________________________
#______________________________DISCORD BOT PART__________________________________________
#________________________________________________________________________________________


import discord
import random
import asyncio
client=discord.Client()

@client.event
async def on_ready():
    print('logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')
    

loop = asyncio.get_event_loop()

async def sendMessage(workout):
    await asyncio.sleep(3)
    channel = client.get_channel(660459367287619586)
    embed=discord.Embed(title="Benign King's Rowing Gains", color=0xfbdcc0, url = "https://benignking.xyz/" )
    embed.set_thumbnail(url="https://www.ssbwiki.com/images/f/f9/Dancer_Spirit.png")
    
    embed.add_field(name="*** Date / Time ***", value="{} \n {}".format(workout["Date"],workout["Time of Day"]), inline=True)
    
    embed.add_field(name="*** Total Time ***", value="{}".format(workout["Workout Name"]), inline=True)
    
    embed.add_field(name="*** Total Meters ***", value="{}".format(workout["Meters"]), inline=True)
    
    embed.add_field(name="*** Average 500m ***", value="{}".format(workout["/500m"]), inline=True)
    
    embed.set_footer(text="Brought to you by the Bot Farm Dev Team at BotFarmers.xyz")
    await channel.send(embed=embed)       



#update the sheet
updateSheet()

#get the thing 
workout = getLastWorkout()

#post it
loop.create_task(sendMessage(workout))


client.run('NjYwNDU2ODA5NjQ3MzA4ODAy.XgdJRQ.u5u8kDLdySAwP1JqEpbvuXOV3NU')

