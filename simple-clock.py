import tkinter as tk
from datetime import datetime


class SimpleClock(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Digital Clock")
        self.geometry("350x280")
        self.resizable(False, False)
        self.configure(bg="black")

        self._use_24hr = False
        self._usegmt = False

        self.time_label = tk.Label(
            self,
            font=("Sans-serif", 40, "normal"),
            bg="black",
            fg="white",
            pady=10,
        )
        self.time_label.pack()

        self.day_label = tk.Label(
            self,
            font=("Ink Free", 28, "bold"),
            bg="black",
            fg="white",
        )
        self.day_label.pack()

        self.date_label = tk.Label(
            self,
            font=("Ink Free", 18, "bold"),
            bg="black",
            fg="white",
            pady=6,
        )
        self.date_label.pack()

        button_frame = tk.Frame(self, bg="black", pady=8)
        button_frame.pack()


        self._update()

    def _update(self):
        now = datetime.now()
        self.time_label.config(text=now.strftime("%I:%M:%S %p"))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))
        self.after(1000, self._update)


if __name__ == "__main__":
    SimpleClock().mainloop()
