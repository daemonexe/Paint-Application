from tkinter import *
from tkinter import ttk, colorchooser,filedialog
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import PIL
import tkinter.ttk as ttk

white = (255, 255, 255)
width = 1000
height =  800
center = height//2
white = (255, 255, 255)
green = (0,128,0)

# images


# Main class

class main:
    def __init__(self, master):
        self.master = master
        self.color_fg = 'black'
        self.color_bg = 'white'
        self.old_x = None
        self.old_y = None
        self.penwidth = 5
        self.brush = ROUND
        self.c = Canvas(self.master, width=1650, height=1050, bg=self.color_bg,bd = 1,relief = 'solid')
        path = "sidepanel.png"
        img = ImageTk.PhotoImage(Image.open(path))
        panel = Label(root, image=img,bd =0)
        panel.photo = img
        self.c.grid(row=1,column =5,columnspan = 5,rowspan = 55)
        panel.grid(column=1, row=45,rowspan = 22,columnspan =3)


        # Creating the color pads
        def color_select_1():
            global color
            color = colorchooser.askcolor()[1]
            self.PAD22['bg'] = color

        def color_select_2():
            color = colorchooser.askcolor()[1]
            self.PAD23['bg'] = color

        def color_select_3():
            color = colorchooser.askcolor()[1]
            self.PAD24['bg'] = color

        def change_brush(b):
            self.brush = BUTT

        def change_brush_1(b):
            self.brush = ROUND

        def eraser(b):
            self.color_fg = 'white'

        def exit_now(b):
            root.destroy()

        def full_clear():
            self.c.delete(ALL)
            self.c['bg'] = 'white'

        def save():
            filename = "image.png"
            image1.save(filename)
            draw.line([0, center, width, center], green)

        image1 = PIL.Image.new("RGB", (width, height), white)
        draw = ImageDraw.Draw(image1)

        def set_baground(b):
            color = colorchooser.askcolor()[1]
            self.c['bg'] = color

        def clear(self):
            self.c.delete(ALL)

        self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
        self.c.bind('<ButtonRelease-1>', self.reset)


    def exit(self):
        root.destroy()
        print("did it exit?")





    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                               capstyle=self.brush, smooth=False)

        self.old_x = e.x
        self.old_y = e.y

    def changeW(self, e):
        self.penwidth = e

    def reset(self, e):
        self.old_x = None
        self.old_y = None



# The Actual MainLoop
if __name__ == '__main__':
    root = Tk()
    main(root)
    root.geometry('1920x1080')
    root.resizable(False,False)
    root.overrideredirect(True)
    root.title('Paint Application')

    menubar = Menu(root)
    root.configure(background='#2b2d30',menu= menubar)

    fileMenu = Menu(menubar, tearoff=0, font=("Hack", 15))
    menubar.add_cascade(label="File", menu=fileMenu)
    fileMenu.add_command(label="New Page",font = ("Hack",13))
    fileMenu.add_command(label="Save",font = ("Hack",13))
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit",command=exit,font = ("Hack",13))

    editMenu = Menu(menubar, tearoff=0, font=("Hack", 13))
    menubar.add_cascade(label="Tools",menu = editMenu)
    editMenu.add_command(label="Change Background Color")
    editMenu.add_command(label="Clear Page")
    editMenu.add_separator()
    editMenu.add_command(label="Pen")
    editMenu.add_command(label="Line Tool")
    editMenu.add_command(label="Cascade Tool")
    editMenu.add_command(label="Eraser")



    root.mainloop()