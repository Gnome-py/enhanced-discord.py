import discord
from discord.ext import commands

# Set slash commands=True when constructing your bot to enable all slash commands
# if your bot is only for a couple of servers, you can use the parameter
# `slash_command_guilds=[list, of, guild, ids]` to specify this,
# then the commands will be much faster to upload.
bot = commands.Bot("!", intents=discord.Intents(guilds=True, messages=True), slash_commands=True)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


@bot.command()
# You can use commands.Option to define descriptions for your options, and converters will still work fine.
async def ping(ctx: commands.Context, emoji: bool = commands.Option(description="whether to use an emoji when responding")):
    # This command can be used with slash commands or message commands
    if emoji:
        await ctx.send("\U0001f3d3")
    else:
        await ctx.send("Pong!")

@bot.command(message_command=False)
async def only_slash(ctx: commands.Context):
    # This command can only be used with slash commands
    await ctx.send("Hello from slash commands!")

@bot.command(slash_command=False)
async def only_message(ctx: commands.Context):
    # This command can only be used with a message
    await ctx.send("Hello from message commands!")

bot.run("token")
