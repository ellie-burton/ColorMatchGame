import pygame_widgets
import pygame
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
from pygame.locals import *
import random

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("The Most Annoying Game Ever")

red = Slider(window, 100, 100, 400, 20, min=0, max=255, step=1,colour=(255,0,0))
green = Slider(window, 100, 300, 400, 20, min=0, max=255, step=1,colour=(0,255,0))
blue = Slider(window, 100, 500, 400, 20, min=0, max=255, step=1,colour=(0,0,255))

redoutput = TextBox(window, 550, 100, 50, 50, fontSize=30)
greenoutput = TextBox(window, 550, 300, 50, 50, fontSize=30)
blueoutput = TextBox(window, 550, 500, 50, 50, fontSize=30)

redoutput.disable()
greenoutput.disable()
blueoutput.disable()

guessr = random.randint(0,255)
guessg = random.randint(0,255)
guessb = random.randint(0,255)

def draw_check_screen():
    screen = pygame.display.set_mode((1000, 600))
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (guessr,guessg,guessb), pygame.Rect(700, 200, 100, 100))
    pygame.draw.rect(screen, (redval,greenval,blueval), pygame.Rect(700, 400, 100, 100))
    diff = 100-((abs(guessr-redval)/255)/3+(abs(guessg-greenval)/255)/3+(abs(guessb-blueval)/255)/3)*100
    output = TextBox(screen, 700, 100, 150, 50, fontSize=50)
    output.setText(str(round(diff,2))+"%")
    pygame.display.update()

while True:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        draw_check_screen()
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False
            quit()

    window.fill((255, 255, 255))
    

    pygame.draw.rect(window, (guessr,guessg,guessb), pygame.Rect(700, 200, 100, 100))


    redval = red.getValue()
    greenval = green.getValue()
    blueval = blue.getValue()

    redoutput.setText(red.getValue())
    greenoutput.setText(green.getValue())
    blueoutput.setText(blue.getValue())

    pygame.draw.rect(window, (redval,greenval,blueval), pygame.Rect(700, 400, 100, 100))

    pygame_widgets.update(events)
    pygame.display.update()