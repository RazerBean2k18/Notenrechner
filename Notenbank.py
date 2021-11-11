from tkinter import *
from tkinter import ttk
from csv import *
import csv as csv
from sqlite3 import *
from tkinter.messagebox import showerror, showwarning, showinfo

#########################################################

con = connect('MasterDataBase.db')
cur = con.cursor()

root = Tk()
root.withdraw()

homeroot = Toplevel()
notenroot = Toplevel()
neuroot = Toplevel()
settingsroot = Toplevel()
subject_settingsroot = Toplevel()
style_settingsroot = Toplevel()
export_settingsroot = Toplevel()

#########################################################

error_message = "Error - Eine oder mehrere Daten fehlen"

global font_type

style = ttk.Style()
style.theme_use("default")

#########################################################

class Labelmaker:
    def __init__(self, master, x, y, w, h, font_size, **kwargs): 
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.label = Label(f, font=(font_type, font_size), **kwargs)
        self.label.pack(fill=BOTH, expand=1)
        
class Buttonmaker:
    def __init__(self, master, x, y, w, h, font_size, *args, **kwargs):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.button = Button(f, font=(font_type, font_size), *args, **kwargs)
        self.button.pack(fill=BOTH, expand=1)

class Optionmenumaker:
    def __init__(self, master, x, y, w, h, font_size, option_list, text, **kwarg):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.value_selected = StringVar(master)
        self.value_selected.set(text)
        self.question_menu = OptionMenu(f, self.value_selected, *option_list, **kwarg)
        self.question_menu.config(font=(font_type, font_size))
        self.styled_menu = root.nametowidget(self.question_menu.menuname)
        self.styled_menu.config(font=(font_type, font_size))
        self.question_menu.pack(fill=BOTH, expand=1)

    def set_value(self, value):
        self.value_selected.set(value)
        notenscreen_selected_fach()

class Treemaker:
    def __init__(self, master, x, y, w, h, font_size, columns):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.tree = ttk.Treeview(f, columns=columns, show='headings')
        style = ttk.Style()
        style.configure("Treeview.Heading", font=(font_type, font_size))
        self.tree.pack(fill=BOTH, expand=1)

    def heading(self, column, title):
        self.tree.heading(column, text=title)

    def column_width(self, column, width_value, custom_anchor):
        self.tree.column(column, width=width_value, anchor=custom_anchor, stretch=NO)

    def insert(self, font_size, place, values):
        self.tree.insert('', place, values=values)
        style = ttk.Style()
        style.configure("Treeview", font=(font_type, font_size))

    def delete_data(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        

class Scrollbarmaker:
    def __init__(self, master, x, y, w, h, own_tree):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.scrollbar = Scrollbar(f, orient=VERTICAL, command=own_tree.tree.yview)
        own_tree.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(fill=BOTH, expand=1)

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

class Setting:
    def __init__(self):
        self.list = []

    def get_data(self, what, table):
        self.pre_list = []
        for row in cur.execute(f"SELECT {what} FROM {table}"):
            data = str(row)
            self.pre_list.append(data)
        for value in self.pre_list:
            self.list.append(value[2:-3])

    def add_data(self, table, where, what):
        cur.execute(f"""INSERT INTO {table}({where}) VALUES ("{what}")""")
        con.commit()

    def delete_data(self, table):
        cur.execute(f"DELETE FROM {table}")
        con.commit()

#########################################################

def activate_homescreen():
    HomeScreen.show()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    SettingsScreen.hide()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.hide()

def activate_notenscreen():
    HomeScreen.hide()
    NotenScreen.show()
    NeueNoteScreen.hide()
    SettingsScreen.hide()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.hide()

def activate_neuenotescreen():
    neue_note_semester_select.value_selected.set("Halbjahr auswählen")
    neue_note_points_select.value_selected.set("Punkte auswählen")
    neue_note_type_select.value_selected.set("Art auswählen")
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.show()
    SettingsScreen.hide()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.hide()

def activate_settingsscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    SettingsScreen.show()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.hide()

def activate_subjectsettingsscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    SettingsScreen.hide()
    SubjectSettingsScreen.show()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.hide()

def activate_stylesettingsscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    SettingsScreen.hide()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.show()
    ExportSettingsScreen.hide()

def activate_exportsettingsscreen():
    HomeScreen.hide()
    NotenScreen.hide()
    NeueNoteScreen.hide()
    SettingsScreen.hide()
    SubjectSettingsScreen.hide()
    StyleSettingsScreen.hide()
    ExportSettingsScreen.show()

def database_initialisation():
    cur.execute("""
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        written_weight INTEGER,
        oral_weight INTEGER,
        special_weight INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        subject_name TEXT NOT NULL,
        grade TEXT NOT NULL,
        weighting_type TEXT NOT NULL,
        semester TEXT NOT NULL,
        FOREIGN KEY (subject_name) REFERENCES subjects (name),
        FOREIGN KEY (semester) REFERENCES semesters (name)
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS semesters (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS points (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS types (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS settings (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        font TEXT NOT NULL
    )
    """)

    con.commit()

    get_font()

def database_backup_full():
    table_list = ["subjects", "grades", "semesters", "points", "types"]
    for table in table_list:
        cur.execute(f"SELECT * FROM {table}")
        with open(f"./backups/{table}-backup.csv", "w") as csv_file:
          csv_writer = csv.writer(csv_file, delimiter="\t")
          csv_writer.writerow([i[0] for i in cur.description])
          csv_writer.writerows(cur)
    con.commit()

def database_backup_grades():
    cur.execute(f"SELECT * FROM grades")
    with open(f"./backups/grades-backup.csv", "w") as csv_file:
        csv_writer = csv.writer(csv_file, delimiter="\t")
        csv_writer.writerow([i[0] for i in cur.description])
        csv_writer.writerows(cur)
    con.commit()

def menubar_initialisation():

    def submenu_fach(value):
        sub_fach_menu.add_command(label=subject_settings.list[value], command=lambda:submenu_fach_select(value))

    def submenu_fach_select(value):
        noten_subject_select.set_value(subject_settings.list[value])
        activate_notenscreen()

    menubar = Menu(root)
    root.config(menu=menubar)
    
    rechner_menu = Menu(menubar, tearoff=False)
    sub_fach_menu = Menu(rechner_menu, tearoff=False)
    
    rechner_menu.add_command(label="Start", command=activate_homescreen)
    rechner_menu.add_separator()
    rechner_menu.add_cascade(label="Fächer", menu=sub_fach_menu)
    rechner_menu.add_command(label="Neue Note", command=activate_neuenotescreen)
    rechner_menu.add_separator()
    rechner_menu.add_command(label="Einstellungen", command=activate_settingsscreen)
    rechner_menu.add_separator()
    rechner_menu.add_command(label="Quit", command=root.destroy)

    number_of_subjects = len(subject_settings.list)
    x=1

    while x < number_of_subjects:
        submenu_fach(x-1)
        x = x+1

    menubar.add_cascade(label="Notenrechner", menu=rechner_menu)

def get_font():
    global font_type
    font_type = cur.execute("SELECT font FROM settings")

def set_font():
    cur.execute(f"""INSERT INTO settings (font) VALUES ("{font_selected}")""")
    get_font()

def command_notenscreen_selected_fach(event):
    notenscreen_selected_fach()
    
def notenscreen_selected_fach():
    subject_selected = noten_subject_select.value_selected.get()
    Labelmaker(notenroot, 85, 34, 430, 40, 36, text=subject_selected)
    noten_display.delete_data()
    cur.execute(f"""SELECT grade, weighting_type, semester FROM grades WHERE subject_name=='{subject_selected}'""")
    rows = cur.fetchall()
    for row in rows:
        noten_display.insert(14, END, row)

def neue_note_fach_already_selected():
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
        showinfo(title='Information', message=f"Fach: {subject_selected}\nPunkte: {points_selected}\nArt: {type_selected}\nHalbjahr: {semester_selected}")
        cur.execute(f"""
                        INSERT INTO
                            grades (subject_name, grade, weighting_type, semester)
                        VALUES
                            ("{subject_selected}", "{points_selected}", "{type_selected}", "{semester_selected}")
                    """)
        con.commit()
        notenscreen_selected_fach()
        activate_notenscreen()

def clear_error_message():
    Labelmaker(neuroot, 215, 270, 171, 30, 14, text="")

def subject_settings_delete_subject():
    subject = subject_settings_subject_select.value_selected.get()
    cur.execute(f"""DELETE FROM  subjects WHERE name='{subject}'""")
    con.commit()

#########################################################

database_initialisation()

subject_settings = Setting()
subject_settings.get_data("name", "subjects")
semester_settings = Setting()
semester_settings.get_data("name", "semesters")
point_settings = Setting()
point_settings.get_data("name", "points")
type_settings = Setting()
type_settings.get_data("name", "types")

HomeScreen = Screen(homeroot, "Notenrechner")
NotenScreen = Screen(notenroot, "Noten")
NeueNoteScreen = Screen(neuroot, "Neue Note")
SettingsScreen = Screen(settingsroot, "Einstellungen")
SubjectSettingsScreen = Screen(subject_settingsroot, "Fächer Optionen")
StyleSettingsScreen = Screen(style_settingsroot, "Style Optionen")
ExportSettingsScreen = Screen(export_settingsroot, "Import/Export Optionen")

home_title = Labelmaker(homeroot, 115, 111, 370, 75, 64, text="Notenrechner")
home_button_noten = Buttonmaker(homeroot, 170, 208, 260, 30, 14, text="Noten", command=activate_notenscreen)
home_button_gesamt = Buttonmaker(homeroot, 170, 260, 260, 30, 14, text="Einstellungen", command=activate_settingsscreen)

settings_title = Labelmaker(settingsroot, 171, 60, 260, 40, 36, text="Einstellungen")
settings_subject_options_button = Buttonmaker(settingsroot, 209, 143, 171, 30, 14, text="Fächer-Optionen", command=activate_subjectsettingsscreen)
settings_style_options_button = Buttonmaker(settingsroot, 209, 191, 171, 30, 14, text="Style-Optionen", command=activate_stylesettingsscreen)
settings_export_options_button = Buttonmaker(settingsroot, 209, 239, 171, 30, 14, text="Import/Export-Optionen", command=activate_exportsettingsscreen)
settings_fertig_button = Buttonmaker(settingsroot, 171, 310, 260, 30, 14, text="Fertig", command=activate_homescreen)

subject_settings_title = Labelmaker(subject_settingsroot, 140, 50, 321, 42, 36, text="Fächer - Optionen")
subject_settings_label_subjects = Labelmaker(subject_settingsroot, 37, 125, 171, 30, 14, text="Fächer:")
subject_settings_label_new_subjects = Labelmaker(subject_settingsroot, 37, 195, 171, 30, 14, text="Neues Fach:")
subject_settings_seperator = Labelmaker(subject_settingsroot, 24, 169, 550, 12, 10, text="---------------------------------------------------------------------------------------------------------------------------------------")
subject_settings_subject_select = Optionmenumaker(subject_settingsroot, 214, 125, 171, 30, 14, subject_settings.list, text="Fächer")
subject_settings_subject_delete = Buttonmaker(subject_settingsroot, 432, 125, 130, 30, 14, text="Fach löschen", command=subject_settings_delete_subject)
subject_settings_subject_delete_disclaimer = Labelmaker(subject_settingsroot, 432, 155, 130, 12, 8, text="Benötigt Restart im Anschluss!")

noten_title = Labelmaker(notenroot, 85, 34, 430, 40, 36, text="Fach auswählen")
noten_subject_select = Optionmenumaker(notenroot, 86, 335, 171, 30, 14, subject_settings.list, text="Fach auswählen", command=command_notenscreen_selected_fach)
noten_button_neuenote = Buttonmaker(notenroot, 343, 335, 171, 30, 14, text="Neue Note", command=neue_note_fach_already_selected)
noten_display = Treemaker(notenroot, 86, 86, 418, 235, 14, ["points", "type", "semester"])
noten_display.heading("points", "Punkte")
noten_display.column_width("points", 139, "center")
noten_display.heading("type", "Art")
noten_display.column_width("type", 138, "w")
noten_display.heading("semester", "Halbjahr")
noten_display.column_width("semester", 138, "w")
noten_display_scrollbar = Scrollbarmaker(notenroot, 504, 86, 10, 235, noten_display)

neue_note_title = Labelmaker(neuroot, 171, 60, 260, 40, 36, text="Neue Note")
neue_note_button_fertig = Buttonmaker(neuroot, 171, 310, 260, 30, 14, text="Fertig", command=neue_noten_values)
neue_note_subject_select = Optionmenumaker(neuroot, 86, 166, 171, 30, 14, subject_settings.list, text="Fach auswählen")
neue_note_semester_select = Optionmenumaker(neuroot, 343, 166, 171, 30, 14, semester_settings.list, text="Halbjahr auswählen")
neue_note_points_select = Optionmenumaker(neuroot, 86, 216, 171, 30, 14, point_settings.list, text="Punkte auswählen")
neue_note_type_select = Optionmenumaker(neuroot, 343, 216, 171, 30, 14, type_settings.list, text="Art auswählen")

#########################################################
menubar_initialisation()
activate_homescreen()





































