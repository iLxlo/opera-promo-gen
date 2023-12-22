import discord
from discord.ext import commands
from src.config import Config
from src.gen import get_timestamp
import ctypes

intents = discord.Intents.default().all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(
        "\x1b[35m ╔═╗┬─┐┌─┐┌┬┐┌─┐  ┌─┐┌─┐┌┐┌\x1b[0m" + "\n"
        "\x1b[35m ╠═╝├┬┘│ │││││ │  │ ┬├┤ │││\x1b[0m" + "\n"
        "\x1b[35m ╩  ┴└─└─┘┴ ┴└─┘  └─┘└─┘┘└┘\x1b[0m" + "\n"
        "\x1b[35m                         Made by ilxlo\x1b[0m"
    )
    print(f'{get_timestamp()} \x1b[32m(!)\x1b[0m Logged in as [\x1b[90m{bot.user.name}\x1b[0m]')
    print(f'{get_timestamp()} \x1b[33m(*)\x1b[0m Invite link: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot')
    ctypes.windll.kernel32.SetConsoleTitleW("Made by @ilxlo | https://github.com/iLxlo")

if __name__ == "__main__":
    bot.load_extension("src.cogs.gen")
    bot.run(Config.TOKEN)
