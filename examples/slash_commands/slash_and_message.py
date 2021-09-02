from discord.ext.commands import Bot, Cog, Option

bot = Bot(slash_commands=True) # To use both normal and slash commands, you only need to enable slash commands
bot.add_cog(Info(bot))

@bot.command(slash=True)
async def hello(ctx):
    await ctx.send(f"Hey, {ctx.author.mention}!")
    
@bot.command()
async def byw(ctx):
    await ctx.send(f"Bye {ctx.author.mention}!")

# And in a cog

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(slash=True)
    async def userinfo(self, ctx, member: discord.Member = Option(description="The user to get info about")): # Note that it must use the description kwarg
        """Get info about a member"""
        await ctx.send(f"ID: {member.id}", ephemeral=True)
    
    @commands.command()
    async def ban(self, ctx, member: discord.Member, reason: str = "No reason"):
        await member.ban(reason=reason)
        await ctx.send("They have been banned")
        
bot.run("token")
