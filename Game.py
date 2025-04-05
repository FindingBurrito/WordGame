import random
import os

WORD_BANK = [
    "sus", "rizz", "slay", "yeet", "vibe", "cap",
    "bet", "drip", "nope", "flex", "simp", "ghosted", "snatched"
]

HIGHSCORE_FILE = "highscores.txt"

def scramble_word(word):
    scrambled = list(word)
    while True:
        random.shuffle(scrambled)
        scrambled_word = ''.join(scrambled)
        if scrambled_word != word:
            return scrambled_word

def load_scores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    scores = []
    with open(HIGHSCORE_FILE, "r") as file:
        for line in file:
            try:
                name, score = line.strip().split()
                scores.append((name, int(score)))
            except ValueError:
                continue
    return scores

def save_scores(scores):
    with open(HIGHSCORE_FILE, "w") as file:
        for name, score in scores:
            file.write(f"{name} {score}\n")

def show_top_scores(scores):
    print("\n--- High Scores ---")
    for i, (name, score) in enumerate(scores[:5], 1):
        print(f"{i}. {name} - {score}")
    print("-------------------\n")

def play_game():
    scores = load_scores()
    score = 0

    print("Welcome to the Word Scramble Game (Gen Z Edition)!")
    print("Hint: You’ve got to be Gen Z to ace this!\n")
    print("Type 'quit' anytime to exit.\n")

    while True:
        original = random.choice(WORD_BANK)
        scrambled = scramble_word(original)

        print(f"Unscramble this word: {scrambled}")
        guess = input("Your guess: ").strip()

        if guess.lower() == "quit":
            break

        if guess == original:
            print("Slay! That’s correct.\n")
            score += 10
        else:
            print(f"Oops! The right word was: {original}\n")

    print(f"Game Over! Your final score is: {score}")
    name = input("Enter your name for the high score list: ").strip()
    scores.append((name, score))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    save_scores(scores)
    show_top_scores(scores)

if __name__ == "__main__":
    play_game()
