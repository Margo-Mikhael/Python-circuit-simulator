import SchemDraw
import SchemDraw.elements as elm 
from tkinter import *
from tkinter import messagebox  
#Creating the window
window = Tk() 
window.geometry('970x550')
window.title('Circit Similator')
window.configure(background='SlateGray1')
window.attributes("-fullscreen",TRUE) 

###big label
l1 = Label(window, text="Circuit Simulator ",font='Helvetica 22 bold',bg='SkyBlue3',width=200)
l1.pack()
###all buttons functions 
d = SchemDraw.Drawing()
def button1():
     d.add(elm.BATTERY,d='up', label='V')

def button2():
     d.add(elm.RES, d='right', label='R ',botlabel='$\Omega$')
def button3():
     d.add(elm.RES, d='left', label='R ',botlabel='$\Omega$')
def button4():
     d.add(elm.RES, d='up', label='R ',botlabel='$\Omega$')
def button5():
     d.add(elm.RES, d='down', label='R ',botlabel='$\Omega$')

def button6():
     d.add(elm.CAP, d='right',label='C', botlabel='$\mu$F' )
def button7():
     d.add(elm.CAP, d='left',label='C', botlabel='$\mu$F' )
def button8():
     d.add(elm.CAP, d='up',label='C', botlabel='$\mu$F' )
def button9():
     d.add(elm.CAP, d='down',label='C', botlabel='$\mu$F' )
     
def button10():
     d.add(elm.LINE,d='right')
def button11():
     d.add(elm.LINE,d='left')
def button12():
     d.add(elm.LINE,d='up')
def button13():
     d.add(elm.LINE,d='down')


def button14():
    d.add(elm.GND,d='right')

def button15():
    d.draw()
    d.save('schematic,svg')
def popup():
    messagebox.showinfo("Important Instructions!","\nPlease read well!\n\n1-Everytime you create a new circuit you have to press the exit button and start over\n(you might have to press it multiple times)\n\n2- Every circuit must start with a battery and end with the ground\n\n3- You have to press the draw button to check you circuit every time you add a new element\n\n4-Choose the correct direction for elements:  V (vertical) for up and down - H (horizontal) for right and left\n")

def clicked():
    v = float(e1.get())
    r_type = dropmenu.current()
    total_resistance = 0
    if r_type == 0:
        for resistor in resistors:
            total_resistance += float(resistor.get())
    else:
        for resistor in resistors:
            total_resistance += 1/float(resistor.get())
        total_resistance = 1/total_resistance

    c = v/total_resistance
    current_string_var.set(c)

def showing_resistors_inputs():
    for i in range(0, int(e2.get())):
        l = Label(frame2,font='Helvetica 10 bold',bg='SlateGray1',text=f"Enter resistance {str(i+1)} value :")
        l.grid(column=3, row=4+i)
        e = Entry(frame2,width=4)
        e.grid(column=4, row=4+i)
        resistors.append(e)
    print(resistors) 

def popup():
    messagebox.showinfo("Important Instructions!","\nPlease read well!\n\n1-Everytime you create a new circuit you have to press the Exit Program button and start over\n(you might have to press it multiple times)\n\n2- Every circuit must start with a battery and end with the ground\n\n3- You have to press the draw button to check you circuit every time you add a new element\n\n4-Choose the correct direction for elements:  V (vertical) for up and down - H (horizontal) for right and left\n")

##instructions button and exit button 
Button(window,text=" Important Instructions !",width=200,font='Helvetica 12 bold',bg="LightSteelBlue3",command=popup).pack()
button_quit = Button(window, text='Exit program',font='Helvetica 10 bold',bg="indian red2",command=window.quit).pack(side=TOP)




##Frame 1
frame1 = LabelFrame(window,text="Simulator",font='Helvetica 10 bold',bg='SlateGray1',padx=150,pady=15)
frame1.pack(pady=10) 

##the widgets that are in frame1 
l1 = Label(frame1, text="Add Circuit elements",font='Helvetica 14 bold',bg="SlateGray1")
l1.grid(column=5,row=0)
from tkinter.ttk import * 
btn1 = Button(frame1,text="Battery",command=button1)
btn1.grid(row=1,column=0)
btn2 = Button(frame1,text="   Resistor V up   ",command=button2)
btn2.grid(row=1,column=3)
btn3 = Button(frame1,text="Resistor V Down ",command=button3)
btn3.grid(row=2,column=3)
btn4 = Button(frame1,text="   Resistor H left  ",command=button4)
btn4.grid(row=3,column=3)
btn5 = Button(frame1,text="Resistor H right ",command=button5)
btn5.grid(row=4,column=3)
btn6 = Button(frame1,text="  Capacitor V up   ",command=button6)
btn6.grid(row=1,column=5)
btn7 = Button(frame1,text="Capacitor V Down",command=button7)
btn7.grid(row=2,column=5)
btn8 = Button(frame1,text=" Capacitor H Left ",command=button8)
btn8.grid(row=3,column=5)
btn9 = Button(frame1,text="Capacitor H Right",command=button9)
btn9.grid(row=4,column=5)
btn10 = Button(frame1,text="Wire V up",command=button10)
btn10.grid(row=1,column=7)
btn11 = Button(frame1,text="Wire V down",command=button11)
btn11.grid(row=2,column=7)
btn12 = Button(frame1,text="Wire H left",command=button12)
btn12.grid(row=3,column=7)
btn13 = Button(frame1,text="Wire H right",command=button13)
btn13.grid(row=4,column=7)
btn14 = Button(frame1,text="Ground",command=button14)
btn14.grid(row=1,column=9)
from tkinter import *
btn15 = Button(frame1,text="Draw ✏",bg='SkyBlue3',font='Helvetica 10 bold',width=10,fg="black",command=button15)
btn15.grid(row=12,column=5)

###frame2
frame2 = LabelFrame(window,text="Current Calculator",font='Helvetica 10 bold',bg='SlateGray1',padx=70)
frame2.pack(ipady=30,pady=15) 

###widgets that are in frame2
ll = Label(frame2, text="Enter the values of voltage and resistance",height=2,font='Helvetica 14 bold',bg="SlateGray1")
ll.grid(column=2,row=1)

l1 = Label(frame2,text="Enter voltage :",font='Helvetica 10 bold',bg='SlateGray1') #labels & entry boxes
l1.grid(row=2,column=1)
e1=Entry(frame2)
e1.grid(row=2,column=2)

l2 = Label(frame2,text="Enter number of resistor :",font='Helvetica 10 bold',bg='SlateGray1')
l2.grid(row=3,column=1)
e2 = Entry(frame2)
e2.grid(row=3,column=2)


current_string_var = StringVar()
l4 = Label(frame2,font='Helvetica 12 bold',bg='SlateGray1',textvariable=current_string_var)
current_string_var.set("Current = 0")
l4.grid(row=4,column=2)

#dropmenu
dropmenu=Combobox(frame2)
dropmenu.grid(row=2,column=3)
dropmenu['values']=("Series","Parallel")
dropmenu.current(0)

resistors = []
btn=Button(frame2,text="calculate Current",font='Helvetica 10 bold',bg='SkyBlue3',command=clicked)
btn.grid(row=4,column=1)

btn2=Button(frame2,text="Enter Values",font='Helvetica 10 bold',bg='SkyBlue3',command=showing_resistors_inputs)
btn2.grid(row=3,column=3)
##
window.mainloop()