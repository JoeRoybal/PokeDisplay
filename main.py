from flask import Flask, render_template
import gather
import random

app = Flask(__name__)

#TODO:
# have the page reload every minute?
# add evolutions or next/last entry in pokedex to left of imgs
# use arrow keys to go forward and backward in the dex
# .

# Want a new pokemon to be displayed and don't want to wait 60 seconds
# just refresh the page, it should update the calls
@app.route('/')     # main URL page
def index():
    nationalNo = gather.getPokeDexNum(random.randint(1, 898))
    pokemon = gather.getPokemon(nationalNo)
    img = gather.getStandImg(pokemon)
    shiny = gather.getShinyImg(pokemon)
    typeTypes = gather.getType(pokemon)
    species = gather.getSpecies(pokemon)
    height = gather.getHeight(pokemon)
    weight = gather.getWeight(pokemon)
    ability1 = gather.getAbilities(pokemon)[0]
    ability2 = gather.getAbilities(pokemon)[1]
    ability3 = gather.getAbilities(pokemon)[2]
    HP = gather.getHP(pokemon)
    attack = gather.getAttack(pokemon)
    defense = gather.getDefense(pokemon)
    spAtk = gather.getSpAtk(pokemon)
    spDef = gather.getSpDef(pokemon)
    speed = gather.getSpeed(pokemon)
    total = gather.getTotal(pokemon)
    entry = gather.getEntry(pokemon)
    gen = gather.getGen(nationalNo)
    nexPokeNo = gather.getNextPokemon(nationalNo)
    nexPokeName = gather.getPokemon(nexPokeNo)
    nexImg = gather.getStandImg(nexPokeName)
    prevPokeNo = gather.getPrevPokemon(nationalNo)
    prevPokeName = gather.getPokemon(prevPokeNo)
    prevImg = gather.getStandImg(prevPokeName)

    return render_template('index.html',
                           nationalNo=nationalNo,
                           pokemon=pokemon,
                           typeTypes=typeTypes,
                           species=species,
                           height=height,
                           weight=weight,
                           ability1=ability1,
                           ability2=ability2,
                           ability3=ability3,
                           HP=HP,
                           attack=attack,
                           defense=defense,
                           spAtk=spAtk,
                           spDef=spDef,
                           speed=speed,
                           img=img,
                           shiny = shiny,
                           total=total,
                           entry=entry,
                           nexPokeNo = nexPokeNo,
                           nexPokeName = nexPokeName,
                           nexImg = nexImg,
                           prevPokeNo = prevPokeNo,
                           prevPokeName = prevPokeName,
                           prevImg = prevImg,
                           gen=gen)


if __name__ == '__main__':
    app.run()
