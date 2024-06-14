import tkinter as tk
from gui import MontyHallGUI

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Monty Hall Game")
    root.geometry("1080x720")
    root.resizable(False, False)
    app = MontyHallGUI(root)
    root.mainloop()