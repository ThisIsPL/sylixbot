import discord
import json
import os
from discord.ext import commands
import random


client = commands.Bot(command_prefix = '+')


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('Sylix bot by Auxy'))
    print(f'[Status] Bot is online')

    

@client.event
async def on_member_join(member):
    print(f'[Server] {member} joined')
    
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    respones = ['Nein.',
                'Ja.',
                'Meine antwort ist ja.',
                'Mein antwort ist nein.',
                'OMG JA',
                'Das kann ich nicht sagen',
                'Nein leider nicht']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(respones)}')
                
@client.command()
async def waifu(ctx):
    respones = ['https://cdn.discordapp.com/attachments/788449794632843294/838486589893902436/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838486780188950548/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838486922619781222/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487012293476402/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487070187061278/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487205696503808/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487319455596554/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487603043893288/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487833996034108/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838487946238885948/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488304764452914/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488528274325574/2Q.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488594405654548/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488662177611806/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488769186365450/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488885125709834/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838488965425659965/OIP.png',
                'https://cdn.discordapp.com/attachments/835112311554310157/838489845570601070/IMG_20210502_205906.jpg',
                'https://cdn.discordapp.com/attachments/788449794632843294/838489105800888350/OIP.png',
                'https://cdn.discordapp.com/attachments/788449794632843294/838489189481840650/OIP.png']
    await ctx.send(f'{random.choice(respones)}')
                
@client.command()
async def abdi(ctx):
    await ctx.send(f'ABDIIIII, ICH KANNNN NICHT MEHRRRR')

@client.command()
async def PH(ctx):
    await ctx.send(f'https://cdn.discordapp.com/attachments/788449794632843294/838492635323826176/tenor.gif')

@client.command()
async def clear(ctx, amount=10):
    if (ctx.message.author.permissions_in(ctx.message.channel).manage_messages):
        await ctx.channel.purge(limit= amount+1)
        print(f'[Server] Deleted 10 messages ')
@clear.error
async def clear_error(ctx, error):
    print(f'[ERROR] Sorry you are not allowed to use this command.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send('Sorry you are not allowed to use this command.')
    

@client.command()
async def gay(ctx):
    respones = ['Du bist zu 34 prozent gay',
                'Du bist zu 14 prozent gay',
                'Du bist zu 56 prozent gay',
                'Du bist zu 5 prozent gay',
                'Du bist zu 74 prozent gay',
                'Du bist zu 87 prozent gay',
                'Du bist zu 80 prozent gay',
                'Du bist zu 61 prozent gay',
                'Du bist zu 0 prozent gay',
                'Du bist zu 43 prozent gay',
                'Du bist zu 10 prozent gay',
                'Du bist zu 37 prozent gay',
                'Du bist zu 99 prozent gay',
                'Du bist zu 62 prozent gay',
                'Du bist zu 87 prozent gay',
                'Du bist zu 100 prozent gay']
    await ctx.send(f'{random.choice(respones)}')






@client.command()
async def ping(ctx):
    await ctx.send(f'ping | {round(client.latency * 1000)}ms')
    print(f'[Bot] Sended Ping  ')



    













client.run('ODM4NDc4NzQzMzMxNzk5MDcw.YI7sLg.e7Ss0nzLHcVxN9aGseOtFpzR9lA')