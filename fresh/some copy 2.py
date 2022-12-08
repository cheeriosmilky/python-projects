import customtkinter as ctk
import tkinter as tk
from tkinter import *
from licensing.models import *
from licensing.methods import Key, Helpers
import os

#python -m PyInstaller --onefile --windowed --add-data "C:/Users/cheer/AppData/Roaming/Python/Python310/site-packages/customtkinter;customtkinter/"  "C:/py/home/fresh/some.py" 

RSAPubKey = "<RSAKeyValue><Modulus>xnTzcz52AZRQ0GRKhHOQ0k8mS2FcgyyWPFD8Ro21uluBLZNaH/ewQGhj8dnXMnJ0HAoaItiGY/BvpHto2FSpypYPNMxXGZC3Go+lswVYPnyfRH76ro5/k0jHRrMLQdErR1BiCJDzUWGhbJIXkoXTj7YnVyGHCbcUC/xuNifGRFhj/SnSg/chpw27DYKVbeC2SzN4q9XvtTqdPKH3AVuC7M5FjjhsSb4+dtwHyqLbGeW8elCPs5bf25tOvQFmWoWK+v3MF/np0Ig+BzTZP5E6hWbSVCGk3kK9yPpQXlEB9dVm3x9oNhwvpl6gHYLjCXaBA5bjUgzdIL00dS/6x0INwQ==</Modulus><Exponent>AQAB</Exponent></RSAKeyValue>"
auth = "WyIzMDg4ODQyNCIsImIvUnJuQVVyaWVHamJMV0pTeG1RRlJXVGhsQVVyc21HUFdYb1lWNXQiXQ=="

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
wwidth=700
wheight=350
swidth = root.winfo_screenwidth()
sheight = root.winfo_screenheight()
xaxis = (swidth/2) - (wwidth/2)
yaxis = (sheight/2) - (wheight/2)
root.geometry("{}x{}+{}+{}".format(wwidth, wheight, int(xaxis), int(yaxis)))
root.resizable(0, 0)
root.iconbitmap('.\\feetpics\\yea.ico')
root.title('Glactic')

frame = ctk.CTkFrame(master=root, fg_color='#1D1E24', bg_color='#1D1E24')
frame.pack(pady=0, padx=0, fill='both', expand=True)

def signuppopup():
        popup = Toplevel(master=root, bg='#1D1E24')
        popup.title('Error')
        popup.geometry('200x150')
        popup.resizable(0, 0)
        ctk.CTkLabel(master=popup, text='Make sure to Signup First', text_color='white').place(y=40, x=30)
        ctk.CTkButton(master=popup, text='Ok',fg_color='#757BC1', width=20, height=10, command=popup.destroy).place(y=70, x=80)
        popup.mainloop()
        
def invalidpopup():
        popup = Toplevel(master=root, bg='#1D1E24')
        popup.title('Error')
        popup.geometry('200x150')
        popup.resizable(0, 0)
        label = ctk.CTkLabel(master=popup, text='Invalid or Expired key', text_color='white')
        okbutton = ctk.CTkButton(master=popup, text='Ok',fg_color='#757BC1', width=20, height=10, command=popup.destroy)
        label.place(y=40, x=30)
        okbutton.place(y=70, x=80)
        popup.mainloop()
        
def signup():
    global regusernameinfo
    global reglicenseinfo
    regusernameinfo = regusername.get()
    regpasswordinfo = regpassword.get()
    reglicenseinfo = reglicense.get()
    result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=17706, \
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
        
def loginT():
    loglicenseinfo = loglicense.get()
    result = Key.activate(token=auth,\
                   rsa_pub_key=RSAPubKey,\
                   product_id=17706, \
                   key=f'{loglicenseinfo}',\
                   machine_code=Helpers.GetMachineCode(v=2))
    if result[0] == None or not Helpers.IsOnRightMachine(result[0], v=2):
        # an error occurred or the key is invalid or it cannot be activated
        # (eg. the limit of activated devices was achieved)
        invalidpopup()
    else:
        # everything went fine if we are here!
        print("The license is valid!")
        
        license1 = loglicense.get()
        
        list_of_files = os.listdir()
        if license1 in list_of_files:
            file1 = open(f'{loglicenseinfo}', 'r')
            verify = file1.read().splitlines()
            if license1 in verify:
                print('log suc')
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
    ctk.CTkLabel(master=frame, text='Glactic', text_font=('Arial Black', 45), text_color='#757BC1').place(y=25, x=230) # label
    
    global regusername
    regusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35, fg_color='#1D1E24', border_color='#757BC1', border_width=1)
    regusername.place(y=115, x=235)
    
    global regpassword
    regpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), show='•', width=230, height=35, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    regpassword.place(y=165, x=235)
    
    global reglicense
    reglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), width=290, height=40, border_color='#757BC1', fg_color='#1D1E24', border_width=1)
    reglicense.place(y=215, x=205)
    
    ctk.CTkButton(master=frame, text='  Signup', command=signup, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=40, border_color='#757BC1').place(y=215, x=415)    # sign up
    
    ctk.CTkButton(master=frame, text='Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=265, x=365)    # register bottom

    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=265, x=205)     # login bottom
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40,).place(y=215, x=415)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=215, x=414)     # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=254, x=414)    # fix out bottom

    root.mainloop()

def loginpage():
    ctk.CTkLabel(master=frame, text='Glactic', text_font=('Arial Black', 45), text_color='#757BC1').place(y=25, x=230) # label
    
    # global logusername
    # logusername = ctk.CTkEntry(master=frame, placeholder_text='Username', text_font=('Arial', 10), bg_color='#1D1E24', width=230, height=35)
    # logusername.place(y=115, x=235)

    # global logpassword
    # logpassword = ctk.CTkEntry(master=frame, placeholder_text='Password', text_font=('Arial', 10), width=230, height=35)
    # logpassword.place(y=165, x=235)
    
    ctk.CTkButton(master=frame, text='Register', text_font=('Arial Black', 10, 'bold'), command=registerclick, bg_color='#1D1E24', fg_color='#1D1E24', width=130, height=45).place(y=265, x=365)   # register bottom
    
    global loglicense
    loglicense = ctk.CTkEntry(master=frame, placeholder_text='License Key', text_font=('Arial', 10), show='•', width=290, height=40, border_color='#757BC1', fg_color='#1D1E24',  border_width=1)
    loglicense.place(y=155, x=205)
    
    # mydiscord = ctk.CTkLabel(master=frame, text='Discord: cheerios#6071', text_font=('Arial', 10), text_color='white')
    # mydiscord.place(y=220, x=205)
    
    ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=40).place(y=155, x=415)  # login top
            
    ctk.CTkButton(master=frame, text='Login', text_font=('Arial Black', 10, 'bold'), command=loginBclick, bg_color='#1D1E24', fg_color='#757BC1', width=130, height=45).place(y=265, x=205) # login bottom
    
    # LoginTbutton = ctk.CTkButton(master=frame, text='  Login', command=loginT, text_font=('Arial Black', 10, 'bold'), bg_color='#1D1E24', fg_color='#757BC1', width=80, height=35)
    # LoginTbutton.place(y=165, x=385)
    
    tk.Frame(frame, background='#1D1E24', width=7, height=40).place(y=155, x=415)   # fix inner
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=155, x=414)    # fix out top
    
    tk.Frame(frame, background='#757BC1', width=8, height=1).place(y=194, x=414)    # fix out bottom

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
    
    ctk.CTkButton(master=frame, text='Sign Out', text_font=('Arial Black', 9), text_color='white', fg_color='#1D1E24', command=loginBclick, width=12, height=6).place(y=15, x=600) # label

    
    root.mainloop()

loginpage()