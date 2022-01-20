from botcity.web import WebBot, Browser
from botcity.plugins.http import BotHttpPlugin
from scrapper import Scrapper
import pokedex
import os

class Bot(WebBot, BotHttpPlugin):
    def action(self, execution=None):
        if os.path.exists('./PKMN.json'):
            print("PKMN.json exists")
            pokedex.main()
        else:
            Scrapper.scrape(self)

    def not_found(self, label):
        print(f"Element not found: {label}")

if __name__ == '__main__':
    Bot.main()

