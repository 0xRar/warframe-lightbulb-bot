import lightbulb
import requests

class CommandsPlugin(lightbulb.Plugin):
    @lightbulb.command()
    async def h(self, ctx):
        await ctx.respond(
            """
            **[ By 0xRar ]**
                        
            **.h** |    list all commands
            **.trader** |   Information on the current Void Trader offerings, or when he will arrive (pc,ps4,xb1,swi)
            """
        )

    @lightbulb.command()
    async def trader(self, ctx, platform):
        trader = requests.get(f'https://api.warframestat.us/{platform}/voidTrader').json()

        await ctx.respond(
            'Platform: '+platform.upper() +'\n'+
            'Name: '+trader['character'] +'\n'+
            'Current Location: '+trader['location'] +'\n'+
            'Ends: '+trader['endString']
        )


def load(bot):
    bot.add_plugin("Commands Plugin")
