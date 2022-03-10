from http.server import executable
import discord.utils
from discord.ext import commands
from youtube_dl import YoutubeDL

from ziedonis_bot import *

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Es ienācu sevī...')


@bot.command()
async def dzejolis(ctx):

    random_poem = get_random_poem()
    await ctx.send(random_poem)


@bot.command()
async def bulduris(ctx):

    from constants import RANDOM_POEMS_FOR_GIBBERISH_AMOUNT
    
    gibberish_poem = get_gibberish_poem(RANDOM_POEMS_FOR_GIBBERISH_AMOUNT)
    await ctx.send(gibberish_poem)


@bot.command()
async def balss(ctx, epifanijas=None):

    from constants import YDL_OPTIONS, FFMPEG_OPTIONS, ZIEDONIS_VOICE_URLS, EPIFANIJAS_URL
    from random import choice

    if epifanijas == 'epifanijas':
        url = EPIFANIJAS_URL
    else:
        url = choice(ZIEDONIS_VOICE_URLS)

    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

    with YoutubeDL(YDL_OPTIONS) as ydl:
        info = ydl.extract_info(url, download=False)
        I_URL = info['formats'][0]['url']
        source = await discord.FFmpegOpusAudio.from_probe(I_URL, **FFMPEG_OPTIONS)
        voice.play(source)
        voice.is_playing()


@bot.command()
async def dzivot(ctx):

    channel = ctx.message.author.voice.channel
    await channel.connect()


@bot.command()
async def nomirt(ctx):

    from constants import NOMIRT_COMMAND_MESSAGE

    await ctx.voice_client.disconnect()
    await ctx.send(NOMIRT_COMMAND_MESSAGE)


@bot.command()
async def paliga(ctx):

    from constants import HELP_LIST
    await ctx.send(HELP_LIST)



bot.run('OTUxNDMwNDA5NjcyMDk3ODAy.YinWng.DsmwDo_xucE3rt_gTpB0E45OrTI')