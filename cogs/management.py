from discord.ext import commands

from agithub.GitHub import GitHub

def can_manage():
    def pred(ctx: commands.Context):
        return ctx.bot.is_owner(ctx.author)
    return commands.check(pred)

class Manage:
    @commands.command(hidden=True)
    @can_manage()
    async def restart(self, ctx: commands.Context):
        await ctx.e_say("Ok **{author}**\n*SYSTEM RESTARTING*")
        ctx.bot.loop.stop()

    @commands.command()
    async def request(self, ctx: commands.Context, *, feature):
        """
        Requests a feature from the author, do not abuse
        """
        msg = "Request from {}:\n".format(ctx.author.mention) + feature
        await ctx.bot.pm_owner(content=msg)
        await ctx.message.add_reaction("✅")

    @commands.command()
    async def changelog(self, ctx: commands.Context):
        """
        Get a log of what has changed in Emily
        """
        status, commits = GitHub().repos.harkonenbade.emily.commits.get(per_page=10)
        if status == 200:
            await ctx.send(content="```Changelog:\n{}```".format("\n".join(["- {}".format(c['commit']['message'])
                                                                            for c in commits])))
        else:
            await ctx.send(content="Error: Cannot reach github")

    @commands.command(hidden=True)
    @can_manage()
    async def prune(self, ctx: commands.Context):
        async with ctx.typing():
            async for message in ctx.history(limit=None):
                if not message.pinned:
                    await message.delete()
