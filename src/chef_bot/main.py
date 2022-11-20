from environs import Env

from .bot import ChefBot
from .utility.log_util import setup_logging

# Read .env file and set environment variables.
env = Env()
env.read_env()

# Setting loggin
setup_logging()

# Set bot
print(env.list("GUILD_IDS"))
bot = ChefBot(debug_guilds=env.list("GUILD_IDS"), command_prefix="!")
bot.run(env("TOKEN"))
