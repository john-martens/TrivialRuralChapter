import pygame as game
import random as r

game.init()
game.display.set_caption("Window Title Goes Here")
screen = game.display.set_mode([800, 600])
gameon = True
bgcolor = game.color.Color("#f6cb39")
alien = game.image.load("space-invader-icon.png")
# main loop of the game
while gameon:
    screen.fill(bgcolor)
    screen.blit(alien, (100, 100))
    game.display.flip()  # redraws / refreshes screen
    event = game.event.poll()  # listens for mouse, keyboard, quitting
    if event.type == game.QUIT:
        gameon = False
# comes here when game is over
while True:
    screen.fill(bgcolor)
    game.display.flip()
    event = game.event.poll()
    if event.type == game.QUIT:
        break
game.quit()
