from tkinter import *
import tkinter

kb = tkinter.Tk()

buttons = [
'~','`','!','@','#','$','%','^','&','*','(',')','-','_','TAB',
'q','w','e', 'r', 't','y','u','i','o','p','\\','7','8','9', 'BACK',
'a','s','d','f','g','h','j','k','l','[',']','4', '5', '6',
'SHIFT','z','x','c','v','b','n','m',',','.', '?','/', '1','2','3','SPACE'
]

def select(value):
    if value == "BACK":
        entry.delete(len(entry.get()-1, tkinter.END))

    elif value == "SPACE":
        entry.insert(tkinter.END, ' ')

    elif value == "TAB":
        entry.insert(tkinter.END, '     ')

    else:
        entry.insert(tkinter.END, value)

def keypop():
    varRow = 2
    varColumn = 0
    for button in buttons:
        command = lambda x=button : select(x)
        if button == "SPACE" or button == "SHIFT" or button == "BACK":
            tkinter.Button(kb, text = button, width = 6, bg = "#3c4987", fg = "#ffffff",
                           activebackground = "#ffffff", activeforeground = "#3c4987", relief = 'flat',
                           padx = 1, bd = 1, command = command).grid(row = varRow, column = varColumn)
        else:
            tkinter.Button(kb, text = button, width = 4, bg = "#3c4987", fg = "#ffffff",
                           activebackground = "#ffffff", activeforeground = "#3c4987", relief = 'flat',
                           padx = 1, bd = 1, command = command).grid(row = varRow, column = varColumn)
        varColumn +=1

        if varColumn >14 and varRow == 2:
            varColumn = 0
            varRow +=1
        if varColumn >14 and varRow == 3:
            varColumn = 0
            varRow += 1
        if varColumn >14 and varRow == 4:
            varColumn = 0
            varRow += 1
    
        
def main():
    kb.title("Faradars KeyBoard")
    kb.resizable(0,0)

    label1 = Label(kb , text ='').grid(row = 0, columnspan = 15)

    global entry

    entry = Entry(kb, width = 50)
    entry.grid(row = 1, columnspan = 15)
    entry.bind("<Button-1>", lambda e: keypop())
    kb.mainloop()

main()
