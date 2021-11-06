##class Treemaker:
##    def __init__(self, master
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

root = Tk()
root.title('Treeview demo')
root.geometry('600x400+0+0')

font='DIN Alternate'

class Treemaker:
    def __init__(self, master, x, y, w, h, columns):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.tree = ttk.Treeview(f, columns=columns, show='headings')
        self.tree.pack(fill=BOTH, expand=1)

    def heading(self, column, text):
        self.tree.heading(column, text=text)

    def insert(self, place, values):
        self.tree.insert('', place, values=values)

    def bind(self, text, *args):
        self.tree.bind(text, *args)

    def selection(self):
        self.record = []
        for selected_item in self.tree.selection():
            item = self.tree.item(selected_item)
            self.record.append(item['values'])
            

class Scrollbarmaker:
    def __init__(self, master, x, y, w, h, own_tree):
        f = Frame(master, height=h, width=w)
        f.pack_propagate(0)
        f.place(x=x, y=y)
        self.scrollbar = Scrollbar(f, orient=VERTICAL, command=own_tree.tree.yview)
        own_tree.tree.configure(yscroll=self.scrollbar.set)
        self.scrollbar.pack(fill=BOTH, expand=1)

def item_selected(event):
    for selected_item in tree.selection():
        item = tree.item(selected_item)
        record = item['values']
        # show a message
        showinfo(title='Information', message=','.join(record))


columns = ('TEST A', 'TEST B', 'TEST C')

test_tree = Treemaker(root, 10, 10, 580, 380, columns)

test_tree.heading('TEST A', 'test a')
test_tree.heading('TEST B', 'test b')
test_tree.heading('TEST C', 'test c')

contacts = []
for n in range(1, 40):
    contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

for i in contacts:
    test_tree.insert(END, i)

def item_selected(event):
    test_tree.selection()

test_tree.bind('<<TreeviewSelect>>', item_selected)

test_scrollbar = Scrollbarmaker(root, 580, 10, 10, 380, test_tree)

# run the app
root.mainloop()
