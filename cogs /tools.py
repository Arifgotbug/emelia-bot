import discord 
from k_pass import GenPass
from discord.ext import commands
from discord_slash import cog_ext, SlashContext

class Tools(commands.Cog, name="tools"):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(
        name="genpass",
        description="Generates a strong password."
    )
    async def genpass(self, ctx: SlashContext):
        '''
        Generates a strong password.
        '''
        pass

def setup(bot):
    bot.add_cog(Tools(bot))

    