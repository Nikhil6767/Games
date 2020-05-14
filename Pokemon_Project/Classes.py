'''
Title:
Author: Nikhil Nayyar
Date Created: 16/05/19
'''
import pygame, random, time

### Classes
class myClass:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
		self.pos = (self.x, self.y)
		self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
		self.red = 0
		self.green = 0
		self.blue = 0
		self.colour = (self.red, self.green, self.blue)

	def getSurface(self):  # encapsulation
		return self.surface

	def getPos(self):
		return self.pos

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getWidth(self):
		return self.width

	def getHeight(self):
		return self.height

	def setPos(self, pos):
		self.x = pos[0]
		self.y = pos[1]
		self.pos = (self.x, self.y)

	def setColour(self, colour):
		self.colour = colour


class box(myClass):
	def __init__(self, width, height, x=0, y=0):
		myClass.__init__(self, x, y)
		self.width = width
		self.height = height
		self.dim = (self.width, self.height)
		self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
		self.surface.fill(self.colour)

	def setColour(self, colour):
		self.colour = colour
		self.surface.fill(self.colour)


class text(myClass):
	def __init__(self, content, fontSize=24):
		myClass.__init__(self)
		self.width = self.surface.get_rect()[2]
		self.height = self.surface.get_rect()[3]
		self.font = 'Pokemon GB.ttf'
		self.fontFam = self.font
		self.fontSize = fontSize
		self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
		self.content = content
		self.surface = self.font.render(self.content, 1, self.colour)

	def setColour(self, colour):
		myClass.setColour(self, colour)
		self.surface = self.font.render(self.content, 1, self.colour)

	def setFont(self, fontFam):
		self.fontFam = fontFam
		self.font = pygame.font.SysFont(self.fontFam, self.fontSize)
		self.surface = self.font.render(self.content, 1, self.colour)

	def setContent(self, content):
		self.content = content
		self.surface = self.font.render(self.content, 1, self.colour)

	def getText(self):
		return myClass.getSurface(self)


class mySprite(myClass):
	def __init__(self, fileName):
		myClass.__init__(self)
		self.surface = pygame.image.load(fileName).convert_alpha()
		self.width = self.surface.get_rect()[2]
		self.height = self.surface.get_rect()[3]

	def resize(self, width, height):
		self.width = width
		self.height = height
		self.dim = (self.width, self.height)
		self.surface = pygame.transform.smoothscale(self.getSurface(), self.dim)

	def rotate(self):
		self.surface = pygame.transform.rotate(self.surface, 270)


class attack(mySprite):
	def __init__(self, filename, name, damage, powerPoints, type, attackType, accuracy):
		mySprite.__init__(self, filename)
		self.name = name
		self.damage = damage
		self.powerPoints = powerPoints
		self.type = type
		self.attackType = attackType
		self.accuracy = accuracy

	def getDamage(self):
		return self.damage

	def getType(self):
		return self.type

	def getAttackType(self):
		return self.attackType

	def getAccuracy(self):
		return self.accuracy

	def getName(self):
		return self.name

	def __str__(self):
		return self.name


class pokemon(mySprite):
	def __init__(self, name, filename, type, stats, attacks, weakness, resistance, immunites):
		mySprite.__init__(self, filename)
		self.name = name
		self.type = type
		self.stats = stats
		self.attacks = attacks
		self.weakness = weakness
		self.resistance = resistance
		self.immunites = immunites

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getStats(self):
		return self.stats

	def getAttacks(self):
		return self.attacks

	def getWeakness(self):
		return self.weakness

	def getResistance(self):
		return self.resistance

	def getImmunites(self):
		return self.immunites


class Battle:
	def __init__(self):
		self.state = 0
		self.poke1 = 0
		self.poke2 = 0
		self.userWin = 0
		self.cpuWin = 0
		self.attack = 0
		self.immune = 0
		self.end = 0
		self.u = 0  # user index number for party pokemon
		self.c = 0  # cpu index number for party pokemon
		self.spd1 = 0
		self.spd2 = 0
		self.cpuHp = 0
		self.userHp = 0
		self.tempcpuHp = 0
		self.tempUserHp = 0
		self.turns = 0
		self.askAttack = 0
		self.cpuFaint = 0
		self.userFaint = 0
		self.start = 1

	def update(self, pkmnParty1, pkmnParty2, disp, key, bbox):  # pkmnparty1 is user, pkmnparty2 is cpu
		if self.cpuWin == 0 and self.userWin == 0: # show the pokemon sprites while now one has won
			userPkN = text(str(pkmnParty1[self.u].getName()), 36)
			cpuPkN = text(str(pkmnParty2[self.c].getName()), 36)
			userHp = text("Hp: " + str(self.userHp), 36)
			cpuHp = text("Hp: " + str(self.cpuHp), 36)
			cpuPkmnName2 = pkmnParty2[self.c].getName()
			pkmnName2 = pkmnParty1[self.u].getName()
			if self.start == 1:
				chalText = text("You are challenged by", 36)
				chalText.setPos((0, 600 - 85))
				disp.blit(chalText.getText(), chalText.getPos())
				chalTextMore = text("Battle Tower Trainer!", 36)
				chalTextMore.setPos((0, 600 - 45))
				disp.blit(chalTextMore.getText(), chalTextMore.getPos())
				pygame.display.flip()
				time.sleep(3)
				disp.blit(bbox.getSurface(), bbox.getPos())
				batIntroText = text("Battle Tower Trainer", 36)
				morebatText = text("sent out " + str(cpuPkmnName2), 36)
				batIntroText.setPos((0, 600 - 85))
				disp.blit(batIntroText.getText(), batIntroText.getPos())
				morebatText.setPos((0, 600 - 45))
				disp.blit(morebatText.getText(), morebatText.getPos())
				pygame.display.flip()
				time.sleep(3)
				disp.blit(bbox.getSurface(), bbox.getPos())
				userBatText = text("You sent out " + str(pkmnName2), 36)
				userBatText.setPos((0, 600 - 85))
				disp.blit(userBatText.getText(), userBatText.getPos())
				pygame.display.flip()
				time.sleep(2)
				self.start = 0
			userPkN.setPos((800 - 200, 400))
			cpuPkN.setPos((0, 30))
			userHp.setPos((800 - 200, 450))
			cpuHp.setPos((0, 60))
			disp.blit(userPkN.getText(), userPkN.getPos())
			disp.blit(cpuPkN.getText(), cpuPkN.getPos())
			disp.blit(userHp.getText(), userHp.getPos())
			disp.blit(cpuHp.getText(), cpuHp.getPos())
			disp.blit(pkmnParty1[self.u].getSurface(), pkmnParty1[self.u].getPos())
			disp.blit(pkmnParty2[self.c].getSurface(), pkmnParty2[self.c].getPos())


		if self.state == 0: # at the beginging of a turn get the speed of each pokemon to determine who goes first
			self.spd1 = pkmnParty1[self.u].getStats()[5]
			self.spd2 = pkmnParty2[self.c].getStats()[5]


			if self.spd1 > self.spd2:
				self.poke1 = 1
			else:
				self.poke2 = 1

			self.state = 1

		if self.state == 1: # get the Hp stat of each pokemon or if a pokemon dies get the new hp of only that pokemon

			if self.cpuFaint == 1:
				self.tempcpuHp = pkmnParty2[self.c].getStats()[0]  # get Hp of cpu
				# hp calc
				self.cpuHp = 2 * self.tempcpuHp * 50
				self.cpuHp = self.cpuHp / 100
				self.cpuHp = self.cpuHp + 60
				self.state = 2
				self.cpuFaint = 0

			elif self.userFaint == 1:
				self.tempUserHp = pkmnParty1[self.u].getStats()[0]  # get Hp of user
				# hp calc
				self.userHp = 2 * self.tempUserHp * 50
				self.userHp = self.userHp / 100
				self.userHp = self.userHp + 60
				self.state = 2
				self.userFaint = 0


			elif self.turns == 0:
				self.tempcpuHp = pkmnParty2[self.c].getStats()[0]  # get Hp of cpu
				# hp calc
				self.cpuHp = 2 * self.tempcpuHp * 50
				self.cpuHp = self.cpuHp / 100
				self.cpuHp = self.cpuHp + 60

				self.tempUserHp = pkmnParty1[self.u].getStats()[0]  # get Hp of user
				# hp calc
				self.userHp = 2 * self.tempUserHp * 50
				self.userHp = self.userHp / 100
				self.userHp = self.userHp + 60
				self.state = 2

			self.cpuHp = int(self.cpuHp)
			self.userHp = int(self.userHp)
		if self.state == 2: # get the input from the user to chose what attack to use
			attk1 = pkmnParty1[self.u].getAttacks()[0]
			attN1 = text("(1) " + str(attk1), 36)
			attN1.setPos((0, 600 - 85))
			attk2 = pkmnParty1[self.u].getAttacks()[1]
			attN2 = text("(2) " + str(attk2), 36)
			attN2.setPos((0, 600 - 45))
			disp.blit(attN1.getText(), attN1.getPos())
			disp.blit(attN2.getText(), attN2.getPos())
			self.askAttack = 0
			if key[pygame.K_1]:
				self.askAttack = 1
				self.turns = 0
				self.state = 3
			elif key[pygame.K_2]:
				self.askAttack = 2
				self.turns = 0
				self.state = 3
			return

		if self.state == 3:
			if self.turns == 2: # if a turn has passed and no one fainted go back to state 2 to get attack inputs
				self.state = 2
				return

			if self.poke1 == 1: # users turn
				pkmnName = pkmnParty1[self.u].getName()
				pkmnAttkName = pkmnParty1[self.u].getAttacks()[self.askAttack - 1]

				# text stuff
				pkAction = text(str(pkmnName) + " used " + str(pkmnAttkName), 36)
				pkAction.setPos((0, 600 - 45))
				monkey = 1
				if monkey == 1: # make text appear for 3 seconds
					disp.blit(pkAction.getText(), pkAction.getPos())
					pygame.display.flip()
					time.sleep(2)
					disp.blit(bbox.getSurface(), bbox.getPos())
					monkey = 0

				attTimer = 1
				if attTimer == 1:  # make attack appear for 3 seconds
					disp.blit(pkmnParty1[self.u].getAttacks()[self.askAttack - 1].getSurface(), pkmnParty1[self.u].getAttacks()[self.askAttack - 1].getPos())
					pygame.display.flip()
					time.sleep(1)
					attTimer = 0

				typeAttack = pkmnParty1[self.u].getAttacks()[self.askAttack - 1].getType()  # get the type of attakc (rock, grounnd etc)
				for i in range(len(pkmnParty2[self.c].getImmunites())): # check for immunites
					if typeAttack == pkmnParty2[self.c].getImmunites()[i]:
						immText = text("It does not effect " + str(pkmnParty2[self.c].getName()), 36)
						immText.setPos((0, 600-45))
						ooga = 1
						if ooga == 1:
							disp.blit(immText.getText(), immText.getPos())
							pygame.display.flip()
							time.sleep(2)
							disp.blit(bbox.getSurface(), bbox.getPos())
							ooga = 0
						self.immune = 1
						self.poke1 = 0
						self.poke2 = 1
						return

				pokeAccur = random.randint(1, 100)  # choose random number
				if pokeAccur > pkmnParty1[self.u].getAttacks()[self.askAttack - 1].getAccuracy():  # check if move hits based on attack accuracy
					missText = text(str(pkmnParty2[self.c].getName()) + " avoided the attack", 36)
					missText.setPos((0, 600 - 45))
					booga = 1
					if booga == 1:
						disp.blit(missText.getText(), missText.getPos())
						pygame.display.flip()
						time.sleep(2)
						disp.blit(bbox.getSurface(), bbox.getPos())
						booga = 0
					self.turns +=1
					self.poke1 = 0
					self.poke2 = 1
					return

				attack = pkmnParty1[self.u].getAttacks()[self.askAttack - 1].getDamage()  # get damage of chosen attack

				attackType = pkmnParty1[self.u].getAttacks()[
					self.askAttack - 1].getAttackType()  # check if attack is physical or special

				if attackType == 1:  # get the appropriate defense based on the attack type
					cpuDef = pkmnParty2[self.c].getStats()[2]
				else:
					cpuDef = pkmnParty2[self.c].getStats()[4]

				if attackType == 1:  # get the appropriate attack stat based on teh attack type
					pkmnAttk = pkmnParty1[self.u].getStats()[1]
				else:
					pkmnAttk = pkmnParty1[self.u].getStats()[3]

				#print("initial cpu Hp: " + str(self.cpuHp))

				# damage calc
				damage = 2 * 50
				damage = damage / 5
				damage += 2
				damage = damage * attack
				damage = damage * pkmnAttk
				damage = damage / cpuDef
				damage = damage / 50
				damage += 2

				for i in range(len(pkmnParty1[
									   self.u].getType())):  # checks if attack is STAB (same type attack bonus) and if so multiply attack by 1.5
					if typeAttack == pkmnParty1[self.u].getType()[i]:
						damage = damage * 1.5
					else:
						pass

				for i in range(len(pkmnParty2[self.c].getWeakness())):  # checks if attack is super effective
					if typeAttack == pkmnParty2[self.c].getWeakness()[i]:
						damage = damage * 2
						time.sleep(1)
						supText = text("Its super effective", 36)
						supText.setPos((0, 600 - 45))
						monkeyagg = 1
						if monkeyagg == 1:  # make text appear for 3 seconds
							disp.blit(supText.getText(), supText.getPos())
							pygame.display.flip()
							time.sleep(2.5)
							disp.blit(bbox.getSurface(), bbox.getPos())
							monkeyagg = 0


				for i in range(len(pkmnParty2[self.c].getResistance())):  # checks if attack is not very effective
					if typeAttack == pkmnParty2[self.c].getResistance()[i]:
						damage = damage * 0.5
						notText = text("Its not very effective", 36)
						notText.setPos((0, 600 - 45))
						moremonkey = 1
						if moremonkey == 1:  # make text appear for 3 seconds
							disp.blit(notText.getText(), notText.getPos())
							pygame.display.flip()
							time.sleep(2.5)
							disp.blit(bbox.getSurface(), bbox.getPos())
							moremonkey = 0

				crit = random.randint(1, 100)
				if crit > 96:  # check for a critical hit (4.16 % chance)
					damage = damage * 1.5
					critText = text("A critical hit!", 36)
					critText.setPos((0, 600 - 45))
					monkeymoremanmonkey = 1
					if monkeymoremanmonkey == 1:  # make text appear for 3 seconds
						disp.blit(critText.getText(), critText.getPos())
						pygame.display.flip()
						time.sleep(2.5)
						monkeymoremanmonkey = 0

				else:
					pass

				roll = random.randint(1, 25)
				damage = damage - roll

				if self.immune == 1:
					damage = 0
					self.immune = 0

				#print("damage given: " + str(damage))
				disp.blit(bbox.getSurface(), bbox.getPos())
				self.cpuHp = self.cpuHp - damage
				self.cpuHp = int(self.cpuHp)
				if self.cpuHp < 0:
					self.cpuHp = 0

					faintText = text(str(pkmnParty2[self.c].getName()) + " fainted", 36)
					faintText.setPos((0, 600 - 45))
					monkeyman = 1
					if monkeyman == 1:
						disp.blit(faintText.getText(), faintText.getPos())
						pygame.display.flip()
						time.sleep(2.5)
						monkeyman = 0

					pkmnParty2.pop(self.c)

					self.cpuFaint = 1
					#print("final cpuHP: " + str(self.cpuHp))
					if len(pkmnParty2) == 0:
						self.userWin = 1
						self.poke2 = 0
						self.poke1 = 0
						return
					else:
						#print("mons fainted")
						self.state = 0
						self.poke1 = 0
						self.poke2 = 1
						return

				#print("final cpuHP: " + str(self.cpuHp))
				self.poke1 = 0
				self.poke2 = 1
				self.turns += 1
				return





			if self.poke2 == 1:  ### CPUS TURN
				#print(self.cpuHp)
				cpuAttacks = pkmnParty2[self.c].getAttacks()
				cpuAskAttack = cpuAttacks[0]

				for i in range(len(pkmnParty1[self.u].getWeakness())):  # cpu checks if it has a super effective attack so it will use it
					for j in range(len(cpuAttacks)):
						if cpuAttacks[j].getType() == pkmnParty1[self.u].getWeakness()[i]:
							cpuAskAttack = cpuAttacks[j]
							#print(cpuAskAttack)

				cpuTypeAttack = cpuAskAttack.getType()
				for i in range(len(pkmnParty1[self.u].getImmunites())): # check for immunites
					if cpuAskAttack.getType() != pkmnParty1[self.u].getImmunites()[i]:
						pass
					else:
						cpuAskAttack = cpuAttacks[1]
					if cpuTypeAttack == pkmnParty1[self.u].getImmunites()[i]:
						immText = text("It does not effect " + str(pkmnParty1[self.u].getName()), 36)
						immText.setPos((0, 600-45))
						ooga = 1
						if ooga == 1:
							disp.blit(immText.getText(), immText.getPos())
							pygame.display.flip()
							time.sleep(2)
							disp.blit(bbox.getSurface(), bbox.getPos())
							ooga = 0
						self.immune = 1
						self.poke1 = 1
						self.poke2 = 0
						return




				cpuPkmnName = pkmnParty2[self.c].getName()
				cpuPkmnAttkName = cpuAskAttack.getName()
				# text stuff
				cpuAction = text(str(cpuPkmnName) + " used " + str(cpuPkmnAttkName), 36)
				cpuAction.setPos((0, 600 - 45))
				cpumonkey = 1
				if cpumonkey == 1:  # make text appear for 3 seconds
					disp.blit(cpuAction.getText(), cpuAction.getPos())
					pygame.display.flip()
					time.sleep(2)
					disp.blit(bbox.getSurface(), bbox.getPos())
					cpumonkey = 0

				attTimer = 1
				if attTimer == 1:  # make attack appear for 1 seconds
					disp.blit(cpuAskAttack.getSurface(), cpuAskAttack.getPos())
					pygame.display.flip()
					time.sleep(1)
					attTimer = 0

				cpuTypeAttack = cpuAskAttack.getType()  # get the type of attakc (rock, grounnd etc)
				cpupokeAccur = random.randint(1, 100)  # choose random number
				if cpupokeAccur > cpuAskAttack.getAccuracy():  # check if move hits based on attack accuracy
					missText = text(str(pkmnParty1[self.u].getName()) + " avoided the attack", 36)
					missText.setPos((0, 600 - 45))
					booga = 1
					if booga == 1:
						disp.blit(missText.getText(), missText.getPos())
						pygame.display.flip()
						time.sleep(2)
						disp.blit(bbox.getSurface(), bbox.getPos())
						booga = 0
					self.poke1 = 1
					self.poke2 = 0
					return

				cpuAttack = cpuAskAttack.getDamage()  # damage of cpu's attack

				cpuAttackType = cpuAskAttack.getAttackType()  # check if attack is physical or special

				if cpuAttackType == 1:  # get the appropriate defense based on the attack type
					userDef = pkmnParty1[self.u].getStats()[2]
				else:
					userDef = pkmnParty1[self.u].getStats()[4]

				if cpuAttackType == 1:  # get the appropriate attack stat based on teh attack type
					cpupkmnAttk = pkmnParty2[self.c].getStats()[1]
				else:
					cpupkmnAttk = pkmnParty2[self.c].getStats()[3]

				#print("inital user hp: " + str(self.userHp))

				# damage calc
				cpuDamage = 2 * 50
				cpuDamage = cpuDamage / 5
				cpuDamage += 2
				cpuDamage = cpuDamage * cpuAttack
				cpuDamage = cpuDamage * cpupkmnAttk
				cpuDamage = cpuDamage / userDef
				cpuDamage = cpuDamage / 50
				cpuDamage += 2

				for i in range(len(pkmnParty2[self.c].getType())):  # checks if attack is STAB (same type attack bonus) and if so multiply attack by 1.5
					if cpuTypeAttack == pkmnParty2[self.c].getType()[i]:
						cpuDamage = cpuDamage * 1.5
					else:
						pass

				for i in range(len(pkmnParty1[self.u].getWeakness())):  # checks if attack is super effective
					if cpuTypeAttack == pkmnParty1[self.u].getWeakness()[i]:
						cpuDamage = cpuDamage * 2
						supText = text("Its super effective", 36)
						supText.setPos((0, 600 - 45))
						monkeyagg = 1
						if monkeyagg == 1:  # make text appear for 3 seconds
							disp.blit(supText.getText(), supText.getPos())
							pygame.display.flip()
							time.sleep(2.5)
							disp.blit(bbox.getSurface(), bbox.getPos())
							monkeyagg = 0

				for i in range(len(pkmnParty1[self.u].getResistance())):  # checks if attack is not very effective
					if cpuTypeAttack == pkmnParty1[self.u].getResistance()[i]:
						cpuDamage = cpuDamage * 0.5
						notText = text("Its not very effective", 36)
						notText.setPos((0, 600 - 45))
						moremonkey = 1
						if moremonkey == 1:  # make text appear for 3 seconds
							disp.blit(notText.getText(), notText.getPos())
							pygame.display.flip()
							time.sleep(2.5)
							disp.blit(bbox.getSurface(), bbox.getPos())
							moremonkey = 0

				cpucrit = random.randint(1, 100)
				if cpucrit > 96:  # check for a critical hit (4.16 % chance)
					cpuDamage = cpuDamage * 1.5
					critText = text("A critical hit!", 36)
					critText.setPos((0, 600 - 45))
					monkeymoremanmonkey = 1
					if monkeymoremanmonkey == 1:  # make text appear for 3 seconds
						disp.blit(critText.getText(), critText.getPos())
						pygame.display.flip()
						time.sleep(2.5)
						monkeymoremanmonkey = 0
				else:
					pass

				if self.immune == 1:
					cpuDamage = 0
					self.immune = 0
				#print("damage given from cpu: " + str(cpuDamage))

				self.userHp = self.userHp - cpuDamage
				self.userHp = int(self.userHp)
				#print("final user Hp: " + str(self.userHp))
				disp.blit(bbox.getSurface(), bbox.getPos())


				if self.userHp < 0:
					self.userHp = 0
					faintText = text(str(pkmnParty1[self.u].getName()) + " fainted", 36)
					faintText.setPos((0, 600 - 45))
					monkeyman = 1
					if monkeyman == 1:
						disp.blit(faintText.getText(), faintText.getPos())
						pygame.display.flip()
						time.sleep(2.5)
						monkeyman = 0
					pkmnParty1.pop(self.u)
					#print("monkey faint activated")
					self.userFaint = 1
					#print(self.userFaint)
					#print("final user Hp: " + str(self.userHp))
					if len(pkmnParty1) == 0:
						#print('monkey')
						self.poke2 = 0
						self.poke1 = 0
						self.cpuWin = 1
						return
					else:
						#print("mons fainted")
						self.state = 0
						self.poke1 = 0
						self.poke2 = 0
						print(self.state)
						return

				self.poke2 = 0
				self.poke1 = 1
				self.turns += 1
				return

			if self.cpuWin == 1:
				#print("You ded cpu win")
				self.end = 2

			if self.userWin == 1:
				#print("you killed pokeman woo yay")
				self.end = 1

		return self.end

class Select: # chose a party of 3 pokemon
	def __init__(self):
		self.bp = [False, False, False, False, False, False]
		self.selection = []

	def choseMon(self, key):
		if len(self.selection) == 3:
			return self.selection

		if key[pygame.K_1] and not self.bp[0]: # makes sure you dont press same button twice
			self.bp[0] = True
			self.selection.append(0) # add the index of pokemon

		if key[pygame.K_2] and not self.bp[1]:
			self.bp[1] = True
			self.selection.append(1)

		if key[pygame.K_3] and not self.bp[2]:
			self.bp[2] = True
			self.selection.append(2)

		if key[pygame.K_4] and not self.bp[3]:
			self.bp[3] = True
			self.selection.append(3)

		if key[pygame.K_5] and not self.bp[4]:
			self.bp[4] = True
			self.selection.append(4)

		if key[pygame.K_6] and not self.bp[5]:
			self.bp[5] = True
			self.selection.append(5)

		return [0]