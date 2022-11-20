from pathlib import Path

import discord
from discord.ext import bridge

from .utility.helper import ChefHelpCommand


class ChefBot(bridge.Bot):
    """Bot with nutrition recipe related application commands.

    Subclassed to enable default intents and message_content.
    Subclassed from `bridge.Bot` instead of `discord.Bot` to generate
    slash and application commands both for same function.

    Making `cogs`to being loaded from cogs directory.
    """

    def __init__(self, description=None, *args, **options):
        # Set intents
        intents = discord.Intents.default()
        intents.message_content = True
        options["intents"] = intents
        options["help_command"] = ChefHelpCommand()

        super().__init__(description=description, *args, **options)

        # List and log cogs, excluding file which start with _(underscode).
        cogs_list = [_path.stem for _path in Path("chef_bot/cogs").glob("[!_]*.py")]

        for cog in cogs_list:
            self.load_extension(f"chef_bot.cogs.{cog}")
