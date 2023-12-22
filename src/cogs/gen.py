import io
import discord
from discord.ext import commands
from src.gen import gen_promo_link, get_timestamp
import ctypes
import time

class PromoCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def gen(self, ctx, num_links: int = None):
        start_time = time.time()
        icon_url = "https://cdn.discordapp.com/avatars/1159414254861037588/6899f4ffead6457390a02d0bde97d44e.png"

        if num_links is None or not isinstance(num_links, int) or num_links <= 0:
            error_embed = discord.Embed(
                title="Error",
                description="```ml\n Please provide a valid Number for Generating Promo Links.```",
                color=0x2f3136,
            )
            error_embed.set_footer(text="Made by @ilxlo", icon_url=icon_url)
            await ctx.send(embed=error_embed)
            return

        received_count = num_links
        success_count = 0
        failed_count = 0

        progress_embed = discord.Embed(
            title="Generating Promo Links", color=0x2f3136
        )
        progress_embed.set_footer(text="Made by @ilxlo", icon_url=icon_url)
        progress_message = await ctx.send(embed=progress_embed)

        generated_links = []

        for i in range(1, num_links + 1):
            progress_embed.description = f"Progress:```md\n# {i}/{num_links}```\n ```ml\nReceived: {received_count} | Success: {success_count} | Failed: {failed_count} | Elapsed: {round(time.time() - start_time, 2)}s```"
            await progress_message.edit(embed=progress_embed)
            links = gen_promo_link(1)

            if links:
                generated_links.extend(links)
                success_count += 1
            else:
                failed_count += 1

            ctypes.windll.kernel32.SetConsoleTitleW(
                f"Made by ilxlo | Received: {received_count} | Success: {success_count} | Failed: {failed_count} | Elapsed: {round(time.time() - start_time, 2)}s"
            )

        success_embed = discord.Embed(
            title="Generation Complete",
            description=f"Generated \n ```md\n> {num_links}/{num_links}```\n ```ml\nReceived: {received_count} | Success: {success_count} | Failed: {failed_count} | Elapsed: {round(time.time() - start_time, 2)}s```",
            color=0x2f3136,
        )
        success_embed.set_footer(text="Made by @ilxlo", icon_url=icon_url)

        await progress_message.edit(embed=success_embed)

        if generated_links:
            file_content = "\n".join(generated_links).encode("utf-8")
            file = discord.File(io.BytesIO(file_content), filename="output.txt")
            await ctx.send(file=file)

        ctypes.windll.kernel32.SetConsoleTitleW(
            f"Made by ilxlo | Received: {received_count} | Success: {success_count} | Failed: {failed_count} | Elapsed: {round(time.time() - start_time, 2)}s"
        )

def setup(bot):
    bot.add_cog(PromoCog(bot))
