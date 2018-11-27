from . import (management, misc, self_management)

def setup(bot):
    bot.add_cog(management.Manage())
    bot.add_cog(misc.Misc())
    bot.add_cog(self_management.selfmanagement())
