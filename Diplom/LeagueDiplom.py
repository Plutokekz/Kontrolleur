import asyncio
import logging

import discord
from datapipelines import NotFoundError
from discord.ext import commands
from .Generator.src.FileGenerator import generate_diploma, delete_diploma
from .Generator.src.LeagueApi import SummonerNotFoundException

logger = logging.getLogger(__name__)


class DiplomaMaker(commands.Cog):

    @commands.command(name='diplom')
    async def diplom(self, context, name: str):
        """
        Generate a legit League of Legends Diplom

        :param name, name of the summoner
        """
        logging.info(f"Generating Pdf for {name}...")
        try:
            path, name = generate_diploma(name)
            await asyncio.sleep(5)
            await context.channel.send(file=discord.File(path))
            await asyncio.sleep(5)
            logger.info("deleting diplom")
            delete_diploma(name)
        except SummonerNotFoundException and NotFoundError:
            logger.warning(f"No account for the name {name}")
            await context.channel.send(f"Kein Spieler mit dem Namen <{name}> gefunden", delete_after=5)
        await context.message.delete(delay=10)


def setup(client):
    client.add_cog(DiplomaMaker(client))
