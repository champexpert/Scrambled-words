import tkinter as tk
import random
from tkinter import messagebox

# Word list (100+ words)
words = [
    "python", "emoji", "spelling", "keyboard", "function", "variable", "loop", "input", "output", "window",
    "button", "screen", "label", "entry", "submit", "canvas", "widget", "click", "game", "score",
    "winner", "player", "puzzle", "random", "scramble", "answer", "correct", "wrong", "start", "finish",
    "apple", "banana", "orange", "grape", "lemon", "cherry", "melon", "peach", "mango", "kiwi",
    "cloud", "storm", "rainbow", "snow", "sunshine", "thunder", "wind", "weather", "season", "sky",
    "cat", "dog", "rabbit", "mouse", "tiger", "lion", "zebra", "koala", "monkey", "panda",
    "train", "bus", "car", "plane", "ship", "bicycle", "rocket", "subway", "motorcycle", "tractor", 
    "pizza", "burger", "fries", "salad", "sushi", "noodles", "bread", "cheese", "egg", "chicken",
    "earth", "moon", "star", "planet", "galaxy", "space", "astronaut", "telescope", "universe", "orbit",
    "music", "violin", "guitar", "piano", "drums", "flute", "trumpet", "singer", "song", "melody",
    "magic", "dragon", "castle", "wizard", "knight", "sword", "potion", "treasure", "quest", "battle"
]

# Scramble function
def scramble(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

class WordScrambleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Scramble Game")
        self.root.geometry("500x350")
        self.root.configure(bg="#f0e68c")

        self.score = 0
        self.current_word = ""
        self.scrambled_word = ""

        # Title and subtitle
        self.title = tk.Label(root, text="🧠 Word Scramble 🌀", font=("Arial", 20, "bold"), bg="#f0e68c")
        self.subtitle = tk.Label(root, text="More than 100 words to scramble and guess!", font=("Arial", 10, "bold"), bg="#f0e68c")
        self.title.pack(pady=10)
        self.subtitle.pack(pady=5)

        # Scrambled word display
        self.word_label = tk.Label(root, text="", font=("Arial", 24), bg="#f0e68c")
        self.word_label.pack(pady=10)

        # Input field
        self.entry = tk.Entry(root, font=("Arial", 16))
        self.entry.pack(pady=5)

        # Buttons
        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer, font=("Arial", 14), bg="#4CAF50", fg="white")
        self.submit_btn.pack(pady=5)

        self.feedback = tk.Label(root, text="", font=("Arial", 14), bg="#f0e68c")
        self.feedback.pack()

        self.next_btn = tk.Button(root, text="Next Word", command=self.next_word, font=("Arial", 14), bg="#4682B4", fg="white")
        self.next_btn.pack(pady=5)

        self.score_label = tk.Label(root, text=f"Score: {self.score}", font=("Arial", 14), bg="#f0e68c")
        self.score_label.pack()

        self.next_word()

    def next_word(self):
        self.current_word = random.choice(words)
        self.scrambled_word = scramble(self.current_word)
        self.word_label.config(text=self.scrambled_word)
        self.entry.delete(0, tk.END)
        self.feedback.config(text="")

    def check_answer(self):
        guess = self.entry.get().strip().lower()
        if guess == self.current_word:
            self.feedback.config(text="✅ Correct!", fg="green")
            self.score += 1
        else:
            self.feedback.config(text=f"❌ Wrong! It was '{self.current_word}'", fg="red")
        self.score_label.config(text=f"Score: {self.score}")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = WordScrambleGame(root)
    root.mainloop()
