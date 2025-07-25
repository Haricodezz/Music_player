import tkinter as tk
from tkinter import filedialog
import pygame
import os

# Initialize pygame mixer
pygame.mixer.init()

# Create main window
root = tk.Tk()
root.title("🎶 Python Music Player")
root.geometry("450x360")
root.config(bg="#1e1e1e")

# Global song path
current_song = ""

# Fonts & Colors
FONT_TITLE = ("Helvetica", 16, "bold")
FONT_BUTTON = ("Helvetica", 11, "bold")
FG = "white"
BG = "#1e1e1e"

# Functions
def load_song():
    global current_song
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        current_song = file
        song_label.config(text="🎵 " + os.path.basename(current_song))
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()

def play_song():
    if current_song:
        pygame.mixer.music.play()

def pause_song():
    pygame.mixer.music.pause()

def resume_song():
    pygame.mixer.music.unpause()

def stop_song():
    pygame.mixer.music.stop()
    song_label.config(text="🎵 No song playing")

# Title Label
title = tk.Label(root, text="🎧 Python Music Player", font=FONT_TITLE, bg=BG, fg="#00ffcc")
title.pack(pady=15)

# Song Label
song_label = tk.Label(root, text="🎵 No song playing", font=("Helvetica", 12), bg=BG, fg="cyan")
song_label.pack(pady=5)

# Frame for buttons
btn_frame = tk.Frame(root, bg=BG)
btn_frame.pack(pady=20)

# Buttons with icons/text
btn_style = {
    "width": 14,
    "font": FONT_BUTTON,
    "bg": "#333",
    "fg": FG,
    "activebackground": "#555",
    "activeforeground": "#00ffcc",
    "bd": 0,
    "cursor": "hand2",
    "padx": 4,
    "pady": 6
}

load_btn = tk.Button(btn_frame, text="📂 Load Song", command=load_song, **btn_style)
play_btn = tk.Button(btn_frame, text="▶️ Play", command=play_song, **btn_style)
pause_btn = tk.Button(btn_frame, text="⏸️ Pause", command=pause_song, **btn_style)
resume_btn = tk.Button(btn_frame, text="🔁 Resume", command=resume_song, **btn_style)
stop_btn = tk.Button(btn_frame, text="⏹️ Stop", command=stop_song, **btn_style)

# Grid Layout
load_btn.grid(row=0, column=0, padx=10, pady=10)
play_btn.grid(row=1, column=0, padx=10, pady=10)
pause_btn.grid(row=1, column=1, padx=10, pady=10)
resume_btn.grid(row=2, column=0, padx=10, pady=10)
stop_btn.grid(row=2, column=1, padx=10, pady=10)

# Run App
root.mainloop()
