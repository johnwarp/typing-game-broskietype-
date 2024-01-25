import pygame, sys, random
from Game_Objects.buttons import Buttons
from Game_Objects.textGenerator import TextGenerator 

def main():
    '''main contains the main meat of the program'''
    #-----------------------------Setup------------------------------------------------------#
    pygame.init()       # Prepare the pygame module for use
    pygame.mixer.init() # initializes the sound effect stuff
    pygame.mixer.music.load("sound_effects\\free bird.mp3") # loads up freebird as the song

    WIDTH = 1200    # Width of the screen
    HEIGHT = 700    # Height of the screen

    # Create surface of (WIDTH, HEIGHT), and its window.
    MAIN_SURFACE = pygame.display.set_mode((WIDTH, HEIGHT))

    clock = pygame.time.Clock()  #Force frame rate to be slower

    #-----------------------------Program Variable Initialization----------------------------#
    gameState = "start" # initializes the gameState to "start"
    freeBirdOn = False  # indicates if freebird is playing, if it is playing the button will disappear and you can't turn it off

    # initializing different font sizes
    titleFont = pygame.font.SysFont("Courier New", 100)
    headerFont = pygame.font.SysFont("Courier New", 80)
    subtitleFont = pygame.font.SysFont("Courier New", 50)
    biggerTypingFont = pygame.font.SysFont("Courier New", 35)
    typingFont = pygame.font.SysFont("Courier New", 20)

    # initializes large non interactable texts
    titleText = titleFont.render("BroskieType.com", 1, "white")
    subtitleText = subtitleFont.render("(not a real website)", 1, "white")
    timerStartText = subtitleFont.render("Timer starts when you start typing", 1, "pink")

    # text for the help screen
    helpTitle = titleFont.render("Stuff to know:", 1, "white")
    tip1 = typingFont.render("1.) BroskieType is like a regular typing test (type as fast as you can)", 1, "white")
    tip2 = typingFont.render("2.) All words must be typed correctly before continuing (like type racer)", 1, "white")
    tip3 = typingFont.render("3.) Timing will begin when you begin typing", 1 ,"white")
    tip4 = typingFont.render("4.) Timing will end when you have typed all of the words", 1, "white")
    tip5 = typingFont.render("5.) A longer test will result in a more accurate wpm", 1, "white")
    tip6 = typingFont.render("6.) Any weird keys that aren't useful like enter will not be rendered properly", 1, "white")
    tip7 = typingFont.render("7.) Turn off free bird? Now why would you want to do that?", 1, "red")

    # initializes the texts for buttons
    startText = titleFont.render("Start", 1, "white")
    helpText = titleFont.render("Help", 1, "white")
    restartText = headerFont.render("Restart", 1, "white")
    menuText = titleFont.render("Menu", 1, "white")
    backText = subtitleFont.render("Back", 1, "white")
    backToMenuText = subtitleFont.render("Menu", 1, "white")
    shortTestText = titleFont.render("Short Test", 1, "white")
    midTestText = titleFont.render("Mid Test", 1, "white")
    longTestText = titleFont.render("Long Test", 1, "white")
    freeBirdText = subtitleFont.render("Free Bird", 1, "white")

    # initializes the button objects
    start = Buttons([200, 400, 350, 125], startText, (222, 406), "green")
    help = Buttons([650, 400, 350, 125], helpText, (706, 406), "orange")
    restart = Buttons([200, 400, 350, 125], restartText, (210, 416), "red")
    menu = Buttons([650, 400, 350, 125], menuText, (706, 406), "blue")
    back = Buttons([20, 635, 140, 50], backText, (30, 632), "orange")
    backToMenu = Buttons([20, 635, 140, 50], backToMenuText, (30, 632), "blue")
    shortTest = Buttons([250, 100, 700, 150], shortTestText, (300, 120), "green")
    midTest = Buttons([250, 275, 700, 150], midTestText, (350, 295), "orange")
    longTest = Buttons([250, 450, 700, 150], longTestText, (323, 470), "red")
    freeBird = Buttons([450, 635, 300, 50], freeBirdText, (460, 632), "red")

    # initializes the timing based stuff
    frameCounter = 0
    seconds = 0
    timerStart = False
    playSoundOnce = True

    # initializes the rectangle that you type text in
    TYPING_BAR = [100, 580, 1000, 40]

    #-----------------------------Main Program Loop---------------------------------------------#
    while True:     # main game loop
        MAIN_SURFACE.fill((60, 60, 60))     # creates a dark gray background by filling the whole screen

        mousePos = pygame.mouse.get_pos()   # gets the mouse's position

        # checks if ctrl is currently being pressed down
        input = pygame.key.get_pressed()
        ctrlIsPressed = False
        if input[pygame.K_LCTRL] or input[pygame.K_RCTRL]:
            ctrlIsPressed = True

        for event in pygame.event.get():            # loop that gets any user input
            if event.type == pygame.QUIT:           # quits when the exit button is clicked
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:      # checks if any of the listed buttons are clicked depending on the gameState
                if gameState == "start":
                    if start.isClicked(mousePos):
                        gameState = "select"
                        mousePos = [0, 0]           # resets mousePos otherwise the game will think i automatically clicked the long test button
                    elif help.isClicked(mousePos):
                        gameState = "help"
                    elif not freeBirdOn:            # checks if freebird is currently playing
                        if freeBird.isClicked(mousePos):
                            pygame.mixer.music.play(-1, 14.0)
                            freeBirdOn = True

                if gameState == "select":           # screen that lets you select the length of your test
                    if shortTest.isClicked(mousePos):
                        textGenerator = TextGenerator(random.randint(1, 1))     # creates an object that generates a defined amount of text objects based on the parameter 'length'
                        seconds, timerStart, gameState, playSoundOnce = startGame()
                    if midTest.isClicked(mousePos):
                        textGenerator = TextGenerator(random.randint(3, 4))
                        seconds, timerStart, gameState, playSoundOnce = startGame()
                    if longTest.isClicked(mousePos):
                        textGenerator = TextGenerator(random.randint(5, 7))
                        seconds, timerStart, gameState, playSoundOnce = startGame()
                    if backToMenu.isClicked(mousePos):
                        gameState = "start"

                elif gameState == "results":
                    if restart.isClicked(mousePos):
                        gameState = "select"
                        mousePos = [0, 0]
                        pygame.mixer.fadeout(250)   # fades out the music when you exit the results screen to not cause any weird audio glitches
                    elif menu.isClicked(mousePos):
                        gameState = "start"
                        pygame.mixer.fadeout(250)

                elif gameState == "help":
                    if back.isClicked(mousePos):
                        gameState = "start"

                elif gameState == "gaming":
                    if backToMenu.isClicked(mousePos):
                        gameState = "start"
                        
            elif event.type == pygame.KEYDOWN:      # checks for any keyboard input
                if event.key == pygame.K_ESCAPE:    # quits pygame when escape is pressed
                    pygame.quit()
                    sys.exit()
                if gameState == "gaming":
                    if event.key == pygame.K_BACKSPACE:     # checks if backspace or ctrl + backspace is pressed
                        if ctrlIsPressed:
                            textGenerator.ctrlBackSpace()
                        else:
                            textGenerator.backSpace()
                    else:                                   # inputs whatever was typed, as long as it isn't backspace or any weird key like enter
                        timerStart = True
                        textGenerator.type(event.unicode)

        if gameState == "gaming":   # the main game
            # if the test is completed, then the gameState will change to results
            if textGenerator.textArray[textGenerator.length - 1].changeGameState:
                gameState = "results"
                textGenerator.textArray[textGenerator.length - 1].changeGameState = False
                totalWordsTyped = textGenerator.length * 15
                wpm = round((totalWordsTyped / seconds) * 60)
                resultsFont = subtitleFont.render(f"Your Words Per Minute is: {wpm}", 1, "white")
                feedBack, victorySound = skillLevel(wpm, subtitleFont)
                pygame.mixer.stop()

            # if the current line is fully typed correctly, and isn't the last line to be typed, the next line will begin to be typed
            elif textGenerator.textArray[textGenerator.index].changeGenIndex:
                textGenerator.textArray[textGenerator.index].changeGenIndex = False
                textGenerator.nextIndex()

            frameCounter += 1

            if timerStart:      # will start timing when user starts typing, otherwise, user will be notified via text on screen
                seconds += 1/60
            else:
                if frameCounter > 80:   # blinks text notifying that timer will start when you start typing
                    frameCounter = 0
                elif frameCounter > 20:
                    MAIN_SURFACE.blit(timerStartText, (80, 200))

            backToMenu.draw(MAIN_SURFACE)
            backToMenu.highlight(MAIN_SURFACE, mousePos)    # when the mouse is over the button, it will highlight

            timerFont = biggerTypingFont.render(f"Timer: {round(seconds, 2)}", 1, "yellow") # updates the timer
            pygame.draw.rect(MAIN_SURFACE, (45, 45, 45), TYPING_BAR)

            textGenerator.draw(MAIN_SURFACE, typingFont)    # draws all the lines of text (each line of text is an object)

            MAIN_SURFACE.blit(timerFont, (100, 170))    # displays the timer on screen

        elif gameState == "start":  # the start screen
            start.draw(MAIN_SURFACE)
            help.draw(MAIN_SURFACE)
            if not freeBirdOn:      # button exists and is pressable if freebird is off, if it's not then the button disappears, causing freebird to be permanently on, unless the user exits the whole game
                freeBird.draw(MAIN_SURFACE)
                freeBird.highlight(MAIN_SURFACE, mousePos)

            start.highlight(MAIN_SURFACE, mousePos)
            help.highlight(MAIN_SURFACE, mousePos)
            MAIN_SURFACE.blit(titleText, (170, 150))
            MAIN_SURFACE.blit(subtitleText, (300, 270))
        
        elif gameState == "select": # screen to select the length of your test
            shortTest.draw(MAIN_SURFACE)
            midTest.draw(MAIN_SURFACE)
            longTest.draw(MAIN_SURFACE)
            backToMenu.draw(MAIN_SURFACE)

            shortTest.highlight(MAIN_SURFACE, mousePos)
            midTest.highlight(MAIN_SURFACE, mousePos)
            longTest.highlight(MAIN_SURFACE, mousePos)
            backToMenu.highlight(MAIN_SURFACE, mousePos)

        elif gameState == "results":    # results screen
            menu.draw(MAIN_SURFACE)
            restart.draw(MAIN_SURFACE)

            if playSoundOnce:           # makes sure that the victory sound is played only once
                victorySound.play()
                playSoundOnce = False

            menu.highlight(MAIN_SURFACE, mousePos)
            restart.highlight(MAIN_SURFACE, mousePos)
            MAIN_SURFACE.blit(resultsFont, (160, 150))
            MAIN_SURFACE.blit(feedBack, (222, 250))
        elif gameState == "help":   # help screen

            back.draw(MAIN_SURFACE)
            back.highlight(MAIN_SURFACE, mousePos)

            MAIN_SURFACE.blit(helpTitle, (150, 100))
            MAIN_SURFACE.blit(tip1, (150, 250))
            MAIN_SURFACE.blit(tip2, (150, 300))
            MAIN_SURFACE.blit(tip3, (150, 350))
            MAIN_SURFACE.blit(tip4, (150, 400))
            MAIN_SURFACE.blit(tip5, (150, 450))
            MAIN_SURFACE.blit(tip6, (150, 500))
            if freeBirdOn:          # tip7 only appears when freebird is on
                MAIN_SURFACE.blit(tip7, (150, 550))

        pygame.display.flip()   # displays everythings that's been drawn on the surface
        
        clock.tick(60) #Force frame rate to be slower

def startGame():
    '''
    Resets all the timing based and state related elements of the game as the game starts

        Parameters:
            None
        
        Returns:
            seconds (int): The reset value of seconds
            timerStart (boolean): The reset value of timerStart as the timer hasn't started yet
            gameState (str): The gameState set to gaming this function starts the game
            playSoundOnce (boolean): Lets a sound play once again
    '''

    seconds = 0
    timerStart = False
    gameState = "gaming"
    playSoundOnce = True

    return seconds, timerStart, gameState, playSoundOnce

def skillLevel(wpm, subtitleFont):
    '''
    Gives feedback based on the wpm the user achieved

        Parameters
        ----------
            wpm (int): The wpm the user achieved
            subtitleFont (pygame.font.Font): The properties of the font the feedback will be displayed using

        Returns
        -------
            feedBack (pygame.surface.Surface): The feedback given in form of text on screen
            soundEffect (pygame.mixer.Sound): The appropriate victory sound based on your wpm
    '''
    if wpm > 200:
        feedBack = subtitleFont.render("Now this is crazy", 1, "blue")
        soundEffect = pygame.mixer.Sound("sound_effects\\dark evil beat.mp3")
    elif wpm > 150:
        feedBack = subtitleFont.render("gaming like a goblin", 1, "cyan")
        soundEffect = pygame.mixer.Sound("sound_effects\\bad to the bone.mp3")
    elif wpm > 120:
        feedBack = subtitleFont.render("gaming like a bro", 1, "green")
        soundEffect = pygame.mixer.Sound("sound_effects\\scream.mp3")
    elif wpm > 80:
        feedBack = subtitleFont.render("Respectable Speed", 1, "yellow")
        soundEffect = pygame.mixer.Sound("sound_effects\\lego breaking.mp3")
    elif wpm > 40:
        feedBack = subtitleFont.render("ur bad", 1, "orange")
        soundEffect = pygame.mixer.Sound("sound_effects\\old car horn.mp3")
    elif wpm > 0:
        feedBack = subtitleFont.render("Type faster lazy ****", 1, "red")
        soundEffect = pygame.mixer.Sound("sound_effects\\fail sound.mp3")

    return feedBack, soundEffect

main()