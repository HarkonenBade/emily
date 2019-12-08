import discord
from discord.ext import commands

class Quote(commands.Cog):
    @commands.command()
    async def quote(self, ctx: commands.Context, user: discord.Member, *, identifier=None):
        """
        Quote a user.

        Sends quotes to http://talesofetheria.tumblr.com
        It can only quote in the last 200 messages on channel.
        If you don't supply an identifier it will quote the users last message block.
        If you do it will quote the rest of the first block
        that starts with a message containing that text, case insensitive.
        """
        quote_user = user.name
        async for message in ctx.channel.history(limit=200, before=ctx.message):
            if message.author == user:
                if identifier is not None:
                    if identifier.lower() in message.clean_content.lower():
                        quote_text = message.clean_content
                        async for msg in ctx.channel.history(limit=100, after=message, reverse=True):
                            if msg.id == ctx.message.id or msg.author != user:
                                break
                            quote_text = quote_text + '\n' + msg.clean_content
                        break
                else:
                    quote_text = message.clean_content
                    async for msg in ctx.channel.history(limit=100, before=message):
                        if msg.author != user:
                            break
                        quote_text = msg.clean_content + '\n' + quote_text
                    break
        else:
            await ctx.send("I'm sorry, I can't find that.")
            return
        print(quote_text)
        ctx.bot.tumblr.create_quote("talesofetheria.tumblr.com",
                                    state="draft",
                                    quote=quote_text,
                                    source=quote_user)
        await ctx.send("Quoting {0.mention}:\n\"{1}\"".format(user, quote_text))
