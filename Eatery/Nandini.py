from Data import eatery
import tkinter as tk

button_height = 5
button_width = 30

frame_height = 5
frame_width = 7


def nandini():
    data = eatery[2]
    print(data)
    root_2 = tk.Tk()
    root_2.title(eatery)
    root_2.mainloop()
