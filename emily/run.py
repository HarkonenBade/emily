import os

from . import extensions
from .bot import Emily

def main():
    client = Emily()
    client.load_extension("cogs")

    client.run(os.environ['DISCORD_TOKEN'])
