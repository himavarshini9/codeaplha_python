import random

# Predefined list of words
word_list = ['apple', 'chair', 'robot', 'light', 'piano']
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Display hidden word
display = ['_'] * word_length

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")

while incorrect_guesses < max_guesses and '_' in display:
    print("\nWord: ", ' '.join(display))
    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("❗ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
        print("✅ Correct guess!")
    else:
        incorrect_guesses += 1
        print(f"❌ Incorrect guess! {max_guesses - incorrect_guesses} tries left.")

# Final result
if '_' not in display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)
