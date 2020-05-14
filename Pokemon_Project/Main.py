'''
Title: Pokemon- Battle Royale
Author: Nikhil Nayyar
Date Created: 16/05/19
'''
from Pokemon_and_Attacks import *
from Text_and_Sprites import *
from maps import *
import pygame, time
###--- CODE STARTS HERE ---###

## TODO add the intro screen that explains how to play game
## TODO make main screen look better
## TODO HP bar and
# TODO NIKHIL: intro to battle and win screen in gamestate 6
# Pokemon party
availablePkmn = [rhydon, blaziken, haxorus, braviary, gardevoir, dusknoir]
userParty = []
cpuParty = [magnezone, crobat, lapras]
cpuParty2 = [lickilicky, krookodile, exeggutor]
userSelection = []

chose = Select()
choseAgain = Select()
pkmnBattle = Battle()
pkmnBattle2 = Battle()

# game variables
playMusic = True
batReady = False
batReady2 = False
fade = -(HEIGHT + 50)
wonFirst = 0
gameState = 0 # start
nextBat = 0
running = True
floor2init=1

while running:
	for event in pygame.event.get(): # returns all inputs and triggers into an array
		if event.type == pygame.QUIT: # if the red x was clicked
			running = False

	pressedKeys = pygame.key.get_pressed()
	screen.fill(GREY)

	if gameState == 0: # Title screen
		screen.blit(title.getSurface(), title.getPos())
		screen.blit(titleText.getText(), titleText.getPos())
		screen.blit(startText.getText(), startText.getPos())
		if pressedKeys[pygame.K_SPACE]:
			screen.fill(GREY)
			gameState = 1

	elif gameState == 1: # intro screen
		screen.fill(WHITE)
		screen.blit(introText.getText(), introText.getPos())
		screen.blit(introText2.getText(), introText2.getPos())
		screen.blit(introText3.getText(), introText3.getPos())
		screen.blit(introText4.getText(), introText4.getPos())
		screen.blit(introText5.getText(), introText5.getPos())
		screen.blit(introText6.getText(), introText6.getPos())
		if pressedKeys[pygame.K_RETURN]:
			screen.fill(GREY)
			gameState = 2

	elif gameState == 2: # first room
		if playMusic == True:
			pygame.mixer.music.load('media/overworld.ogg')
			pygame.mixer.music.play(-1)
			playMusic = False

		for i in range(len(movingSprites)):
			sprite = movingSprites[i]
			screen.blit(sprite.getSurface(), sprite.getPos())

		collision(background)
		goBattle = interaction(trainer, pokeManager, pressedKeys)
		goNext = nextFloor(background, pressedKeys)
		screen.blit(player.getSurface(), player.getPos())  # THE player on the screen

		for i in range(len(movingSprites)):
			screenMovement.move(pressedKeys, movingSprites[0], movingSprites[i])

		if goBattle == 2: # talk to nurse to get pokemon
			gameState = 3

		elif goBattle == 1 and nextBat == 1: # if you talk to first guy
			playMusic = True
			pygame.mixer.music.stop()
			batReady = True

		if batReady == True:
			screen.blit(blackBox.getSurface(), (0, fade))
			if playMusic == True:
				pygame.mixer.music.load('media/battle.ogg')
				pygame.mixer.music.play(-1)
				playMusic = False
			fade += 10
			if fade >= 0:
				fade = -(HEIGHT + 50)
				gameState = 4
				batReady = False

		if goNext == True and wonFirst == 1:
			gameState = 7
			goNext = False


	elif gameState == 7: # second room
		if floor2init==1:
			screenMovement2=movement(movingSprites2)
			floor2init=0
		if playMusic == True:
			pygame.mixer.music.load('media/overworld.ogg')
			pygame.mixer.music.play(-1)
			playMusic = False

		for i in range(len(movingSprites2)):
			sprite = movingSprites2[i]
			screen.blit(sprite.getSurface(), sprite.getPos())

		collision(background2)
		goBattle = interaction(trainer2, pokeManager2, pressedKeys)
		screen.blit(player.getSurface(), player.getPos())  # THE player on the screen

		for i in range(len(movingSprites2)):
			screenMovement2.move(pressedKeys, movingSprites2[0], movingSprites2[i])

		if goBattle == 2: # talk to nurse to get pokemon
			gameState = 3

		elif goBattle == 1 and nextBat == 2: # if you talk to second guy
			playMusic = True
			pygame.mixer.music.stop()
			batReady2 = True

		if batReady2 == True:
			screen.blit(blackBox.getSurface(), (0, fade))
			if playMusic == True:
				pygame.mixer.music.load('media/battle.ogg')
				pygame.mixer.music.play(-1)
				playMusic = False
			fade += 10
			if fade >= 0:
				gameState = 5
				batReady2 = False


	elif gameState == 3: # chose pokemon screen
		screen.fill(WHITE)
		screen.blit(choseMonTxt.getText(), choseMonTxt.getPos())

		screen.blit(rhyChose.getSurface(), rhyChose.getPos())
		screen.blit(rhyText.getText(), rhyText.getPos())

		screen.blit(blaChose.getSurface(), blaChose.getPos())
		screen.blit(blaText.getText(), blaText.getPos())

		screen.blit(haxChose.getSurface(), haxChose.getPos())
		screen.blit(haxText.getText(), haxText.getPos())

		screen.blit(brvChose.getSurface(), brvChose.getPos())
		screen.blit(brvText.getText(), brvText.getPos())

		screen.blit(garChose.getSurface(), garChose.getPos())
		screen.blit(garText.getText(), garText.getPos())

		screen.blit(dusChose.getSurface(), dusChose.getPos())
		screen.blit(dusText.getText(), dusText.getPos())

		if len(userSelection) != 3:
			if wonFirst == 0:
				userSelection = chose.choseMon(pressedKeys)
			else:
				userSelection = choseAgain.choseMon(pressedKeys)
		else:
			for i in range(3): # once you get the three indexs find what pokemon they are for your party
				userParty.append(availablePkmn[userSelection[i]])

			if wonFirst == 0:  # if you lost first battle you play again
				gameState = 2
				nextBat = 1

			elif wonFirst == 1:# if you won first battle you go next guy
				gameState = 7
				nextBat = 2

	elif gameState == 4: # first battle
		screen.blit(back.getSurface(), back.getPos())
		screen.blit(userBattleBox.getSurface(), userBattleBox.getPos())
		screen.blit(userHpBox.getSurface(), userHpBox.getPos())
		screen.blit(cpuHpBox.getSurface(), cpuHpBox.getPos())
		go = pkmnBattle.update(userParty, cpuParty, screen, pressedKeys, userBattleBox)
		if go == 1: # win
			pygame.mixer.music.stop()
			for i in range(len(userSelection)):
				userSelection.pop(0)
			for i in range(len(userParty)):
				userParty.pop(0)
			gameState = 2
			wonFirst = 1
			playMusic = True
		elif go == 2: # died
			pygame.mixer.music.stop()
			for i in range(len(userSelection)):
				userSelection.pop(0)
			for i in range(len(userParty)):
				userParty.pop(0)
			gameState = 2
			wonFirst = 0
			playMusic = True
		else:
			pass

	elif gameState == 5: # second battle
		screen.blit(back.getSurface(), back.getPos())
		screen.blit(userBattleBox.getSurface(), userBattleBox.getPos())
		screen.blit(userHpBox.getSurface(), userHpBox.getPos())
		screen.blit(cpuHpBox.getSurface(), cpuHpBox.getPos())
		go = pkmnBattle2.update(userParty, cpuParty2, screen, pressedKeys, userBattleBox)
		if go == 1: # win
			gameState = 6
		elif go == 2:
			pygame.mixer.music.stop()
			for i in range(len(userSelection)):
				userSelection.pop(0)
			for i in range(len(userParty)):
				userParty.pop(0)
			playMusic = True
			gameState = 2

	elif gameState == 6: # win screen
		screen.blit(winText.getText(), winText.getPos())
		screen.blit(moreWinText.getText(), moreWinText.getPos())

	clock.tick(FPS) # pause the game until the FPS time is reached
	pygame.display.flip() # update the screen with changes

pygame.quit()