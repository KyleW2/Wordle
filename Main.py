import Dictionary as poo
import Dealer as pee

if __name__ == "__main__":
    wordSet = poo.Dictionary("dictionaries/small.txt")
    dealer = pee.Dealer(wordSet)

    print(dealer.word)

    guesses = 0
    while guesses <= 6:
        currentGuess = input("Guess: ")

        if currentGuess == "quit game":
            break

        print(dealer.guessWord(currentGuess))
        guesses += 1