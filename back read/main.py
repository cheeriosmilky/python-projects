import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from licensing.models import *
from licensing.methods import Key, Helpers
import pymysql
import mysql.connector as mysql
import shutil
import threading
from ctypes import windll
import shelve
import os
import cv2
from PIL import Image, ImageTk
import pyttsx3
import threading
import _thread	
import multiprocessing

ctk.set_appearance_mode('light')
ctk.set_default_color_theme('green')

root = ctk.CTk()
root.title('proj') 
wwidth=750
wheight=400
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
xaxis = (swidth/2) - (wwidth/2)
yaxis = (sheight/2) - (wheight/2)
root.geometry("{}x{}+{}+{}".format(wwidth, wheight, int(xaxis), int(yaxis)))

def read():
    global ts
    cd = txt.get()
    ts = pyttsx3.init()
    go = cd
    ts.say(go)
    try:
        ts.runAndWait()
    except Exception:
        ts.endLoop()
def delete():
    txt.delete(0, END)
def stop():
    ('asd')

def d():
    try:
        threading.Thread(target=read).start()
    except RuntimeError:
        threading.Thread(target=read)
def s():
    try:
        threading.Thread(target=stop).start()
    except RuntimeError:
        threading.Thread(target=stop)

txt = ctk.CTkEntry(master=root, text_font=('Arial', 10), width=230, height=33, border_width=1)
txt.place(y=72, x=200)
talk = ctk.CTkButton(master=root, text='read', text_font=('Arial Black', 10), command=d, width=130, height=45).place(y=210, x=71)
clear = ctk.CTkButton(master=root, text='clear', text_font=('Arial Black', 10), command=delete, width=130, height=45).place(y=210, x=209.49999999999995)
stops = ctk.CTkButton(master=root, text='stop', text_font=('Arial Black', 10), command=s, width=130, height=45).place(y=210, x=348)

root.mainloop()