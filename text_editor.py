from tkinter import *
from tkinter import filedialog
import re


name = None
temp = False



def newFile():
    global name 
    name = "Untitled"
    text.delete(0.0, END)

def saveFile():
    
    if temp:  
        global name 
        txt = text.get(0.0, END)
        fil = open(name, 'w')
        fil.write(txt)
        fil.close()

def saveAsFile():
    temp = True
    fil = filedialog.asksaveasfile(mode = 'w', defaultextension = '.txt')
    txt = text.get(0.0, END)
    try:
        fil.write(txt.rstrip())
    except:
       filedialog.showerror(title = "Oops!", message = "unable to save file")

def openFile():
    f = filedialog.askopenfile(mode = 'r')
    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

def fontHelvectica():
    global text 
    text.config(font = "Helvetica")

def fontArial():
    global text 
    text.config(font = "Arial")
def fontCourier():
    global text
    text.config(font = "Courier")

def wordCount(event = None):
   
    txt = text.get(1.0, END)
    all_words = re.findall(r'\b\w+\b', txt)
    word_count.set(f"Words: {len(all_words)}")


root = Tk()
root.title("Python Text Editor V 1.0")
root.minsize(width = 500, height = 400)
root.maxsize(width = 800, height = 400)

text = Text(root, width = 400, height = 400, wrap = "none")
text.pack(expand = YES, fill = BOTH)

scrollbar = Scrollbar(text, command = text.yview)
scrollbar.pack(side = RIGHT, fill = Y)
text.config(yscrollcommand= scrollbar.set)

scrollbar2 = Scrollbar(text, command = text.xview)
scrollbar2.pack(side = BOTTOM, fill = X)
text.config(xscrollcommand= scrollbar2.set)



helvetica = StringVar()
arial = StringVar()
courier = StringVar()

menu = Menu(root)
filemenu = Menu(menu)
filemenu.add_command(label = "New", command = newFile)
filemenu.add_command(label = "Open", command = openFile)
filemenu.add_command(label = "Save", command = saveFile)
filemenu.add_command(label = "Save as", command = saveAsFile)

filemenu.add_separator()
filemenu.add_command(label = "Quit", command = root.quit())

fontmenu = Menu(menu)
fontmenu.add_command(label = "Helvetica",command = fontHelvectica)
fontmenu.add_command(label = "Arial", command = fontArial)
fontmenu.add_command(label = "Courier", command = fontCourier)
menu.add_cascade(label = "File", menu = filemenu)
menu.add_cascade(label = "Font", menu = fontmenu )
root.config(menu = menu)

word_count = StringVar()
word_count_label = Label(root, textvariable= word_count, bd = 1, relief = SUNKEN, anchor = W)
word_count_label.pack(side= BOTTOM, fill = X)


text.bind('<KeyRelease>', lambda event: wordCount())
wordCount()
root.mainloop()


