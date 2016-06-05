import discord
from discord.ext import commands

class CheesecakeCustom:
    """This Cog Was Built By LegitCheesecake"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def about(self):
        """A Basic About Command"""

        #Your code will go here
        await self.bot.say("`Toothy, A DiscordBot By Blazy/n/nMy prefix Is !t (e.g: To do help you will put !thelp/nA Remake Of Red By TwentySix`")

def setup(bot):
    bot.add_cog(Chesecake Custom Commands(bot))
