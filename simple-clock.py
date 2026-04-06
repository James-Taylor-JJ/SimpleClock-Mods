import tkinter as tk
from datetime import datetime, timezone


class SimpleClock(tk.Tk):

    def __init__(self):
        self._use_24hr = False                                           
        self._use_gmt = False
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

        self._fmt_btn = tk.Button(                                      
            button_frame, text="24 hr", width=8,                           
            command=self._toggle_format,                                 
        )                                                               
        self._fmt_btn.pack(side=tk.LEFT, padx=10)                       
 
        self._tz_btn = tk.Button(                                       
            button_frame, text="GMT", width=8,                             
            command=self._toggle_timezone,                               
        )                                                                
        self._tz_btn.pack(side=tk.LEFT, padx=10)                        
 
        self._update()
    
    def _toggle_format(self):                                           
        self._use_24hr = not self._use_24hr                             
        self._fmt_btn.config(text="12 hr" if self._use_24hr else "24 hr")
        self.update()  
 
    def _toggle_timezone(self):                                         
        self._use_gmt = not self._use_gmt                               
        self._tz_btn.config(text="Local" if self._use_gmt else "GMT")  
        self.update()  

    def _update(self):
        now = datetime.now(timezone.utc) if self._use_gmt else datetime.now()
        time_fmt = "%H:%M:%S" if self._use_24hr else "%I:%M:%S %p"
        self.time_label.config(text=now.strftime(time_fmt))
        self.day_label.config(text=now.strftime("%A"))
        self.date_label.config(text=now.strftime("%d %B, %Y"))
        self.after(1000, self._update)


if __name__ == "__main__":
    SimpleClock().mainloop()
