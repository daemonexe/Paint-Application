import random
from tkinter import *

root = Tk()
root.geometry('1920x1080')
root.resizable(False, False)
root.overrideredirect(True)
root.title('Paint Application')

############## IMAGES SRC #####################
SidePanelImage = PhotoImage(file = "sidepanel.png")
LeftSidePanelImage = PhotoImage(file= "leftsidepannel.png")
Button1Image = PhotoImage(file = "Button.png")



############## DEFINED VARIABLES #####################
color_fg = 'black'
color_bg = 'white'
old_x = None
old_y = None
penwidth = 5
brush = ROUND



############## CANVAS FUNCTIONS #####################
def paint(e):
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


def reset(e):
    global old_x,old_y
    old_x = None
    old_y = None


############## WIDGET CREATIONS #####################
canvas = Canvas(root,highlightthickness = 0, width=1650, height=1060, bg="white",bd = 1,relief = 'solid')
pane = Label(root,bd = 0,image = SidePanelImage)
leftPane = Label(root,bd = 0,image = LeftSidePanelImage)
button1 = Label(root,bd = 0,image = Button1Image)
button2 = Label(root,bd = 0,image = Button1Image)
button3 = Label(root,bd = 0,image = Button1Image)
button4 = Label(root,bd = 0,image = Button1Image)
button5 = Label(root,bd = 0,image = Button1Image)
button6 = Label(root,bd = 0,image = Button1Image)
button7 = Label(root,bd = 0,image = Button1Image)
button8 = Label(root,bd = 0,bg ='black')

############## WIDGET GRIDDING #####################
button1.grid(row=1,column = 1,rowspan = 1,columnspan = 1,padx = 12,pady = 1)
button2.grid(row=2,column = 1,rowspan = 1,columnspan = 1,padx = 10)
button3.grid(row=3,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button4.grid(row=4,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button5.grid(row=5,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button6.grid(row=6,column = 1,rowspan = 1,columnspan = 1,padx = 11)
button7.grid(row=7,column = 1,rowspan = 1,columnspan = 1,padx = 11)

canvas.grid(row=1,column =2,rowspan = 50,columnspan = 50)
leftPane.grid(column = 100,row = 1,rowspan = 100,columnspan = 50)

############## WIDGET BINDING #####################
canvas.bind('<B1-Motion>', paint)  # drwaing the line change to button 1 and remove reset to line tool
canvas.bind('<ButtonRelease-1>',reset)

############## MENU BAR  #####################
menubar = Menu(root)
root.configure(background='#161616', menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Hack", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Page", font=("Hack", 13))
fileMenu.add_command(label="Clear Page",font=("Hack", 13))
fileMenu.add_command(label="Save", font=("Hack", 13))
fileMenu.add_command(label="Save As", font=("Hack", 13))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit, font=("Hack", 13))

editMenu = Menu(menubar, tearoff=0, font=("Hack", 13))
menubar.add_cascade(label="Tools", menu=editMenu)
editMenu.add_command(label="Change Background Color")
editMenu.add_separator()
editMenu.add_command(label="Pen")
editMenu.add_command(label="Line Tool")
editMenu.add_command(label="Cascade Tool")
editMenu.add_command(label="Eraser")
editMenu.add_command(label="Change pen color")

root.mainloop()