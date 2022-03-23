import logging
import random

import discord
from discord.ext import commands

logger = logging.getLogger(__name__)


class Flip(commands.Cog):

    @commands.command(name="flip", description="Flips the Hamza Coin for you")
    async def _flip(self, context: commands.Context):
        """
        Flip a fucking Coin, like a League of Legens Solo Q game
        """
        flip = random.randint(0, 1)
        logger.info("flipping a coin")
        if flip == 0:
            await context.channel.send(file=discord.File("Random/EinEuroZahl.png"), delete_after=30)
            logger.info("flipped to number")
        else:
            await context.channel.send(file=discord.File("Random/EinEuroKopf.png"), delete_after=30)
            logger.info("flipped to head")


def setup(client):
    client.add_cog(Flip(client))
