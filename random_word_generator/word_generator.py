## word_generator.py
import threading
from random_word import RandomWords

class WordGenerator:
    def __init__(self):
        self.current_word = ""
        self.is_running = False
        self.random_word_generator = RandomWords()

    def start(self):
        self.is_running = True
        self._generate_word_thread()

    def stop(self):
        self.is_running = False

    def generate_word(self) -> str:
        return self.random_word_generator.get_random_word()

    def _generate_word_thread(self):
        if self.is_running:
            self.current_word = self.generate_word()
            threading.Timer(1, self._generate_word_thread).start()
