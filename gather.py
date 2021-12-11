import requests
from bs4 import BeautifulSoup
import json

URL = "https://pokemondb.net/pokedex/all"
page = requests.get(URL)
key = 445

soup = BeautifulSoup(page.content, "html.parser")
with open('PokeDex.json') as f:
    PokeDex = json.load(f)

for tr in soup.find_all('tr')[1:]:
    tds = tr.find_all('td')

# TODO:
# -decide random dex num
# -find pokemon from pokedex json
# -scape db for info
# -format info for page
# -set up refresh /timer for new pokemon?
