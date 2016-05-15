from discord.ext import commands
from random import choice as randchoice


class Fortune:
    """Fortune Dwaggy Commands."""

    def __init__(self, bot):
        self.bot = bot
        self.fortune = ["Die in a firey dragons breath, you noob",
                        "You magically type in legitcheesecake into your browser to find the most awesome website #noadplz",
                        "Man who go to bed with itchy butt wake up with stinky finger",
                        "There is no I in team but U in cunt",
                        "",
                        "Man piss in wind, wind piss back"]

    @commands.command(name="fortune", aliases=["cookie"])
    async def _cookie(self):
        """Ask for your fortune
        And look deeply into my scales
        """
        return await self.bot.say("`" + randchoice(self.fortune) + "`")


def setup(bot):
    bot.add_cog(Fortune(bot))