from cgitb import text
from turtle import color
import discord
from discord.ext import commands

client=commands.Bot(command_prefix="--")

@client.command(name="expose")

async def expose(context):
    myEmbed=discord.Embed(title="Who the fuck is bhati?",value="An asshole",color=0x10931)
    myEmbed.add_field(name="Also known as",value="Yashodhra",inline=False)
    myEmbed.add_field(name="What describes him the best",value="Noob",inline=False)
    myEmbed.add_field(name="GirlFriend",value="This is top secret",inline=False)
    myEmbed.set_author(name="Bhati_Noob_INC.")
    myEmbed.set_footer(text="Fuck him")

    await context.message.channel.send(embed=myEmbed)



@client.command(name="version")

async def version(context):

  

    myEmbed=discord.Embed(title="Current Version", value="This bot is in it's version 1.0", color=0x10931)
    myEmbed.add_field(name="Version Code:", value="v1.0.0",inline=False)
    myEmbed.add_field(name="Release Date:", value="January 20, 2022", inline=False)
    myEmbed.set_author(name="Arshroop Singh Saini")
    myEmbed.set_footer(text="This is a footer")

    await context.message.channel.send(embed=myEmbed)

@client.event
async def on_ready():
    #client will search for general channel and then print hello world.
    general_channel=client.get_channel("your channels ID")

    await general_channel.send("I am here to expose bhati type, '--bhati' if you want to expose him! \n if you want to know the current version of the bot type, '--version'")

@client.event
async def on_message(message):
    if message.content=="expose":
        general_channel=client.get_channel("your channels ID")
        
        myEmbed=discord.Embed(title="Who the fuck is bhati?",description="An asshole",color=0x10931)
        myEmbed.add_field(name="Also known as",value="Yashodhra",inline=False)
        myEmbed.add_field(name="What describes him the best",value="Noob",inline=False)
        myEmbed.add_field(name="GirlFriend",value="This is top secret",inline=False)
        myEmbed.set_author(name="Bhati_expose_INC.")
        myEmbed.set_footer(text="Fuck him")


        await general_channel.send(embed=myEmbed)
    
    await client.process_commands(message)

@client.event
async def on_message(message):
    if message.content=="version":
        general_channel=client.get_channel("your channels ID")
        
        myEmbed=discord.Embed(title="Current Version", value="This bot is in it's version 1.0", color=0x10931)
        myEmbed.add_field(name="Version Code:", value="v1.0.0",inline=False)
        myEmbed.add_field(name="Release Date:", value="January 20, 2022", inline=False)
        myEmbed.set_author(name="Arshroop Singh Saini")
        myEmbed.set_footer(text="This is a footer")

        await general_channel.send(embed=myEmbed)
    
    await client.process_commands(message)
    
#Uncomment the line below and paste your bot's token
#client.run("paste your bot's token here")
