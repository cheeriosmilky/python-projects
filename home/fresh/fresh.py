import customtkinter as ctk
import tkinter as tk
from tkinter import *

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
button = ctk.CTk()
root.geometry('700x350')
root.resizable(0, 0)
root.title('Monke')

frame = ctk.CTkFrame(master=root, fg_color='#1D1E24', bg_color='#1D1E24')
frame.pack(pady=0, padx=0, fill='both', expand=True)
# logframe = ctk.CTkFrame(master=root, fg_color='#1D1E24', bg_color='#1D1E24')
# logframe.pack(pady=0, padx=0, fill='both', expand=True)
# regframe = ctk.CTkFrame(master=root, fg_color='#1D1E24', bg_color='#1D1E24')
# regframe.pack(pady=0, padx=0, fill='both', expand=True)

def loginT():
    print('Test Log')
def signup():
    print('Test Sign')
def loginBclick():
    for widget in frame.winfo_children():
        widget.destroy()
    loginpage() 
def registerclick():
    for widget in frame.winfo_children():
        widget.destroy()
    registerpage()

def loginpage():
    label = ctk.CTkLabel(master=frame, text='Monke', text_font=('Arial Black', 45), text_color='#AF7AC5')
    label.place(y=25, x=240)
            
    license = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=290, height=40)
    license.place(y=140, x=205)

    LoginTbutton = ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#AF7AC5', width=80, height=40)
    LoginTbutton.place(y=140, x=415)

    # username = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), width=230, height=35)
    # username.place(y=120, x=235)
            
    # password = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='*', width=230, height=35)
    # password.place(y=180, x=235)

    registerbutton = ctk.CTkButton(master=frame, text='Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45)
    registerbutton.place(y=265, x=365)
            
    loginBbutton = ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#AF7AC5', width=130, height=45)
    loginBbutton.place(y=265, x=205)

    framefixiner = tk.Frame(frame, background='#3D3D3D', width=7, height=40)
    framefixiner.place(y=140, x=415)
    
    framefixoutT = tk.Frame(frame, background='#525252', width=8, height=2)
    framefixoutT.place(y=140, x=414)
    
    framefixoutB = tk.Frame(frame, background='#525252', width=8, height=2)
    framefixoutB.place(y=178, x=414)

    remme = ctk.CTkCheckBox(master=frame, text='Remember Me', fg_color='#AF7AC5')
    remme.place(y=220, x=205)
            
    root.mainloop()

def registerpage():
    label = ctk.CTkLabel(master=frame, text='Monke', text_font=('Arial Black', 45), text_color='#AF7AC5')
    label.place(y=25, x=240)

    license = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=290, height=40)
    license.place(y=215, x=205)
    
    username = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35)
    username.place(y=115, x=235)
    
    password = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='*', width=230, height=35)
    password.place(y=165, x=235)
    
    signupbutton = ctk.CTkButton(master=frame, text='  Signup', command=signup, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#AF7AC5', width=80, height=40)
    signupbutton.place(y=215, x=415)
    
    registerbutton = ctk.CTkButton(master=frame, text='Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#AF7AC5', width=130, height=45)
    registerbutton.place(y=265, x=365)
    
    loginBbutton = ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45)
    loginBbutton.place(y=265, x=205)
    
    framefixiner = tk.Frame(frame, background='#3D3D3D', width=7, height=40)
    framefixiner.place(y=215, x=415)
    
    framefixoutT = tk.Frame(frame, background='#525252', width=8, height=2)
    framefixoutT.place(y=215, x=414)
    
    framefixoutB = tk.Frame(frame, background='#525252', width=8, height=2)
    framefixoutB.place(y=253, x=414)

    root.mainloop()
loginpage()