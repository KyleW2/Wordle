import Dictionary

class Dealer:
    def __init__(self, dict) -> None:
        self.dictionary = dict
        self.word = self.dictionary.getRandomWord()
    
    def guessWord(self, word: str) -> dict:
        out = {}

        if word != self.word:
            for i in range(0, len(word)):
                # Green case
                if word[i] == self.word[i]:
                    out[word[i]] = "green"
                
                # Yellow case
                elif word[i] in self.word:
                    out[word[i]] = "yellow"

                # Black case
                else:
                    out[word[i]] = "black"
        
        for i in range(0, len(word)):
            out[word[i]] = "green"

        return out