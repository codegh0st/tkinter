from tkinter import *
root = Tk()
#define action of the button when it is clicked.
def myclick():
    mylabel = Label(root, text="result after clicking the button")
    mylabel.pack()
#creating Button
mybutton = Button(root, text="My first button", padx=20, pady=25, command=myclick, fg="white", bg="grey")
mybutton.pack()

##############################################
#creating input box
entry_box = Entry(root, width=30, borderwidth=5)
entry_box.pack()

# fuction runs after button is clicked. see command parameters in input_button
def take_input():
    myvariable = "Hello  " + entry_box.get()
    mylabel1 = Label(root, text=myvariable)
    mylabel1.pack() 
input_button = Button(root, text="takes input from above box and print", padx=30, pady=10, command=take_input, fg="red", borderwidth=2)
input_button.pack()


###############################################
print("this line added to push in other branch")

root.mainloop()