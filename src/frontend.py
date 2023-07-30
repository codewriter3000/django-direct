from tkinter import *
import tkinter.ttk as ttk

class Window:
    def __init__(self, master):
        notebook = ttk.Notebook(master)
        notebook.place(x=0, y=0)
        file = ttk.Frame(notebook)
        insert = ttk.Frame(notebook)

        notebook.add(file, text='File')
        file_pane = ttk.Panedwindow(file, orient=HORIZONTAL)
        new = ttk.Labelframe(file_pane, text='New', width=100, height=100)
        open = ttk.Labelframe(file_pane, text='Open', width=100, height=100)
        save = ttk.Labelframe(file_pane, text='Save', width=100, height=100)
        export = ttk.Labelframe(file_pane, text='Export', width=100, height=100)
        file_pane.add(new)
        file_pane.add(open)
        file_pane.add(save)
        file_pane.add(export)

        notebook.add(insert, text='Insert')
        insert_pane = ttk.Panedwindow(insert, orient=HORIZONTAL)
        shapes = ttk.Labelframe(insert_pane, text='Shapes', width=100, height=100)
        connectors = ttk.Labelframe(insert_pane, text='Connectors', width=100, height=100)
        font = ttk.Labelframe(insert_pane, text='Font', width=100, height=100)
        tools = ttk.Labelframe(insert_pane, text='Tools', width=100, height=100)
        insert_pane.add(shapes)
        insert_pane.add(connectors)
        insert_pane.add(font)
        insert_pane.add(tools)

        notebook.pack(side=TOP, fill=X, height=150)

        canvas = Canvas(master)
        canvas.pack(fill=BOTH, side=BOTTOM)


root = Tk()
root.geometry('1600x700')
root.title('Django Direct')
window = Window(root)
root.mainloop()