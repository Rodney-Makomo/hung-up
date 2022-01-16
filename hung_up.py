import random, os, graphics, hard_words

# hangman game that works with boolean values and functions

word = random.choice(hard_words.game_words)
word = word.upper()
reveal = list(len(word)*'_')
lives = 7
gameOver = False

def check_letters(letter, word):
    """
    Checks what letters have been put in by the user and reveals letter
    if correct.
    """
    global reveal
    for i in range(0, len(word)):
        letter = word[i]
        if attempt == letter:
            reveal[i] = attempt
    if '_' not in reveal:
        return True
    else:
        return False

def monitor():
    os.system("clear")
    print(graphics.hangman[7-lives])
    print(reveal)
    print('You have ', lives, ' shots left at this.')

while gameOver == False and lives > 0:
    print(reveal)
    attempt = input('Guess the letter or word:')
    attempt = attempt.upper()

    if attempt == word:
        gameOver = True
        reveal = word
if len(attempt) == 1 and attempt in word:
    gameOver = check_letters(attempt, word)
else:
    lives -= 1

monitor()

if gameOver:
    print('Well done on not letting an innocent man hang')
else:
    print('You just let an innocent man hang through your incompetence. The word in question was: ' word)
