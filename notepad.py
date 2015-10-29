from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
from tkinter.font import *
import sys, time, sched, math

class format:
    def __init__(self, notepad):
        f = Tk()

        self.b = Button(f, text="Hi", command = self.hi).pack()

        def hi(self):
            print("Hello")

        f.mainloop()
        
class ZPad:
    def __init__(self):
        self.root = Tk()
        self.root.title("ZPad")
        self.root.wm_iconbitmap('Notepad.ico')

        self.scrollbar = Scrollbar(self.root)
        self.scrollbar.pack(side=RIGHT, fill=Y)

        self.textbox = Text(self.root, yscrollcommand=self.scrollbar.set, undo=TRUE)
        self.textbox.pack(side=LEFT, fill=BOTH, expand=YES)

        self.textbox.bind("<Control-Key-a>", self.Select_All)
        self.textbox.bind("<Control-Key-A>", self.Select_All)
        self.root.bind("<Control-o>", self.Open)
        self.root.bind("<Control-Shift-s>", self.Save_as)
        

        #Popup menu
        self.the_menu = Menu(self.root, tearoff=0)
        self.the_menu.add_command(label="Cut", command=lambda: self.textbox.event_generate("<<Cut>>"))
        self.the_menu.add_command(label="Copy", command=lambda: self.textbox.event_generate("<<Copy>>"))
        self.the_menu.add_command(label="Paste", command=lambda: self.textbox.event_generate("<<Paste>>"))

        def popup(event):
            self.the_menu.post(event.x_root, event.y_root)

        self.textbox.bind("<Button-3>", popup)

        #Menu Bar
        self.menubar = Menu(self.root)
        self.filemenu = Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label="New", command=self.New, accelerator="Ctrl+N")
        self.filemenu.add_command(label="Open...", command=self.open, accelerator="Ctrl+O")
        self.filemenu.add_command(label="Save", command=self.Save, accelerator="Ctrl+S")
        self.filemenu.add_command(label="Save as...", command=self.Save_as, accelerator="Ctrl+Shift+S")
        self.filemenu.add_separator()
        self.filemenu.add_command(label="Exit", command=self.quit, accelerator="Ctrl+Q")
        self.menubar.add_cascade(label="File", menu=self.filemenu)

        self.editmenu = Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label="Undo", command=self.Undo, accelerator="Ctrl+Z")
        self.editmenu.add_command(label="Redo", command=self.Redo, accelerator="Ctrl+Y")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Cut", command=self.Cut, accelerator="Ctrl+X")
        self.editmenu.add_command(label="Copy", command=self.Copy, accelerator="Ctrl+C")
        self.editmenu.add_command(label="Paste", command=self.Paste, accelerator="Ctrl+P")
        self.editmenu.add_command(label="Clear All", command=self.Clear_All, accelerator="Ctrl+Shift+A")
        self.editmenu.add_separator()
        self.editmenu.add_command(label="Format", command=self.options, accelerator="Ctrl+T")
        self.menubar.add_cascade(label="Edit", menu=self.editmenu)

        self.helpmenu = Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label="About...", command=self.About)
        self.menubar.add_cascade(label="Help", menu=self.helpmenu)


        self.root.config(menu=self.menubar)

        self.root.protocol('WM_DELETE_WINDOW', self.quit)

        self.root.mainloop()

    def Copy(self):
        self.textbox.event_generate("<<Copy>>")

    def Cut(self):
        self.textbox.event_generate("<<Cut>>")

    def Paste(self):
        self.textbox.event_generate("<<Paste>>")

    def options(self):
        if hasattr(self, "opt"):
            if self.opt.format.winfo_exists():
                self.opt.format.lift()
            else:
                self.opt = format(self)
        else:
            self.opt = format(self)

    def New(self):
        data = self.textbox.get(0.0, END)
        if len(data) >= 2:
            message = tkinter.messagebox.askyesnocancel("Save...", "Do you want to Save?")
            if message == True:
                #if file == True:
                    #print("Already done")
                #else:
                file = tkinter.filedialog.asksaveasfile(mode='w', initialfile=".z", defaultextension=".z")
                if file is None:
                    return
                textoutput = self.textbox.get(0.0, END)
                file.write(textoutput.rstrip())
                file.write("\n")
                self.textbox.delete(0.0, END)
            elif message == False:
                self.textbox.delete(0.0, END)
            else:
                pass
        else:
            pass
   
    def Open(self, event):
        self.f = filedialog.askopenfile(mode='r', filetypes = ( ("ztext file", "*.z"),("zytext", "*.zy"), ("Text", "*.txt"), ("All files", "*.*") ) )
        if self.f is None:
                    return
        self.readfile = self.f.read()
        self.textbox.delete(0.0, END)
        self.textbox.insert('0.0', self.readfile)

    def open(self):
        global f, readfile
        self.f = filedialog.askopenfile(mode='r', filetypes = ( ("ztext file", "*.z"),("zytext", "*.zy"), ("Text", "*.txt"), ("All files", "*.*") ) )
        if self.f is None:
                    return
        self.readfile = self.f.read()
        self.textbox.delete(0.0, END)
        self.textbox.insert('0.0', self.readfile)

    def Save(self):
        contents = self.textbox.get(0.0, END)
        try:
            with open(self.f, 'w') and Open(self.f, 'w') and Save_as() as file:
                outputFile.write(contents) 
        except AttributeError:
            self.Save_as()   

    def Save_as(self):
        global outpuFile
        outputFile = tkinter.filedialog.asksaveasfile(mode='w', initialfile=".z", defaultextension=".z")
        if outputFile is None:
            return
        textoutput = self.textbox.get(0.0, END)
        outputFile.write(textoutput.rstrip())
        outputFile.write("\n")

    def quit(self):
        data = self.textbox.get(0.0, END)
        if len(data) >= 2:
            message = tkinter.messagebox.askyesnocancel("Save...", "Do you want to Save?")
            if message == True:
                file = tkinter.filedialog.asksaveasfile(mode='w', initialfile=".z", defaultextension=".z")
                if file is None:
                    return
                textoutput = self.textbox.get(0.0, END)
                file.write(textoutput.rstrip())
                file.write("\n")
            elif message == False:
                self.root.destroy()
            else:
                pass
        else:
            self.root.destroy()

    def Undo(self):
        self.textbox.edit_undo()

    def Redo(self):
        self.textbox.edit_redo()

    def Clear_All(self):
        self.textbox.delete(0.0, END)

    def Select_All(self, event):
        self.textbox.tag_add(SEL, "1.0", END)
        self.textbox.mark_set(INSERT, "1.0")
        self.textbox.see(INSERT)
        return 'break'

    def About(self):
        #About window
        self.top = Toplevel()
        self.top.title("About...")

        self.msg = Message(self.top, text="Note pad\n Created by Zac Hadjineophytou", width=200, anchor=CENTER)
        self.msg.pack()

        self.top.mainloop()

notepad = ZPad()
