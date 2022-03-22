import random

import discord
from discord.ext import commands


class Flip(commands.Cog):

    @commands.command(name="flip", description="Flips the Hamza Coin for you")
    async def _flip(self, context: commands.Context):
        """
        Flip a fucking Coin, like a League of Legens Solo Q game
        """
        flip = random.randint(0, 1)
        if flip == 0:
            await context.channel.send(file=discord.File("Random/EinEuroZahl.png"), delete_after=30)
        else:
            await context.channel.send(file=discord.File("Random/EinEuroKopf.png"), delete_after=30)


def setup(client):
    client.add_cog(Flip(client))
