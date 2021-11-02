from tkinter import *
from sqlite3 import *

#########################################################

con = connect('MasterDataBase.db')
cur = con.cursor()

root = Tk()
root.withdraw()

homeroot = Toplevel()
notenroot = Toplevel()
neuroot = Toplevel()
gesamtroot = Toplevel()
detailroot = Toplevel()

#########################################################

subjects_list = ["Wirtschaft", "Englisch", "Mathe", "Deutsch", "Biologie",
                 "Physik", "Geschichte", "Gemeinschaftskunde", "Geographie",
                 "Ethik", "Bildende Kunst", "Sport", "Seminarkurs", "Informatik"]

semesters_list = ["Halbjahr I", "Halbjahr II", "Halbjahr III", "Halbjahr IV"]

points_list = [15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

types_list = ["schriftlich", "mündlich", "spezial"]

error_message = "Error - Eine oder mehrere Daten fehlen"

font_type = "DIN Alternate"

#########################################################

class Labelmaker:
    def __init__(self, master, x, y, w, h, size, **kwargs): 
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.label = Label(f, font=(font_type, size), **kwargs)
        self.label.pack(fill=BOTH, expand=1)
        
class Buttonmaker:
    def __init__(self, master, x, y, w, h, size, *args, **kwargs):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.button = Button(f, font=(font_type, size), *args, **kwargs)
        self.button.pack(fill=BOTH, expand=1)

class Optionmenumaker:
    def __init__(self, master, x, y, w, h, size, option_list, text, **kwarg):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.value_selected = StringVar(master)
        self.value_selected.set(text)
        self.question_menu = OptionMenu(f, self.value_selected, *option_list, **kwarg)
        self.question_menu.config(font=(font_type, size))
        self.styled_menu = root.nametowidget(self.question_menu.menuname)
        self.styled_menu.config(font=(font_type, size))
        self.question_menu.pack(fill=BOTH, expand=1)

    def set_value(self, value):
        self.value_selected.set(value)
        notenscreen_selected_fach()

class Screen:
    def __init__(self, master, text):
        self.master = master
        master.geometry('600x400+0+0')
        master.resizable(False, False)
        master.title(text)

    def hide(self):
        self.master.withdraw()

    def show(self):
        self.master.deiconify()

#########################################################

def menubar_initialisation():

    def submenu_fach(value):
        sub_fach_menu.add_command(label=subjects_list[value], command=lambda:submenu_fach_select(value))

    def submenu_fach_select(value):
        noten_subject_select.set_value(subjects_list[value])
        activate_notenscreen()

    menubar = Menu(root)
    root.config(menu=menubar)
    
    rechner_menu = Menu(menubar, tearoff=False)
    noten_menu = Menu(menubar, tearoff=False)
    gesamt_menu = Menu(menubar, tearoff=False)
    sub_fach_menu = Menu(noten_menu, tearoff=False)
    
    rechner_menu.add_command(label="Start", command=activate_homescreen)
    rechner_menu.add_separator()
    rechner_menu.add_command(label="Quit", command=root.destroy)
    
    noten_menu.add_cascade(label="Fächer", menu=sub_fach_menu)
    noten_menu.add_separator()
    noten_menu.add_command(label="Neue Note", command=activate_neuenotescreen)

    number_of_subjects = len(subjects_list)
    x=1

    while x < number_of_subjects:
        submenu_fach(x-1)
        x = x+1
    
    gesamt_menu.add_command(label="Übersicht", command=activate_gesamtscreen)
    gesamt_menu.add_separator()
    gesamt_menu.add_command(label="Details", command=activate_detailscreen)

    menubar.add_cascade(label="Notenrechner", menu=rechner_menu)
    menubar.add_cascade(label="Noten", menu=noten_menu)
    menubar.add_cascade(label="Gesamt", menu=gesamt_menu)

def command_notenscreen_selected_fach(event):
    notenscreen_selected_fach()
    
def notenscreen_selected_fach():
    Labelmaker(notenroot, 85, 34, 430, 40, 36, text=noten_subject_select.value_selected.get())

def fach_already_selected():
    selected_fach = noten_subject_select.value_selected.get()
    if selected_fach != "Fach auswählen":
        neue_note_subject_select.value_selected.set(selected_fach)
        activate_neuenotescreen()
    else:
        activate_neuenotescreen()
        

def neue_noten_values():
    subject_selected = neue_note_subject_select.value_selected.get()
    semester_selected = neue_note_semester_select.value_selected.get()
    points_selected = neue_note_points_select.value_selected.get()
    type_selected = neue_note_type_select.value_selected.get()
    if subject_selected == "Fach auswählen" or semester_selected == "Halbjahr auswählen" or points_selected == "Punkte auswählen" or type_selected == "Art auswählen":
        Labelmaker(neuroot, 171, 270, 260, 30, 14, text=error_message)
    else:
        
        activate_notenscreen()

def clear_error_message():
    Labelmaker(neuroot, 215, 270, 171, 30, 14, text="")

def activate_homescreen():
    HomeScreen.show()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    GesamtScreen.hide()
    DetailScreen.hide()

def activate_notenscreen():
    HomeScreen.hide()
    NotenScreen.show()
    NeueNoteScreen.hide()
    GesamtScreen.hide()
    DetailScreen.hide()

def activate_neuenotescreen():
    clear_error_message()
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.show()
    GesamtScreen.hide()
    DetailScreen.hide()

def activate_gesamtscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    GesamtScreen.show()
    DetailScreen.hide()

def activate_detailscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    GesamtScreen.hide()
    DetailScreen.show()

#########################################################

HomeScreen = Screen(homeroot, "Notenrechner")
NotenScreen = Screen(notenroot, "Noten")
NeueNoteScreen = Screen(neuroot, "Neue Note")
GesamtScreen = Screen(gesamtroot, "Übersicht")
DetailScreen = Screen(detailroot, "Details")

home_title = Labelmaker(homeroot, 115, 111, 370, 75, 64, text="Notenrechner")
home_button_noten = Buttonmaker(homeroot, 170, 208, 260, 30, 14, text="Noten", command=activate_notenscreen)
home_button_gesamt = Buttonmaker(homeroot, 170, 260, 260, 30, 14, text="Gesamt", command=activate_gesamtscreen)

noten_title = Labelmaker(notenroot, 85, 34, 430, 40, 36, text="Fach auswählen")
noten_subject_select = Optionmenumaker(notenroot, 86, 335, 171, 30, 14, subjects_list, text="Fach auswählen", command=command_notenscreen_selected_fach)
noten_button_neuenote = Buttonmaker(notenroot, 343, 335, 171, 30, 14, text="Neue Note", command=fach_already_selected)

neue_note_title = Labelmaker(neuroot, 171, 60, 260, 40, 36, text="Neue Note")
neue_note_button_fertig = Buttonmaker(neuroot, 171, 310, 260, 30, 14, text="Fertig", command=neue_noten_values)
neue_note_subject_select = Optionmenumaker(neuroot, 86, 166, 171, 30, 14, subjects_list, text="Fach auswählen")
neue_note_semester_select = Optionmenumaker(neuroot, 343, 166, 171, 30, 14, semesters_list, text="Halbjahr auswählen")
neue_note_points_select = Optionmenumaker(neuroot, 86, 216, 171, 30, 14, points_list, text="Punkte auswählen")
neue_note_type_select = Optionmenumaker(neuroot, 343, 216, 171, 30, 14, types_list, text="Art auswählen")

#########################################################

menubar_initialisation()
activate_homescreen()

con.close()
