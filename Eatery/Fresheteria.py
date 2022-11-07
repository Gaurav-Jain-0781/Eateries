from Data import eatery
import tkinter as tk

i = 0
buttons = None

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
    frame_1 = tk.Frame(root_2, height=frame_height, width=frame_width)
    frame_2 = tk.Frame(root_2, height=frame_height, width=frame_width)
    frame_3 = tk.Frame(root_2, height=frame_height, width=frame_width)
    frame_4 = tk.Frame(root_2, height=frame_height, width=frame_width)
    frame_5 = tk.Frame(root_2, height=frame_height, width=frame_width)
    frame_6 = tk.Frame(root_2, height=frame_height, width=frame_width)

    # buttons of root
    values = data.values()
    for v in values:
        global buttons
        buttons = list(v.keys())

    for b in buttons:
        global i
        i = 1
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
    frame_1.pack()
    frame_2.pack()
    frame_3.pack()
    frame_4.pack()
    frame_5.pack()
    frame_6.pack()

    root_2.mainloop()
