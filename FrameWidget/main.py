import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.geometry('600x400')
window.title('Frames and parenting')

frame = ttk.Frame(master=window, borderwidth=10, relief= tk.GROOVE)
frame.pack(side='left')

label = ttk.Label(master=frame, text='Label inside Frame')
label.pack()

button = ttk.Button(master=frame, text='Button inside Frame')
button.pack()

label02 = ttk.Label(master=window, text='Label outside Frame')
label02.pack(side='left')

frame02 = ttk.Frame(master=window, borderwidth=10, relief= tk.GROOVE)
label03 = ttk.Label(master=frame02, text='Label inside Frame').pack()
button02 = ttk.Button(master=frame02, text='Button inside Frame').pack()
entry = ttk.Entry(master=frame02).pack()
frame02.pack(side="left")

window.mainloop()