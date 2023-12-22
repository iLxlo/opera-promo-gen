import discord
from discord.ext import commands
from src.config import Config
from src.gen import get_timestamp
import ctypes
import os

intents = discord.Intents.default().all()

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    center_lines = [
        "\x1b[35m ╔═╗┬─┐┌─┐┌┬┐┌─┐  ┌─┐┌─┐┌┐┌\x1b[0m",
        "\x1b[35m ╠═╝├┬┘│ │││││ │  │ ┬├┤ │││\x1b[0m",
        "\x1b[35m ╩  ┴└─└─┘┴ ┴└─┘  └─┘└─┘┘└┘\x1b[0m",
        "\x1b[35m                      Made by ilxlo\x1b[0m"
    ]
    for line in center_lines:
        console_width = os.get_terminal_size().columns
        center_position = (console_width - len(line)) // 2
        print(f"{' ' * center_position}{line}")
    print(f"{' ' * ((console_width - 35) // 2)}\x1b[32m(!)\x1b[0m {get_timestamp()} Logged in as [\x1b[90m{bot.user.name}\x1b[0m]")
    line_count = sum(1 for line in open("./data/promos.txt"))
    print(f"{' ' * ((console_width - 35) // 2)}\x1b[34m(/)\x1b[0m {get_timestamp()} Stock: [\x1b[90m{line_count}\x1b[0m]")
    print(f"{' ' * ((console_width - 125) // 2)}\x1b[33m(*)\x1b[0m {get_timestamp()} Invite link: https://discord.com/api/oauth2/authorize?client_id={bot.user.id}&permissions=8&scope=bot")

    ctypes.windll.kernel32.SetConsoleTitleW("Made by @ilxlo | https://github.com/iLxlo")

if __name__ == "__main__":
    bot.load_extension("src.cogs.gen")
    bot.run(Config.TOKEN)
