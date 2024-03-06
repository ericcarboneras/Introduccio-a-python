import tkinter as tk

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    window.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = tk.Tk()
root.title("Zoo X")

center_window(root, 320, 200)

root.configure(bg="#FFFF00")

image_path = "/home/alumne/Baixades/Mono.png"

image = tk.PhotoImage(file=image_path)

label = tk.Label(root, image=image)
label.pack()

root.mainloop()
