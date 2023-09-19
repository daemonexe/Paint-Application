import random
from tkinter import *
from tkinter import colorchooser
import tkinter as tk


root = Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.overrideredirect(True)
root.title('Paint Application')

############## IMAGES SRC #####################
SidePanelImage = PhotoImage(file ="Srcimages/sidepanel.png")
LeftSidePanelImage = PhotoImage(file="Srcimages/leftsidepannel.png")
Button1Image = PhotoImage(file ="Srcimages/pencilToolImage.png")
LineBrushImage = PhotoImage(file ="Srcimages/linebrushTool.png")
EraserToolImage = PhotoImage(file ="Srcimages/erasertool.png")
PencilTool2Image = PhotoImage(file ="Srcimages/pencilTool2Image.png")
PencilTool2HoverImage = PhotoImage(file ="Srcimages/pencilTool2ImageHover.png")
saveIconImage = PhotoImage(file = 'Srcimages/saveicon.png')
PencilImage = PhotoImage(file = "Srcimages/selectedPencilBrushImage.png")
EraserSelected = PhotoImage(file = "Srcimages/eraserSelected.png")
LineBrushToolSelected = PhotoImage(file = "Srcimages/linebrushToolSeelected.png")
PencilBrush2 = PhotoImage(file = "Srcimages/pencilTool2ImageSelected.png")
EmptyBlock = PhotoImage(file = "Srcimages/empty.png")
subButtonImage = PhotoImage(file ="Srcimages/subractbutton.png")
addbuttonImage = PhotoImage(file = "Srcimages/addbutton.png")

############## DEFINED VARIABLES #####################
color_fg = 'black'
color_bg = 'white'
old_x = None
old_y = None
penwidth = 5
brush = ROUND
tool = "pen"

############## CANVAS FUNCTIONS #####################
def paint(e):
        global old_x
        global old_y
        if old_x and old_y:
            canvas.create_line(old_x, old_y, e.x, e.y, width=penwidth, fill=color_fg,
                               capstyle=brush, smooth=False)
        old_x = e.x
        old_y = e.y
        canvas.bind("<Button-1>",paint)

def colourChose():
    global color_fg
    color = colorchooser.askcolor()[1]
    button8['bg'] = color
    color_fg = color

def changeBgCanvas():
    color1 = colorchooser.askcolor()[1]
    canvas.config(bg = color1)

def clearCanvas():
    canvas.delete(ALL)
    canvas['bg'] = 'white'

def reset(e):
    if tool == 'line':
        pass
    if tool == "1":
        global old_x,old_y
        old_x = None
        old_y = None

def HoverAnimation(e):
    button2.config(image = PencilTool2HoverImage)

def LeaveAnimation(e):
    button2.config(image = PencilTool2Image)

def pressedOnPencilToolA(e):
    global color_fg,tool,old_x,old_y #1
    old_x = None
    old_y = None
    button1.configure(image= PencilImage)
    button2.configure(image = PencilTool2Image)
    button4.configure(image = EraserToolImage)
    button3.configure(image = LineBrushImage)
    tool = '1'

def pressedOnP2P(e):
    global color_fg,tool
    button2.configure(image = PencilBrush2)
    button1.configure(image =Button1Image)
    button3.configure(image =LineBrushImage)
    button4.configure(image = EraserToolImage)
    color_fg = 'black'

def pressedOnLineBrush(e):
    global color_fg, selectedBrush, tool
    tool = 'line'
    button1.configure(image =Button1Image)
    button2.configure(image = PencilTool2Image)
    button3.configure(image = LineBrushToolSelected)
    button4.configure(image = EraserToolImage)
    color_fg = 'black'

def pressedOnEraser(e):
    global selectedBrush
    global color_fg,color_bg
    button1.configure(image =Button1Image)
    button2.configure(image = PencilTool2Image)
    button4.configure(image = EraserSelected)
    button3.configure(image = LineBrushImage)
    color_fg = color_bg

def add_value(e):
    global penwidth
    if penwidth <= 29:
        penwidth += 1
        numDisplay.configure(text = penwidth)
    else:
        pass

def sub_value(e):
    global penwidth,old_x
    if penwidth > 1 and penwidth != 0:
        penwidth -= 1
        numDisplay.configure(text = penwidth)
    else:
        pass

############## WIDGET CREATIONS #####################
canvas = Canvas(root,highlightthickness = 0, width=1640, height=1060, bg="white",bd = 1,relief = 'solid')
pane = Label(root,bd = 0,image = SidePanelImage)
leftPane = Label(root,bd = 0,image = LeftSidePanelImage)
button1 = Label(root,bd = 0,image = Button1Image)
button2 = Label(root,bd = 0,image = PencilTool2Image)
button3 = Label(root,bd = 0,image = LineBrushImage)
button4 = Label(root,bd = 0,image = EraserToolImage)
button5 = Label(root,bd = 0,image = EmptyBlock)
button6 = Label(root,bd = 0,image = EmptyBlock)
button7 = Label(root,bd = 0,image = saveIconImage)
button8 = Button(root,bd = 5,bg = color_fg,width= 5, height= 2,relief= SUNKEN,command= colourChose)
frame = Frame(root,bg = 'red')

if tool == "pen":
    pressedOnPencilToolA(E)

## COLOR PALETS
p1 = Button(frame,bg = 'red',width = 4,height= 2)
p2 = Button(frame,bg = 'green',width = 4,height= 2)
p3 = Button(frame,bg = 'yellow',width = 4,height= 2)
p4 = Button(frame,bg = 'orange',width = 4,height= 2)
p5 = Button(frame,bg = 'orange',width = 4,height= 2)

p6 = Button(frame,bg = 'black',width = 4,height= 2)
p7 = Button(frame,bg = 'yellow',width = 4,height= 2)
p8 = Button(frame,bg = 'orange',width = 4,height= 2)
p9 = Button(frame,bg = 'orange',width = 4,height= 2)
p10 = Button(frame,bg = 'black',width = 4,height= 2)

p11 = Button(frame,bg = 'black',width = 4,height= 2)
p12 = Button(frame,bg = 'yellow',width = 4,height= 2)
p13 = Button(frame,bg = 'orange',width = 4,height= 2)
p14 = Button(frame,bg = 'orange',width = 4,height= 2)
p15 = Button(frame,bg = 'black',width = 4,height= 2)

p16 = Button(frame,bg = 'black',width = 4,height= 2)
p17 = Button(frame,bg = 'black',width = 4,height= 2)
p18 = Button(frame,bg = 'yellow',width = 4,height= 2)
p19 = Button(frame,bg = 'orange',width = 4,height= 2)
p20 = Button(frame,bg = 'orange',width = 4,height= 2)

p21 = Button(frame,bg = 'black',width = 4,height= 2)
p22 = Button(frame,bg = 'black',width = 4,height= 2)
p23 = Button(frame,bg = 'black',width = 4,height= 2)
p24 = Button(frame,bg = 'yellow',width = 4,height= 2)
p25 = Button(frame,bg = 'orange',width = 4,height= 2)

p26 = Button(frame,bg = 'black',width = 4,height= 2)
p27 = Button(frame,bg = 'black',width = 4,height= 2)
p28 = Button(frame,bg = 'black',width = 4,height= 2)
p29 = Button(frame,bg = '#323e45',width = 4,height= 2)
p30 = Button(frame,bg = 'orange',width = 4,height= 2)

p31 = Button(frame,bg = 'red',width = 4,height= 2)
p32 = Button(frame,bg = '#efeeb4',width = 4,height= 2)
p33 = Button(frame,bg = '#58b368',width = 4,height= 2)
p34 = Button(frame,bg = '#dad873',width = 4,height= 2)
p35 = Button(frame,bg = '#efeeb4',width = 4,height= 2)

p36 = Button(frame,bg = 'blue',width = 4,height= 2)
p37 = Button(frame,bg = '#8ba88e',width = 4,height= 2)
p38= Button(frame,bg = '#5a786f',width = 4,height= 2)
p39 = Button(frame,bg = '#3a4e51',width = 4,height= 2)
p40 = Button(frame,bg = '#323e45',width = 4,height= 2)

p41 = Button(frame,bg = '#323e45',width = 4,height= 2)
p42 = Button(frame,bg = '#ccd2c6',width = 4,height= 2)
p43 =  Button(frame,bg = '#95adbe',width = 4,height= 2)
p44 = Button(frame,bg = '#574f7d',width = 4,height= 2)
p45 = Button(frame,bg = '#503a65',width = 4,height= 2)
p46 = Button(frame,bg = '#3c2a4d',width = 4,height= 2)

############## WIDGET GRIDDING #####################

button1.grid(row=1,column = 1,rowspan = 1,columnspan = 1)
button2.grid(row=2,column = 1)
button3.grid(row=3,column = 1,rowspan = 1,columnspan = 1,padx = 1)
button4.grid(row=4,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button5.grid(row=5,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button6.grid(row=6,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button7.grid(row=41,column = 1,rowspan = 15,columnspan = 1,padx = 0)
button8.grid(row=50,column = 1,rowspan = 1,columnspan = 1,padx = 11)

subButton = Label(image =subButtonImage,bd=0,bg = "#161616")
numDisplay = Label(text = f"{penwidth}",fg = '#c8c8c8',bd = 5,bg ="#161616",font = ("Hack",14) )
addButton = Label(image =addbuttonImage,bd=0,bg = "#161616")

frame.grid(row=1,column = 100,rowspan = 5,columnspan = 5,padx = 12,pady = 15)

p1.grid(row = 1,column = 1,rowspan = 1,columnspan = 1)
p2.grid(row = 1,column = 2,rowspan = 1,columnspan = 1)
p3.grid(row = 1,column = 3,rowspan = 1,columnspan = 1)
p4.grid(row = 1,column = 4,rowspan = 1,columnspan = 1)
p5.grid(row = 1,column = 5,rowspan = 1,columnspan = 1)

p6.grid(row = 2,column = 1,rowspan = 1,columnspan = 1)
p7.grid(row = 2,column = 2,rowspan = 1,columnspan = 1)
p8.grid(row = 2,column = 3,rowspan = 1,columnspan = 1)
p9.grid(row = 2,column = 4,rowspan = 1,columnspan = 1)
p10.grid(row = 2,column = 5,rowspan = 1,columnspan = 1)

p11.grid(row = 3,column = 1,rowspan = 1,columnspan = 1)
p12.grid(row = 3,column = 2,rowspan = 1,columnspan = 1)
p13.grid(row = 3,column = 3,rowspan = 1,columnspan = 1)
p14.grid(row = 3,column = 4,rowspan = 1,columnspan = 1)
p15.grid(row = 3,column = 5,rowspan = 1,columnspan = 1)

p16.grid(row = 4,column = 1,rowspan = 1,columnspan = 1)
p17.grid(row = 4,column = 2,rowspan = 1,columnspan = 1)
p18.grid(row = 4,column = 3,rowspan = 1,columnspan = 1)
p19.grid(row = 4,column = 4,rowspan = 1,columnspan = 1)
p20.grid(row = 4,column = 5,rowspan = 1,columnspan = 1)

p16.grid(row = 4,column = 1,rowspan = 1,columnspan = 1)
p17.grid(row = 4,column = 2,rowspan = 1,columnspan = 1)
p18.grid(row = 4,column = 3,rowspan = 1,columnspan = 1)
p19.grid(row = 4,column = 4,rowspan = 1,columnspan = 1)
p20.grid(row = 5,column = 5,rowspan = 1,columnspan = 1)

p21.grid(row = 5,column = 1,rowspan = 1,columnspan = 1)
p22.grid(row = 5,column = 2,rowspan = 1,columnspan = 1)
p23.grid(row = 5,column = 3,rowspan = 1,columnspan = 1)
p24.grid(row = 5,column = 4,rowspan = 1,columnspan = 1)
p25.grid(row = 5,column = 5,rowspan = 1,columnspan = 1)

p26.grid(row = 6,column = 1,rowspan = 1,columnspan = 1)
p27.grid(row = 6,column = 2,rowspan = 1,columnspan = 1)
p28.grid(row = 6,column = 3,rowspan = 1,columnspan = 1)
p29.grid(row = 6,column = 4,rowspan = 1,columnspan = 1)
p30.grid(row = 6,column = 5,rowspan = 1,columnspan = 1)

p31.grid(row = 6,column = 1,rowspan = 1,columnspan = 1)
p32.grid(row = 6,column = 2,rowspan = 1,columnspan = 1)
p33.grid(row = 6,column = 3,rowspan = 1,columnspan = 1)
p34.grid(row = 6,column = 4,rowspan = 1,columnspan = 1)
p35.grid(row = 6,column = 5,rowspan = 1,columnspan = 1)

p36.grid(row = 4,column = 5,rowspan = 1,columnspan = 1)
p37.grid(row = 7,column = 1,rowspan = 1,columnspan = 1)
p38.grid(row = 7,column = 2,rowspan = 1,columnspan = 1)
p39.grid(row = 7,column = 3,rowspan = 1,columnspan = 1)
p40.grid(row = 7,column = 4,rowspan = 1,columnspan = 1)

p41.grid(row = 7,column = 5,rowspan = 1,columnspan = 1)
p42.grid(row = 8,column = 1,rowspan = 1,columnspan = 1)
p43.grid(row = 8,column = 2,rowspan = 1,columnspan = 1)
p44.grid(row = 8,column = 3,rowspan = 1,columnspan = 1)
p45.grid(row = 8,column = 4,rowspan = 1,columnspan = 1)

p46.grid(row = 8,column = 5,rowspan = 1,columnspan = 1)
canvas.grid(row=1,column =2,rowspan = 50,columnspan = 50)

leftPane.grid(column = 100,row = 1,rowspan = 100,columnspan = 50)
subButton.grid(row = 2,column = 55,rowspan = 28,columnspan = 51)
numDisplay.grid(row = 2,column = 101,rowspan = 28,columnspan = 100)
addButton.grid(row = 2,column = 102,rowspan = 28,columnspan = 100)

############## WIDGET BINDING #####################

button4.bind("<Button-1>",pressedOnEraser)
button1.bind("<Button-1>",pressedOnPencilToolA)
button3.bind("<Button-1>",pressedOnLineBrush)
button2.bind("<Button-1>",pressedOnP2P)

canvas.bind('<B1-Motion>', paint)  # drwaing the line
canvas.bind('<ButtonRelease-1>', reset)
addButton.bind("<Button-1>",add_value)
subButton.bind("<Button-1>",sub_value)

addButton.bind("<B1-Motion>",add_value)
subButton.bind("<B1-Motion>",sub_value)

############## MENU BAR  #####################
menubar = Menu(root)
root.configure(background='#161616', menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Hack", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Page", font=("Hack", 13),command=clearCanvas)
fileMenu.add_command(label="Clear Page",font=("Hack", 13),command=clearCanvas)
fileMenu.add_command(label="Save", font=("Hack", 13))
fileMenu.add_command(label="Save As", font=("Hack", 13))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit, font=("Hack", 13))

editMenu = Menu(menubar, tearoff=0, font=("Hack", 13))
menubar.add_cascade(label="Tools", menu=editMenu)
editMenu.add_command(label="Change Background Color",command = changeBgCanvas)
editMenu.add_separator()
editMenu.add_command(label="Pen")
editMenu.add_command(label="Line Tool")
editMenu.add_command(label="Cascade Tool")
editMenu.add_command(label="Eraser")
editMenu.add_command(label="Change pen color")

root.mainloop()