# skeucore.com 2023
from tkinter import *
from tkinter import filedialog
import datetime
import os
import webbrowser
from tkinter import messagebox
import pyperclip
import math

log_list = []

def delete():
    global equation_text
    global equation_label
    leng = len(equation_text)
    equation_text = equation_text[:-1]
    if leng < 15:
        display.config(font="Helvetica 40 bold",pady=1)
        display.update()
        root.update()
    equation_label.set(equation_text)
    log_list.append(str("Delete"))

def basic():
    root.geometry("304x450")
    equalsbtn.config(width="223",image=equals_new_basic)
    backspacebtn.grid(column=4,row=4)
    root.update()


def piPress():
    global equation_text
    pivar = math.pi
    equation_text = equation_text + str(pivar)
    leng = len(equation_text)
    if leng > 9:
        display.config(font="Helvetica 20 bold",pady=16)
        display.update()
        root.update()
    
    equation_label.set(equation_text)
    log_list.append(str("PI"))




def extended():
    root.geometry("380x450")
    equalsbtn.config(width="298",image=equals_ext)
    backspacebtn.grid(column=5,row=4)
    root.update()


def openPDF():

    os.startfile("Calculator_User_Guide.pdf")


def aboutPopup():
    messagebox.showinfo(title="About", message="Calculator v1.0.1")

def openWeb():
    webbrowser.open('http://skeucore.com')

def clearLog():
    log_list.clear()

def saveLog():
    dir = filedialog.askdirectory()
    current_time = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    time = str(current_time)
    filepath = os.path.join(dir +"/log_save_"+time+".txt")
    list_to_str = str(log_list)
    with open(filepath, "x") as log:
        log.write(list_to_str)
        log.close()



def button_press(num):
    
    global equation_text
    leng = len(equation_text)
    if leng > 9:
        display.config(font="Helvetica 20 bold",pady=16)
        display.update()
        root.update()
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    log_list.append(str(equation_text))


def equals():
    global equation_text
    global calculation
    try:
        calculation = str(eval(equation_text))
        equation_label.set(calculation)
        equation_text = calculation
        log_list.append("Equals: "+str(calculation))
        
    
    except ZeroDivisionError:
        log_list.append("Zero Division Error")
        equation_label.set("Error")
        equation_text = "Error"
    

    leng = len(calculation)
    if leng > 10:
        display.config(font="Helvetica 20 bold",pady=16)
        display.update()
        root.update()
    else:
        display.config(font="Helvetica 40 bold",pady=1)
        display.update()
        root.update()

def copyRes(): #copy result
    global calculation
    pyperclip.copy(calculation)


    

def clear():
    global equation_label
    global equation_text
    log_list.append(str("Clear"))
    equation_text = ""
    equation_label.set(equation_text)
    display.config(font="Helvetica 40 bold",pady=1)
    display.update()
    root.update()
    


    


root = Tk()
root.geometry("304x450")
root.config(bg="#262626")
root.resizable(False, False)
root.title("Calculator")
logo = PhotoImage(file="calclogo.png")
root.iconphoto(True,logo)


menubar = Menu(root)
root.config(menu=menubar)

fileMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Export Log",command=saveLog)
fileMenu.add_command(label="Clear Log",command=clearLog)
fileMenu.add_command(label="Copy Result",command=copyRes)
#fileMenu.add_command(label="Delete",command=delete) Used to be delete button for testing


var = StringVar(value="Basic")
windowMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Window",menu=windowMenu)
windowMenu.add_radiobutton(label="Basic",variable=var,command=basic)
windowMenu.add_radiobutton(label="Extended",variable=var,command=extended)


helpMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="Help",menu=helpMenu)
helpMenu.add_command(label="User Guide",command=openPDF)
helpMenu.add_command(label="Website",command=openWeb)
helpMenu.add_command(label="About",command=aboutPopup)



#Images

oneimg = PhotoImage(file="one.png")
twoimg = PhotoImage(file="two.png")
threeimg = PhotoImage(file="three.png")
fourimg = PhotoImage(file="four.png")
fiveimg = PhotoImage(file="five.png")
siximg = PhotoImage(file="six.png")
sevenimg = PhotoImage(file="seven.png")
eightimg = PhotoImage(file="eight.png")
nineimg = PhotoImage(file="nine.png")
zeroimg = PhotoImage(file="zero.png")
plusimg = PhotoImage(file="plus.png")
minusimg = PhotoImage(file="minus.png")
timesimg = PhotoImage(file="times.png")
divideimg = PhotoImage(file="divide.png")
commaimg = PhotoImage(file="comma.png")
equalsimg = PhotoImage(file="equals.png")
clearimg = PhotoImage(file="clear.png")
piimg = PhotoImage(file="pi.png")
openbr = PhotoImage(file="openbracket.png")
closebr = PhotoImage(file="closebracket.png")
percentimg = PhotoImage(file="percent.png")
equals_ext = PhotoImage(file="equals_extended.png")
equals_new_basic = PhotoImage(file="enter_new_basic.png")
backspace = PhotoImage(file="backspace.png")

equation_text = ""

equation_label = StringVar()

display = Label(root, width=300,font="Helvetica 40 bold",bg="#5c5c5c",fg="white", textvariable=equation_label)


display.pack()
frame = Frame(root)
frame.pack(anchor=NW)


one = Button(frame, image=oneimg, width=70, height=70,command=lambda: button_press(1))
one.grid(column=1,row=0)

two = Button(frame, image=twoimg, width=70, height=70,command=lambda: button_press(2))
two.grid(column=2,row=0)

three = Button(frame, image=threeimg, width=70, height=70,command=lambda: button_press(3))
three.grid(column=3,row=0)

four = Button(frame, image=fourimg, width=70, height=70,command=lambda: button_press(4))
four.grid(column=1,row=1)

five = Button(frame, image=fiveimg, width=70, height=70,command=lambda: button_press(5))
five.grid(column=2,row=1)

six = Button(frame, image=siximg, width=70, height=70,command=lambda: button_press(6))
six.grid(column=3,row=1)

seven = Button(frame, image=sevenimg, width=70, height=70,command=lambda: button_press(7))
seven.grid(column=1,row=2)

eight = Button(frame, image=eightimg, width=70, height=70,command=lambda: button_press(8))
eight.grid(column=2,row=2)

nine = Button(frame, image=nineimg, width=70, height=70,command=lambda: button_press(9))
nine.grid(column=3,row=2)

zero = Button(frame, image=zeroimg, width=70, height=70,command=lambda: button_press(0))
zero.grid(column=1,row=3)

plus = Button(frame, image=plusimg, width=70, height=70,command=lambda: button_press("+"))
plus.grid(column=4,row=0)

minus = Button(frame, image=minusimg, width=70, height=70,command=lambda: button_press("-"))
minus.grid(column=4,row=1)

times = Button(frame, image=timesimg, width=70, height=70,command=lambda: button_press("*"))
times.grid(column=4,row=2)

divide = Button(frame, image=divideimg, width=70, height=70,command=lambda: button_press("/"))
divide.grid(column=4,row=3)


percent = Button(frame, image=percentimg, width=70, height=70,command=lambda: button_press("%"))
percent.grid(column=5,row=0)

openbracket = Button(frame, image=openbr, width=70, height=70,command=lambda: button_press("("))
openbracket.grid(column=5,row=1)

closebracket = Button(frame, image=closebr, width=70, height=70,command=lambda: button_press(")"))
closebracket.grid(column=5,row=2)



pi = Button(frame, image=piimg, width=70, height=70,command=piPress)
pi.grid(column=5,row=3)







comma = Button(frame, image=commaimg, width=70, height=70,command=lambda: button_press("."))
comma.grid(column=2,row=3)

clearbtn = Button(frame, image=clearimg, width=70, height=70,command=clear)
clearbtn.grid(column=3,row=3)

backspacebtn = Button(frame, image=backspace, width=70, height=70,command=delete)
backspacebtn.grid(column=4,row=4)

equalsbtn = Button(root, image=equals_new_basic, width=223, height=70,command=equals,padx=-10,pady=-10)
equalsbtn.place(y=372)










root.mainloop()