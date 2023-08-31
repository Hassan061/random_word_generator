import tkinter as tk
from word_generator import WordGenerator

class GUI:
    def __init__(self, word_generator: WordGenerator):
        self.root = tk.Tk()
        self.root.title("Random Word Generator")
        self.word_label = tk.Label(self.root, text="", font=("Helvetica", 32))
        self.word_label.pack(pady=20)
        self.start_stop_button = tk.Button(self.root, text="Start", command=self.start_stop, font=("Helvetica", 16))
        self.start_stop_button.pack(pady=20)
        self.word_generator = word_generator

    def start_stop(self):
        if self.word_generator.is_running:
            self.word_generator.stop()
            self.start_stop_button.config(text="Start")
        else:
            self.word_generator.start()
            self.start_stop_button.config(text="Stop")
            self.update_word()

    def update_word(self):
        if self.word_generator.is_running:
            self.word_label.config(text=self.word_generator.current_word)
            self.root.after(1000, self.update_word)

    def run(self):
        self.root.mainloop()
