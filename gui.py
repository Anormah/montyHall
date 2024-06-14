import tkinter as tk
from tkinter import messagebox
from montyHall import MontyHall

class MontyHallGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Monty Hall Game")
        self.game = MontyHall()

        self.door_buttons = []
        for i in range(3):
            button = tk.Button(self.root, text=f"Door {i+1}", command=lambda i=i: self.choose_door(i))
            button.grid(row=0, column=i)
            self.door_buttons.append(button)

        self.switch_button = tk.Button(self.root, text="Switch Door", command=self.switch_door, state=tk.DISABLED)
        self.switch_button.grid(row=1, column=0, columnspan=3)

        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=2, column=0, columnspan=3)

    def choose_door(self, choice):
        self.game.user_choice = choice
        self.game.reveal_door()
        self.update_buttons()
        self.switch_button.config(state=tk.NORMAL)

    def switch_door(self):
        self.game.make_switch()
        self.update_buttons()
        self.show_result()

    def update_buttons(self):
        for i in range(3):
            if i == self.game.reveal:
                self.door_buttons[i].config(state=tk.DISABLED, text=f"Door {i+1}\n(Goat)")
            elif i == self.game.user_choice:
                self.door_buttons[i].config(text=f"Door {i+1}\n(Your Choice)")
            else:
                self.door_buttons[i].config(state=tk.DISABLED)

    def show_result(self):
        if self.game.check_win():
            self.result_label.config(text="Congratulations! You won a car!")
        else:
            self.result_label.config(text="Sorry! You got a goat.")
        messagebox.showinfo("Game Over", self.result_label.cget("text"))
        self.reset_game()

    def reset_game(self):
        self.game.reset()
        self.result_label.config(text="")
        for i in range(3):
            self.door_buttons[i].config(state=tk.NORMAL, text=f"Door {i+1}")
        self.switch_button.config(state=tk.DISABLED)
