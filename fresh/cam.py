from tkinter import *
import customtkinter
import cv2
from PIL import Image, ImageTk
import time

root=customtkinter.CTk()
root.geometry('600x500')


# lmain = Label(root,width=630,height=300)
cap=cv2.VideoCapture(0)
def video_stream():
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA) 
    img = Image.fromarray(cv2image)
    
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(1, video_stream)

global ison
ison = True
def switch():
    global ison
    if ison == True:
        global btn
        btn = customtkinter.CTkButton(master=root, text='Stop', text_font=('Arial Black', 10), command=switch).place(y=30, x=30) # label
        global lmain
        lmain = Label(root,width=630,height=300)
        lmain.place(y=50, x=60)
        time.sleep(0.5)
        video_stream()
        root.update()
        ison = False
    else:
        btn = customtkinter.CTkButton(master=root, text='Start', text_font=('Arial Black', 10), command=switch).place(y=30, x=30) # label
        lmain.destroy()
        root.update()
        ison = True

btn=customtkinter.CTkButton(master = root, text='btn', command=switch).place(y=30, x=30)
root.mainloop()