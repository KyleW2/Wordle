import Dictionary

class Dealer:
    def __init__(self, dict) -> None:
        self.dictionary = dict
        self.word = self.dictionary.getRandomWord()
    
    def guessWord(self, word: str) -> list:
        out = []

        if word != self.word:
            for i in range(0, len(word)):
                # Green case
                if word[i] == self.word[i]:
                    out.append((word[i], "green"))
                
                # Yellow case
                elif word[i] in self.word:
                    out.append((word[i], "yellow"))

                # Black case
                else:
                    out.append((word[i], "black"))
                
            return out
        
        for i in range(0, len(word)):
            out.append((word[i], "green"))

        return out