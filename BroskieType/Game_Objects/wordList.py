import random, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))   # gets rid of file not found error (from stackoverflow)

class WordList:
    '''
    A class that creates a list of the top 200 most common words in English plus an extra few bonuses
    
    Methods
    -------
    randomizeWords(length):
        creates a list of random words from default_words.txt
    '''

    def __init__(self):
        '''initializes the list of words in the file'''

        self.defaultWords = []

        with open('default_words.txt') as file:     # creates a list with all the words in default_words.txt
            for i in file.readlines():
                self.defaultWords.append(i.strip())

    def randomizeWords(self, length):
        '''
        creates a list of random words from default_words.txt
        
        Parameters
        ----------
        length : int
            the length of the list

        Returns
        -------
        tempArray : list
            a list of randomly picked out worrds from the list of default words
        '''

        tempArray = []

        for i in range(length):                     # randomly appends words from the default words
            tempArray.append(self.defaultWords[random.randint(0, 211)])

        return tempArray