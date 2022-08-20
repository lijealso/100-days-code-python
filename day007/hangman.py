import random
import hangman_art as art
import hangman_words as words

print(art.logo)

# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(words.word_list)

# Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

# replaced letter for _ : unused local variables should de removed, python:S1481
display = ['_' for _ in chosen_word]

# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

lifes = 6
print(f'You have {lifes} lifes left')
print(art.stages[lifes])

# while ''.join(str(x) for x in display) != chosen_word:

while '_' in display:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    guess = input("Guess a letter: ").lower()

    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

    for i in range(len(chosen_word)):
        if  chosen_word[i] == guess:
            display[i] = chosen_word[i]
   
    if guess not in chosen_word:
        lifes -= 1
        print(f'You have {lifes} lifes left')
    else:
        print(f'You have {lifes} lifes left')

    if lifes == 0:
        print("You lost")
        print(art.stages[lifes])
        break
    elif '_' not in display:
        print("You won")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    # Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
    print(display)
    print(art.stages[lifes])
