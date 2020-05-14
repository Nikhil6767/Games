'''
Pokemon Tower
Simon Gordon
05-20-2019
'''
# https://www.spriters-resource.com/game_boy_advance/pokemonfireredleafgreen/sheet/3863/
import pygame
pygame.init() # loads the pygame module commands in the program
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SCREENDIM)

# COLOURS #
GREY=(50,50,50)

### CODE STARTS HERE ###

class movement:
	def __init__(self, movingSprites):
		self.movingSprites=movingSprites


	def move(self, pressedkeys, background, sprite, temp=True):
		while temp:
			leftMovement=1
			rightMovement=1
			upMovement=1
			downMovement=1
			temp=False

		if background.getX()>=256:
			leftMovement=0

		if background.getX()<=-220:
			rightMovement=0

		if background.getY()>=140:
			upMovement=0

		if background.getY()<=-147:
			downMovement=0

		if pressedkeys[pygame.K_w] and upMovement==1:
			for i in range(len(self.movingSprites)):
				sprite=self.movingSprites[i]
				sprite.y=sprite.y+1
				sprite.setPos(sprite.x, sprite.y)
				downMovement=0


		if pressedkeys[pygame.K_s] and downMovement==1:
			for i in range(len(self.movingSprites)):
				sprite=self.movingSprites[i]
				sprite.y=sprite.y-1
				sprite.setPos(sprite.x, sprite.y)
				upMovement=0

		if pressedkeys[pygame.K_a] and leftMovement==1:
			for i in range(len(self.movingSprites)):
				sprite=self.movingSprites[i]
				sprite.x=sprite.x+1
				sprite.setPos(sprite.x, sprite.y)
				rightMovement=1

		if pressedkeys[pygame.K_d] and rightMovement==1:
			for i in range(len(self.movingSprites)):
				sprite=self.movingSprites[i]
				sprite.x=sprite.x-1
				sprite.setPos(sprite.x, sprite.y)
				leftMovement=1

class healthBar:
	def __init__(self, healthMax, x, y):
		self.healthMax=healthMax
		self.x=x
		self.y=y


class myClass:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.pos = (self.x, self.y)
		self.surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
		self.red = 0
		self.green = 0
		self.blue = 0
		self.colour = (self.red, self.green, self.blue)

	def getSurface(self):
		return self.surface

	def getPos(self):
		return self.pos

	def getX(self):
		return self.x

	def getY(self):
		return self.y

class mySprite(myClass):
	def __init__(self, fileName, x=0, y=0):
		myClass.__init__(self)
		self.surface = pygame.image.load(fileName).convert_alpha()
		self.width = self.surface.get_rect()[2]
		self.height = self.surface.get_rect()[3]
		self.x=x
		self.y=y
		self.pos=(self.x, self.y)

	def setPos(self, x, y):
		self.pos=((x, y))

	def resize(self, width, height):
		self.width = width
		self.height = height
		self.dim = (self.width, self.height)
		self.surface = pygame.transform.smoothscale(self.getSurface(), self.dim)

	def rotate(self):
		self.surface = pygame.transform.rotate(self.surface, 270)

background=mySprite("media/background1.png", -5, 0)
background.resize(800,600)
background.setPos(background.x, background.y)

background2=mySprite("media/background2.png", -5, 0)
background2.resize(800,600)
background2.setPos(background2.x, background2.y)

player=mySprite("media/character.png", WIDTH/2, HEIGHT/2)
player.resize(50, 50)
player.setPos(player.x, player.y)

trainer=mySprite("media/trainer1.png", WIDTH/2-25, HEIGHT/2-100)
trainer.resize(50,50)
trainer.setPos(trainer.x, trainer.y)

trainer2=mySprite("media/trainer2.png", WIDTH/2-25, HEIGHT/2-100)
trainer2.resize(50,50)
trainer2.setPos(trainer2.x, trainer2.y)

pokeManager=mySprite("media/pokemonManager.png", 200, 300)
pokeManager.resize(50,50)
pokeManager.setPos(pokeManager.x, pokeManager.y)

pokeManager2=mySprite("media/pokemonManager.png", 200, 300)
pokeManager2.resize(50,50)
pokeManager2.setPos(pokeManager.x, pokeManager.y)

movingSprites=[] # list containing the sprites that will move
movingSprites.append(background)
movingSprites.append(trainer)
movingSprites.append(pokeManager)

movingSprites2=[] # list containing the sprites that will move
movingSprites2.append(background2)
movingSprites2.append(trainer2)
movingSprites2.append(pokeManager2)


def collision(mapSprite):
	if mapSprite.getX()>256:
		mapSprite.x=256

	elif mapSprite.getX()<-220:
		mapSprite.x=-220

	if mapSprite.getY()>159:
		mapSprite.y=159

	elif mapSprite.getY()<-147:
		mapSprite.y=-147

def interaction(npc, nurse, pressedKeys):
	if npc.x>350 and npc.x<425:
		if npc.y>250 and npc.y<300:
			if pressedKeys[pygame.K_e]:
				return 1
			else:
				return 0

	if nurse.x>350 and nurse.x<425:
		if nurse.y<320 and nurse.x>250:
			if pressedKeys[pygame.K_e]:
				return 2
			else:
				return 0

def nurse(npc, pressedKeys):
	if npc.x>350 and npc.x<425:
		if npc.y<320 and npc.x>250:
			if pressedKeys[pygame.K_e]:
				return 1
			else:
				return 0

def nextFloor(background, pressedKeys):
	if background.x>0 and background.x<50:
		if background.y>130:
			if pressedKeys[pygame.K_e]:
				return True


screenMovement = movement(movingSprites) # object in charge of player movement

'''
running = True
while running:
	for event in pygame.event.get(): # returns all inputs and triggers into an array
		if event.type == pygame.QUIT: # if the red x was clicked
			running = False
	pressedkeys=pygame.key.get_pressed() # inputs from a person

	screen.fill(GREY)

	for i in range(len(movingSprites)):
		sprite=movingSprites[i]
		screen.blit(sprite.getSurface(), sprite.getPos())

	collision(background)
	tempvar=interaction(trainer, pokeManager, pressedkeys)
	pkVar = nurse(pokeManager, pressedkeys)

	nextFloor(background, pressedkeys)
	print(background.x, background.y)

	screen.blit(player.getSurface(), player.getPos()) # THE player on the screen

	for i in range(len(movingSprites)):
		screenMovement.move(pressedkeys, movingSprites[0], movingSprites[i])

	pygame.display.flip() # update the screen with changes

pygame.quit()
'''