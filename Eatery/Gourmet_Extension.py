from Data import eatery
import tkinter as tk

button_height = 5
button_width = 30

frame_height = 5
frame_width = 7


def gourmet_extension():
    data = eatery[4]
    print(data)
    root_2 = tk.Tk()
    root_2.title(eatery)
    root_2.mainloop()
