import tkinter as tk
from tkinter import *
 
root = Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = Text(root, height = 5, width = 52)

# Create label
l = Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""
def prints():
    x = T.get("1.0", "end-1c")
    print(x)
# Create button for next text.
b1 = Button(root, text = "Next", command=prints)

# Create an Exit button.
b2 = Button(root, text = "Exit",
      command = root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()





# Insert The Fact.
T.insert(tk.END, Fact)


tk.mainloop()