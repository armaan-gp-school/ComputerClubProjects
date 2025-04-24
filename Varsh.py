import random

def scramble_word(word):
    word_letters = list(word)
    random.shuffle(word_letters)
    return ''.join(word_letters)

def get_player_guess():
    guess = input("Your guess: ").strip()
    return guess

def play_round(word):
    scrambled = scramble_word(word)
    print(f"Scrambled word: {scrambled}")
    
    attempts = 0

    while True:
        guess = get_player_guess()
        attempts += 1

        if guess.lower() == word.lower():
            print(f"Correct! You solved it in {attempts} attempt(s)!\n")
            break
        else:
            print("Wrong! Try again.")

def main():
    word_list = ["python", "banana", "computer", "giraffe", "puzzle"]
    print("=== Welcome to Word Scramble! ===")

    while True:
        chosen_word = random.choice(word_list)
        play_round(chosen_word)

        try:
            play_again = input("Play again? (yes/no): ").lower()
            if play_again != "yes":
                print("Thanks for playing! Goodbye.")
                break
        except Exception as e:
            print("Something went wrong, exiting the game.")
            break

# Start the game
main()