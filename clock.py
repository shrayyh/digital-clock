import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.configure(bg="black")

label = tk.Label(root, font=("Courier", 60), bg="pink", fg="black")
label.pack(anchor="center")

update_time()
root.mainloop()
