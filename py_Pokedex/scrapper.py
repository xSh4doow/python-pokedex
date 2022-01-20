from botcity.web import WebBot, Browser
import lxml.html as lhtml
from urllib.request import urlopen, Request
import pandas as pd
import requests
from bs4 import BeautifulSoup

class Scrapper(WebBot):
    def config(self):
        # Driver mode.
        self.headless = False
        # WebDriver path.
        self.driver_path = 'C:/Users/xsh4d/Documents/Pythons/py_Pokedex/chromedriver.exe'

    def scrape(self):
        #config
        page = requests.get("https://pokemondb.net/pokedex/all")
        lpage = lhtml.fromstring(page.content)
        tr = lpage.xpath('//tr')
        # list
        col = []
        i = 0
        for t in tr[0]:
            i += 1
            name = t.text_content()
            col.append((name, []))

        for p in range(1, len(tr)):
            t = tr[p]
            # break if t != 10
            if len(t) != 10:
                break
            i = 0
            for t in t.iterchildren():
                data = t.text_content()
                if i > 0:
                    try:
                        data = int(data)
                    except:
                        pass
                col[i][1].append(data)
                i += 1
        Dict = {title: column for (title, column) in col}
        df = pd.DataFrame(Dict)

        # Fix Name
        def str_bracket(word):
            list = [x for x in word]
            for char_ind in range(1, len(list)):
                if list[char_ind].isupper():
                    list[char_ind] = ' ' + list[char_ind]
            fin_list = ''.join(list).split(' ')
            length = len(fin_list)
            if length > 1:
                fin_list.insert(1, '(')
                fin_list.append(')')
            return ' '.join(fin_list)

        # Fix Name
        def str_break(word):
            list = [x for x in word]
            for char_ind in range(1, len(list)):
                if list[char_ind].isupper():
                    list[char_ind] = ' ' + list[char_ind]
            fin_list = ''.join(list).split(' ')
            return fin_list

        df.to_json('PKMN.json')
        df['Name'] = df['Name'].apply(str_bracket)
        df['Type'] = df['Type'].apply(str_break)
        df.head()

Scrapper.scrape(Scrapper)