import requests
import random
from bs4 import BeautifulSoup
import json

with open('PokeDex.json') as f:
    PokeDex = json.load(f)
nationalNo = random.randint(1, 898)
key_list = list(PokeDex.keys())
value_list = list(PokeDex.values())
for i in range(0, len(key_list)):
    key_list[i] = int(key_list[i])

pokedexnum = key_list.index(nationalNo)
pokemon = value_list[pokedexnum]
URL = "https://pokemondb.net/pokedex/"+pokemon.split()[0]
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

main = soup.find(id="main")
name = main.find("h1").text
pokedexData = main.find(class_="vitals-table").text
baseStats = main.find(class_="grid-col span-md-12 span-lg-8").text
# needs reformating, not sure if it will be included yet...
typeDefenses = main.find(class_="resp-scroll text-center").text
img = "<a href=\"http://pokemondb.net/pokedex/"+pokemon.lower() + \
    "\"><img src=\"https://img.pokemondb.net/sprites/home/normal/" + \
    pokemon.lower()+".png\" alt="+pokemon+"></a>"
shinyImg = "<a href=\"http://pokemondb.net/pokedex/"+pokemon.lower()+"\"><img src=\"https://img.pokemondb.net/sprites/home/shiny/" + \
    pokemon.lower()+".png\" alt=\""+pokemon+"\"></a>"


typeBegin = pokedexData.find('Type')
typeEnd = pokedexData.find('Species')
typeTypes = pokedexData[typeBegin+6:typeEnd-3]

speciesBegin = pokedexData.find('Species')
speciesEnd = pokedexData.find('Height')
species = pokedexData[speciesBegin+8:speciesEnd-3]
heightBegin = pokedexData.find('Height')
heightEnd = pokedexData.find('Weight')
height = pokedexData[heightBegin+7:heightEnd-3]
weightBegin = pokedexData.find('Weight')
weightEnd = pokedexData.find('Abilities')
weight = pokedexData[weightBegin+7:weightEnd-3]
abilitiesBegin = pokedexData.find('Abilities')
abilitiesEnd = pokedexData.find('Local')
abilities = pokedexData[abilitiesBegin+13:abilitiesEnd-3]
firstCheck = '2. '
secondCheck = 'hidden ability'
ability1 = ''
ability2 = ''
ability3 = ''


def getHiddenAbility(String):
    sus = String.split()
    count = 0
    keyPhrase = 'NONE'
    for x in sus:
        for index in range(len(x)):
            if x[index].isupper():
                count += 1
        if count > 1:
            keyPhrase = x
        count = 0
    for index in range(len(keyPhrase)):
        if keyPhrase[index].isupper():
            Last = index
    hidden = keyPhrase[Last:]
    hiddenAbility = String.find(hidden)
    return hiddenAbility


if firstCheck in abilities and secondCheck in abilities:
    ability1 = abilities[:abilities.find('2.')]
    hiddenAbility = getHiddenAbility(abilities)
    ability2 = abilities[abilities.find('2.')+3:hiddenAbility]
    ability3 = abilities[hiddenAbility:]
elif firstCheck in abilities and not secondCheck in abilities:
    ability1 = abilities[:abilities.find('2.')]
    ability2 = abilities[abilities.find('2.')+3:]
elif firstCheck not in abilities and secondCheck in abilities:
    hiddenAbility = getHiddenAbility(abilities)
    ability1 = abilities[:hiddenAbility]
    ability2 = abilities[hiddenAbility:]
else:
    pass
localBegin = pokedexData.find('Local')
local = pokedexData[localBegin+8:-3]

HPBegin = baseStats.find('HP')
HPEnd = baseStats.find('Attack')
HP = baseStats[HPBegin+3:HPEnd-3].split()
attackBegin = baseStats.find('Attack')
attackEnd = baseStats.find('Defense')
attack = baseStats[attackBegin+7:attackEnd-3].split()
defenseBegin = baseStats.find('Defense')
defenseEnd = baseStats.find('Sp.')
defense = baseStats[defenseBegin+8:defenseEnd].split()
spAtkBegin = baseStats.find('Sp. Atk')
spAtkEnd = baseStats.find('Sp. Def')
spAtk = baseStats[spAtkBegin+8:spAtkEnd].split()
spDefBegin = baseStats.find('Sp. Def')
spDefEnd = baseStats.find('Speed')
spDef = baseStats[spDefBegin+8:spDefEnd].split()
speedBegin = baseStats.find('Speed')
speedEnd = baseStats.find('Total')
speed = baseStats[speedBegin+6:speedEnd].split()
total = baseStats[speedEnd+5:speedEnd+10].split()
