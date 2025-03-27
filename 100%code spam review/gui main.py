

from tkinter import *
import tkinter as tk


from PIL import Image ,ImageTk

from tkinter.ttk import *
from pymsgbox import *


root=tk.Tk()

root.title("Spam Review Detection ")
w,h = root.winfo_screenwidth(),root.winfo_screenheight()

bg = Image.open(r"y9.png")
bg.resize((1200,300),Image.LANCZOS)
print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root,image=bg_img)
bg_lbl.place(x=0,y=93)
#, relwidth=1, relheight=1)

w = tk.Label(root, text="Spam Review Detection ",width=40,background="#212F3D",foreground="white",height=2,font=("Times new roman",19,"bold"))
w.place(x=0,y=15)



w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#212F3D")


from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login1.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])
    
def Contact():
    from subprocess import call
    call(["python","spam contact_us.py"])
        
def AboutUs():
    from subprocess import call
    call(["python","spam About Us.py"])


wlcm=tk.Label(root,text="......Welcome to Spam Review Detection System ......",width=95,height=3,background="#212F3D",foreground="white",font=("Times new roman",22,"bold"))
wlcm.place(x=0,y=620)




d2=tk.Button(root,text="Login",command=Login,width=9,height=2,bd=0,background="#6699ff",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=800,y=18)


d3=tk.Button(root,text="Register",command=Register,width=9,height=2,bd=0,background="#6699ff",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=950,y=18)

d2=tk.Button(root,text="Contact",command=Contact,width=9,height=2,bd=0,background="#6699ff",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1100,y=18)

d2=tk.Button(root,text="About Us",command=AboutUs ,width=9,height=2,bd=0,background="#6699ff",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1250,y=18)

root.mainloop()
