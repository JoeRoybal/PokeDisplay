import requests
import random
from bs4 import BeautifulSoup
import json

from main import pokemonUpdate

with open('PokeDex.json') as f:
    PokeDex = json.load(f)

def getGen(NatNo):
    genNum=0
    if 1 <= NatNo <= 151:
        genNum=1
    elif 152 <= NatNo <= 251:
        genNum = 2
    elif 252 <= NatNo <= 386:
        genNum = 3
    elif 387 <= NatNo <= 493:
        genNum = 4
    elif 494 <= NatNo <= 649:
        genNum = 5
    elif 650 <= NatNo <= 721:
        genNum = 6
    elif 722 <= NatNo <= 809:
        genNum = 7
    else:
        genNum=8
    return genNum

key_list = list(PokeDex.keys())
value_list = list(PokeDex.values())
for i in range(0, len(key_list)):
    key_list[i] = int(key_list[i])

def getPokeDexNum(NatNo):
    pokedexnum = key_list.index(NatNo)
    print("Pokedex num" + pokedexnum)
    return pokedexnum

def getPokemon(NatNo):
    pokemon = value_list[NatNo]
    print("Pokemon: {}".format(pokemon))
    return pokemon

def getTextFromSite(pokemon):
    URL = "https://pokemondb.net/pokedex/"+pokemon.split()[0]
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    main = soup.find(id="main")
    return main

def getName(pokemon):
    name = getTextFromSite(pokemon).find("h1").text
    return name

def getPokedexData(pokemon):
    pokedexData = getTextFromSite(pokemon).find(class_="vitals-table").text
    return pokedexData

def getBaseStats(pokemon):
    BaseStats = getTextFromSite(pokemon).find(class_="grid-col span-md-12 span-lg-8").text
    return BaseStats
    
def getEntry(pokemon):
    entry = getTextFromSite(pokemon).find(class_="cell-med-text").text
    return entry


# needs reformating, not sure if it will be included yet...
def getTypeAdDad(pokemon):
    typeDefenses = getTextFromSite(pokemon).find(class_="resp-scroll text-center").text
    return typeDefenses

def getStandImg(pokemon):
    return "https://img.pokemondb.net/sprites/home/normal/"+pokemon.lower().split()[0]+".png"

def getShinyImg(pokemon):
    return "https://img.pokemondb.net/sprites/home/shiny/"+pokemon.lower().split()[0]+".png"

def getType(pokemon):    
    typeBegin = getPokedexData(pokemon).find('Type')
    typeEnd = getPokedexData(pokemon).find('Species')
    typeTypes = getPokedexData(pokemon)[typeBegin+6:typeEnd-3].split()
    return typeTypes

def getSpecies(pokemon):
    speciesBegin = getPokedexData(pokemon).find('Species')
    speciesEnd = getPokedexData(pokemon).find('Height')
    species = getPokedexData(pokemon)[speciesBegin+8:speciesEnd-3]
    return species

def getHeight(pokemon):
    heightBegin = getPokedexData(pokemon).find('Height')
    heightEnd = getPokedexData(pokemon).find('Weight')
    height = getPokedexData(pokemon)[heightBegin+7:heightEnd-3]
    return height

def getWeight(pokemon):
    weightBegin = getPokedexData(pokemon).find('Weight')
    weightEnd = getPokedexData(pokemon).find('Abilities')
    weight = getPokedexData(pokemon)[weightBegin+7:weightEnd-3]
    return weight

def getAbilitiesData(pokemon):
    abilitiesBegin = getPokedexData(pokemon).find('Abilities')
    abilitiesEnd = getPokedexData(pokemon).find('Local')
    abilities = getPokedexData(pokemon)[abilitiesBegin+13:abilitiesEnd-3]
    return abilities

def getAbilities(pokemon):
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

    abilities = getAbilitiesData(pokemon)
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
    return ability1,ability2, ability3

def getLocalDex(pokemon):
    localBegin = getPokedexData(pokemon).find('Local')
    local = getPokedexData(pokemon)[localBegin+8:-3]
    return local

def getHP(pokemon):
    HPBegin = getBaseStats(pokemon).find('HP')
    HPEnd = getBaseStats(pokemon).find('Attack')
    HP = getBaseStats(pokemon)[HPBegin+3:HPEnd-3].split()
    return HP

def getAttack(pokemon):
    attackBegin = getBaseStats(pokemon).find('Attack')
    attackEnd = getBaseStats(pokemon).find('Defense')
    attack = getBaseStats(pokemon)[attackBegin+7:attackEnd-3].split()
    return attack

def getDefense(pokemon):
    defenseBegin = getBaseStats(pokemon).find('Defense')
    defenseEnd = getBaseStats(pokemon).find('Sp.')
    defense = getBaseStats(pokemon)[defenseBegin+8:defenseEnd].split()
    return defense

def getSpAtk(pokemon):
    spAtkBegin = getBaseStats(pokemon).find('Sp. Atk')
    spAtkEnd = getBaseStats(pokemon).find('Sp. Def')
    spAtk = getBaseStats(pokemon)[spAtkBegin+8:spAtkEnd].split()
    return spAtk

def getSpDef(pokemon):
    spDefBegin = getBaseStats(pokemon).find('Sp. Def')
    spDefEnd = getBaseStats(pokemon).find('Speed')
    spDef = getBaseStats(pokemon)[spDefBegin+8:spDefEnd].split()
    return spDef

def getSpeed(pokemon):
    speedBegin = getBaseStats(pokemon).find('Speed')
    speedEnd = getBaseStats(pokemon).find('Total')
    speed = getBaseStats(pokemon)[speedBegin+6:speedEnd].split()
    return speed

def getTotal(pokemon):
    speedEnd = getBaseStats(pokemon).find('Total')
    total = getBaseStats(pokemon)[speedEnd+5:speedEnd+10].split()
    return total
