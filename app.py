import random
from tkinter import *
from tkinter import colorchooser

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


############## DEFINED VARIABLES #####################
color_fg = 'black'
color_bg = 'white'
old_x = None
old_y = None
penwidth = 5
brush = ROUND
selectedBrush = "default"


############## CANVAS FUNCTIONS #####################
def paint(e):
    global selectedBrush
    if selectedBrush == "default":
        global old_x
        global old_y

        if old_x and old_y:
            canvas.create_line(old_x, old_y, e.x, e.y, width=penwidth, fill=color_fg,
                               capstyle=brush, smooth=False)
        old_x = e.x
        old_y = e.y

        # remove old x oldy = e.x or e.y to remove this
        # to create a diagonal layout replace e.x to e.y
        # add + 500 e.x and keep the same for e.y and vise versa

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
    global old_x,old_y
    old_x = None
    old_y = None

def HoverAnimation(e):
    button2.config(image = PencilTool2HoverImage)

def LeaveAnimation(e):
    button2.config(image = PencilTool2Image)


############## WIDGET CREATIONS #####################
canvas = Canvas(root,highlightthickness = 0, width=1650, height=1060, bg="white",bd = 1,relief = 'solid')
pane = Label(root,bd = 0,image = SidePanelImage)
leftPane = Label(root,bd = 0,image = LeftSidePanelImage)
button1 = Label(root,bd = 0,image = Button1Image)
button2 = Label(root,bd = 0,image = PencilTool2Image)
button3 = Label(root,bd = 0,image = LineBrushImage)
button4 = Label(root,bd = 0,image = EraserToolImage)
button5 = Label(root,bd = 0,image = Button1Image)
button6 = Label(root,bd = 0,image = Button1Image)
button7 = Label(root,bd = 0,image = Button1Image)
button8 = Button(root,bd = 5,bg = color_fg,width= 5, height= 2,relief= SUNKEN,command= colourChose)

## COLOR PALETS
P1 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P2 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P3 = Label(root,bd = 0,bg = "red",width= 4, height= 2)
P4 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P5 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P6 = Label(root,bd = 0,bg = "red",width= 4, height= 2)
P7 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P8 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P9 = Label(root,bd = 0,bg = "red",width= 4, height= 2)
P10 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P11 = Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P12 = Label(root,bd = 0,bg = "red",width= 4, height= 2)
P13= Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P14= Label(root,bd = 0,bg = 'red',width= 4, height= 2)
P15= Label(root,bd = 0,bg = "red",width= 4, height= 2)


############## WIDGET GRIDDING #####################
button1.grid(row=1,column = 1,rowspan = 1,columnspan = 1,padx = 12,pady = 1)
button2.grid(row=2,column = 1,rowspan = 1,columnspan = 1,padx = 10)
button3.grid(row=3,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button4.grid(row=4,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button5.grid(row=5,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button6.grid(row=6,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button7.grid(row=41,column = 1,rowspan = 15,columnspan = 1,padx = 0)
button8.grid(row=50,column = 1,rowspan = 1,columnspan = 1,padx = 11)

P1.grid(row=2,column = 70,rowspan = 1,columnspan = 1,padx = 28)
P2.grid(row=2,column = 72,rowspan = 1,columnspan = 1)
P3.grid(row=2,column = 74,rowspan = 1,columnspan = 1,padx = 27)
P4.grid(row=3,column = 70,rowspan = 1,columnspan = 1,padx = 28)
P5.grid(row=3,column = 72,rowspan = 1,columnspan = 1)
P6.grid(row=3,column = 74,rowspan = 1,columnspan = 1,padx = 27)
P7.grid(row=4,column = 70,rowspan = 1,columnspan = 1,padx = 28)
P8.grid(row=4,column = 72,rowspan = 1,columnspan = 1)
P9.grid(row=4,column = 74,rowspan = 1,columnspan = 1,padx = 27)

P10.grid(row=5,column = 70,rowspan = 1,columnspan = 1,padx = 28)
P11.grid(row=5,column = 72,rowspan = 1,columnspan = 1)
P12.grid(row=5,column = 74,rowspan = 1,columnspan = 1,padx = 27)

P13.grid(row=6,column = 70,rowspan = 1,columnspan = 1,padx = 28)
P14.grid(row=6,column = 72,rowspan = 1,columnspan = 1)
P15.grid(row=6,column = 74,rowspan = 1,columnspan = 1,padx = 27)


canvas.grid(row=1,column =2,rowspan = 50,columnspan = 50)
leftPane.grid(column = 100,row = 1,rowspan = 100,columnspan = 50)

############## WIDGET BINDING #####################

canvas.bind('<B1-Motion>', paint)  # drwaing the line change to button 1 and remove reset to line tool
canvas.bind('<ButtonRelease-1>',reset)

button2.bind('<Enter>', HoverAnimation)  # drwaing the line change to button 1 and remove reset to line tool
button2.bind('<Leave>', LeaveAnimation)  # drwaing the line change to button 1 and remove reset to line tool


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