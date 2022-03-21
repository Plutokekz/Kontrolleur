import random

import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashCommand


class Flip(commands.Cog):

    def __init__(self, client):
        if not hasattr(client, "slash"):
            # Creates new SlashCommand instance to bot if bot doesn't have.
            client.slash = SlashCommand(client, override_type=True, auto_register=True)
        self.client = client
        self.client.slash.get_cog_commands(self)

    def cog_unload(self):
        self.client.slash.remove_cog_commands(self)

    @cog_ext.cog_slash(name="flip", description="Flips the Hamza Coin for you", guild_ids=[522571256843730955,
                                                                                           523877042727550991])
    async def _flip(self, context: commands.Context):
        flip = random.randint(0, 1)
        if flip == 0:
            await context.channel.send(file=discord.File("Random/EinEuroZahl.png"), delete_after=30)
        else:
            await context.channel.send(file=discord.File("Random/EinEuroKopf.png"), delete_after=30)


def setup(client):
    client.add_cog(Flip(client))
