import os

import pytumblr

from . import extensions
from .bot import Emily

def main():
    client = Emily()
    client.load_extension("cogs")

    if 'EMILY_DEBUG' in os.environ:
        client.tumblr = None  # FIXME
    else:
        client.tumblr = pytumblr.TumblrRestClient(
            os.environ['TUMBLR_CONSUMER_KEY'],
            os.environ['TUMBLR_CONSUMER_SECRET'],
            os.environ['TUMBLR_OAUTH_TOKEN'],
            os.environ['TUMBLR_OAUTH_SECRET']
        )

    client.run(os.environ['DISCORD_TOKEN'])
