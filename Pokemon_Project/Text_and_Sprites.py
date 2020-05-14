'''
Title: Text and Other Sprites stuff
Author: Nikhil Nayyar
Date Created: 04/06/19
'''
from Classes import *
import pygame
## pygame stuff
pygame.init() # loads the pygame module commands in the program
# display variables
TITLE = 'Pokemon: Battle Royale' # title that appears in the window title
FPS = 30 # frames per second
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# colour variables
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (50, 50, 50)
BLUE = (100, 0, 255)

# Create the window
screen = pygame.display.set_mode(SCREENDIM) # creates the main surface were all other assets are placed on top.
pygame.display.set_caption(TITLE) # updates the window title with TITLE
screen.fill(GREY) # fills the entire surface with the colour (think of fill as erase or clear)

clock = pygame.time.Clock() # starts a clock object to measure time
# Title and Intro Text
title = mySprite("media/title.png")
title.resize(400, 250)
title.setPos((200, 5))

titleText = text("Battle Tower", 50)
titleText.setPos((WIDTH/2 - titleText.getWidth() - 125, title.getHeight() + titleText.getHeight()+ 30))
titleText.setColour((255, 255, 0))

startText = text("Press SPACE to play", 50)
startText.setPos((WIDTH/2 - startText.getWidth() - 125, title.getHeight() + startText.getHeight()+ 80))
startText.setColour((255, 255, 0))

introText = text("Welcome to Pokemon Battle Tower!", 50)
introText.setPos((100, 0))
introText2 = text("In this game you will battle through 2 different trainers to get to the ", 36)
introText2.setPos((0, 50))
introText3 = text("top of the Battle Tower. You can chose a party of 3 Pokemon before", 36)
introText3.setPos((0, 80))
introText4 = text("each battle.", 36)
introText4.setPos((0, 110))
introText5 = text("Press E to interact with trainers and doors", 36)
introText5.setPos((140, 110))
introText6 = text("Press ENTER to continue", 50)
introText6.setPos((190, 400))
### CHOSE MONS SCREEN
choseMonTxt = text("Chose 3 Pokemon for your party", 48)
choseMonTxt.setPos((WIDTH/2-225, 0))

rhyChose = mySprite("media/rhydon-f.png")
rhyChose.resize(200, 200)
rhyText = text("(1) Rhydon", 36)
rhyChose.setPos((20, 60))
rhyText.setPos((45, 250))

blaChose = mySprite("media/blaziken.png")
blaChose.resize(190, 190)
blaText = text("(2) Blaziken", 36)
blaChose.setPos((310, 60))
blaText.setPos((325, 250))

haxChose = mySprite("media/haxorus.png")
haxChose.resize(175, 175)
haxText = text("(3) Haxorus", 36)
haxChose.setPos((575, 60))
haxText.setPos((590, 250))

brvChose = mySprite("media/braviary.png")
brvChose.resize(200, 200)
brvText = text("(4) Braviary", 36)
brvChose.setPos((20, 320))
brvText.setPos((45, 500))

garChose = mySprite("media/gardevoir.png")
garChose.resize(190, 190)
garText = text("(5) Gardevoir", 36)
garChose.setPos((310, 320))
garText.setPos((325, 500))

dusChose = mySprite("media/dusknoir.png")
dusChose.resize(175, 175)
dusText = text("(6) Dusknoir", 36)
dusChose.setPos((575, 320))
dusText.setPos((590, 500))


# Battleing Sprites and Text
#background
back = mySprite("media/bBack.png")
back.resize(800, 700)

#main battle bottom box
userBattleBox = box(WIDTH/2, 100, 0, HEIGHT-100)
userBattleBox.setColour(WHITE)

#hp boxes
userHpBox = box(WIDTH/4, 80, WIDTH - 200, HEIGHT-200)
userHpBox.setColour(BLUE)
cpuHpBox = box(WIDTH/4, 80, 0, 30)
cpuHpBox.setColour(BLUE)

blackBox = box(WIDTH, HEIGHT + 50)

# win screen
winText = text("Congratulations!", 54)
winText.setPos((250, 0))

moreWinText = text('You beat the Battle Tower', 48)
moreWinText.setPos((200, 50))

