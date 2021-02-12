import tkinter

mainWindow = tkinter.Tk()

label1 = tkinter.Label(mainWindow, text = "label 1")
label2 = tkinter.Label(mainWindow, text = "label 2")

tombol1 = tkinter.Button(mainWindow, text = "tombol 1")
tombol2 = tkinter.Button(mainWindow, text = "tombol 2")

# method positioning
label1.pack()
label2.pack()
tombol1.pack()
tombol2.pack()

# method menampilkan gui
mainWindow.mainloop()