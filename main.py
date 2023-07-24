import keyboard
import threading
import time
import json

from tkinter import messagebox
import tkinter as tk
import tkinter.font as tkFont

settings = {}
running = False
active = False
shortcut_assign = False
key_assign = False

def run():
    global settings, active
    key, speed = settings["key"], settings["speed"]
    if not str(speed).isdigit():
        messagebox.showerror("Reading error", "Error: 'speed' must be convertable to int!")
        return
    while True:
        if not running:
            break
        if active:
            keyboard.press(key)
            time.sleep(1.0 / int(speed) / 2)
            keyboard.release(key)
            time.sleep(1.0 / int(speed) / 2)

def hotkey_press():
    global active, running
    if running:
        active = not active
    else:
        active = False

def assign_new_shortcut(label_321, button_313, button_971, button_985):
    global settings, shortcut_assign
    shortcut = keyboard.read_key()
    if shortcut == settings["key"]:
        messagebox.showerror("Duplication Error", "Key and Shortcut cannot be the same!")
        shortcut_assign = False
        button_971.configure(bg="blue" if shortcut_assign else root.cget("background"))
        button_313.configure(state="disabled" if shortcut_assign else "normal")
        button_985.configure(state="disabled" if shortcut_assign else "normal")
        return
    settings["shortcut"] = shortcut
    with open("settings.json", "w") as file:
        file.write(json.dumps(settings))
    try:
        keyboard.unhook_all_hotkeys()
    except:
        pass
    keyboard.add_hotkey(shortcut, hotkey_press)
    shortcut_assign = False
    label_321.configure(text=settings["shortcut"])
    button_971.configure(bg="blue" if shortcut_assign else root.cget("background"))
    button_313.configure(state="disabled" if shortcut_assign else "normal")
    button_985.configure(state="disabled" if shortcut_assign else "normal")

def assign_new_key(label_545, button_313, button_971, button_985):
    global settings, key_assign
    key = keyboard.read_key()
    if key == settings["shortcut"]:
        messagebox.showerror("Key and Shortcut cannot be the same!")
        key_assign = False
        button_985.configure(bg="blue" if key_assign else root.cget("background"))
        button_313.configure(state="disabled" if key_assign else "normal")
        button_971.configure(state="disabled" if key_assign else "normal")
        return
    settings["key"] = key
    with open("settings.json", "w") as file:
        file.write(json.dumps(settings))
    key_assign = False
    label_545.configure(text=settings["key"])
    button_985.configure(bg="blue" if key_assign else root.cget("background"))
    button_313.configure(state="disabled" if key_assign else "normal")
    button_971.configure(state="disabled" if key_assign else "normal")

class App:
    def __init__(self, root):
        global settings
        #setting title
        root.title("Keyboard Auto Clicker")
        #setting window size
        width=310
        height=194
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_971=tk.Button(root)
        GButton_971["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_971["font"] = ft
        GButton_971["fg"] = "#000000"
        GButton_971["justify"] = "center"
        GButton_971["text"] = "Change"
        GButton_971.place(x=190,y=100,width=104,height=30)
        GButton_971["command"] = lambda: self.GButton_971_command(GButton_313, GButton_971, GButton_985, GLabel_330, GLabel_321, GLabel_545)

        GLabel_102=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_102["font"] = ft
        GLabel_102["fg"] = "#333333"
        GLabel_102["justify"] = "center"
        GLabel_102["text"] = "Shortcut: "
        GLabel_102.place(x=0,y=100,width=69,height=30)

        GLabel_545=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_545["font"] = ft
        GLabel_545["fg"] = "#333333"
        GLabel_545["justify"] = "center"
        GLabel_545["text"] = settings["shortcut"]
        GLabel_545.place(x=70,y=100,width=31,height=30)

        GButton_313=tk.Button(root)
        GButton_313["bg"] = "#ff0000"
        ft = tkFont.Font(family='Times',size=10)
        GButton_313["font"] = ft
        GButton_313["fg"] = "#0000ff"
        GButton_313["justify"] = "center"
        GButton_313["text"] = "ON / OFF"
        GButton_313.place(x=30,y=140,width=237,height=30)
        GButton_313["command"] = lambda: self.GButton_313_command(GButton_313, GButton_971, GButton_985)

        GButton_985=tk.Button(root)
        GButton_985["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_985["font"] = ft
        GButton_985["fg"] = "#000000"
        GButton_985["justify"] = "center"
        GButton_985["text"] = "Change"
        GButton_985.place(x=190,y=60,width=104,height=30)
        GButton_985["command"] = lambda: self.GButton_985_command(GButton_313, GButton_971, GButton_985, GLabel_330, GLabel_321, GLabel_545)

        GButton_601=tk.Button(root)
        GButton_601["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=20)
        GButton_601["font"] = ft
        GButton_601["fg"] = "#000000"
        GButton_601["justify"] = "center"
        GButton_601["text"] = "+"
        GButton_601.place(x=200,y=20,width=34,height=30)
        GButton_601["command"] = lambda: self.GButton_601_command(GLabel_330)

        GButton_711=tk.Button(root)
        GButton_711["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=20)
        GButton_711["font"] = ft
        GButton_711["fg"] = "#000000"
        GButton_711["justify"] = "center"
        GButton_711["text"] = "-"
        GButton_711.place(x=250,y=20,width=38,height=30)
        GButton_711["command"] = lambda: self.GButton_711_command(GLabel_330)

        GLabel_819=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_819["font"] = ft
        GLabel_819["fg"] = "#333333"
        GLabel_819["justify"] = "center"
        GLabel_819["text"] = "Speed: "
        GLabel_819.place(x=0,y=20,width=51,height=30)

        GLabel_330=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_330["font"] = ft
        GLabel_330["fg"] = "#333333"
        GLabel_330["justify"] = "center"
        GLabel_330["text"] = f"{settings['speed']} cps"
        GLabel_330.place(x=70,y=20,width=70,height=30)

        GLabel_567=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_567["font"] = ft
        GLabel_567["fg"] = "#333333"
        GLabel_567["justify"] = "center"
        GLabel_567["text"] = "Key:"
        GLabel_567.place(x=0,y=60,width=38,height=30)

        GLabel_321=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_321["font"] = ft
        GLabel_321["fg"] = "#333333"
        GLabel_321["justify"] = "center"
        GLabel_321["text"] = settings["key"]
        GLabel_321.place(x=40,y=60,width=61,height=30)

    def GButton_971_command(self, button_313, button_971, button_985, label_330, label_321, label_545):
        global shortcut_assign
        shortcut_assign = not shortcut_assign
        button_971.configure(bg="blue" if shortcut_assign else root.cget("background"))
        button_313.configure(state="disabled" if shortcut_assign else "normal")
        button_985.configure(state="disabled" if shortcut_assign else "normal")
        if shortcut_assign:
            assigner = threading.Thread(target=assign_new_shortcut, args=[label_545, button_313, button_971, button_985])
            assigner.start()


    def GButton_313_command(self, button_313, button_971, button_985):
        global running, settings
        try:
            keyboard.unhook_all_hotkeys()
        except:
            pass
        keyboard.add_hotkey(settings["shortcut"], hotkey_press)
        running = not running
        button_313.configure(bg="green" if running else "red")
        button_971.configure(state="disabled" if running else "normal")
        button_985.configure(state="disabled" if running else "normal")
        if running:
            runner = threading.Thread(target=run)
            runner.start()


    def GButton_985_command(self, button_313, button_971, button_985, label_330, label_321, label_545):
        global key_assign
        key_assign = not key_assign
        button_985.configure(bg="blue" if key_assign else root.cget("background"))
        button_313.configure(state="disabled" if key_assign else "normal")
        button_971.configure(state="disabled" if key_assign else "normal")
        if key_assign:
            assigner = threading.Thread(target=assign_new_key, args=[label_321, button_313, button_971, button_985])
            assigner.start()


    def GButton_601_command(self, label_330):
        try:
            speed = int(settings["speed"])
        except Exception as e:
            messagebox.showerror("Conversion error", "Error while converting from \n'settings.json > speed' to integer!")
        else:
            if speed <= 10000:
                speed += 1
            settings["speed"] = speed
            with open("settings.json", "w") as file:
                file.write(json.dumps(settings))
            label_330.configure(text=f"{speed} cps")

    def GButton_711_command(self, label_330):
        try:
            speed = int(settings["speed"])
        except Exception as e:
            messagebox.showerror("Conversion error", "Error while converting from \n'settings.json > speed' to integer!")
        else:
            if speed > 1:
                speed -= 1
            settings["speed"] = speed
            with open("settings.json", "w") as file:
                file.write(json.dumps(settings))
            label_330.configure(text=f"{speed} cps")

if __name__ == "__main__":
    settings = json.load(open("settings.json", "r"))
    root = tk.Tk()
    app = App(root)
    root.mainloop()
    running = False
    shortcut_assign = False
    key_assign = False
