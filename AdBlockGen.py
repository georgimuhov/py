import sys
from tkinter import *
from tkinter import ttk, messagebox
import os.path

# Main Window
mywin = Tk()
mywin.title("AdBlock Generator v0.1")
mywin.geometry("339x160")
mywin.eval('tk::PlaceWindow . center')
mywin.resizable(False, False)
mywin.attributes("-alpha", 0.91)
icon = os.path.join(sys.path[0], "pyicon.ico")
mywin.iconbitmap(icon)


def about():
    messagebox.showinfo("About", "Created by 6l4br10n!")


def info():
    messagebox.showinfo("Information", "Success!")


def generate():
    the_first_part = "@@||"
    the_second_part = "^$generichide"
    the_tird_part = "##script:inject(bab-defuser.js)"

    theSite = siteEingabe.get()
    generated_code.insert(INSERT, the_first_part + theSite + the_second_part + '\n')
    generated_code.insert(INSERT, theSite + the_tird_part)
    button1['state'] = 'disabled'


def copy_code():
    generated_code1 = generated_code.get("1.0", 'end-1c')
    mywin.clipboard_clear()
    mywin.clipboard_append(generated_code1)
    button2['state'] = 'disabled'


# Menu
menubar = Menu(mywin)
mywin.config(menu=menubar)
# Undermenu
file_menu = Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=mywin.destroy)

help_menu = Menu(menubar, tearoff=0)
help_menu.add_command(label="About", command=about)
# Hauptmenu
menubar.add_cascade(label="File", menu=file_menu)
menubar.add_cascade(label="Help", menu=help_menu)

# Labels 
inputLabel = ttk.Label(mywin, text="Website:", anchor="w")
inputLabel.place(x=10, y=11, width=200)

# TextBoxes
siteEingabe = ttk.Entry(mywin)
siteEingabe.place(x=70, y=12, width=125)

generated_code = Text(mywin)
generated_code.place(x=10, y=45, height=80, width=320)

# Buttons
button1 = ttk.Button(mywin, text="Generate", command=generate)
button1.place(x=200, y=10, width=70)
button1.bind("<ButtonRelease-1>")

button2 = ttk.Button(mywin, text="Copy", command=copy_code)
button2.place(x=270, y=10, width=60)
button2.bind("<ButtonRelease-1>")

mywin.mainloop()
