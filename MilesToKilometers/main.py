import tkinter as tk
import ttkbootstrap as ttk

def convert():
    mile_inp = entry_int.get()
    km_out = mile_inp * 1.61
    out_string.set(km_out)


window = ttk.Window(themename="darkly")
window.title("Miles to Kilometers")
window.geometry('300x150')

title_label = ttk.Label(master=window, text="Miles to Kilometers", font="Calibri 24 bold")
title_label.pack()

inp_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=inp_frame, textvariable=entry_int)
button = ttk.Button(master=inp_frame, text="Convert", command=convert)
entry.pack(side="left", padx=10)
button.pack(side="left")
inp_frame.pack(pady=15)

out_string = tk.StringVar()
out_label = ttk.Label(master=window, text="Output", font="Calibri 15", textvariable=out_string)
out_label.pack(pady=5)

window.mainloop()