import tkinter as tk
import random
from tkinter import messagebox

class RockPaperScissors:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors Game")
        self.choices = ['R', 'P', 'S']
        self.user_score = 0
        self.comp_score = 0
        self.total_points = 0

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="WELCOME TO ROCK-PAPER-SCISSORS GAME!", font=('Arial', 16)).pack(pady=10)

        tk.Label(self.root, text="Enter total points to win:").pack()
        self.points_entry = tk.Entry(self.root)
        self.points_entry.pack()

        tk.Button(self.root, text="Start Game", command=self.start_game).pack(pady=10)

        self.status_label = tk.Label(self.root, text="", font=('Arial', 12))
        self.status_label.pack(pady=10)

        self.buttons_frame = tk.Frame(self.root)
        self.buttons_frame.pack(pady=10)

        self.rock_button = tk.Button(self.buttons_frame, text="Rock", command=lambda: self.play('R'), state=tk.DISABLED)
        self.rock_button.grid(row=0, column=0, padx=10)

        self.paper_button = tk.Button(self.buttons_frame, text="Paper", command=lambda: self.play('P'), state=tk.DISABLED)
        self.paper_button.grid(row=0, column=1, padx=10)

        self.scissors_button = tk.Button(self.buttons_frame, text="Scissors", command=lambda: self.play('S'), state=tk.DISABLED)
        self.scissors_button.grid(row=0, column=2, padx=10)

        self.score_label = tk.Label(self.root, text="Your Score: 0 | Computer Score: 0", font=('Arial', 12))
        self.score_label.pack(pady=10)

    def start_game(self):
        try:
            self.total_points = int(self.points_entry.get())
            if self.total_points <= 0:
                raise ValueError
            self.status_label.config(text="Game Started! Make your choice.")
            self.rock_button.config(state=tk.NORMAL)
            self.paper_button.config(state=tk.NORMAL)
            self.scissors_button.config(state=tk.NORMAL)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid positive integer for total points.")

    def play(self, user_choice):
        comp_choice = random.choice(self.choices)
        result = ""

        if (comp_choice == 'R' and user_choice == 'P') or \
           (comp_choice == 'P' and user_choice == 'S') or \
           (comp_choice == 'S' and user_choice == 'R'):
            self.user_score += 1
            result = f"You chose {user_choice}, Computer chose {comp_choice}. You get a point!"
        elif comp_choice == user_choice:
            result = f"Both chose {user_choice}. It's a tie!"
        else:
            self.comp_score += 1
            result = f"You chose {user_choice}, Computer chose {comp_choice}. Computer gets a point."

        self.status_label.config(text=result)
        self.score_label.config(text=f"Your Score: {self.user_score} | Computer Score: {self.comp_score}")

        if self.user_score == self.total_points:
            messagebox.showinfo("Game Over", "Congratulations! You Win!")
            self.ask_replay()
        elif self.comp_score == self.total_points:
            messagebox.showinfo("Game Over", "Computer Wins!")
            self.ask_replay()

    def ask_replay(self):
        play_again = messagebox.askyesno("Play Again?", "Would you like to play again?")
        if play_again:
            self.reset_game()
        else:
            self.root.destroy()

    def reset_game(self):
        self.user_score = 0
        self.comp_score = 0
        self.points_entry.delete(0, tk.END)
        self.status_label.config(text="")
        self.score_label.config(text="Your Score: 0 | Computer Score: 0")
        self.rock_button.config(state=tk.DISABLED)
        self.paper_button.config(state=tk.DISABLED)
        self.scissors_button.config(state=tk.DISABLED)


if __name__ == "__main__":
    root = tk.Tk()
    game = RockPaperScissors(root)
    root.mainloop()
