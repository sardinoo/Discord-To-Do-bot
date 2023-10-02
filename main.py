import discord
from discord.ext import commands
import os
import logging
from storage import variables
from cogs import buttons

intents = discord.Intents.all()
client = commands.Bot(command_prefix='$', intents=intents)

requests_log = logging.getLogger('urllib3.connectionpool')
requests_log.setLevel(logging.CRITICAL)
requests_log.propagate = True


class buttonhandler(commands.Bot):
    def __init__(self):
        intents = discord.Intents().all()
        super().__init__(command_prefix=commands.when_mentioned_or('.'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(buttons.buttons.ctodo())
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'cogs.{filename[:-3]}')
                    print(f'✅  Loaded {filename}')
                except Exception as e:
                    print(f'❌  Failed to load {filename}')
                    print(f'❌  [ERROR] {e}')


client = buttonhandler()

client.remove_command('help')


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return

client.run(variables.token)