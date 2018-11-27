import asyncio

from discord.utils import get
from discord.ext import commands


class selfmanagement:
    @commands.command()
    async def imlewd(self, ctx: commands.Context):
        """
        Grants you access to the NSFW channels
        """
        DECLARATION = "I assert that I am over the age of 18"
        if get(ctx.guild.roles, name="no nsfw") in ctx.author.roles:
            await ctx.send("{0.mention}, you are not allowed to give yourself the nsfw role.".format(ctx.author))
            return

        nwde = get(ctx.guild.roles, name="nsfw")
        if nwde in ctx.author.roles:
            await ctx.send("But {0.mention}, you are already have access to nsfw.".format(ctx.author))
        else:
            await ctx.send("Please confirm you are over 18. "
                           "Please reply to this message with the following declaration."
                           "\"{}\"".format(DECLARATION))

            try:
                def check(msg):
                    return (msg.author == ctx.author and
                            msg.channel == ctx.channel and
                            DECLARATION in msg.content)
                await ctx.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await ctx.send("Your request has timed out, please try again.")
            else:
                await ctx.author.add_roles(nwde, reason="Added by ~imlewd command.")
                await ctx.send("Ok {0.mention}, Granting you access to #nsfw".format(ctx.author))
    
    @commands.command(aliases=['pronoun'])
    async def pronouns(self, ctx: commands.Context, *, pronouns):
        """
        Use to set your pronouns
        
        Enter any number of the following after the command, seperated by spaces:
        he, she, they, they/she, they/he
        """
        if not hasattr(self.pronouns, "roles"):
            self.pronouns.roles = {"he": get(ctx.guild.roles, name="he/him"),
                                   "he/him": get(ctx.guild.roles, name="he/him"),
                                   "she": get(ctx.guild.roles, name="she/her"),
                                   "she/her": get(ctx.guild.roles, name="she/her"),
                                   "they": get(ctx.guild.roles, name="they/them"),
                                   "they/them": get(ctx.guild.roles, name="they/them"),
                                   "they/she": get(ctx.guild.roles, name="they/she"),
                                   "they/he": get(ctx.guild.roles, name="they/he")}

        try:
            roles_add = {self.pronouns.roles[p] for p in pronouns.lower().split(" ")}
        except KeyError:
            raise commands.BadArgument()
        roles_remove = set(self.pronouns.roles.values())-roles_add
        await ctx.author.add_roles(*list(roles_add))
        await ctx.author.remove_roles(*list(roles_remove))
        await ctx.send("Ok {0.mention}, I have updated your pronoun roles.".format(ctx.author))
