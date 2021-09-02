from discord.ext.commands import Bot, Cog, Option

bot = Bot(slash_commands=True, normal_commands=False) # Setting normal_commands to False will make this slash commands only
bot.add_cog(Info(bot))

@bot.command(slash=True)
async def hello(ctx):
    await ctx.send(f"Hey, {ctx.author.mention}!")

# And in a cog

class Info(Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(slash=True)
    async def userinfo(self, ctx, member: discord.Member = Option(description="The user to get info about")): # Note that it must use the description kwarg
        """Get info about a member"""
        await ctx.send(f"ID: {member.id}")
    
    @commands.command(slash=True)
    async def ban(self, ctx, member: discord.Member = Option(description="The member to ban"), reason: str = Option("No reason", description="Why to ban them")): # The first arg here will be used as default if nothing was provided
        await member.ban(reason=reason)
        await ctx.send("They have been banned", ephemeral=True)
        
bot.run("token")
