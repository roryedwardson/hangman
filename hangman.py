import random
import time

validLetters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')
unusedLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
usedLetters = []

# Used an online random word generator to create a list of approx 2500 words,
# Stored them in a txt file to be accessed by this program
words = open("words.txt", "r")
wordList = []
for word in words:
    word = word.replace("\n", "")  # remove line breaks
    wordList.append(word)

# Select a random word from txt file
secretWord = random.choice(wordList).upper()

# List of letters in word
secretWordList = []
for letter in secretWord:
    secretWordList.append(letter)

# List of empty "_", to represent letters in word
secretWordListDisplay = []
for letter in secretWordList:
    secretWordListDisplay.append("_")


def display_secret():
    item = " ".join(secretWordListDisplay)
    return item


def display_used():
    item = ", ".join(usedLetters)
    return item


# Hangman score - each score from 1-7 can be displayed using hangmanList[score-1]
hangmanScore = 0

h1 = "  |‾‾‾|\n      |\n      |\n      |\n     _|_"
h2 = "  |‾‾‾|\n  0   |\n      |\n      |\n     _|_"
h3 = "  |‾‾‾|\n  0   |\n  |   |\n      |\n     _|_"
h4 = "  |‾‾‾|\n  0   |\n /|   |\n      |\n     _|_"
h5 = "  |‾‾‾|\n  0   |\n /|\\  |\n      |\n     _|_"
h6 = "  |‾‾‾|\n  0   |\n /|\\  |\n /    |\n     _|_"
h7 = "  |‾‾‾|\n  0   |\n /|\\  |\n / \\  |\n     _|_"
win = "  |‾‾‾|\n      |\n \\0/  |\n  |   |\n / \\ _|_"

hangmanList = [h1, h2, h3, h4, h5, h6, h7]

# User input while loop, guess a letter
running = True
while running:
    print(display_secret())                         # Display currently discovered characters in word
    userInput = input("Guess a letter: ")
    if userInput.upper() not in validLetters:       # Check if input is a valid letter
        print("Enter a valid letter.")
    elif userInput.upper() in validLetters:
        if userInput.upper() not in unusedLetters:  # Check if input in unusedLetters
            print("Choose a letter that you have not already guessed.")
        elif userInput.upper() in unusedLetters:
            unusedLetters.remove(userInput.upper())
            usedLetters.append(userInput.upper())

            if userInput.upper() not in secretWordList:
                hangmanScore += 1                   # If input not in secretWord, hangmanScore += 1
                print("\n" + hangmanList[hangmanScore-1] + "\n")
                if hangmanScore == 7:               # Lose state after 7 wrong guesses
                    print(display_secret())
                    print("Sorry, you lose!")
                    print(f"The secret word was {secretWord}.")
                    time.sleep(5)
                    quit()

            elif userInput.upper() in secretWordList:
                hitCount = secretWordList.count(userInput.upper())  # Check for multiple instances of same letter
                workingList = secretWordList
                for i in range(hitCount):
                    let_ind = workingList.index(userInput.upper())
                    workingList[let_ind] = "_"
                    secretWordListDisplay[let_ind] = userInput.upper()

                if secretWordListDisplay.count("_") == 0:  # Win state - no more empty spaces
                    print("\n" + win + "\n")
                    print(display_secret())
                    print("You win!")
                    time.sleep(5)
                    quit()

            usedLetters.sort()
            print("Used:", display_used())

