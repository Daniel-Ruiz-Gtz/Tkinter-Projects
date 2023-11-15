import tkinter as tk

window = tk.Tk()
window.geometry('600x400')
window.title('Canva Widget')

canvas = tk.Canvas(master=window, background='white')
canvas.pack()

def drawOnCanvas(event):
    x = event.x
    y = event.y
    canvas.create_oval((x - brushSize / 2, y - brushSize/2,x+brushSize/2,y+brushSize/2), fill='black')

def brush_size_adjust(event):
    global brushSize
    if event.delta > 0:
        brushSize += 4
    else:
        brushSize -= 4
    brushSize = max(0, min(brushSize, 50))
    

brushSize = 4
canvas.bind('<Motion>', drawOnCanvas)
canvas.bind('<MouseWheel>', brush_size_adjust)

window.mainloop()