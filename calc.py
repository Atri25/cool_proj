from tkinter import *

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print(e)
                value = "Error!"
        scvalue.set(value)
        screen.update()
    elif text == "del":
        length = len(screen.get())
        screen.delete(length-1, 'end')
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()
Atri_root = Tk()
Atri_root.geometry("426x600")
Atri_root.title("Calculator")
Atri_root.resizable(0,0)

scvalue = StringVar()
scvalue.set("")
screen = Entry(Atri_root, textvar = scvalue, font = "Arial 35 ")
screen.pack(fill = X, ipadx = 8, pady = 8, padx = 8)

f1 = Frame(Atri_root)
b = Button(f1, text = "7", padx =  10, pady = 5 ,font = "Arial 35", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT, padx = 5, pady = 5)

b = Button(f1, text = "8", padx =  10, pady = 5 ,font = "Arial 35", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT,padx = 5, pady = 5)

b = Button(f1, text = "9", padx =  10, pady = 5 ,font = "Arial 35", bg = "white", fg = "black")
b.pack(side = LEFT,padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f1, text = "+", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT,padx = 5, pady = 5)
f1.pack()

f1 = Frame(Atri_root)
b = Button(f1, text = "4", padx =  10, pady = 5 ,font = "Arial 35" , bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT, padx = 5, pady = 5)

b = Button(f1, text = "5", padx =  10, pady = 5 ,font = "Arial 35", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT,padx = 5, pady = 5)

b = Button(f1, text = "6", padx =  10, pady = 5 ,font = "Arial 35", bg = "white", fg = "black")
b.pack(side = LEFT,padx = 5, pady = 5)
b.bind("<Button-1>", click)

b = Button(f1, text = "-", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.pack(side = RIGHT,padx = 10, pady = 5)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(Atri_root)
b = Button(f1, text = "1", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT, padx = 5, pady = 5)

b = Button(f1, text = "2", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT,padx = 5, pady = 5)

b = Button(f1, text = "3", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.pack(side = LEFT,padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(f1, text = "*", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT,padx = 10, pady = 5)
f1.pack()

f1 = Frame(Atri_root)
b = Button(f1, text = "=", padx =  60, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT,padx = 10, pady = 5)

b = Button(f1, text = "0", padx = 10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = LEFT, padx = 10, pady = 5)

b = Button(f1, text = "/", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT, padx = 10, pady = 5)
f1.pack()

f1 = Frame(Atri_root)
b = Button(f1, text = "del" ,padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.pack(side = LEFT,padx = 10, pady = 5)
b.bind("<Button-1>", click)

b = Button(f1, text = ".", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT,padx = 10, pady = 5)

b = Button(f1, text = "%", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT,padx = 10, pady = 5)

b = Button(f1, text = "C", padx =  10, pady = 5 ,font = "Arial 35 ", bg = "white", fg = "black")
b.bind("<Button-1>", click)
b.pack(side = RIGHT, padx = 10, pady = 5)
f1.pack(padx=10)
Atri_root.mainloop()
