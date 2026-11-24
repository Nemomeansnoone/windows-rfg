import tkinter as tk
from tkinter import ttk
from PIL import Image
from PIL import ImageTk
import pygame

import os
import random
import time
from time import strftime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

THEME_BG = "#3A6EA5"
THEME_FG = "#1a1a1a"
THEME_ACCENT = "#2a7de1"
THEME_ACCENT_FG = "#ffffff"
THEME_FIELD_BG = "#ffffff"
THEME_FONT = ("Helvetica", 10)

startmenuopen = False

def mycomputer():
    for widget in main_frame.winfo_children():
        widget.destroy()

def mydocuments():
    for widget in main_frame.winfo_children():
        widget.destroy()

def recyclebin():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openwmplayer():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openword():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openupdate():
    for widget in main_frame.winfo_children():
        widget.destroy()

def opencrash():
    for widget in main_frame.winfo_children():
        widget.destroy()

def opensolitaire():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openfood():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openie():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openpaint():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openhelp():
    for widget in main_frame.winfo_children():
        widget.destroy()

def reboot():
    for widget in main_frame.winfo_children():
        widget.destroy()
    

def shutdown():
    for widget in main_frame.winfo_children():
        widget.destroy()

def openstart():
    global startmenu
    global startmenuopen
    startmenuopen = True
    startmenu = tk.Frame(root, bg="#D4D0C8")
    startmenu.place(x=0, y=70, width=240, height=300)
    startrfgimgpath = os.path.join(BASE_DIR, "assets", "startrfg.png")
    startmenu.startrfg_img = ImageTk.PhotoImage(Image.open(startrfgimgpath).resize((40, 300)))
    startmenurfg = tk.Label(startmenu, image=startmenu.startrfg_img, bg="#D4D0C8")
    startmenurfg.place(x=0, y=0, width=40, height=300)
    wordbtn = tk.Button(startmenu, text="Word", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openword and startmenu.destroy)
    wordbtn.place(x=40, y=0, width=200, height=30)
    updatebtn = tk.Button(startmenu, text="Windows Update", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openupdate and startmenu.destroy)
    updatebtn.place(x=40, y=30, width=200, height=30)
    crashbtn = tk.Button(startmenu, text="Crash", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=opencrash and startmenu.destroy)
    crashbtn.place(x=40, y=60, width=200, height=30)
    solitairebtn = tk.Button(startmenu, text="Solitaire", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=opensolitaire and startmenu.destroy)
    solitairebtn.place(x=40, y=90, width=200, height=30)
    foodbtn = tk.Button(startmenu, text="Order Food", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openfood and startmenu.destroy)
    foodbtn.place(x=40, y=120, width=200, height=30)
    iebtn = tk.Button(startmenu, text="Go Online", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openie and startmenu.destroy)
    iebtn.place(x=40, y=150, width=200, height=30)
    paintbtn = tk.Button(startmenu, text="Paint", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openpaint and startmenu.destroy)
    paintbtn.place(x=40, y=180, width=200, height=30)
    helpbtn = tk.Button(startmenu, text="Help", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=openhelp and startmenu.destroy)
    helpbtn.place(x=40, y=210, width=200, height=30)
    rebootbtn = tk.Button(startmenu, text="Reboot", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=reboot and startmenu.destroy)
    rebootbtn.place(x=40, y=240, width=200, height=30)
    shutdownbtn = tk.Button(startmenu, text="Shut Down", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT, command=shutdown and startmenu.destroy)
    shutdownbtn.place(x=40, y=270, width=200, height=30)
    root.update()
    root.after(5000, startmenu.destroy)

def closestart():
    global startmenu
    global startmenuopen
    startmenu.destroy()
    startmenuopen = False

def startbutton():
    if startmenuopen == False:
        openstart()
    else:
        closestart()

def troll1():
    pixel = tk.PhotoImage(width=1, height=1)
    errorsoundpath = os.path.join(BASE_DIR, "assets", "error.mp3")
    pygame.mixer.music.load(errorsoundpath)
    pygame.mixer.music.play(loops=0)
    trollwindow1 = tk.Frame(main_frame, bg="#D4D0C8", relief="raised")
    trollwindow1.place(x=210, y=135, width=180, height=130)
    trollblue1 = tk.Frame(trollwindow1, bg="#2a7de1", relief="raised")
    trollblue1.place(x=0, y=0, width=180, height=20)
    closebutton1 = tk.Button(trollblue1, text="X", image=pixel, bg="#D4D0C8", command=trollwindow1.destroy)
    closebutton1.place(x=161, y=1, width=18, height=18)
    markpath = os.path.join(BASE_DIR, "assets", "mark.png")
    trollwindow1.mark1_img = ImageTk.PhotoImage(Image.open(markpath).resize((40,40)))
    mark1img = tk.Label(trollwindow1, image=trollwindow1.mark1_img)
    mark1img.place(x=10, y=40, width=40, height=40)
    trolltext1 = tk.Label(trollwindow1, text="Required dll: windows.dll has been found. so windows has deleted it.", fg="#1a1a1a", bg="#D4D0C8", font=THEME_FONT)
    trolltext1.place(x=60, y=35, width=110, height=60)
    okbutton1 = tk.Button(trollwindow1, text="OK", image=pixel, fg="#1a1a1a", bg="#D4D0C8", command=trollwindow1.destroy)
    okbutton1.place(x=55, y=100, width=70, height=20)
    closebutton1.image = pixel
    okbutton1.image = pixel

def loadscreen1():
    global clock
    for widget in main_frame.winfo_children():
        widget.destroy()
    for widget in taskbar.winfo_children():
        widget.destroy()

    bootsoundpath = os.path.join(BASE_DIR, "assets", "boot.mp3")
    pygame.mixer.music.load(bootsoundpath)
    pygame.mixer.music.play(loops=0)
    startbtnimagepath = os.path.join(BASE_DIR, "assets", "startbutton.png")
    taskbar.startbtn_img = ImageTk.PhotoImage(Image.open(startbtnimagepath).resize((100, 20)))
    startbtn = tk.Button(taskbar, image=taskbar.startbtn_img, bg="#D4D0C8", command=startbutton)
    startbtn.place(x=10, y=5, width=100, height=20)
    clock = tk.Label(taskbar, text="6:39 PM", fg=THEME_FG, bg="#D4D0C8")
    clock.place(x=500, y=2, width=90, height=26)

    mycptimgpath = os.path.join(BASE_DIR, "assets", "mycomputer.png")
    main_frame.mycpt_img = ImageTk.PhotoImage(Image.open(mycptimgpath).resize((50, 50)))
    mycpt = tk.Button(main_frame, image=main_frame.mycpt_img, bg=THEME_FG, command=mycomputer)
    mycpt.place(x=10, y=10, width=50, height=50)

    mydocsimgpath = os.path.join(BASE_DIR, "assets", "mydocuments.png")
    main_frame.mydocs_img = ImageTk.PhotoImage(Image.open(mydocsimgpath).resize((50, 50)))
    mydocs = tk.Button(main_frame, image=main_frame.mydocs_img, bg=THEME_FG, command=mydocuments)
    mydocs.place(x=10, y=70, width=50, height=50)

    recycleimgpath = os.path.join(BASE_DIR, "assets", "recyclebin.png")
    main_frame.recycle_img = ImageTk.PhotoImage(Image.open(recycleimgpath).resize((50, 50)))
    recycle = tk.Button(main_frame, image=main_frame.recycle_img, bg=THEME_FG, command=recyclebin)
    recycle.place(x=10, y=130, width=50, height=50)

    wmpimgpath = os.path.join(BASE_DIR, "assets", "wmp.png")
    main_frame.wmp_img = ImageTk.PhotoImage(Image.open(wmpimgpath).resize((50, 50)))
    wmp = tk.Button(main_frame, image=main_frame.wmp_img, bg=THEME_BG, command=openwmplayer)
    wmp.place(x=10, y=190, width=50, height=50)

    updatetime()
    root.update()
    root.after(6000, troll1)

def updatetime():
    global clock
    currenttime = strftime('%I:%M %p')
    clock.config(text=currenttime)
    clock.after(60000, updatetime)

def boot():
    for widget in main_frame.winfo_children():
        widget.destroy()
    for widget in taskbar.winfo_children():
        widget.destroy()
    bootsplashpath = os.path.join(BASE_DIR, "assets", "bootsplash.png")
    root.bootsplash_img = ImageTk.PhotoImage(Image.open(bootsplashpath).resize((600,400)))
    bootsplash = tk.Label(main_frame, image=root.bootsplash_img)
    bootsplash.place(x=0, y=0, width=600, height=400)
    root.update()
    root.after(3000, loadscreen1)

root = tk.Tk()
root.geometry("600x400")
root.title("Windows RFG")
root.configure(bg=THEME_BG)
root.option_add("*background", THEME_BG)
root.option_add("*foreground", THEME_FG)
root.option_add("*font", THEME_FONT)
root.option_add("*Entry.background", THEME_FIELD_BG)
root.option_add("*Text.background", THEME_FIELD_BG)
root.option_add("*Listbox.background", THEME_FIELD_BG)
root.option_add("*Button.background", THEME_ACCENT)
root.option_add("*Button.foreground", THEME_ACCENT_FG)
style = ttk.Style()
try:
    style.theme_use("clam")
except tk.TclError:
    pass
style.configure(".", background=THEME_BG, foreground=THEME_FG, font=THEME_FONT)
main_frame = tk.Frame(root, bg=THEME_BG)
main_frame.place(x=0, y=0, width=600, height=370)
taskbar = tk.Frame(root, bg="#D4D0C8")
taskbar.place(x=0, y=370, width=600, height=30)
pygame.mixer.init()
boot()
root.mainloop()
