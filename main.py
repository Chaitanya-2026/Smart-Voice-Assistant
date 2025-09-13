import sys
from gui import VoiceAssistantWindow  
import tkinter as tk


def main():
    root = tk.Tk()
    app = VoiceAssistantWindow(root)  
    root.mainloop()


if __name__ == "__main__":
    main()
