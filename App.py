from flask import Flask, render_template, request

from Dictionary import Dictionary
from Dealer import Dealer 

app = Flask(__name__)

wordSet = Dictionary("dictionaries/small.txt")
dealer = Dealer(wordSet)
numberOfGuesses = -1
print(dealer.word)

MAX_GUESSES = 6
WORD_LENGTH = 5

wordList = []
for i in range(0, MAX_GUESSES):
    temp = []
    for j in range(0, WORD_LENGTH):
        temp.append((" ", "#424242"))
    wordList.append(temp)

@app.route('/', methods=['GET', 'POST'])
def home():
    global numberOfGuesses
    
    if request.method == 'POST':
        numberOfGuesses += 1
        wordList[numberOfGuesses] = dealer.guessWord(request.form["guess"])
    
    return render_template("home.html", wordList = wordList)

if __name__ == "__main__":
    app.run()