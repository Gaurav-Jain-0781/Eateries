import tkinter as tk
from Data import names
from Data import eatery
from Eatery import Fresheteria, Gourmet, Gourmet_Extension, Mingos, Minus_1, Just_Bakes, ICH, Ivy_Hall, Kiosk, Nandini

yash = names
eateries = eatery

root = tk.Tk()
root.title("Eateries")
label = tk.Label(root, text="CHRIST (Deemed To Be University) Bangalore ")
label.pack()
root.geometry('440x440')

frame_height = 5
frame_width = 7
frame = tk.Frame(root, height=frame_height, width=frame_width)
frame_2 = tk.Frame(root, height=frame_height, width=frame_width)
frame_3 = tk.Frame(root, height=frame_height, width=frame_width)
frame_4 = tk.Frame(root, height=frame_height, width=frame_width)
frame_5 = tk.Frame(root, height=frame_height, width=frame_width)

button_height = 5
button_width = 30

for i in yash:
    if i == 1:
        value = yash[i]
        button_1 = tk.Button(
            frame, height=button_height, width=button_width, text=value, command=lambda: Gourmet.gourmet()
        )
        button_1.pack(side="left")
    elif i == 2:
        value = yash[i]
        button_2 = tk.Button(
            frame, height=button_height, width=button_width, text=value, command=lambda: Mingos.mingos()
        )
        button_2.pack(side="left")
    elif i == 3:
        value = yash[i]
        button_3 = tk.Button(
            frame_2, height=button_height, width=button_width, text=value, command=lambda: Nandini.nandini()
        )
        button_3.pack(side="left")
    elif i == 4:
        value = yash[i]
        button_4 = tk.Button(
            frame_2, height=button_height, width=button_width, text=value, command=lambda: Fresheteria.fresheteria()
        )
        button_4.pack(side="left")
    elif i == 5:
        value = yash[i]
        button_5 = tk.Button(
            frame_3, height=button_height, width=button_width, text=value,
            command=lambda: Gourmet_Extension.gourmet_extension()
        )
        button_5.pack(side="left")
    elif i == 6:
        value = yash[i]
        button_6 = tk.Button(
            frame_3, height=button_height, width=button_width, text=value, command=lambda: Ivy_Hall.ivy_hall()
        )
        button_6.pack(side="left")
    elif i == 7:
        value = yash[i]
        button_7 = tk.Button(
            frame_4, height=button_height, width=button_width, text=value, command=lambda: ICH.ich()
        )
        button_7.pack(side="left")
    elif i == 8:
        value = yash[i]
        button_8 = tk.Button(
            frame_4, height=button_height, width=button_width, text=value, command=lambda: Just_Bakes.just_bakes()
        )
        button_8.pack(side="left")
    elif i == 9:
        value = yash[i]
        button_9 = tk.Button(
            frame_5, height=button_height, width=button_width, text=value, command=lambda: Minus_1.minus_1()
        )
        button_9.pack(side="left")
    elif i == 10:
        value = yash[i]
        button_10 = tk.Button(
            frame_5, height=button_height, width=button_width, text=value, command=lambda: Kiosk.kiosk()
        )
        button_10.pack(side="left")
    else:
        raise ValueError

frame.pack()
frame_2.pack()
frame_3.pack()
frame_4.pack()
frame_5.pack()
root.mainloop()
