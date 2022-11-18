from Data import eatery
import tkinter as tk

button_height = 5
button_width = 30

i = 1

frame_height = 5
frame_width = 7

data = eatery[1]
title = "Fresheteria"


def func_buttons(buttons, frame_1, frame_2, frame_3, frame_4, frame_5, frame_6):
    global i
    for b in buttons:
        if i == 1:
            button_1 = tk.Button(frame_1, text=b, height=button_height, width=button_width, command=lambda: final())
            button_1.pack(side="left")
        elif i == 2:
            button_2 = tk.Button(frame_1, text=b, height=button_height, width=button_width, command=lambda: final())
            button_2.pack(side="right")
        elif i == 3:
            button_3 = tk.Button(frame_2, text=b, height=button_height, width=button_width, command=lambda: final())
            button_3.pack(side="left")
        elif i == 4:
            button_4 = tk.Button(frame_2, text=b, height=button_height, width=button_width, command=lambda: final())
            button_4.pack(side="right")
        elif i == 5:
            button_5 = tk.Button(frame_3, text=b, height=button_height, width=button_width, command=lambda: final())
            button_5.pack(side="left")
        elif i == 6:
            button_6 = tk.Button(frame_3, text=b, height=button_height, width=button_width, command=lambda: final())
            button_6.pack(side="right")
        elif i == 7:
            button_7 = tk.Button(frame_4, text=b, height=button_height, width=button_width, command=lambda: final())
            button_7.pack(side="left")
        elif i == 8:
            button_8 = tk.Button(frame_4, text=b, height=button_height, width=button_width, command=lambda: final())
            button_8.pack(side="right")
        elif i == 9:
            button_9 = tk.Button(frame_5, text=b, height=button_height, width=button_width, command=lambda: final())
            button_9.pack(side="left")
        elif i == 10:
            button_10 = tk.Button(frame_5, text=b, height=button_height, width=button_width, command=lambda: final())
            button_10.pack(side="right")
        elif i == 11:
            button_11 = tk.Button(frame_6, text=b, height=button_height, width=button_width, command=lambda: final())
            button_11.pack(side="left")
        i = i+1


def fresheteria():
    # creating new root for each eatery
    sub_eatery = tk.Tk()

    # basic configuration of root
    sub_eatery.geometry('440x535')
    label = tk.Label(sub_eatery, text="Fresheteria")
    label.pack()
    sub_eatery.title(str(title))

    # creating frames for app
    frame_1 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)
    frame_2 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)
    frame_3 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)
    frame_4 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)
    frame_5 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)
    frame_6 = tk.Frame(sub_eatery, height=frame_height, width=frame_width)

    # buttons of root
    values = data.values()
    for v in values:
        buttons = list(v.keys())

    func_buttons(buttons, frame_1, frame_2, frame_3, frame_4, frame_5, frame_6)
    frame_1.pack()
    frame_2.pack()
    frame_3.pack()
    frame_4.pack()
    frame_5.pack()
    frame_6.pack()
    sub_eatery.mainloop()


def final():
    print("abc")
