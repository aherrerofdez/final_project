import backend
import sys
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import ImageTk, Image


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
        self.font_title = font.Font(family='Courier', size=20, weight='bold')
        self.font_body = font.Font(family='Courier', size=14, weight='bold')

        # Add window properties
        self.window = w
        self.window.title("Car Race Game")
        self.window.geometry("935x600")
        self.window.resizable(0, 0)

        # Create main frame
        self.mainframe = tk.Frame(master=window, bg=self.bg_color)
        self.mainframe.pack_propagate(0)
        self.mainframe.pack(fill=tk.BOTH, expand=1)

        # Create Race Track Canvas
        self.racetrack = tk.Canvas(self.mainframe, width=500, height=550, bg=self.path_color, highlightthickness=0)
        self.racetrack.grid(row=0, column=0, rowspan=8, padx=(25, 25), pady=(25, 0))

        car_size = 100, 100
        player_png = Image.open("img/player_car.png")
        player_png.thumbnail(car_size)
        self.player_img = ImageTk.PhotoImage(player_png)
        self.player_car = self.racetrack.create_image(250, 495, image=self.player_img)

        obstacle_png = Image.open("img/obstacle_car.png")
        obstacle_png.thumbnail(car_size)
        self.obstacle_img = ImageTk.PhotoImage(obstacle_png)
        self.obstacle_car = self.racetrack.create_image(25, -50, image=self.obstacle_img)

        # Create Settings Panel
        self.instructions = tk.Button(self.mainframe, text="INSTRUCTIONS", command=self.show_instructions)
        self.instructions.config(font=self.font_body, bg=self.btn_color, fg=self.font_color)
        self.instructions.grid(row=0, column=1, columnspan=6, pady=(50, 0))

        self.mode_lb = tk.Label(self.mainframe, text="MODE", bg=self.bg_color, fg=self.btn_color)
        self.mode_lb.config(font=self.font_title)
        self.mode_lb.grid(row=1, column=1, columnspan=6, pady=(20, 5))

        self.user_btn = tk.Button(self.mainframe, text="USER", command=self.play_user, font=self.font_body)
        self.user_btn.config(bg=self.btn_color, fg=self.font_color, width=15)
        self.user_btn.grid(row=2, column=1, columnspan=3, padx=(5, 0))

        self.comp_btn = tk.Button(self.mainframe, text="COMPUTER AI", command=self.play_comp, font=self.font_body)
        self.comp_btn.config(bg=self.btn_color, fg=self.font_color, width=15)
        self.comp_btn.grid(row=2, column=4, columnspan=3, padx=(0, 5))

        self.difficulties_lb = tk.Label(self.mainframe, text="DIFFICULTY", bg=self.bg_color, fg=self.btn_color)
        self.difficulties_lb.config(font=self.font_title)
        self.difficulties_lb.grid(row=3, column=1, columnspan=6, pady=(20, 5))

        self.difficulties = []
        mode = ["EASY", "MEDIUM", "DIFFICULT"]
        col = 1
        for i in range(3):
            self.diff_opt = tk.Button(self.mainframe, text=mode[i], font=self.font_body, width=10)
            self.diff_opt.config(bg=self.btn_color, fg=self.font_color,
                                 command=lambda track=self.diff_opt: self.choose_difficulty(track))
            self.diff_opt.grid(row=4, column=i+col, columnspan=2)
            self.difficulties.append(self.diff_opt)
            col += 1

        self.speed = 0

        self.play = tk.Button(self.mainframe, text="PLAY", command=self.play, font=self.font_title, width=6)
        self.play.config(bg=self.btn_color, fg=self.font_color)
        self.play.grid(row=5, column=1, columnspan=6, pady=(30, 25))

        self.controls_frame = tk.Frame(master=self.mainframe, bg=self.bg_color, width=325, height=100)
        self.controls_frame.grid(row=6, column=1, columnspan=6)

        size = 40, 80
        arrow_left = Image.open("img/left.png")
        arrow_left.thumbnail(size)
        self.left_arrow = ImageTk.PhotoImage(arrow_left)
        self.left_btn = tk.Button(self.controls_frame, image=self.left_arrow, bg=self.bg_color, bd=0)
        self.left_btn.config(activebackground=self.bg_color, state="disabled",
                             command=lambda direction="Left": self.move(direction))
        self.left_btn.grid(row=0, column=0)

        space_lb = tk.Label(self.controls_frame, bg=self.bg_color, width=8)
        space_lb.grid(row=0, column=1)

        arrow_right = Image.open("img/right.png")
        arrow_right.thumbnail(size)
        self.right_arrow = ImageTk.PhotoImage(arrow_right)
        self.right_btn = tk.Button(self.controls_frame, image=self.right_arrow, bg=self.bg_color, bd=0)
        self.right_btn.config(activebackground=self.bg_color, state="disabled",
                              command=lambda direction="Right": self.move(direction))
        self.right_btn.grid(row=0, column=2)

        self.exit = tk.Button(self.mainframe, text="EXIT", command=sys.exit, font=self.font_body, width=6)
        self.exit.config(bg=self.btn_color, fg=self.font_color)
        self.exit.grid(row=7, column=1, columnspan=6, pady=25)

    def show_instructions(self):
        messagebox.showinfo(message=self.bk.get_instructions(), parent=self.mainframe, title="Instructions")

    def play_user(self):
        self.comp_btn.config(bg=self.btn_color, fg=self.font_color)
        self.user_btn.config(bg=self.font_color, fg=self.btn_color)

    def play_comp(self):
        self.user_btn.config(bg=self.btn_color, fg=self.font_color)
        self.comp_btn.config(bg=self.font_color, fg=self.btn_color)

    def choose_difficulty(self, track):
        for btn in self.difficulties:
            btn.config(bg=self.btn_color, fg=self.font_color)
        track.config(bg=self.font_color, fg=self.btn_color)
        self.speed = self.bk.get_track(self.difficulties.index(track))

    def play(self):
        self.play["state"] = "disabled"
        self.play.config(disabledforeground=self.btn_color, bg=self.font_color)
        # Place Player Car in the middle
        self.racetrack.coords(self.player_car, 250, 495)
        # If 'User' mode is chosen or user clicks "PLAY" without choosing a mode (Default: User Mode)
        self.user_btn.config(bg=self.font_color, fg=self.btn_color)
        self.left_btn["state"] = "active"
        self.right_btn["state"] = "active"
        window.bind("<KeyPress-Left>", lambda e: self.move(e))
        window.bind("<KeyPress-Right>", lambda e: self.move(e))
        # If 'Computer AI' mode is chosen
        if self.comp_btn["bg"] == self.font_color:
            self.user_btn.config(bg=self.btn_color, fg=self.font_color)
            self.left_btn["state"] = "disabled"
            self.right_btn["state"] = "disabled"
            window.unbind("<KeyPress-Left>")
            window.unbind("<KeyPress-Right>")
        # If no track is chosen, play default track 1
        play_default = True
        for btn in self.difficulties:
            if btn["bg"] == self.font_color:
                play_default = False
        if play_default:
            self.difficulties[1].config(bg=self.font_color, fg=self.btn_color)
            self.speed = self.bk.get_track(1)

        self.play_background()

    def move(self, event):
        direction = event
        if type(event) is not str:
            direction = event.keysym
        if direction == "Left":
            self.racetrack.move(self.player_car, -10, 0)
        else:
            self.racetrack.move(self.player_car, 10, 0)

    def play_background(self):
        if int(self.racetrack.coords(self.obstacle_car)[1]) < 600:
            self.racetrack.move(self.obstacle_car, 0, 10)
            self.window.after(self.speed, self.play_background)


window = tk.Tk()
new_game = Front(window)
window.mainloop()
