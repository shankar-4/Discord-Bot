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
* Anudeep N - Club Co Lead
* Aakash R - Club Manager
* Amy Mariam Thomas - Club Co-Manager
* Vishnu Sai A - Club Treasurer
* Abhishek S - Head Designer
* Monish - Designer
* Rahul Ram R - Social Media Manager
* Diksha C - Outreach Coordinator
* Nishtha - Content Creator
* Raghavendra - PR Head
* Sohan Simha - Content Head''')
    
  if  message.content.startswith('!help'):
        await message.channel.send(''' 
-> !team
-> !sig
-> !agenda
-> !current event
-> !upcoming event
-> !partnerships
-> !goals
-> !social media
-> !mentors
-> !hello
-> !bye''')
    
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
    
    if  message.content.startswith('!upcoming event'):
        await message.channel.send('''
Project Sprint

Project Sprint is an initiative aimed at inspiring students to embrace their creative side and put their skills into a real project. This will benefit the students' resume and improving skillsets. This event is meant to highlight student efforts in project building in their respective fields. Students may work in group or individually. They are encouraged to design and implement an innovative technology or implement an existing technology to a new use case, relating to either hardware or software fields.  
The event is currently scheduled to kick off on April 1st, with the showcase happening on 16th of April.
Registration : https://forms.gle/GW7edYYJpqDfCUMK7''')
    
  if message.content.startswith('How are you'):
    await message.channel.send("I am a bot and i dont have feelings")
    
  if message.content.startswith('Who are you'):
    await message.channel.send("I am TTC Help Bot and i will provide information regarding TTC club ")

  
  
    
keep_alive()
client.run(os.getenv('TOKEN'))
