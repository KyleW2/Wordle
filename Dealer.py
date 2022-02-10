import Dictionary

class Dealer:
    def __init__(self, dict, hexColors = False) -> None:
        self.dictionary = dict
        self.word = self.dictionary.getRandomWord()
        self.hexColors = hexColors
    
    def guessWord(self, word: str) -> list:
        out = []

        if word != self.word:
            for i in range(0, len(word)):
                # Green case
                if word[i] == self.word[i]:
                    color = "#528d4d" if self.hexColors else "green"
                    out.append((word[i], color))
                
                # Yellow case
                elif word[i] in self.word:
                    color = "#b59e3a" if self.hexColors else "yellow"
                    out.append((word[i], "yellow"))

                # Black case
                else:
                    color = "#3a3a3c" if self.hexColors else "black"
                    out.append((word[i], color))
                
            return out
        
        for i in range(0, len(word)):
            out.append((word[i], "green"))

        return out