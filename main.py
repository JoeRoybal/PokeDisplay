from flask import Flask, render_template
import gather
import time, sched
import os
import multiprocessing

app = Flask(__name__)

#TODO:
# have the page reload every minute?
# add evolutions
# use arrow keys to go forward and backward in the dex
# .

@app.route('/')     # main URL page
def index():
    img = gather.standard
    shiny = gather.shiny
    nationalNo = gather.nationalNo
    pokemon = gather.pokemon
    typeTypes = gather.typeTypes
    species = gather.species
    height = gather.height
    weight = gather.weight
    ability1 = gather.ability1
    ability2 = gather.ability2
    ability3 = gather.ability3
    HP = gather.HP
    attack = gather.attack
    defense = gather.defense
    spAtk = gather.spAtk
    spDef = gather.spDef
    speed = gather.speed
    total = gather.total
    entry = gather.entry
    gen = gather.genNum

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
                           gen=gen)

def pokemonUpdate():
    s = sched.scheduler(time.time, time.sleep)
    def PokemonPerMinute(sc): 
        os.system('python gather.py')
        print(gather.pokemon)
        s.enter(5, 1, PokemonPerMinute, (sc,))

    s.enter(5, 1, PokemonPerMinute, (s,))
    s.run()

def mainApp():
    app.run()

if __name__ == '__main__':
    # updater = multiprocessing.Process(name='updater', target=pokemonUpdate)
    # webApp = multiprocessing.Process(name='webApp', target=mainApp)
    # updater.start()
    # webApp.start()
    mainApp()

    #gather.py runs three times?