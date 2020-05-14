from Classes import *
from Text_and_Sprites import *
## Creating Attacks
attackTypes = {
	"normal": 1,
	"fighting": 2,
	"flying": 3,
	"poison": 4,
	"ground": 5,
	"rock": 6,
	"bug": 7,
	"ghost": 8,
	"steel": 9,
	"fire": 10,
	"water": 11,
	"grass": 12,
	"electric": 13,
	"psychic": 14,
	"ice": 15,
	"dragon": 16,
	"dark": 17,
	"fairy": 18
}

# ground
earthquake = attack('media/earthquake.png', "Earthquake", 100, 10, attackTypes["ground"], 1, 100) # 1 is physical 2 is special
# rock
rockSlide = attack('media/rockslide.png', "Rock Slide", 75, 10, attackTypes["rock"], 1, 90)
# electric
thunderbolt = attack('media/thunderbolt.png', "Thunderbolt", 90, 15, attackTypes["electric"], 2, 100)
# steel
flashCannon = attack('media/flashCannon.png', "Flash Cannon", 80, 10, attackTypes["steel"], 2, 100)
# dragon
dragonClaw = attack('media/dragonClaw.png', "Dragon Claw", 80, 15, attackTypes["dragon"], 1, 100)
# water
surf = attack('media/surf.png', "Surf", 90, 15, attackTypes["water"], 2, 100)
#ice
iceBeam = attack('media/iceBeam.png', "Ice Beam", 90, 10, attackTypes["ice"], 2, 100)
#fire
blazeKick = attack('media/blazeKick.png', "Blaze Kick", 85, 10, attackTypes["fire"], 1, 90)
#fighting
highJumpKick = attack('media/highJumpKick.png', "Hi Jump Kick", 130, 10, attackTypes["fighting"], 1, 70)
hammerArm = attack('media/hammerArm.png', "Hammer Arm", 100, 10, attackTypes["fighting"], 1, 90)
#grass ## GET IMAGE
#leafStorm = attack('media/leafStorm/png', "Leaf Storm", 130, 5, attackTypes["grass"], 2, 90)
# psychic
psychic = attack('media/psychic.png', "Psychic", 90, 10, attackTypes["psychic"], 2, 100)
# ghost
shadowClaw = attack('media/shadowClaw.png', "Shadow Claw", 70, 15, attackTypes["ghost"], 1, 100)
# dark
nightSlash = attack('media/nightSlash.png', "Night Slash", 70, 15, attackTypes["dark"], 1, 100)
crunch = attack('media/crunch.png', "Crunch", 80, 15, attackTypes["dark"], 1, 100)
#flying
airSlash = attack('media/airSlash.png', "Air Slash", 75, 20, attackTypes["flying"], 2, 100)
braveBird = attack('media/braveBird.png', "Brave Bird", 120, 15, attackTypes["flying"], 1, 80)
# fairy
moonBlast = attack('media/moonBlast.png', "Moonblast", 95, 15, attackTypes["fairy"], 2, 100)
# normal
bodySlam = attack('media/bodySlam.png', "Body Slam", 85, 15, attackTypes["normal"], 1, 100)
crushClaw = attack('media/crushClaw.png', "Crush Claw", 75, 10, attackTypes["normal"], 1, 95)

bodySlam.resize(200, 150)
bodySlam.setPos((350, 200))

earthquake.resize(200, 150)
earthquake.setPos((350, 200))

rockSlide.resize(200, 150)
rockSlide.setPos((350, 200))

crushClaw.resize(200, 150)
crushClaw.setPos((350, 200))

moonBlast.resize(200, 150)
moonBlast.setPos((350, 200))

crunch.resize(200, 150)
crunch.setPos((350, 200))

airSlash.resize(200, 150)
airSlash.setPos((350, 200))

braveBird.resize(200, 150)
braveBird.setPos((350, 200))

nightSlash.resize(200, 150)
nightSlash.setPos((350, 200))

shadowClaw.resize(200, 150)
shadowClaw.setPos((350, 200))

psychic.resize(200, 150)
psychic.setPos((350, 200))

highJumpKick.resize(200, 150)
highJumpKick.setPos((350, 200))

hammerArm.resize(200, 150)
hammerArm.setPos((350, 200))

blazeKick.resize(200, 150)
blazeKick.setPos((350, 200))

iceBeam.resize(200, 150)
iceBeam.setPos((350, 200))

surf.resize(200, 150)
surf.setPos((350, 200))

dragonClaw.resize(200, 150)
dragonClaw.setPos((350, 200))

flashCannon.resize(200, 150)
flashCannon.setPos((350, 200))

thunderbolt.resize(200, 150)
thunderbolt.setPos((350, 200))

# stats go Hp, Attk, Def, SpAttk, SpDef, spd
## Creating pokemons
# name, sprite, type, stats, attacks, weakness, resistance, immunites
rhydon = pokemon("Rhydon", 'media/rhydonBack.png', [attackTypes["rock"], attackTypes["ground"]], [105, 130, 120, 45, 45, 40], [earthquake, rockSlide], [attackTypes["water"], attackTypes["grass"], attackTypes["steel"], attackTypes["ice"], attackTypes["fighting"], attackTypes["ground"]], [attackTypes["normal"], attackTypes["fire"], attackTypes["poison"], attackTypes["flying"], attackTypes["rock"]], [attackTypes["electric"]])
magnezone = pokemon("Magnezone", 'media/magnezone.png', [attackTypes["electric"], attackTypes["steel"]], [70, 70, 115, 130, 90, 60], [thunderbolt, flashCannon], [attackTypes["fire"], attackTypes["fighting"], attackTypes["ground"]], [attackTypes["normal"], attackTypes["electric"], attackTypes["grass"], attackTypes["ice"], attackTypes["flying"], attackTypes["psychic"], attackTypes["bug"], attackTypes["rock"], attackTypes["dragon"], attackTypes["steel"], attackTypes["fairy"]], [attackTypes["poison"]])
haxorus = pokemon("Haxorus", 'media/haxorusBack.png', [attackTypes["dragon"]], [76, 147, 90, 60, 70, 97], [dragonClaw, earthquake], [attackTypes["fairy"], attackTypes["dragon"], attackTypes["ice"]], [attackTypes["fire"], attackTypes["water"], attackTypes["grass"], attackTypes["electric"]], [0])
lapras = pokemon("Lapras", 'media/lapras.png', [attackTypes["water"], attackTypes["ice"]], [130, 85, 80, 85, 95, 60], [surf, iceBeam], [attackTypes["electric"], attackTypes["grass"], attackTypes["fighting"], attackTypes["rock"]], [attackTypes["water"], attackTypes["ice"]], [0])
exeggutor = pokemon("Exeggutor", "media/exeggutor.png", [attackTypes["grass"], attackTypes["psychic"]], [95, 95, 85, 125, 75, 55], [psychic], [attackTypes["fire"], attackTypes["ice"], attackTypes["poison"], attackTypes["flying"], attackTypes["bug"], attackTypes["ghost"], attackTypes["dark"]], [attackTypes["water"], attackTypes["electric"], attackTypes["grass"], attackTypes["fighting"], attackTypes["ground"], attackTypes["psychic"]], [0])
# add leaf storm to exeggutor
blaziken = pokemon("Blaziken", "media/blazikenBack.png", [attackTypes["fire"], attackTypes["fighting"]], [80, 120, 70, 110, 70, 800], [blazeKick, highJumpKick], [attackTypes["water"], attackTypes["ground"], attackTypes["flying"], attackTypes["psychic"]], [attackTypes["fire"], attackTypes["grass"], attackTypes["ice"], attackTypes["bug"], attackTypes["dark"], attackTypes["steel"]], [0])
crobat = pokemon("Crobat", "media/crobat.png", [attackTypes["poison"], attackTypes["flying"]], [85, 90, 80, 70, 80, 130], [crunch, airSlash], [attackTypes["electric"], attackTypes["ice"], attackTypes["psychic"], attackTypes["rock"]], [attackTypes["grass"], attackTypes["fighting"],  attackTypes["poison"], attackTypes["bug"], attackTypes["fairy"]], [attackTypes["ground"]])# crobat cpu
dusknoir = pokemon("Dusknoir", "media/dusknoirBack.png", [attackTypes["ghost"]], [45, 100, 135, 65, 135, 45], [shadowClaw, nightSlash], [attackTypes["dark"], attackTypes["ghost"]], [attackTypes["poison"], attackTypes["bug"]], [attackTypes["fighting"], attackTypes["normal"]])# dusknoir user
krookodile = pokemon("Krookodile", "media/krookodile.png", [attackTypes["ground"], attackTypes["dark"]], [95, 117, 80, 65, 70, 92], [nightSlash, earthquake], [attackTypes["water"], attackTypes["grass"], attackTypes["ice"], attackTypes["fighting"], attackTypes["bug"], attackTypes["fairy"]], [attackTypes["poison"], attackTypes["rock"], attackTypes["ghost"], attackTypes["dark"]], [attackTypes["electric"], attackTypes["psychic"]])# krookodile cpu
gardevoir = pokemon("Gardevoir", "media/gardevoirBack.png", [attackTypes["psychic"], attackTypes["fairy"]], [68, 65, 65, 125, 115, 80], [moonBlast, psychic], [attackTypes["poison"], attackTypes["steel"], attackTypes["ghost"]], [attackTypes["fighting"], attackTypes["psychic"]], [attackTypes["dragon"]]) # gardevoir user
lickilicky = pokemon("Lickilicky", "media/lickilicky.png", [attackTypes["normal"]], [110, 85, 95, 80, 95, 50], [bodySlam, hammerArm], [attackTypes["fighting"]], [0], [attackTypes["ghost"]]) # lickilicky cpu
braviary = pokemon("Braviary", "media/braviaryBack.png", [attackTypes["normal"], attackTypes["flying"]], [100, 123, 75, 57, 75, 80], [crushClaw, braveBird], [attackTypes["electric"], attackTypes["ice"], attackTypes["rock"]], [attackTypes["grass"], attackTypes["bug"]], [attackTypes["ground"], attackTypes["ghost"]]) #braviary user

# making stuff the right size
rhydon.resize(350, 350)
rhydon.setPos((10, HEIGHT-userBattleBox.getHeight()-290))

magnezone.resize(300, 300)
magnezone.setPos((WIDTH-330, 10))

haxorus.resize(350, 300)
haxorus.setPos((10, HEIGHT-userBattleBox.getHeight()-290))

lapras.resize(300, 300)
lapras.setPos((WIDTH-330, 10))

blaziken.resize(375, 375)
blaziken.setPos((10, HEIGHT-userBattleBox.getHeight()-340))

exeggutor.resize(300, 300)
exeggutor.setPos((WIDTH-330, 10))

dusknoir.resize(350, 350)
dusknoir.setPos((10, HEIGHT-userBattleBox.getHeight()-305))

crobat.resize(300, 300)
crobat.setPos((WIDTH-330, 10))

gardevoir.resize(335, 335)
gardevoir.setPos((5, HEIGHT-userBattleBox.getHeight()-305))

krookodile.resize(300, 280)
krookodile.setPos((WIDTH-300, 10))

braviary.resize(300, 300)
braviary.setPos((5, HEIGHT-userBattleBox.getHeight()-305))

lickilicky.resize(300, 325)
lickilicky.setPos((WIDTH-300, 10))