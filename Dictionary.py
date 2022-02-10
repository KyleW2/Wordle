import random

class Dictionary:
    def __init__(self, file) -> None:
        self.file = file
        self.dictionary = set()
        self.numberOfWords = 0

        self.__loadDictionary()

    def __loadDictionary(self) -> None:
        dict = open(self.file, "r")
        words = dict.readlines()

        for word in words:
            self.dictionary.add(str(word.strip()))
            self.numberOfWords += 1
    
    def isInDictionary(self, word) -> bool:
        if word in self.dictionary:
            return True
        
        return False
    
    # random.sample() was depreciated for sets so im doing this
    # its not *that* inefficent/dumb
    def getRandomWord(self) -> str:
        x = random.randint(0, self.numberOfWords)
        c = 0

        for word in self.dictionary:
            c += 1
            if c == x:
                return word
        
        return None

if __name__ == "__main__":
    test = Dictionary("dictionaries/small.txt")
    print(test.getRandomWord())
    print(test.isInDictionary("apple"))