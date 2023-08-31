## main.py
from word_generator import WordGenerator
from gui import GUI

def main():
    word_generator = WordGenerator()
    gui = GUI(word_generator)
    gui.run()

if __name__ == "__main__":
    main()
