#.withdraw() -> Hide/Unvisible
#.deiconify() -> Show/Visible
#con = connect('MasterDataBase.db')
#cur = con.cursor()
#con.close()

from tkinter import *
from sqlite3 import *



### EASY MAKER OF LABLES AND BUTTONS ###
def make_label(master, x, y, w, h, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.place(x=x, y=y)
    label = Label(f, *args, **kwargs)
    label.pack(fill=BOTH, expand=1)
    return label

def make_button(master, x, y, w, h, *args, **kwargs):
    f = Frame(master, height=h, width=w)
    f.pack_propagate(0)
    f.place(x=x, y=y)
    button = Button(f, *args, **kwargs)
    button.pack(fill=BOTH, expand=1)
    return button



### SETS UP ALL SCREENS ###
def ScreenSetup():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot

    #HOME SCREEN
    homeroot.geometry('600x400+0+0')
    homeroot.resizable(False, False)
    homeroot.title("Notenrechner")
    make_label(homeroot, 115, 111, 370, 75, text="Notenrechner", font=("DIN Alternate", 64))
    make_button(homeroot, 170, 209, 260, 30, text="Noten", command=NotenScreen)
    make_button(homeroot, 170, 261, 260, 30, text="Gesamt", command=GesamtScreen)

    #NOTEN SCREEN
    notenroot.geometry('600x400+0+0')
    notenroot.resizable(False, False)
    notenroot.title("Noten")
    make_button(notenroot, 170, 261, 260, 30, text="Gesamt", command=HomeScreen)

    #NEUE NOTE SCREEN
    neuroot.geometry('600x400+0+0')
    neuroot.resizable(False, False)
    neuroot.title("Neue Note")

    #GESAMT SCREEN
    gesamtroot.geometry('600x400+0+0')
    gesamtroot.resizable(False, False)
    gesamtroot.title("Übersicht")

    #DETAIL SCREEN
    detailroot.geometry('600x400+0+0')
    detailroot.resizable(False, False)
    detailroot.title("Details")



### INITIAL START UP ###
def StartUp():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    
    root = Tk()
    root.withdraw()
    
    menubar = Menu(root)
    root.config(menu=menubar)
    
    rechner_menu = Menu(menubar, tearoff=0)
    noten_menu = Menu(menubar, tearoff=0)
    gesamt_menu = Menu(menubar, tearoff=0)
    sub_fach_menu = Menu(noten_menu, tearoff=0)
    
    rechner_menu.add_command(label="Start", command=HomeScreen)
    rechner_menu.add_command(label="Exit", command=root.destroy)
    noten_menu.add_cascade(label="Fächer", menu=sub_fach_menu)
    noten_menu.add_command(label="Neue Note", command=NeueNoteScreen)
    gesamt_menu.add_command(label="Übersicht", command=GesamtScreen)
    gesamt_menu.add_command(label="Details", command=DetailScreen)
    sub_fach_menu.add_command(label="Wirtschaft")
    sub_fach_menu.add_command(label="Englisch")
    sub_fach_menu.add_command(label="Mathe")
    sub_fach_menu.add_command(label="Deutsch")
    sub_fach_menu.add_command(label="Biologie")
    sub_fach_menu.add_command(label="Phyisk")
    sub_fach_menu.add_command(label="Geschichte")
    sub_fach_menu.add_command(label="Gemeinschaftskunde")
    sub_fach_menu.add_command(label="Geographie")
    sub_fach_menu.add_command(label="Ethik")
    sub_fach_menu.add_command(label="Bildende Kunst")
    sub_fach_menu.add_command(label="Sport")
    sub_fach_menu.add_command(label="Seminarkurs")
    sub_fach_menu.add_command(label="Informatik")
    menubar.add_cascade(label="Notenrechner", menu=rechner_menu)
    menubar.add_cascade(label="Noten", menu=noten_menu)
    menubar.add_cascade(label="Gesamt", menu=gesamt_menu)
    
    homeroot = Toplevel()
    notenroot = Toplevel()
    gesamtroot = Toplevel()
    detailroot = Toplevel()
    neuroot = Toplevel()

    ScreenSetup()
    HomeScreen()



### CALL SCREENS FUNCTIONS ###
def HomeScreen():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    notenroot.withdraw()
    gesamtroot.withdraw()
    detailroot.withdraw()
    neuroot.withdraw()
    homeroot.deiconify()

def NotenScreen():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    homeroot.withdraw()
    gesamtroot.withdraw()
    detailroot.withdraw()
    neuroot.withdraw()
    notenroot.deiconify()

def NeueNoteScreen():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    homeroot.withdraw()
    notenroot.withdraw()
    detailroot.withdraw()
    gesamtroot.withdraw()
    neuroot.deiconify()

def GesamtScreen():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    homeroot.withdraw()
    notenroot.withdraw()
    detailroot.withdraw()
    neuroot.withdraw()
    gesamtroot.deiconify()


def DetailScreen():
    global homeroot, notenroot, gesamtroot, detailroot, neuroot
    homeroot.withdraw()
    notenroot.withdraw()
    gesamtroot.withdraw()
    neuroot.withdraw()
    detailroot.deiconify()

### END OF FUNCTIONS ###

StartUp()
