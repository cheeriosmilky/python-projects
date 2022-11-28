import pygame
from pygame import mixer
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
gray = (128, 128, 128)
dgray = (50, 50, 50)
lgray = (170, 170, 170)         # colors
blue = (0, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gold = (212, 175, 55)
width = 1400      # app size
height = 800    
activelength = 0
activebeat = 0

# sounds
hihat = mixer.Sound('sounds\hi hat.wav')
snare = mixer.Sound('sounds\snare.wav')
kick = mixer.Sound('sounds\kick.wav')
crash = mixer.Sound('sounds\crash.wav')
clap = mixer.Sound('sounds\clap.wav')
tom = mixer.Sound('sounds\\tom.wav')

screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('The Beat Maker')
labelfont = pygame.font.Font('New Athletic M54.ttf', 32)        # font
mediumfont = pygame.font.Font('New Athletic M54.ttf', 24)
beatchanged = True
timer = pygame.time.Clock()
fps = 60
beats = 8
bpm = 240
instruments = 6
playing = True
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
activelist = [1 for _ in range(instruments)]
pygame.mixer.set_num_channels(instruments * 3)
savemenu = False
loadmenu = False
savedbeats = []
file = open('saved_beats.txt', 'r')     # saved beats
for line in file:
    savedbeats.append(line)
beatname = ''
typing = False
index = 100

def drawgrid(clicks, beat, actives):
    boxes = []
    leftbox = pygame.draw.rect(screen, gray, [0, 0, 200, height - 200], 5)  # box holding inst
    bottombox = pygame.draw.rect(screen, gray, [0, height - 200, width, 200], 5)  # box holding settings
    for i in range(instruments + 1):
        pygame.draw.line(screen, gray, (0, i * 100), (200, i * 100), 3)
    colors = [gray, white, gray]
    hihattxt = labelfont.render('Hi Hat', True, colors[actives[0]])
    screen.blit(hihattxt, (30, 30))
    snaretxt = labelfont.render('Snare', True, colors[actives[1]])  # gray on and off (actives)
    screen.blit(snaretxt, (30, 130))                                     # inst names
    kicktxt = labelfont.render('Bass Drum', True, colors[actives[2]])
    screen.blit(kicktxt, (30, 230))
    crashtext = labelfont.render('Crash', True, colors[actives[3]])
    screen.blit(crashtext, (30, 330))
    claptxt = labelfont.render('Clap', True, colors[actives[4]])
    screen.blit(claptxt, (30, 430))
    tomtxt = labelfont.render('Floor Tom', True, colors[actives[5]])
    screen.blit(tomtxt, (30, 530))
    for i in range(beats):
        for j in range(instruments):
            if clicks[j][i] == -1:
                color = gray
            else:
                if actives[j] == 1:
                    color = green   # turning green when clicked
                else:
                    color = dgray
            rect = pygame.draw.rect(screen, color, [i * ((width - 200) // beats) + 205, (j * 100) + 5, ((width - 200) // beats) - 10, 90], 0, 1)
            pygame.draw.rect(screen, dgray, [i * ((width - 200) // beats) + 200, j * 100, ((width - 200) // beats), 100], 5, 5)  # all drawing of grid
            pygame.draw.rect(screen, black, [i * ((width - 200) // beats) + 200, j * 100, ((width - 200) // beats), 100], 2, 5)
            boxes.append((rect, (i, j)))
    active = pygame.draw.rect(screen, blue, [beat * ((width - 200) // beats) + 200, 0, ((width - 200) // beats), instruments * 100], 5, 3)  # blue active detector
    return boxes

def playnotes():
    for i in range(len(clicked)):
        if clicked[i][activebeat] == 1 and activelist[i] == 1:
            if i == 0:
                hihat.play()
            if i == 1:
                snare.play()
            if i == 2:
                kick.play()           # play notes
            if i == 3:
                crash.play()
            if i == 4:
                clap.play()
            if i == 5:
                tom.play()

def drawsavemenu(beatname, typing):
    pygame.draw.rect(screen, black, [0, 0, width, height])              # save menu tings
    menutxt = labelfont.render('SAVE MENU: Enter a Name for this beat', True, white)
    screen.blit(menutxt, (400, 40))
    exitbtn = pygame.draw.rect(screen, gray, [width - 200, height - 100, 180, 90], 0, 5)
    exittxt = labelfont.render('Close', True, white)
    screen.blit(exittxt, (width - 160, height - 70))                        # save beat y n
    savingbtn = pygame.draw.rect(screen, gray, [width // 2 - 100, height * 0.75, 200, 100], 0, 5) 
    savingtxt = labelfont.render('Save Beat', True, white)
    screen.blit(savingtxt, (width // 2 - 70, height * 0.75 + 30))
    if typing:
        pygame.draw.rect(screen, dgray, [400, 200, 600, 200], 0, 5)
    entryrect = pygame.draw.rect(screen, gray, [400, 200, 600, 200], 5, 5)
    entrytxt = labelfont.render(f'{beatname}', True, white)
    screen.blit(entrytxt, (430, 250))
    return exitbtn, savingbtn, beatname, entryrect

def drawloadmenu(index):
    loadedclicked = []
    loadedbeats = 0
    loadedbpm = 0
    pygame.draw.rect(screen, black, [0, 0, width, height])
    menutxt = labelfont.render('LOAD MENU: Select a beat to load in', True, white)
    screen.blit(menutxt, (400, 40))
    exitbtn = pygame.draw.rect(screen, gray, [width - 200, height - 100, 180, 90], 0, 5)
    exittxt = labelfont.render('Close', True, white)                                        # load menu tings
    screen.blit(exittxt, (width - 160, height - 70))
    loadingbtn = pygame.draw.rect(screen, gray, [width // 2 - 100, height * 0.87, 200, 100], 0, 5)
    loadingtxt = labelfont.render('Load Beat', True, white)                                 # load delete beat
    screen.blit(loadingtxt, (width // 2 - 70, height * 0.87 + 30))
    deletebtn = pygame.draw.rect(screen, gray, [width // 2 - 400, height * 0.87, 200, 100], 0, 5)
    deletetxt = labelfont.render('Delete Beat', True, white)
    screen.blit(deletetxt, (width // 2 - 385, height * 0.87 + 30))
    if 0 <= index < len(savedbeats):
        pygame.draw.rect(screen, lgray, [190, 100 + index*50, 1000, 50])
    for beat in range(len(savedbeats)):
        if beat < 10:
            beatclicked = []
            rowtxt = mediumfont.render(f'{beat + 1}', True, white)          # load menu select
            screen.blit(rowtxt, (200, 100 + beat * 50))
            nameindexstart = savedbeats[beat].index('name: ') + 6
            nameindexend = savedbeats[beat].index(', beats:')
            nametxt = mediumfont.render(savedbeats[beat][nameindexstart:nameindexend], True, white)
            screen.blit(nametxt, (240, 100 + beat * 50))
        if 0 <= index < len(savedbeats) and beat == index:
            beatsindexend = savedbeats[beat].index(', bpm:')
            loadedbeats = int(savedbeats[beat][nameindexend + 8:beatsindexend])
            bpmindexend = savedbeats[beat].index(', selected:')
            loadedbpm = int(savedbeats[beat][beatsindexend + 6:bpmindexend])
            loadedclicksstring = savedbeats[beat][bpmindexend + 14: -3]
            loadedclicksrows = list(loadedclicksstring.split("], ["))
            for row in range(len(loadedclicksrows)):
                loadedclicksrow = (loadedclicksrows[row].split(', '))
                for item in range(len(loadedclicksrow)):
                    if loadedclicksrow[item] == '1' or loadedclicksrow[item] == '-1':
                        loadedclicksrow[item] = int(loadedclicksrow[item])
                beatclicked.append(loadedclicksrow)
                loadedclicked = beatclicked
    loadedinfo = [loadedbeats, loadedbpm, loadedclicked]
    entryrect = pygame.draw.rect(screen, gray, [190, 90, 1000, 600], 5, 5)
    return exitbtn, loadingbtn, entryrect, deletebtn, loadedinfo

run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = drawgrid(clicked, activebeat, activelist)
    # drawing lower menu
    playpause = pygame.draw.rect(screen, gray, [50, height - 150, 200, 100], 0, 5)
    playtxt = labelfont.render('Play/Pause', True, white)  # play pause
    screen.blit(playtxt, (70, height - 130))
    if playing:
        playtext2 = mediumfont.render('Playing', True, dgray)
    else:
        playtext2 = mediumfont.render('Paused', True, dgray)
    screen.blit(playtext2, (70, height - 100))
    # beats per minute buttons
    bpmrect = pygame.draw.rect(screen, gray, [300, height - 150, 200, 100], 5, 5)
    bpmtxt = mediumfont.render('Beats Per Minute', True, white)  # bpm tings
    screen.blit(bpmtxt, (312, height - 130))
    bpmtxt2 = labelfont.render(f'{bpm}', True, white)
    screen.blit(bpmtxt2, (370, height - 100))
    bpmaddrect = pygame.draw.rect(screen, gray, [510, height - 150, 48, 48], 0, 5)
    bpmsubrect = pygame.draw.rect(screen, gray, [510, height - 100, 48, 48], 0, 5)
    addtxt = mediumfont.render('+5', True, white)
    screen.blit(addtxt, (526, height - 140))
    subtxt = mediumfont.render('-5', True, white)
    screen.blit(subtxt, (526, height - 90))
    # beats per loop buttons
    beatsrect = pygame.draw.rect(screen, gray, [600, height - 150, 200, 100], 5, 5)
    beatstxt = mediumfont.render('Beats In Loop', True, white)
    screen.blit(beatstxt, (633, height - 130))
    beatstxt2 = labelfont.render(f'{beats}', True, white)
    screen.blit(beatstxt2, (690, height - 100))
    beatsaddrect = pygame.draw.rect(screen, gray, [810, height - 150, 48, 48], 0, 5)
    beatssubrect = pygame.draw.rect(screen, gray, [810, height - 100, 48, 48], 0, 5)
    addtxt2 = mediumfont.render('+1', True, white)
    screen.blit(addtxt2, (828, height - 140))
    subtxt2 = mediumfont.render('-1', True, white)
    screen.blit(subtxt2, (828, height - 90))
    # clear board button
    clear = pygame.draw.rect(screen, gray, [1150, height - 150, 200, 70], 0, 5)
    playtxt = labelfont.render('Clear Board', True, white)
    screen.blit(playtxt, (1167, height - 133))
    # save and load buttons
    savebutton = pygame.draw.rect(screen, gray, [900, height - 150, 200, 48], 0, 5)
    savetxt = labelfont.render('Save Beat', True, white)
    screen.blit(savetxt, (935, height - 145))
    loadbutton = pygame.draw.rect(screen, gray, [900, height - 98, 200, 48], 0, 5)
    loadtext = labelfont.render('Load Beat', True, white)
    screen.blit(loadtext, (935, height - 93))
    # instrument rectangles
    instrumentrects = []
    for i in range(instruments):
        rect = pygame.rect.Rect((0, i * 100), (200, 100))
        instrumentrects.append(rect)
    if beatchanged:
        playnotes()
        beatchanged = False
    if savemenu:
        exitbutton, savingbutton, beatname, entryrect = drawsavemenu(beatname, typing)
    elif loadmenu:
        exitbutton, loadingbutton, entryrect, deletebutton, loadedinformation = drawloadmenu(index)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False                         # click detection
        if event.type == pygame.MOUSEBUTTONDOWN and not savemenu and not loadmenu:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
        if event.type == pygame.MOUSEBUTTONUP and not savemenu and not loadmenu:
            if playpause.collidepoint(event.pos) and playing:
                playing = False
            elif playpause.collidepoint(event.pos) and not playing:
                playing = True
                activebeat = 0
                activelength = 0
            if beatsaddrect.collidepoint(event.pos):
                beats += 1                              # beat section add sub
                for i in range(len(clicked)):
                    clicked[i].append(-1)
            elif beatssubrect.collidepoint(event.pos):
                beats -= 1
                for i in range(len(clicked)):
                    clicked[i].pop(-1)
            if bpmaddrect.collidepoint(event.pos):
                bpm += 5                                # bpm add sub
            elif bpmsubrect.collidepoint(event.pos):
                bpm -= 5
            if clear.collidepoint(event.pos):
                clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
            for i in range(len(instrumentrects)):
                if instrumentrects[i].collidepoint(event.pos):
                    activelist[i] *= -1
            if savebutton.collidepoint(event.pos):
                savemenu = True
            if loadbutton.collidepoint(event.pos):
                load_menu = True
                playing = False
        elif event.type == pygame.MOUSEBUTTONUP:
            if exitbutton.collidepoint(event.pos):
                savemenu = False
                loadmenu = False
                playing = True
                typing = False
                beat_name = ''
            if entryrect.collidepoint(event.pos):
                if savemenu:
                    if typing:
                        typing = False
                    else:
                        typing = True
                if loadmenu:
                    index = (event.pos[1] - 100) // 50
            if savemenu:
                if savingbutton.collidepoint(event.pos):
                    file = open('saved_beats.txt', 'w')
                    savedbeats.append(f'\nname: {beatname}, beats: {beats}, bpm: {bpm}, selected: {clicked}')
                    for i in range(len(savedbeats)):
                        file.write(str(savedbeats[i]))
                    file.close()
                    savemenu = False
                    loadmenu = False
                    playing = True
                    typing = False
                    beatname = ''
            if loadmenu:
                if deletebutton.collidepoint(event.pos):
                    if 0 <= index < len(savedbeats):
                        savedbeats.pop(index)
                if loadingbutton.collidepoint(event.pos):
                    if 0 <= index < len(savedbeats):
                        beats = loadedinformation[0]
                        bpm = loadedinformation[1]
                        clicked = loadedinformation[2]
                        index = 100
                        savemenu = False
                        loadmenu = False
                        playing = True
                        typing = False
        if event.type == pygame.TEXTINPUT and typing:
            beatname += event.text
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE and len(beatname) > 0:
                beatname = beatname[:-1]

    beatlength = 3600 // bpm

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

file = open('saved_beats.txt', 'w')
for i in range(len(savedbeats)):
    file.write(str(savedbeats[i]))
file.close()
pygame.quit()