from tkinter import *  # Python 3.x
  
  
root = Tk()
root.geometry("200x100")
  
e = Entry(root)
e.insert(END, 'default text', show)
e.pack()
root.mainloop()