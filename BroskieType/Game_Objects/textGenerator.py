from Game_Objects.wordList import WordList
from Game_Objects.text import Text

class TextGenerator:
    '''
    A class that generates multiple text line objects depending on the length of the test

    Attributes
    ----------
    length : int
        the amount of text objects that are created

    Methods
    -------
    type(letter):
        checks if the key the user pressed on the keyboard has a typeable unicode, then calls the current text object's typing method

    nextIndex():
        moves to the next text line object when the current one is finished being typed

    backSpace():
        calls the current text object's backspace method

    ctrlBackSpace():
        calls the current text object's ctrl backspace method

    draw(surface, font):
        draws all the text objects by using all of the text object's draw methods

    arrayToString(randomWords):
        turns a list of words into a string of words separated by spaces
    '''

    def __init__(self, length):
        '''
        Takes in and initializes all the specific and necessary parameters and variables
        
        Parameters
        ----------
        length : int
            the amount of text line objects created
        '''

        self.wordList = WordList()
        self.index = 0              # index to keep track of which text line is currently being typed
        self.length = length
        self.changeIndex = False

        tempArray = []              # temporary array to hold the text line objects

        for i in range(length):     # creates a list of text line objects based on the specified length
            randomWords = self.wordList.randomizeWords(15)
            displayWords = self.arrayToString(randomWords)
            tempText = Text(randomWords, displayWords, length, i)
            tempArray.append(tempText)
        
        self.textArray = tempArray

        currentText = self.textArray[self.index]    # the current text line that is being typed
        currentText.nextWord()                      # calling a method from the text object to go to the next word

    def type(self, letter):
        '''
        checks if the key the user pressed on the keyboard has a typeable unicode, then calls the current text object's typing method

        Parameters
        ----------
        letter : string
            calls the current text object's typing method if the key pressed has a typeable unicode
        '''

        currentText = self.textArray[self.index]
        try:
            currentText.typing(letter)
        except IndexError:
            pass

    def nextIndex(self):
        '''moves to the next text line object when the current one is finished being typed'''

        self.index += 1
        currentText = self.textArray[self.index]
        currentText.nextWord()

    def backSpace(self):
        '''calls the current text object's backspace method'''

        currentText = self.textArray[self.index]
        currentText.backSpace()

    def ctrlBackSpace(self):
        '''calls the current text object's ctrl backspace method'''

        currentText = self.textArray[self.index]
        currentText.ctrlBackSpace()

    def draw(self, surface, font):
        '''
        draws all the text objects by using all of the text object's draw methods

        Parameters
        ----------
        surface : pygame.surface.Surface
            the surface to draw the text on

        font : pygame.font.Font
            the font the text will use
        '''

        # the count is there to evenly space out the text lines from each other
        for count, text in enumerate(self.textArray):
            text.draw(surface, font, (110, 260 + count * 40))

    def arrayToString(self, randomWords):
        '''
        turns a list of words into a string of words separated by spaces
        
        Parameters
        ----------
        randomWords : list
            list of random words picked from the defaul_words.txt

        Returns
        -------
        displayWords : string
            a string version of randomWords with spaces between each word
        '''

        displayWords = ""

        for i, word in enumerate(randomWords):
            if i == 0:                          # doesn't add a space before the first word in the list
                displayWords += word
            else:
                displayWords += " " + word

        return displayWords