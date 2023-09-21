from tkinter import *
from tkinter import colorchooser
from tkinter import messagebox
import pyautogui
from tkinter.filedialog import asksaveasfile

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
width = 1000
height =  800
center = height//2
white = (255, 255, 255)
green = (0,128,0)

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
    if tool == "1" or tool == "2" or tool == "3":
        global old_x,old_y
        old_x = None
        old_y = None

def HoverAnimation(e):
    button2.config(image = PencilTool2HoverImage)

def LeaveAnimation(e):
    button2.config(image = PencilTool2Image)

def pressedOnPencilToolA(e):
    global color_fg,tool,old_x,old_y,brush
    old_x = None
    old_y = None
    button1.configure(image= PencilImage)
    button2.configure(image = PencilTool2Image)
    button4.configure(image = EraserToolImage)
    button3.configure(image = LineBrushImage)
    tool = '1'
    brush = ROUND

def pressedOnP2P(e):
    global color_fg,tool,brush
    button2.configure(image = PencilBrush2)
    button1.configure(image =Button1Image)
    button3.configure(image =LineBrushImage)
    button4.configure(image = EraserToolImage)
    color_fg = 'black'
    tool = '2'
    brush = BUTT

def pressedOnLineBrush(e):
    global color_fg, selectedBrush, tool,brush
    tool = 'line'
    button1.configure(image =Button1Image)
    button2.configure(image = PencilTool2Image)
    button3.configure(image = LineBrushToolSelected)
    button4.configure(image = EraserToolImage)
    color_fg = 'black'
    brush = ROUND

def pressedOnEraser(e):
    global selectedBrush,brush,tool
    global color_fg,color_bg
    button1.configure(image =Button1Image)
    button2.configure(image = PencilTool2Image)
    button4.configure(image = EraserSelected)
    button3.configure(image = LineBrushImage)
    color_fg = color_bg
    tool = "3"
    brush = ROUND

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

def save(e):
    files = [('JPEG', '*.jpeg'),('PNG', '*.png')]
    file = asksaveasfile(filetypes = files, defaultextension = files)
    myScreenshot = pyautogui.screenshot(region = (72,20 ,1650,1050))

    myScreenshot.save(file)
    messagebox.showinfo("Paint Application","File Saved Succesfully ")

def saveWithinDirectory(e):
    # file = r"C:\Users\Thanujan.K\PycharmProjects\PaintProjectHittler\United.jpg"
    # myScreenshot = pyautogui.screenshot(region = (72,20 ,1650,1050))
    # myScreenshot.save(file)
    screenshot = pyautogui.screenshot(region = (72,20 ,1650,1050))
    screenshot.save("screenshot.png")

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
frame2 = Frame(root,bg = 'red')
frame3 = Frame(root,bg = 'red')
frame4 = Frame(root,bg = 'red')


def getColorCodeFromButton(e):
    global color_fg,button8
    button8['bg'] = e
    color_fg = e

if tool == "pen":
    pressedOnPencilToolA(E)

def save_delay(e):
    root.after(2000,save(E))

## COLOR PALETS
p1 = Button(frame,bg = '#ff1919',width = 4,height= 2,command=lambda:getColorCodeFromButton("#ff1919"))
p2 = Button(frame,bg = '#ff7733',width = 4,height= 2,command=lambda:getColorCodeFromButton("#ff7733"))
p3 = Button(frame,bg = '#ffbb34',width = 4,height= 2,command=lambda:getColorCodeFromButton("#ffbb34"))
p4 = Button(frame,bg = '#ffff3e',width = 4,height= 2,command=lambda:getColorCodeFromButton("#ffff3e"))
p5 = Button(frame,bg = '#bbfe33',width = 4,height= 2,command=lambda:getColorCodeFromButton("#bbfe33"))

p6 = Button(frame,bg = '#bbfe33',width = 4,height= 2,command=lambda:getColorCodeFromButton("#bbfe33"))
p7 = Button(frame,bg = '#66ff19',width = 4,height= 2,command=lambda:getColorCodeFromButton("#bbfe33"))
p8 = Button(frame,bg = '#33ff77',width = 4,height= 2,command=lambda:getColorCodeFromButton("#bbfe33"))
p9 = Button(frame,bg = '#4dfb88',width = 4,height= 2,command=lambda:getColorCodeFromButton("#3233ff"))
p10 = Button(frame,bg = '#4dffc5',width = 4,height= 2,command=lambda:getColorCodeFromButton("#7734fe"))

p11 = Button(frame,bg = '#33fdfd',width = 4,height= 2)
p12 = Button(frame,bg = '#34baff',width = 4,height= 2)
p13 = Button(frame,bg = '#3377fe',width = 4,height= 2)
p14 = Button(frame,bg = '#3233ff',width = 4,height= 2)
p15 = Button(frame,bg = 'red',width = 4,height= 2)

p16 = Button(frame2,bg = '#ff7d92',width = 4,height= 2)
p17 = Button(frame2,bg = '#fcb9c2',width = 4,height= 2)
p18 = Button(frame2,bg = '#fed3b4',width = 4,height= 2)
p19 = Button(frame2,bg = '#ffe5ce',width = 4,height= 2)
p36 = Button(frame2,bg = '#faf8c9',width = 4,height= 2)

p20 = Button(frame2,bg = 'black',width = 4,height= 2)

p21 = Button(frame2,bg = '#f4f1e7',width = 4,height= 2)
p22 = Button(frame2,bg = '#dcd7f4',width = 4,height= 2)
p23 = Button(frame2,bg = '#c1bbdf',width = 4,height= 2)
p24 = Button(frame2,bg = '#ccd0fe',width = 4,height= 2)

p25 = Button(frame2,bg = '#f4f1e7',width = 4,height= 2)

p26 = Button(frame2,bg = 'black',width = 4,height= 2)
p27 = Button(frame2,bg = 'black',width = 4,height= 2)
p28 = Button(frame2,bg = 'black',width = 4,height= 2)
p29 = Button(frame2,bg = 'black',width = 4,height= 2)
p30 = Button(frame2,bg = 'black',width = 4,height= 2)

p31 = Button(frame3,bg = '#b99976',width = 4,height= 2)
p32 = Button(frame3,bg = '#d2b48c',width = 4,height= 2)
p33 = Button(frame3,bg = '#e5d3b3',width = 4,height= 2)
p34 = Button(frame3,bg = '#987554',width = 4,height= 2)
p35 = Button(frame3,bg = '#664229',width = 4,height= 2)

p37 = Button(frame3,bg = '#8ba88e',width = 4,height= 2)
p38= Button(frame3,bg = '#5a786f',width = 4,height= 2)
p39 = Button(frame3,bg = '#3a4e51',width = 4,height= 2)
p40 = Button(frame3,bg = '#323e45',width = 4,height= 2)
p41 = Button(frame3,bg = '#323e45',width = 4,height= 2)

p42 = Button(frame3,bg = 'orange',width = 4,height= 2)
p43 =  Button(frame3,bg = 'orange',width = 4,height= 2)
p44 = Button(frame3,bg = 'orange',width = 4,height= 2)
p45 = Button(frame3,bg = 'orange',width = 4,height= 2)
p46 = Button(frame3,bg = 'orange',width = 4,height= 2)

p47 = Button(frame4,bg = 'red',width = 4,height= 2)
p48 = Button(frame4,bg = 'red',width = 4,height= 2)
p49 = Button(frame4,bg = 'red',width = 4,height= 2)
p50 = Button(frame4,bg = 'red',width = 4,height= 2)
p51 = Button(frame4,bg = 'red',width = 4,height= 2)

p52 = Button(frame4,bg = 'red',width = 4,height= 2)
p53 = Button(frame4,bg = 'red',width = 4,height= 2)
p54 = Button(frame4,bg = 'red',width = 4,height= 2)
p55 = Button(frame4,bg = 'red',width = 4,height= 2)
p56 = Button(frame4,bg = 'red',width = 4,height= 2)

p57 = Button(frame4,bg = 'red',width = 4,height= 2)
p58 = Button(frame4,bg = 'red',width = 4,height= 2)
p59 = Button(frame4,bg = 'red',width = 4,height= 2)
p60 = Button(frame4,bg = 'red',width = 4,height= 2)
p61 = Button(frame4,bg = 'red',width = 4,height= 2)

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

frame.grid(row=1,column = 100,rowspan =3 ,columnspan = 5,padx = 12)
frame2.grid(row=2,column = 100,rowspan =10 ,columnspan = 5,padx = 12)
frame3.grid(row=3,column = 100,rowspan =25 ,columnspan = 5,padx = 12)
frame4.grid(row=4,column = 100,rowspan =40 ,columnspan = 5,padx = 12)

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

p31.grid(row = 7,column = 1,rowspan = 1,columnspan = 1)
p32.grid(row = 7,column = 2,rowspan = 1,columnspan = 1)
p33.grid(row = 7,column = 3,rowspan = 1,columnspan = 1)
p34.grid(row = 7,column = 4,rowspan = 1,columnspan = 1)
p35.grid(row = 7,column = 5,rowspan = 1,columnspan = 1)

p37.grid(row = 8,column = 1,rowspan = 1,columnspan = 1)
p38.grid(row = 8,column = 2,rowspan = 1,columnspan = 1)
p39.grid(row = 8,column = 3,rowspan = 1,columnspan = 1)
p40.grid(row = 8,column = 4,rowspan = 1,columnspan = 1)
p41.grid(row = 8,column = 5,rowspan = 1,columnspan = 1)

p42.grid(row = 9,column = 1,rowspan = 1,columnspan = 1)
p43.grid(row = 9,column = 2,rowspan = 1,columnspan = 1)
p44.grid(row = 9,column = 3,rowspan = 1,columnspan = 1)
p45.grid(row = 9,column = 4,rowspan = 1,columnspan = 1)
p46.grid(row = 9,column = 5,rowspan = 1,columnspan = 1)

p47.grid(row = 10,column = 1,rowspan = 1,columnspan = 1)
p48.grid(row = 10,column = 2,rowspan = 1,columnspan = 1)
p49.grid(row = 10,column = 3,rowspan = 1,columnspan = 1)
p50.grid(row = 10,column = 4,rowspan = 1,columnspan = 1)
p51.grid(row = 10,column = 5,rowspan = 1,columnspan = 1)

p52.grid(row = 11,column = 1,rowspan = 1,columnspan = 1)
p53.grid(row = 11,column = 2,rowspan = 1,columnspan = 1)
p54.grid(row = 11,column = 3,rowspan = 1,columnspan = 1)
p55.grid(row = 11,column = 4,rowspan = 1,columnspan = 1)
p56.grid(row = 11,column = 5,rowspan = 1,columnspan = 1)

p57.grid(row = 12,column = 1,rowspan = 1,columnspan = 1)
p58.grid(row = 12,column = 2,rowspan = 1,columnspan = 1)
p59.grid(row = 12,column = 3,rowspan = 1,columnspan = 1)
p60.grid(row = 12,column = 4,rowspan = 1,columnspan = 1)
p61.grid(row = 12,column = 5,rowspan = 1,columnspan = 1)


canvas.grid(row=1,column =2,rowspan = 50,columnspan = 50)

leftPane.grid(column = 100,row = 1,rowspan = 100,columnspan = 50)

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
button7.bind("<Button-1>",save)

############## MENU BAR  #####################
menubar = Menu(root)
root.configure(background='#161616', menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("Hack", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="New Page", font=("Hack", 13),command=clearCanvas)
fileMenu.add_command(label="Clear Page",font=("Hack", 13),command=clearCanvas)
fileMenu.add_command(label="Save As", font=("Hack", 13),command = lambda:save_delay(E))
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit, font=("Hack", 13))

editMenu = Menu(menubar, tearoff=0, font=("Hack", 13))
menubar.add_cascade(label="Tools", menu=editMenu)
editMenu.add_command(label="Change Background Color",command = changeBgCanvas)
editMenu.add_separator()
editMenu.add_command(label="Pen",command=lambda:pressedOnPencilToolA(E))
editMenu.add_command(label="Line Tool",command=lambda:pressedOnLineBrush(E))
editMenu.add_command(label="Cascade Tool")
editMenu.add_command(label="Eraser",command=lambda:pressedOnEraser(E))
editMenu.add_command(label="Change pen color",command=colourChose)

root.mainloop()