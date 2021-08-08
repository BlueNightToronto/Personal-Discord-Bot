import discord
from discord.ext import commands


class jellytime(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def jellytime(self, ctx):
        embed_name = 'Jelly Time'
        embed = discord.Embed(color=0x1e405d)
        embed.add_field(name=embed_name,
                        value='Do you know what time is it.  Build Up      Beat Drops      Jelly Time!'
                        inline=False)
        embed.set_image(url='')
        await ctx.send(embed=embed)
