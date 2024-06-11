import tkinter as tk
from tkinter import filedialog
import pygame

class MediaPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("senti sta musica cazzo")
        self.root.geometry("300x150")
        
        self.label = tk.Label(root, text="benvenuto in sto coso che ti fa sentire la musica")
        self.label.pack(pady=20)
        
        self.open_button = tk.Button(root, text="apri sto file", command=self.open_file)
        self.open_button.pack()
        
        self.play_button = tk.Button(root, text="parti", command=self.play, state=tk.DISABLED)
        self.play_button.pack()
        
        self.stop_button = tk.Button(root, text="fermati", command=self.stop, state=tk.DISABLED)
        self.stop_button.pack()
        
        pygame.mixer.init()

    def open_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.label.config(text=self.file_path)
            self.play_button.config(state=tk.NORMAL)
            self.stop_button.config(state=tk.NORMAL)
        
    def play(self):
        pygame.mixer.music.load(self.file_path)
        pygame.mixer.music.play()
        
    def stop(self):
        pygame.mixer.music.stop()
        
if __name__ == "__main__":
    root = tk.Tk()
    player = MediaPlayer(root)
    root.mainloop()
