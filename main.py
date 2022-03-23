import configparser
import logging

import discord
from discord import Game
from discord.ext.commands import Bot
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

config = configparser.ConfigParser()
config.read("config.ini")
default_config = config['DEFAULT']
BOT_PREFIX = default_config['BotPrefix']
BOT_ACTIVITY = default_config['Activity']

client = Bot(intents=discord.Intents.all(), command_prefix=BOT_PREFIX, activity=Game(BOT_ACTIVITY))


@client.event
async def on_ready():
    [logger.info(f"Server Name:{server.name}, Server Id: {server.id}") for server in client.guilds]
    logger.info("logged in as " + client.user.name)


if __name__ == '__main__':
    token = os.getenv('TOKEN')
    modules = os.getenv('MODULES').split(",")
    for extension in modules:
        client.load_extension(extension)
        logger.info(f"Loaded module {extension}")
    client.run(token)
