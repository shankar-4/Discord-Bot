import discord
import os
import requests
from keep_alive import keep_alive
client = discord.Client()
 
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  await client.change_presence(activity=discord.Game('!help'))

  if message.author == client.user:
    return

#   msg = message.content
  if message.author == client.user:
    return
  
  if message.content.startswith('!hello'):
       await message.channel.send(f'Hello {message.author.name}!')
    
  if message.content.startswith('!bye'):
       await message.channel.send(f'Bye {message.author.name}! have a nice day')
    
  if message.content.startswith('!agenda'):
    await message.channel.send('TTC navigate the culture of Open Source Collaboration. This club is being created by the students with interests to create greater opportunities for the students in their career further ahead')
  
  if message.content.startswith('!goals'):
    await message.channel.send('''
* Expose Members to Open - Source Community

* Train students in the Opensource platform to take up projects

* Delivering technical assistance, including peer-to-peer learning

* More active partnerships with opensource industry members.

* Improved coordination and focus of resources, and Better use of data.

''')
    
  if  message.content.startswith('!current event'):
        await message.channel.send('''
  Current event going on is BOT-A-THON''')
  
  if  message.content.startswith('!partnerships'):
        await message.channel.send('''
* DataCamp
* Interview Cake
* Azure Developer
* Codeflow - OpeForce 2022''')
    
  if  message.content.startswith('!sig'):
        await message.channel.send('''
SIG is a Special Intrest Group where students work on specific ways to contribute to the club .
1.Intel SIG 
2.Codestorming SIG
3.Xploit SIG''')
    
  if  message.content.startswith('!team'):
        await message.channel.send('''
* Rishi R - Club Lead
* Anudeep Nameneni - Club Manager
* Vishnu Sai A - Treasurer 
* Amy Mariam Thomas - Student Coordinator     
* Abhishek S - Head Designer
* Raghavendra Dabral - Pr Head 
* Nishtha Jain - Co Pr Head 
* Nihal Kadam - Bootcamp Coordinator
* Aakash Rajaraman - Project Strategist''')
    
  if  message.content.startswith('!help'):
        await message.channel.send(''' 
* !team
* !sig
* !agenda
* !current event
* !partnerships
* !goals
* !social media
* !mentors
* !hello
* !bye''')
    
  if  message.content.startswith('!social media'):
        await message.channel.send('''     
Discord Server link: https://discord.gg/8aUecspTfC

Instagram - https://instagram.com/theturingclub_ju?r=nametag

Linkedin - https://www.linkedin.com/company/the-turing-club-jainuniversity
                                   
Medium - https://medium.com/@ttclub.ju

Whatsapp - https://chat.whatsapp.com/LZSRzkXIdpKLuHtgBByxNd

Youtube - https://www.youtube.com/channel/UCoj5JIWPp2bPj99K2Yw293g

Twitter - https://twitter.com/theturingclubJU

Official website - https://theturingclub.in/ ''')
    
  if  message.content.startswith('!mentors'):
        await message.channel.send('''    
*  Dr. Chenraj Roychand 
*  Varun Jain 
*  Dr. Hariprasad S A 
*  Dr. V. Vivek 
*  Prof. Roopashree S
*  Jatinder Pal Singh Bagga ''')
    
  if message.content.startswith('How are you'):
    await message.channel.send("I am a bot and i dont have feelings")
    
  if message.content.startswith('Who are you'):
    await message.channel.send("I am TTC Help Bot and i will provide information regarding TTC club ")

  
  
    
keep_alive()
client.run(os.getenv('TOKEN'))
