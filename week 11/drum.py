import pygame
from pygame import mixer
pygame.init()

width = 1400
height = 800

black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)
green = (0,255,90)
gold = (212,175,55)
blue = (0,255,255)
screen = pygame.display.set_mode([width,height]) #display
pygame.display.set_caption('Beat Maker') #name
labelfont = pygame.font.Font('New Athletic M54.ttf', 32) #font

fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
boxes = []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
bpm = 240
playing = True
activelength = 0
activebeat = 1
beatchanged = True

def drawgrid(clicks, beat):
    leftbox = pygame.draw.rect(screen, gray, [0, 0, 200, height - 200], 5) #left menu
    bottombox = pygame.draw.rect(screen, gray, [0, height - 200, width, 200], 5)
    boxes = []
    colors = [gray, white, gray]
    hihattext = labelfont.render('Hi Hat', True, white) #Hi Hat
    screen.blit(hihattext, (30, 30))
    snaretext = labelfont.render('Snare', True, white) #Snare
    screen.blit(snaretext, (30, 130))
    basetext = labelfont.render('Base Drum', True, white) #Base Drum
    screen.blit(basetext, (30, 230))
    crashtext = labelfont.render('Crash', True, white) #Crash
    screen.blit(crashtext, (30, 330))
    basetext = labelfont.render('Clap', True, white) #Clap
    screen.blit(basetext, (30, 430))
    crashtext = labelfont.render('Floor Tom', True, white) #Floor Tom
    screen.blit(crashtext, (30, 530))
    for i in range(instruments):
        pygame.draw.line(screen, gray, (0, (i * 100) + 100), (198, (i * 100) + 100), 3) #Lines dividing main names

    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen, color, [i * ((width - 200) // beats) + 205, (j * 100) + 5, ((width - 200) //  beats) - 10, ((height - 200) // instruments)- 10], 0, 3) #Lines dividing main names
            
            pygame.draw.rect(screen, gold, [i * ((width - 200) // beats) + 200, (j * 100), ((width - 200) //  beats), ((height - 200) // instruments)], 5, 5) #Lines dividing main names

            pygame.draw.rect(screen, black, [i * ((width - 200) // beats) + 200, (j * 100), ((width - 200) //  beats), ((height - 200) // instruments)], 2, 5) #Lines dividing main names
            boxes.append((rect, (i, j)))

        active = pygame.draw.rect(screen, blue, [beat * ((width - 200) // beats) + 200, 0, ((width - 200) // beats), instruments * 100], 5, 3)
    return boxes

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = drawgrid(clicked, activebeat)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN: #click detection
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1

        beatlength = 3600 // bpm #while ^ loops per minute

    if playing:
        if activelength < beatlength:
            activelength += 1
        else:
            activelength = 0
            if activebeat < beats - 1:
                activebeat += 1
                beatchanged = True
            else:
                activebeat = 0
                beatchanged = True

    pygame.display.flip()
pygame.quit()