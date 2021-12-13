from flask import Flask, render_template
import gather

app = Flask(__name__)


@app.route('/')     # main URL page
def index():
    nationalNo = gather.nationalNo
    pokemon = gather.pokemon
    img = gather.img
    shinyImg = gather.shinyImg
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

    return render_template('index.html',
                           nationalNo=nationalNo,
                           pokemon=pokemon,
                           img=img,
                           shinyImg=shinyImg,
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
                           total=total)


if __name__ == '__main__':
    app.run()
