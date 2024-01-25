import pygame

class Text:
    '''
    An object to that is a line of typeable text

    Attributes
    ----------
    wordList : list
        the words in the line of text in an array

    displayWords : string
        a string version of wordList that is displayed for the user to see and type

    genLength : int
        the total amount of text objects that were created

    genIndex : int
        the current text object's index in the textGenerator's index as the text objects are in a list of another object

    Methods
    -------
    nextWord():
        moves to the next word to be typed in the line of text

    typing(letter):
        types the letter the user inputted on screen

    backSpace():
        deletes the latest letter

    ctrlBackSpace():
        deletes the whole current word that was typed

    draw(surface, font, textPos):
        draws the line of text on screen
    '''

    def __init__(self, wordList, displayWords, genLength, genIndex):
        '''
        Takes in and initializes all the specific and necessary parameters and variables

        Parameters
        ----------
        wordList : list
            the words in the line of text in an array

        displayWords : string
            a string version of wordList that is displayed for the user to see and type

        genLength : int
            the total amount of text objects that were created

        genIndex : int
            the current text object's index in the textGenerator's index as the text objects are in a list of another object
        '''
        pygame.mixer.init()
        self.wordList = wordList
        self.wordIndex = -1
        self.highlightIndex = 0
        self.letterIndex = 0
        self.ctrlIndex = 0
        self.genIndex = genIndex

        self.genLength = genLength
        self.word = ""
        self.inputText = ""
        self.displayWords = displayWords
        self.highlightText = self.displayWords[0:self.highlightIndex]   # text that highlights words and letters you've typed correctly
        self.wrongText = self.highlightText     # text that appears when you type something wrong
        self.underLine = ""

        self.totalWords = len(wordList)
        self.gamerState = "gaming"
        self.changeGameState = False
        self.changeGenIndex = False

        self.failSound = pygame.mixer.Sound("sound_effects\\fail sound.mp3")

    def nextWord(self):
        '''Moves to the next word to be typed in the line of text'''
        self.letterIndex = 0
        self.wordIndex += 1

        try:    # IndexError occurs when last word is typed, and will trigger either the next text line or the results screen
            if self.wordIndex == self.totalWords - 1 and self.genIndex == self.genLength - 1:
                self.word = self.wordList[self.wordIndex]
            else:
                self.word = self.wordList[self.wordIndex] + " "
        except IndexError:
            if self.genIndex == self.genLength - 1:
                self.gamerState = "results"
                self.changeGameState = True
            else:
                self.changeGenIndex = True

        self.inputText = ""

        element = ""

        # creates an underline to highlight the current word you're typing
        for i in self.word[0:-1]:
            element += '_'

        if self.wordIndex != 0:
            tempStr = ""
            for j in self.underLine:
                tempStr += " "

            self.underLine = tempStr + " "

        if self.wordIndex != self.totalWords:
            self.underLine += element

        if self.wordIndex == self.totalWords - 1 and self.genIndex == self.genLength - 1:
            self.underLine += '_'

    def typing(self, letter):
        '''
        types the letter the user inputted on screen

        Parameters
        ----------
        letter : str
            the key the user pressed on the keyboard
        '''

        self.inputText += letter

        inputLetter = self.inputText[self.letterIndex]
        currentLetter = self.word[self.letterIndex]

        if inputLetter == currentLetter:    # checks if the letter you typed matches with the letter the word requires
            self.letterIndex += 1

            if self.inputText == self.word:
                self.highlightIndex += 1
                self.highlightText = self.displayWords[0:self.highlightIndex]
                self.wrongText = self.highlightText
                self.ctrlIndex = self.highlightIndex
                self.nextWord()
            else:
                self.highlightIndex += 1
                self.highlightText = self.displayWords[0:self.highlightIndex]
                self.wrongText = self.highlightText
        else:
            self.wrongText += 'X'
            self.failSound.play()

    def backSpace(self):
        '''deletes the latest letter using substrings'''
        if self.inputText != "":    # checks if the inputText exists, else an IndexError will occur
            self.inputText = self.inputText[0:-1]
            if self.highlightText == self.wrongText:
                self.highlightIndex -= 1
                self.highlightText = self.displayWords[0:self.highlightIndex]
                self.wrongText = self.highlightText
                self.letterIndex -= 1
            else:
                self.wrongText = self.wrongText[0:-1]

    def ctrlBackSpace(self):
        '''deletes the whole current word that was typed'''
        if self.inputText != "":
            self.inputText = ""
            self.highlightIndex = self.ctrlIndex
            self.highlightText = self.displayWords[0:self.highlightIndex]
            self.wrongText = self.highlightText
            self.letterIndex = 0

    def draw(self, surface, font, textPos):
        '''
        draws the line of text on screen

        Parameters
        ----------
        surface : pygame.surface.Surface
            the surface the text is blitted/drawn on

        font : pygame.font.Font
            the font the text uses

        textPos : tuple
            the position the text is drawn at
        '''

        displayedText = font.render(self.displayWords, 1, "white")
        typingText = font.render(self.inputText, 1, "green")
        highlight = font.render(self.underLine, 1, "green")
        wrongText = font.render(self.wrongText, 1, "red")
        highlightText = font.render(self.highlightText, 1, "green")

        surface.blit(displayedText, textPos)
        surface.blit(highlight, textPos)
        surface.blit(wrongText, textPos)
        surface.blit(highlightText, textPos)
        surface.blit(typingText, (110, 590))