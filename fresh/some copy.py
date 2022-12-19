import customtkinter as ctk
from customtkinter import *
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from licensing.models import *
from licensing.methods import Key, Helpers
import pymysql
import shutil
from ctypes import windll
import os

#python -m PyInstaller --onefile --windowed --icon=C:\py\home\fresh\pics\yea.ico --add-data "C:/Users/cheer/AppData/Roaming/Python/Python310/site-packages/customtkinter;customtkinter/"  "C:/py/home/fresh/some.py" 

RSAPubKey = "<RSAKeyValue><Modulus>xnTzcz52AZRQ0GRKhHOQ0k8mS2FcgyyWPFD8Ro21uluBLZNaH/ewQGhj8dnXMnJ0HAoaItiGY/BvpHto2FSpypYPNMxXGZC3Go+lswVYPnyfRH76ro5/k0jHRrMLQdErR1BiCJDzUWGhbJIXkoXTj7YnVyGHCbcUC/xuNifGRFhj/SnSg/chpw27DYKVbeC2SzN4q9XvtTqdPKH3AVuC7M5FjjhsSb4+dtwHyqLbGeW8elCPs5bf25tOvQFmWoWK+v3MF/np0Ig+BzTZP5E6hWbSVCGk3kK9yPpQXlEB9dVm3x9oNhwvpl6gHYLjCXaBA5bjUgzdIL00dS/6x0INwQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIzMTc3MzcyOCIsIk5Od2xkdVk4RVhZbERyR2ViN2lORFhFR2xqWUhOZ1NLMkZ6cHU0aDUiXQ=="

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

mainc = '#1D1E24'

root = ctk.CTk()
root.title('Glactic') 
root.overrideredirect(True)
wwidth=430
wheight=225
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
xaxis = (swidth/2) - (wwidth/2)
yaxis = (sheight/2) - (wheight/2)
root.geometry("{}x{}+{}+{}".format(wwidth, wheight, int(xaxis), int(yaxis)))
root.resizable(0, 0)

titlebar = Frame(root, bg='#31333D', relief='raised', bd=0, highlightthickness=6, highlightbackground='#31333D')
titlebar.pack(fill=X)
titlebartitle = Label(root, text='Glactic', bg='#31333D',bd=0,fg='#808080', font=('helvetica', 10), highlightthickness=0)
titlebartitle.place(y=5, x=9)
titlebartitle = Label(titlebar, bg='#31333D',bd=0,fg='#808080', font=('helvetica', 8, 'bold'), highlightthickness=0)
titlebartitle.pack(side=TOP, padx=10)
closebutton = Button(root, text='  ×  ', command=root.destroy,bg='#31333D',font=("calibri", 10, 'bold'),bd=0,fg='#808080',highlightthickness=0, width=5)
closebutton.place(y=4, x=458)

def changex_on_hovering(event):
    global closebutton
    closebutton['bg']='#5A5A5A'
def returnx_to_normalstate(event):
    global closebutton
    closebutton['bg']='#31333D'
    
closebutton.bind('<Enter>',changex_on_hovering)
closebutton.bind('<Leave>',returnx_to_normalstate)


def set_appwindow(mainWindow): # to display the window icon on the taskbar, 
                               # even when using root.overrideredirect(True
    # Some WindowsOS styles, required for task bar integration
    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def get_pos(event): # this is executed when the title bar is clicked to move the window
 
    xwin = root.winfo_x()
    ywin = root.winfo_y()
    startx = event.x_root
    starty = event.y_root

    ywin = ywin - starty
    xwin = xwin - startx

        
    def move_window(event): # runs when window is dragged
        root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


    def release_window(event): # runs when window is released
        root.config(cursor="arrow")
            
            
    titlebar.bind('<B1-Motion>', move_window)
    titlebar.bind('<ButtonRelease-1>', release_window)
    titlebartitle.bind('<B1-Motion>', move_window)
    titlebartitle.bind('<ButtonRelease-1>', release_window)

titlebar.bind('<Button-1>', get_pos) # so you can drag the window from the title bar
titlebartitle.bind('<Button-1>', get_pos) # so you can drag the window from the title 

root.after(10, lambda: set_appwindow(root)) # to see the icon on the task bar

frame = ctk.CTkFrame(master=root, fg_color='#1D1E24', bg_color='#1D1E24')
frame.pack(fill='both', expand=True)

def signup():
    if regusername.get() == '' or regpassword.get() == '' or reglicense.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='camo')
            mycur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue\n              Try Again')
            return
        
        global reglicenseinfo
        reglicenseinfo = reglicense.get()
        result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=17840, \
                    key=f'{reglicenseinfo}',\
                    machine_code=Helpers.GetMachineCode())
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            messagebox.showerror('Error', 'Invalid or Expired License Key')
        else:
            # everything went fine if we are here!
            try:    
                query = 'create database userdata'
                mycur.execute(query)
                query = 'use userdata'
                mycur.execute(query)
                query = 'create table data(id int auto_increment primary key not null, username varchar(15), password varchar(15), licensekey varchar(24))'
                mycur.execute(query)
            except:
                mycur.execute('use userdata')

            query = 'select * from data where username=%s'
            mycur.execute(query,(regusername.get()))
            row = mycur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Username Already Exists')
                return
            query = 'select * from data where licensekey=%s'
            mycur.execute(query,(reglicense.get()))
            row = mycur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'License Key Already in Use')
                return
            
            else:
                query = 'insert into data(username,password,licensekey) values(%s,%s,%s)'
                mycur.execute(query, (regusername.get(), regpassword.get(), reglicense.get()))
                con.commit()
                con.close()
                loginBclick()

def loginT():
    if loglicense.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='camo')
            mycur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue\n              Try Again')
            return
        
        global loglicenseinfo
        loglicenseinfo = loglicense.get()
        result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=17840, \
                    key=f'{loglicenseinfo}',\
                    machine_code=Helpers.GetMachineCode())
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            messagebox.showerror('Error', 'Invalid or Expired License Key')
        else:   
            try:
                query = 'use userdata'
                mycur.execute(query)
                query= 'select * from data where licensekey=%s'
                mycur.execute(query, (loglicense.get()))
                row = mycur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid or Expired License Key')
                else:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    mainpage()
            except:
                messagebox.showerror('Error', 'License Key not Registered')

def oldsignup():
    # global regusernameinfo
    # global reglicenseinfo
    regusernameinfo = regusername.get()
    regpasswordinfo = regpassword.get()
    reglicenseinfo = reglicense.get()
    result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=17840, \
                   key=f'{reglicenseinfo}',\
                   machine_code=Helpers.GetMachineCode(v=2))
    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        invalidpopup()
    else:
        # everything went fine if we are here!
        print("The license is valid!")
        file = open(reglicenseinfo, 'w')
        file.write(regusernameinfo+'\n')
        file.write(regpasswordinfo+'\n')
        file.write(reglicenseinfo)
        file.close()
        loginBclick()

def oldloginT():
    loglicenseinfo = loglicense.get()
    result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=17840, \
                   key=f'{loglicenseinfo}',\
                   machine_code=Helpers.GetMachineCode(v=2))
    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        invalidpopup()
    else:
        # everything went fine if we are here!
        pass
        
        license1 = loglicense.get()
        
        list_of_files = os.listdir()
        if license1 in list_of_files:
            file1 = open(f'{loglicenseinfo}', 'r')
            verify = file1.read().splitlines()
            if license1 in verify:
                for widget in frame.winfo_children():
                    widget.destroy()
                mainpage()
        else:
            signuppopup()

def loginBclick():
    for widget in frame.winfo_children():
        widget.destroy()
    loginpage() 
def registerclick():
    for widget in frame.winfo_children():
        widget.destroy()
    registerpage()

def registerpage():
    # ctk.CTkLabel(master=frame, text='Glactic', text_font=('Arial Black', 45), text_color='#757BC1').place(y=0, x=209) # label
    
    global regusername
    regusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    regusername.place(y=10, x=20)
    
    global regpassword
    regpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='•', width=230, height=35, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    regpassword.place(y=52, x=20)
    
    global reglicense
    reglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=265, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    reglicense.place(y=95, x=20)
    
    ctk.CTkButton(master=frame, text='  Signup', command=signup, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=40, border_color='#757BC1').place(y=95, x=208)    # sign up
    
    ctk.CTkButton(master=frame, text=' Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=145, x=158)     # register bottom

    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=145, x=20)    # login bottom
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40,).place(y=95, x=208)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=95, x=208)     # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=134, x=208)    # fix out bottom

    root.mainloop()

def loginpage():
    # ctk.CTkLabel(master=frame, text='Glactic', text_font=('Arial Black', 45), text_color='#757BC1').place(y=0, x=209) # label
    
    # global logusername
    # logusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35)
    # logusername.place(y=115, x=235)

    # global logpassword
    # logpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), width=230, height=35)
    # logpassword.place(y=165, x=235)
        
    global loglicense
    loglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), show='•', width=265, height=40, border_color='#757BC1', fg_color='#1D1E24',  border_width=1)
    loglicense.place(y=100, x=20)
    
    # mydiscord = ctk.CTkLabel(master=frame, text='Discord: cheerios#6071', text_font=('Arial', 10), text_color='white')
    # mydiscord.place(y=220, x=205)
    
    ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=40).place(y=100, x=208)  # login top
    
    ctk.CTkButton(master=frame, text=' Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=165, x=158)   # register bottom
            
    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=165, x=20)# login bottom
    
    # LoginTbutton = ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=35)
    # LoginTbutton.place(y=165, x=385)
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40).place(y=100, x=208)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=100, x=208)    # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=139, x=208)    # fix out bottom

    # framefixiner = tk.Frame(frame, background='#3D3D3D', width=7, height=34)
    # framefixiner.place(y=165, x=385)
    
    # framefixoutT = tk.Frame(frame, background='#525252', width=8, height=2)
    # framefixoutT.place(y=165, x=384)
    
    # framefixoutB = tk.Frame(frame, background='#525252', width=8, height=2)
    # framefixoutB.place(y=197, x=384)

    # remme = ctk.CTkCheckBox(master=frame, text='Remember Me', fg_color='#757BC1')
    # remme.place(y=220, x=205)
        
    root.mainloop()

def mainpage():
    # regusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    # reglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=290, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    # regusernameinfo = regusername.get()
    # reglicenseinfo = reglicense.get()
    
    ctk.CTkButton(master=frame, text='Sign Out', text_font=('Arial Black', 9), text_color='white', fg_color='#1D1E24', command=loginBclick, width=12, height=6).place(y=15, x=565) # label

    root.mainloop()

loginpage()