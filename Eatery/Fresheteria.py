from Data import eatery
import tkinter as tk

button_height = 5
button_width = 30

frame_height = 5
frame_width = 7


def final():
    print("abc")


def fresheteria():
    data = eatery[1]
    title = list(data.keys())

    # creating new root for each eatery
    root_2 = tk.Tk()

    # basic configuration of root
    root_2.geometry('400x600')
    label = tk.Label(root_2, text="Fresheteria")
    label.pack()
    root_2.title(str(title))

    # creating frames for app
    frame = tk.Frame(root_2, height=frame_height, width=frame_width)

    # buttons of root
    values = data.values()
    for v in values:
        buttons = list(v.keys())

    for b in buttons:
        button = tk.Button(frame, text=b, height=button_height, width=button_width, command=lambda: final())
        button.pack(side="left")

    frame.pack()
    root_2.mainloop()
