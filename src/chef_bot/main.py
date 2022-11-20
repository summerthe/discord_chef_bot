from .bot import ChefBot
from .utility.env_util import set_env
from .utility.log_util import setup_logging

env = set_env()
# Setting loggin
setup_logging()

# Set bot
print(env.list("GUILD_IDS"))
bot = ChefBot(debug_guilds=env.list("GUILD_IDS"), command_prefix="!")
bot.run(env("TOKEN"))
