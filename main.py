import random
from logo import logo, stages
from words import words

def get_random_letter():

    """Gets a random word"""
    return random.choice(words)


def display(word, guessed_letters):

    """Returns a string with correct guessed letters and underscores for missed ones"""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])


def get_user_guess(guessed_letters):

    """Gets valid input from the user to guess letter in secret word and ensure input is a single letter"""

    while True:
        guess = input("Guess a letter from the secret word: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter")

        elif guess in guessed_letters:
            print(f"You already guessed {guess}. Try again!")
        
        else:
            return guess


def play_game():

    """Runs the game main loop"""

    print(logo + '\n')

    random_word = get_random_letter()
    guessed_letters = []
    lives = 6
    game_on = True

    print(f"The secret word has {len(random_word)} letters \n")
    print(display(random_word, guessed_letters) + '\n')

    while game_on:
        
        print(f"\n************ YOU HAVE {lives} {'LIFE' if lives == 1 else 'LIVES'} LEFT ************\n")

        user_input = get_user_guess(guessed_letters)
        guessed_letters.append(user_input)

        if user_input in random_word:
            print(f"✅ Good guess. {user_input} is in the word.")
        
        else:
            print(f"❌ Wrong. {user_input} is not in the word")
            lives -= 1
        
        current_display = display(random_word, guessed_letters)

        print(current_display + '\n')

        if '_' not in current_display:
            print(f"🎉 Congrats! You've Won! The word was: {random_word}")
            game_on = False
        
        if lives == 0:
            print(f"💀 You lost. The secret word was: {random_word}")
            game_on = False
        
        print(stages[lives])


play_game()
