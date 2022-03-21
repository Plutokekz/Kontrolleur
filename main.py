import configparser
import logging

import discord
from discord import Game
from discord.ext.commands import Bot
import os
from discord_slash import SlashCommand

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read("config.ini")
default_config = config['DEFAULT']
BOT_PREFIX = default_config['BotPrefix']
BOT_ACTIVITY = default_config['Activity']

client = Bot(intents=discord.Intents.all(), command_prefix=BOT_PREFIX, activity=Game(BOT_ACTIVITY))

client.slash = SlashCommand(client)


@client.event
async def on_ready():
    [(logging.info(server.name), logging.info(server.id)) for server in client.guilds]
    logging.info("logged in as " + client.user.name)


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    modules = os.getenv('MODULES').split(",")
    for extension in modules:
        client.load_extension(extension)
        logging.info(f"Loaded module {extension}")
    logging.info(client.slash.commands)
    client.run(token)

"""['MusicBackend.Sounds', 'Certificat.LeagueDiplom', 'Random.Coinflip',
                      'Decode.Decode', 'Calculator.CalculatorModule', 'AI.ImagesDetection.CatOrDog',
                      'AI.MakeCat.MakeCat', 'FourConnect.CFDmodule']:  # 'AI.ImagesDetection.CatOrDog', 'AI.MakeCat.MakeCat' 'FourConnect.CFDmodule',"""
