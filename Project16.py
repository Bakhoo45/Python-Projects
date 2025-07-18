import random
from wordlist import words

def show_hangman(attempts):
    stages = {
        0: ("   ", "   ", "   "),
        1: (" o  ", "   ", "   "),
        2: (" o  ", " |  ", "   "),
        3: (" o  ", " |  ", "/  "),
        4: (" o  ", " |  ", "/ \\ "),
        5: (" o  ", "\\|  ", "/ \\ "),
        6: (" o  ", "\\|/ ", "/ \\ ")
    }
    print("\nCurrent Hangman Stage:")
    for line in stages[attempts]:
        print(line)

def play_hangman():
    word = random.choice(words).upper()
    guessed_letters = set()
    attempts = 0
    max_attempts = 6
    word_completion = "_" * len(word)

    print("\n🎮 Welcome to Hangman!")
    print("Try to guess the word one letter at a time.\n")

    while attempts < max_attempts and "_" in word_completion:
        show_hangman(attempts)
        print(f"\nWord: {' '.join(word_completion)}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")
        guess = input("Enter a letter: ").upper().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("❌ Please enter a single alphabetical character.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try again.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            word_completion = "".join([letter if letter in guessed_letters else "_" for letter in word])
            print("✅ Good guess!\n")
        else:
            attempts += 1
            print(f"❌ Wrong guess! You have {max_attempts - attempts} attempts left.\n")

    # Game end result
    show_hangman(attempts)
    print(f"\nWord: {' '.join(word_completion)}")

    if "_" not in word_completion:
        print(f"🎉 Congratulations! You've guessed the word: **{word}**\n")
    else:
        print(f"💀 Sorry, you've run out of attempts. The word was: **{word}**\n")

def main():
    play_hangman()
    while input("🔁 Do you want to play again? (Y/N): ").strip().upper() == "Y":
        play_hangman()
    print("\n👋 Thanks for playing Hangman!")

if __name__ == "__main__":
    main()
