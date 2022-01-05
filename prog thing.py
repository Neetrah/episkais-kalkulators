from tkinter import *
import turtle
import random

a = 0
b = 0

def draw():
    global nr1E
    global nr2E
    global mult
    global btnm
    global warn
    global result
    global under
    under.set("")
    mult.set("")
    hide(nr1E)
    hide(nr2E)
    hide(btnm)
    warn.set("")
    result.set("")
    wt = turtle.Screen()
    wt.bgcolor("#f0f0f0")
    wt.title("The drawing")
    wt.setup(800, 800)
    tt = turtle.Turtle()
    tt.shape("classic")
    tt.color("black")
    tt.fillcolor("black")
    tt.penup()
    tt.goto(-150, -150)
    tt.pendown()
    tt.goto(150, -150)
    tt.goto(250, -50)
    tt.goto(200, 0)
    tt.goto(250, 50)
    tt.goto(150, 100)
    tt.goto(100, 200)
    tt.goto(50, 100)
    tt.goto(-50, 100)
    tt.goto(-100, 200)
    tt.goto(-150, 100)
    tt.goto(-250, 50)
    tt.goto(-200, 0)
    tt.goto(-250, -50)
    tt.goto(-150, -150)
    tt.penup()
    tt.goto(-100, -50)
    tt.pendown()
    tt.begin_fill()
    tt.goto(-50, -50)
    tt.goto(-50, 50)
    tt.goto(-100, 50)
    tt.goto(-100, -50)
    tt.end_fill()
    tt.penup()
    tt.goto(50, -50)
    tt.pendown()
    tt.begin_fill()
    tt.goto(100, -50)
    tt.goto(100, 50)
    tt.goto(50, 50)
    tt.goto(50, -50)
    tt.end_fill()
    tt.penup()
    tt.goto(-300, -300)
    turtle.done()

def advice():
    global a
    global b
    global nr1E
    global nr2E
    global mult
    global btnm
    global warn
    global result
    global under
    hide(nr1E)
    hide(nr2E)
    hide(btnm)
    warn.set("")
    result.set("")
    b = a
    while a == b:
        a = random.randint(1,4)
    if a == 1:
        mult.set("Don't be a karen")
        under.set("")
    elif a == 2:
        mult.set("Santa claus isn't real")
        under.set("")
    elif a == 3:
        mult.set("Fighting bears isn't a good idea")
        under.set("")
    else:
        mult.set("If you accidentally give your address to someone on the internet, dw,")
        under.set("they prolly could've gotten it themselves anyways")

def question():
    intro3.set("What would you like to do?")
    
def multiply():
    try:
        a=float(nr1.get())
        b=float(nr2.get())
    except:
        warn.set("You need to enter a number")
        result.set("")
    else:
        warn.set("")
        mul = a * b
        result.set(f"Result: {mul:.1f}")
    
    
def multE():
    global nr1E
    global nr2E
    global mult
    global btnm
    global under
    mult.set("*")
    nr1E.place(x=220, y=360, anchor=CENTER)
    nr2E.place(x=380, y=360, anchor=CENTER)
    btnm.place(x=500, y=360, anchor=CENTER)
    under.set("")

def BtnONE():
    btn1=Button(ws, text="Multiply", height= 1, width=10, command=multE)
    btn1.place(x=120, y=185, anchor=CENTER)  
def BtnTWO():
    btn2=Button(ws, text="Advice (:", height= 1, width=10, command=advice)
    btn2.place(x=240, y=185, anchor=CENTER)
def BtnTHR():
    btn3=Button(ws, text="Drawing", height= 1, width=10, command=draw)
    btn3.place(x=360, y=185, anchor=CENTER)  
def BtnFOU():
    btn2=Button(ws, text="Cool picture", height= 1, width=10)
    btn2.place(x=480, y=185, anchor=CENTER)

def hide(widget):
    widget.place_forget()

def first():
    global intro2
    global nameE
    global btn
    global intro
    hide(nameE)
    hide(btn)
    intro.set("")
    
    name=name_var.get()
    intro2.set(f"Hello, {name}!")
    ws.after(1000, question)
    ws.after(2500, BtnONE)
    ws.after(2700, BtnTWO)
    ws.after(2900, BtnTHR)
    ws.after(3100, BtnFOU)


ws = Tk()
ws.title("Hello")
ws.geometry("600x600")


#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
nr1=StringVar()
nr1E = Entry(ws, textvariable = nr1, width = 10)
nr1E.place(x=220, y=360, anchor=CENTER)
hide(nr1E)

mult = StringVar()
mults = Label(ws, textvariable=mult).place(x=300, y=360, anchor=CENTER)
mult.set("")
    
nr2=StringVar()
nr2E = Entry(ws, textvariable = nr2, width = 10)
nr2E.place(x=380, y=360, anchor=CENTER)
hide(nr2E)
    
btnm=Button(ws, text="Enter", height= 1, width=5, command=multiply)
btnm.place(x=500, y=360, anchor=CENTER)
hide(btnm)

warn = StringVar()
warning = Label(ws, textvariable=warn).place(x=300, y=500, anchor=CENTER)
warn.set("")
result = StringVar()
resultL = Label(ws, textvariable=result).place(x=300, y=425, anchor=CENTER)
result.set("")

under = StringVar()
underm = Label(ws, textvariable=under).place(x=300, y=390, anchor=CENTER)
under.set("")
#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa

intro = StringVar()
label = Label(ws, textvariable=intro).place(x=300, y=220, anchor=CENTER)
intro.set("Hi there, what should I call you?")

name_var=StringVar()
nameE = Entry(ws, textvariable = name_var)
nameE.place(x=300, y=275, anchor=CENTER)

intro2 = StringVar()
label2 = Label(ws, textvariable=intro2).place(x=300, y=100, anchor=CENTER)
intro2.set("")

intro3 = StringVar()
label3 = Label(ws, textvariable=intro3).place(x=300, y=135, anchor=CENTER)
intro3.set("")

btn=Button(ws, text="Submit", command=first)
btn.place(x=300, y=340, anchor=CENTER)

ws.mainloop()