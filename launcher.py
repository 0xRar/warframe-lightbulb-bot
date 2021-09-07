import lightbulb
import Plugins

bot = lightbulb.Bot(prefix='.', token='')

bot.add_plugin(Plugins.CommandsPlugin())
bot.run()
