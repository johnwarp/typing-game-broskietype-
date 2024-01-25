import pygame

class Buttons:
    '''
    A class to represent pressable buttons

    Attributes
    ----------
    rect : list
        a list of properties of a rectangle such as the posX, posY, length, height
    
    text : pygame.font.Font
        text on the button

    textPos : tuple
        the x and y position of the text on the button

    buttonColour : str
        the colour of the button

    Methods
    -------
    isClicked(mousePos):
        checks if the button is clicked

    draw(surface):
        draws the button

    highlight(surface, mousePos):
        highlights the button if the mouse hovers over it
    '''

    def __init__(self, rect, text, textPos, buttonColour):
        pygame.mixer.init()             # initializes sound effects or something
        self.rect = rect
        self.text = text
        self.textPos = textPos
        self.buttonColour = buttonColour
        self.clickedSfx = pygame.mixer.Sound("sound_effects\\button click.mp3")

    def isClicked(self, mousePos):
        '''
        checks if the button is clicked
        
        Parameters
        ----------
        mousePos : list
            the current x and y position of the mouse cursor

        Returns
        -------
        True : boolean
            returns true if the mouse is within the button
        '''

        # assigns the mouse's x and y position from mousePos
        mouseX = mousePos[0]
        mouseY = mousePos[1]

        # assigns the button's sides from the rectangle properties of the button
        buttonTop = self.rect[1]
        buttonBottom = self.rect[1] + self.rect[3]
        buttonLeft = self.rect[0]
        buttonRight = self.rect[0] + self.rect[2]

        # checks if the mouse is within the button
        if buttonLeft < mouseX < buttonRight and buttonTop < mouseY < buttonBottom:
            self.clickedSfx.play()
            return True

    def draw(self, surface):
        '''
        draws the button

        Parameters
        ----------
        surface : pygame.surface.Surface
            the surface the button is drawn on
        '''

        pygame.draw.rect(surface, self.buttonColour, self.rect)
        surface.blit(self.text, self.textPos)
    
    def highlight(self, surface, mousePos):
        '''
        highlights the button if the mouse hovers over it
        
        Parameters
        ----------
        surface : pygame.surface.Surface
            the surface the highlight is drawn on

        mousePos:
            the x and y position of the mouse
        '''

        # assigns the mouse's x and y position from mousePos
        mouseX = mousePos[0]
        mouseY = mousePos[1]

        # assigns the button's sides from the rectangle properties of the button
        buttonTop = self.rect[1]
        buttonBottom = self.rect[1] + self.rect[3]
        buttonLeft = self.rect[0]
        buttonRight = self.rect[0] + self.rect[2]

        # highlights the button with a white rectangular outline when the mouse is within/hovering the button
        if buttonLeft < mouseX < buttonRight and buttonTop < mouseY < buttonBottom:
            pygame.draw.rect(surface, "white", self.rect, 2)