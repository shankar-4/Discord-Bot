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
-> Expose Members to Open - Source Community

-> Train students in the Opensource platform to take up projects

-> Delivering technical assistance, including peer-to-peer learning

-> More active partnerships with opensource industry members.

-> Improved coordination and focus of resources, and Better use of data.

''')
  if  message.content.startswith('!features'):
    await message.channel.send('''It provides information about the Turing club and it will also delete message which are NSFW''''')
    
  if  message.content.startswith('!current event'):
        await message.channel.send('''
  Current event going on is BOT-A-THON''')
  
  if  message.content.startswith('!partnerships'):
        await message.channel.send('''
-> DataCamp
-> Interview Cake
-> Azure Developer
-> Codeflow - OpeForce 2022''')
    
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
-> !history
-> !features
-> !team
-> !sig
-> !agenda
-> !current event
-> !upcoming event
-> !partnerships
-> !goals
-> !list of events
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
    
    if  message.content.startswith('!history'):
    await message.channel.send('''  
August 2021 - Foundation of TTC
TTC was established at Jain University on August 6, 2021, and
is entirely driven by students. TTC began its journey with 
lively interactive sessions with well-known technical advocates
such as Jason Mayes (senior developer advocate at Google for
TensorFlow) and Sangam Biradar (Technical Advocate at Tenable).''')
    
     if  message.content.startswith('!list of events'):
    await message.channel.send('''  
October 2021 - TTC's First tech event
Turing Developer's Summit
The Turing Developer's Summit was a tech-focused event hosted
by TTC; a chance to engage with industry leaders such as 
Vice President of the Linux Foundation, Ibrahim Haddad, and 
EC Council Board Member Tapan Kumar Jha about concepts that 
developers will find extremely useful: an introduction to the
vast world of Linux, and hacking with Kali.

January 2022 -TTC's First Patnership 
TTC has previously hosted events with industry leaders and 
hands-on workshops, but for the first time in January 2022,
TTC partnered with Datacamp to provide certified courses, 
guided and unguided projects worth $399 for free.

Engineer's day event ''')
    
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
  swearwords=['fuck','fuck you','shit','asshole','son of a b*tch','bitch','bastard','nigga','holy shit']
      
  for x in swearwords:
    if x in message.content: 
     await message.delete()
     await message.channel.send("You can't say that!")
    
  
  
    
keep_alive()
client.run(os.getenv('TOKEN'))
