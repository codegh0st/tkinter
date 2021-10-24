from tkinter import *
root = Tk()
#creating a label widget
mylabel = Label(root, text="Hi tkinter window ")
mylabel1 = Label(root, text="Hi tkinter window ")
mylabel2 = Label(root, text="Hi tkinter window ")


mylabel.grid(row=0, column=0)
mylabel1.grid(row=1, column=0)
mylabel2.grid(row=2, column=0)

# OR you can use this syntax will do the same thing. 
# mylabel = Label(root, text="Hi tkinter window ").grid(row=0, column=0)
# mylabel1 = Label(root, text="Hi tkinter window ").grid(row=1, column=0)
# mylabel2 = Label(root, text="Hi tkinter window ").grid(row=1, column=0)
# mylabel2 = Label(root, text="Hi tkinter window ").grid(row=1, column=0)

root.mainloop()