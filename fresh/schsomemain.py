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
from ctypes import windll
import shelve
import os

#python -m PyInstaller --onefile --windowed --icon=C:\py\home\fresh\pics\yea.ico --add-data "C:/Users/cheer/AppData/Roaming/Python/Python310/site-packages/customtkinter;customtkinter/"  "C:/py/home/fresh/schsomemain.py" 

RSAPubKey = "<RSAKeyValue><Modulus>nakBsggAFPeri5w98jlWfQ2bLlFG4b704be79ox+VOhze7kiqGZFc4zHAAHFVObC8sCAXT443NXxp4vxUwkXuMOjDl+WYzzGEeOvaotnjbSUwwKnF9mmHn3HxR8vahvpxcdOK/QErj20D6FArgqSAPNe4fWBowfK0LBcsmUgA9S4aAWqdbzn5I/wymbEdFALLDP00q1sDmEYlLNGXI+ixwX1ozn8gK0dx7QPyyK9GqJ551wWCknFwc63dJbYA1c7k98FLhgWC/vxcBdNZTH66WGtsRLT/sYboYd/2LRUoFGCeZ8GOiJ4F2oTOVLGImJaXmdod6sB1jXB8YQAImqbjQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIzNjA2NjYxNCIsInlLSWJ5VVJEdFVPZHpkN3A3TE1rVk9HQ3Zxa29UcTVVaE1YeUtmR0giXQ=="

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

mainc = '#1D1E24'

root = ctk.CTk()
root.title('Malware') 
root.overrideredirect(True)
wwidth=550
wheight=300
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
xaxis = (swidth/2) - (wwidth/2)
yaxis = (sheight/2) - (wheight/2)
root.geometry("{}x{}+{}+{}".format(wwidth, wheight, int(xaxis), int(yaxis)))
root.resizable(0, 0)

def combine_funcs(*funcs):
  
    # this function will call the passed functions
    # with the arguments that are passed to the functions
    def inner_combined_func(*args, **kwargs):
        for f in funcs:
  
            # Calling functions with arguments, if any
            f(*args, **kwargs)
  
    # returning the reference of inner_combined_func
    # this reference will have the called result of all
    # the functions that are passed to the combined_funcs
    return inner_combined_func

def save_state():
    with open("checkbox_state.txt", "w") as file:
        file.write(str(var.get()))
def save_state2():
    with open("checkbox_state.txt", "w") as file:
        file.write(str(var.get()))
        root.destroy

def load_state():
    try:
        with open("checkbox_state.txt", "r") as file:
            state = file.read().strip()
            if state == "True":
                var.set(True)
            else:
                var.set(False)
    except:
        pass

titlebar = Frame(root, bg='#31333D', relief='raised', bd=0, highlightthickness=6, highlightbackground='#31333D')
titlebar.pack(fill=X)
titlebartitle = Label(root, text='Malware', bg='#31333D',bd=0,fg='#808080', font=('helvetica', 10), highlightthickness=0)
titlebartitle.place(y=5, x=9)
titlebartitle = Label(titlebar, bg='#31333D',bd=0,fg='#808080', font=('helvetica', 8, 'bold'), highlightthickness=0)
titlebartitle.pack(side=TOP, padx=10)
closebutton = Button(root, text='  ×  ', command=combine_funcs(save_state, root.destroy), bg='#31333D',font=("calibri", 10, 'bold'),bd=0,fg='#808080',highlightthickness=0, width=5)
closebutton.place(y=4, x=507)

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

con = pymysql.connect(host='192.169.144.133', user='santucci', password='mcctcrocks', database='carter_santucci')

def loginT():
    if loglicense.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            mycur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue\n              Try Again')
            return
        
        global loglicenseinfo
        loglicenseinfo = loglicense.get()
        result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=18644, \
                    key=f'{loglicenseinfo}',\
                    machine_code=Helpers.GetMachineCode())
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            messagebox.showerror('Error', 'Invalid or Expired License Key')
        else:   
            try:
                query = 'use carter_santucci'
                mycur.execute(query)
                query= 'select * from customer where licensekey=%s'
                mycur.execute(query, (loglicense.get()))
                row = mycur.fetchone()
                if row == None:
                    messagebox.showerror('Error', 'Invalid or Expired License Key')
                else:
                    for widget in frame.winfo_children():
                        widget.destroy()
                    # save_state()
                    mainpage()
            except:
                messagebox.showerror('Error', 'License Key not Registered')

def signup():
    if regusername.get() == '' or regpassword.get() == '' or reglicense.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            mycur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue\n              Try Again')
            return
        
        global reglicenseinfo
        reglicenseinfo = reglicense.get()
        result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=18644, \
                    key=f'{reglicenseinfo}',\
                    machine_code=Helpers.GetMachineCode())
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            messagebox.showerror('Error', 'Invalid or Expired License Key')
        else:
            mycur.execute('use carter_santucci')
            
            query = 'select * from customer where username=%s'
            mycur.execute(query,(regusername.get()))
            row = mycur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'Username Already Exists')
                return
            query = 'select * from customer where licensekey=%s'
            mycur.execute(query,(reglicense.get()))
            row = mycur.fetchone()
            if row != None:
                messagebox.showerror('Error', 'License Key Already in Use')
                return
            else:
                query = 'insert into customer(username,password,licensekey) values(%s,%s,%s)'
                mycur.execute(query, (regusername.get(), regpassword.get(), reglicense.get()))
                con.commit()
                con.close()
                loginBclick()
                
def upgrade():
    if upusername.get() == '' or uppassword.get() == '' or upnewlicense.get() == '':
        messagebox.showerror('Error', 'All Fields are Required')
    else:
        try:
            mycur = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue\n              Try Again')
            return
        
        global upnewlicenseinfo
        global upusernameinfo
        upusernameinfo = upusername.get()
        upnewlicenseinfo = upnewlicense.get()
        result = Key.activate(token=auth,\
                    rsa_pub_key=RSAPubKey,\
                    product_id=18644, \
                    key=f'{upnewlicenseinfo}',\
                    machine_code=Helpers.GetMachineCode())
        if result[0] == None or not Helpers.IsOnRightMachine(result[0]):
            # an error occurred or the key is invalid or it cannot be activated
            # (eg. the limit of activated devices was achieved)
            messagebox.showerror('Error', 'Invalid or Expired License Key')
        else:
            mycur.execute('use carter_santucci')

            try:
                query = 'select * from customer where licensekey=%s'
                mycur.execute(query,(upnewlicense.get()))
                row = mycur.fetchone()
                if row != None:
                    messagebox.showerror('Error', 'License Key Already in Use')
                    return
                query = 'select * from customer where username=%s'
                mycur.execute(query,(upusername.get()))
                row = mycur.fetchone()
                if row != None:
                    query = f"update customer set licensekey = '{upnewlicense.get()}' where username = '{upusername.get()}'"
                    mycur.execute(query)
                    con.commit()
                    con.close()
                    loginBclick()
                else:
                    messagebox.showerror('Error', 'User not Found')
            except:
                messagebox.showerror('Error', 'User not Found')


def oldsignup():
    # global regusernameinfo
    # global reglicenseinfo
    regusernameinfo = regusername.get()
    regpasswordinfo = regpassword.get()
    reglicenseinfo = reglicense.get()
    result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=18644, \
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
                   product_id=18644, \
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

var = ctk.BooleanVar()

def loginBclick():
    for widget in frame.winfo_children():
        widget.destroy()
    loginpage() 
def registerclick():
    for widget in frame.winfo_children():
        widget.destroy()
    registerpage()
def upgradeclick():
    for widget in frame.winfo_children():
        widget.destroy()
    upgradepage()
    
def loginpage():
    ctk.CTkLabel(master=frame, text='', text_font=('Arial Black', 30), text_color='#757BC1').place(y=0, x=85) # label
    
    # global logusername
    # logusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35)
    # logusername.place(y=115, x=235)

    # global logpassword
    # logpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), width=230, height=35)
    # logpassword.place(y=165, x=235)
        
    global loglicense
    loglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), show='•', width=265, height=40, border_color='#757BC1', fg_color='#1D1E24',  border_width=1)
    loglicense.place(y=105, x=120)
    
    # mydiscord = ctk.CTkLabel(master=frame, text='Discord: cheerios#6071', text_font=('Arial', 10), text_color='white')
    # mydiscord.place(y=220, x=205)
    
    ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=92, height=40).place(y=105, x=348)  # login top
    
    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=210, x=71)  # login bottom

    ctk.CTkButton(master=frame, text=' Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=209.49999999999995)   # register bottom
                
    ctk.CTkButton(master=frame, text=' Upgrade', text_font=('Arial Black', 10, 'bold'), command=upgradeclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=348)    # upgrade bottom

    
    # LoginTbutton = ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=35)
    # LoginTbutton.place(y=165, x=385)
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40).place(y=105, x=348)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=105, x=348)    # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=144, x=348)    # fix out bottom

    # framefixiner = tk.Frame(frame, background='#3D3D3D', width=7, height=34)
    # framefixiner.place(y=165, x=385)
    
    # framefixoutT = tk.Frame(frame, background='#525252', width=8, height=2)
    # framefixoutT.place(y=165, x=384)
    
    # framefixoutB = tk.Frame(frame, background='#525252', width=8, height=2)
    # framefixoutB.place(y=197, x=384)

    global remme
    remme = ctk.CTkCheckBox(master=frame, text='Remember me', fg_color='#757BC1', width=20, height=20, variable=var, border_width=1.5, border_color='#757BC1')
    remme.place(y=160, x=120)
        
    root.mainloop()

def registerpage():
    ctk.CTkLabel(master=frame, text='', text_font=('Arial Black', 30), text_color='#757BC1').place(y=0, x=145) # label
    
    global regusername
    regusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=33, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    regusername.place(y=72, x=160)
    
    global regpassword
    regpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='•', width=230, height=33, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    regpassword.place(y=113, x=160)
    
    global reglicense
    reglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=265, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    reglicense.place(y=155, x=120)
    
    ctk.CTkButton(master=frame, text='  Signup', command=signup, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=92, height=40, border_color='#757BC1').place(y=155, x=348)    # sign up
    
    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=71)    # login bottom
    
    ctk.CTkButton(master=frame, text=' Register', text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=210, x=209.49999999999995)     # register bottom
    
    ctk.CTkButton(master=frame, text=' Upgrade', text_font=('Arial Black', 10, 'bold'), command=upgradeclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=348)    # upgrade bottom
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40,).place(y=155, x=348)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=155, x=348)     # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=194, x=348)    # fix out bottom

    root.mainloop()
    
def upgradepage():
    ctk.CTkLabel(master=frame, text='', text_font=('Arial Black', 30), text_color='#757BC1').place(y=0, x=85) # label

    global upusername
    upusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=33, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    upusername.place(y=72, x=160)
    
    global uppassword
    uppassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='•', width=230, height=33, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    uppassword.place(y=113, x=160)
    
    global upnewlicense
    upnewlicense = ctk.CTkEntry(master=frame, placeholder_text='New License Key', text_font=('Arial', 10), width=265, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    upnewlicense.place(y=155, x=120)
    
    ctk.CTkButton(master=frame, text='  Upgrade', command=upgrade, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=92, height=40, border_color='#757BC1').place(y=155, x=348)    # upgrade

    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=71)    # login bottom
    
    ctk.CTkButton(master=frame, text=' Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=210, x=209.49999999999995)     # register bottom
    
    ctk.CTkButton(master=frame, text='Upgrade', text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=210, x=348)    # upgrade bottom

    tk.Frame(frame, background='#1D1E24', width=7, height=40,).place(y=155, x=348)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=155, x=348)     # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=194, x=348)    # fix out bottom

def mainpage():
    # regusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    # reglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=290, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    # regusernameinfo = regusername.get()
    # reglicenseinfo = reglicense.get()
    
    ctk.CTkButton(master=frame, text='TEST', text_font=('Arial Black', 9), text_color='white', fg_color='#1D1E24', command=loginBclick, width=100, height=30).place(y=75, x=200) # label

    root.mainloop()

load_state()
root.protocol("WM_DELETE_WINDOW", save_state)

loginpage()