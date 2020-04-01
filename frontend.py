import tkinter as tk
from tkinter import font
from tkinter import messagebox
import backend
import sys


class Front(object):
    def __init__(self, w):
        # Connect with BackEnd
        self.bk = backend.Back()

        # Define Colors
        self.bg_color = "#85A7B4"
        self.wall_color = "#313331"
        self.path_color = "#746944"
        self.btn_color = "#5D6568"
        self.font_color = "#B9D7C4"

        # Define Fonts
        self.font = font.Font(family='Courier', size=20, weight='bold')

        # Add window properties
        self.window = w
        self.window.title("Car Race Game")
        self.window.geometry("900x600")
        self.window.resizable(0, 0)

        # Create main frame
        self.mainframe = tk.Frame(master=window, bg=self.bg_color)
        self.mainframe.pack_propagate(0)
        self.mainframe.pack(fill=tk.BOTH, expand=1)

        # Create Race Track Canvas
        self.racetrack = tk.Canvas(self.mainframe, width=500, height=550, bg=self.wall_color, highlightthickness=0)
        self.racetrack.grid(row=0, column=0, rowspan=9, padx=(25, 28), pady=(25, 0))

        # Create Settings Panel
        self.mode_lb = tk.Label(self.mainframe, text="MODE", bg=self.bg_color, fg=self.btn_color)
        self.mode_lb.config(font=self.font)
        self.mode_lb.grid(row=0, column=1, columnspan=6, pady=(25, 0))

        self.user_btn = tk.Button(self.mainframe, text="USER", command=self.play_user, font=self.font)
        self.user_btn.config(bg=self.btn_color, fg=self.font_color, width=9)
        self.user_btn.grid(row=1, column=1, columnspan=3, padx=(5, 0))

        self.comp_btn = tk.Button(self.mainframe, text="COMPUTER", command=self.play_comp, font=self.font)
        self.comp_btn.config(bg=self.btn_color, fg=self.font_color, width=9)
        self.comp_btn.grid(row=1, column=4, columnspan=3, padx=(0, 5))

        self.racetrack_lb = tk.Label(self.mainframe, text="RACE TRACK", bg=self.bg_color, fg=self.btn_color)
        self.racetrack_lb.config(font=self.font)
        self.racetrack_lb.grid(row=3, column=1, columnspan=6, pady=(25, 0))

        self.racetracks = []
        col = 1
        for i in range(3):
            self.racetrack_opt = tk.Button(self.mainframe, text=i+1, font=self.font, width=6)
            self.racetrack_opt.config(bg=self.btn_color, fg=self.font_color,
                                      command=lambda track=self.racetrack_opt: self.choose_racetrack(track))
            self.racetrack_opt.grid(row=4, column=i+col, columnspan=2)
            self.racetracks.append(self.racetrack_opt)
            col += 1

        self.instructions = tk.Button(self.mainframe, text="INSTRUCTIONS", command=self.show_instructions)
        self.instructions.config(font=self.font, bg=self.btn_color, fg=self.font_color)
        self.instructions.grid(row=6, column=1, columnspan=6, pady=(25, 0))

        self.exit = tk.Button(self.mainframe, text="EXIT", command=sys.exit, font=self.font)
        self.exit.config(bg=self.btn_color, fg=self.font_color)
        self.exit.grid(row=8, column=1, columnspan=6, pady=(25, 0))

    def play_user(self):
        self.comp_btn.config(bg=self.btn_color, fg=self.font_color)
        self.user_btn.config(bg=self.font_color, fg=self.btn_color)

    def play_comp(self):
        self.user_btn.config(bg=self.btn_color, fg=self.font_color)
        self.comp_btn.config(bg=self.font_color, fg=self.btn_color)

    def choose_racetrack(self, track):
        for btn in self.racetracks:
            btn.config(bg=self.btn_color, fg=self.font_color)
        track.config(bg=self.font_color, fg=self.btn_color)

    def show_instructions(self):
        instructions = '1. Choosing a Mode: \n     - User Mode: if you want to play the game. \n     - Computer Mode:' \
                       ' if you want to watch our AI play. \n \n 2. Choosing a race track: \n You can choose your ' \
                       'favourite track to play on. \n \n 3. Click on "EXIT" if you want to close the game.'
        info = messagebox.showinfo(message=instructions, parent=self.mainframe, title="Instructions")


window = tk.Tk()
new_game = Front(window)
window.mainloop()
