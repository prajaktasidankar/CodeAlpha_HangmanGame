import random

def play_hangman():
    word_list = ['apple', 'banana', 'cherry', 'grape', 'mango']
    secret_word = random.choice(word_list)
    guessed_word = ['_'] * len(secret_word)
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6

    print("\nWelcome to Hangman!")

    while wrong_guesses < max_guesses and '_' in guessed_word:
        print("\nCurrent word: ", ' '.join(guessed_word))
        print("Guessed letters: ", ' '.join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!")
            for i in range(len(secret_word)):
                if secret_word[i] == guess:
                    guessed_word[i] = guess
        else:
            print("Wrong guess.")
            wrong_guesses += 1
            print(f"Remaining wrong guesses: {max_guesses - wrong_guesses}")

    if '_' not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        return True
    else:
        print("\n❌ Game over. The word was:", secret_word)
        return False

# Main game loop
score = 0
while True:
    if play_hangman():
        score += 1

    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        break

print(f"\nYour total score: {score} win(s). Thanks for playing!")