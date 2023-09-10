from tkinter import *
from tkinter import ttk, colorchooser,filedialog
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import PIL
white = (255, 255, 255)

width = 1000
height =  800
center = height//2
white = (255, 255, 255)
green = (0,128,0)

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
        self.c = Canvas(self.master, width=820, height=770, bg=self.color_bg,bd = 1,relief = 'solid')
        self.header = Label(text = 'Colours',font = ('Aleo',25))

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


        # Creating all buttons

        self.PAD1 = Button(bg='dark red', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD2 = Button(bg='red', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD3 = Button(bg='orange', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD4 = Button(bg='blue', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD5 = Button(bg='dark blue', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD6 = Button(bg='light blue', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD7 = Button(bg='green', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD8 = Button(bg='light green', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD9 = Button(bg='dark green', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD10 = Button(bg='lavender', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD11 = Button(bg='pink', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD12 = Button(bg='magenta', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD13 = Button(bg='orange', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD14 = Button(bg='yellow', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD15 = Button(bg='light yellow', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD16 = Button(bg='grey', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD17 = Button(bg='dark grey', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD18 = Button(bg='light grey', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD19 = Button(bg='black', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD20 = Button(bg='red', font=('beon', 13), width=2, height=1, bd=2, relief='solid')
        self.PAD21 = Button(bg='white', font=('beon', 13), width=2, height=1, bd=2, relief='solid')

        self.PAD22 = Button(font=('beon', 13), width=2, height=1, bd=2, relief='solid', command=color_select_1)
        self.PAD23 = Button(font=('beon', 13), width=2, height=1, bd=2, relief='solid', command=color_select_2)
        self.PAD24 = Button(font=('beon', 13), width=2, height=1, bd=2, relief='solid', command=color_select_3)
        self.PAD25 = Button(font=('beon', 13),text = 'P', width=2, height=1, bd=2, relief='solid', command=None)
        self.PAD26 = Button(font=('beon', 13),text = 'Pe', width=2, height=1, bd=2, relief='solid', command=None)
        self.PAD27 = Button(font=('beon', 13),text = 'E', width=2, height=1, bd=2, relief='solid', command=None)

        self.PAD28 = Button(font=('beon', 13),text = 'NEW', width=10, height=1, bd=2, relief='solid', command= lambda :full_clear())
        self.PAD29 = Button(font=('beon', 13),text = 'IMPORT', width=10, height=1, bd=2, relief='solid', command=None)
        self.PAD30 = Button(font=('beon', 13),text = 'EXPORT', width=10, height=1, bd=2, relief='solid', command=save)
        self.PAD31 = Button(font=('beon', 13),text = 'EXIT', width=10, height=1, bd=2, relief='solid', command=None)
        self.PAD32 = Button(font=('beon', 13),text = 'CREDITS', width=10, height=1, bd=2, relief='solid', command=None)

        self.BAGSETTER = Button(text = 'BACKROUND ',font=('beon', 14), width=10, height=4, bd=2, relief='solid', command=None)

        # Baground Attribute

        def set_baground(b):
            color = colorchooser.askcolor()[1]
            self.c['bg'] = color

        # Gridding Label and Canvas

        self.c.grid(columnspan = 200,rowspan = 100,padx = 150,pady = 10)
        self.header.grid(row = 1,columnspan = 10)

        # Gridding the buttons

        self.PAD1.grid(row = 2,column = 3)
        self.PAD2.grid(row = 2,column = 4)
        self.PAD3.grid(row = 2,column = 5)

        self.PAD4.grid(row = 3,column = 4)
        self.PAD5.grid(row = 3,column = 3)
        self.PAD6.grid(row = 3,column = 5)

        self.PAD7.grid(row = 4,column = 4)
        self.PAD8.grid(row = 4,column = 5)
        self.PAD9.grid(row = 4,column = 3)

        self.PAD10.grid(row = 5,column = 5)
        self.PAD11.grid(row = 5,column = 4)
        self.PAD12.grid(row = 5,column = 3)

        self.PAD13.grid(row = 6,column = 3)
        self.PAD14.grid(row = 6,column = 4)
        self.PAD15.grid(row = 6,column = 5)

        self.PAD16.grid(row = 7,column = 3)
        self.PAD17.grid(row = 7,column = 4)
        self.PAD18.grid(row = 7,column = 5)

        self.PAD19.grid(row = 8,column = 3)
        self.PAD20.grid(row = 8,column = 4)
        self.PAD21.grid(row = 8,column = 5)
        self.PAD25.grid(row = 9,column = 3)
        self.PAD26.grid(row = 9,column = 4)
        self.PAD27.grid(row = 9,column = 5)
        self.PAD28.grid(row = 12,columnspan =10,pady = 10)
        self.PAD29.grid(row = 13,columnspan =10,pady = 5)
        self.PAD30.grid(row = 14,columnspan =10,pady = 5)
        self.PAD31.grid(row = 15,columnspan =10,pady = 5)
        self.BAGSETTER.grid(row = 19,columnspan =10,pady = 10)
        self.PAD32.grid(row = 18,columnspan =10,pady = 5)

        # Labels and Scale

        self.density_label = Label(text = 'Density',font = ('Aleo',20))
        self.density_label.grid(row = 10,columnspan = 10)
        self.brush_sclae = Scale(master, from_=5, to=30, orient=HORIZONTAL,font = ('aloe',12),command=self.changeW,)
        self.brush_sclae.grid(row = 11,columnspan = 10)

        # Binding canvas and buttons

        self.c.bind('<B1-Motion>', self.paint)  # drwaing the line
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.PAD25.bind("<Button>",change_brush)
        self.PAD26.bind("<Button>",change_brush_1)
        self.PAD27.bind("<Button>",eraser)
        self.PAD28.bind("<Button>",full_clear)
        self.BAGSETTER.bind("<Button>",set_baground)
        self.PAD31.bind("<Button>",exit_now)


        # Color Attributes

        def clear(self):
            self.c.delete(ALL)

        def change_color(b):
            self.color_fg = 'dark red'

        def change_color1(b):
            self.color_fg = 'red'

        def change_color2(b):
            self.color_fg = 'orange'

        def change_color3(b):
            self.color_fg = 'blue'

        def change_color4(b):
            self.color_fg = 'dark blue'

        def change_color5(b):
            self.color_fg = 'light blue'

        def change_color6(b):
            self.color_fg = 'green'

        def change_color7(b):
            self.color_fg = 'light green'

        def change_color8(b):
            self.color_fg = 'dark green'

        def change_color9(b):
            self.color_fg = 'lavender'

        def change_color10(b):
            self.color_fg = 'pink'

        def change_color11(b):
            self.color_fg = 'magenta'

        def change_color12(b):
            self.color_fg = 'orange'

        def change_color13(b):
            self.color_fg = 'yellow'

        def change_color14(b):
            self.color_fg = 'light yellow'

        def change_color15(b):
            self.color_fg = 'grey'

        def change_color16(b):
            self.color_fg = 'dark grey'

        def change_color17(b):
            self.color_fg = 'light grey'

        def change_color18(b):
            self.color_fg = 'black'

        def change_color19(b):
            self.color_fg = 'red'

        def change_color20(b):
            self.color_fg = 'white'

        def change_color21(b):
            self.color_fg = self.PAD22['bg']

        # Binding the buttons to their respective colors

        self.PAD1.bind("<Button>",change_color)
        self.PAD2.bind("<Button>",change_color1)
        self.PAD3.bind("<Button>",change_color2)
        self.PAD4.bind("<Button>",change_color3)
        self.PAD5.bind("<Button>",change_color4)
        self.PAD6.bind("<Button>",change_color5)
        self.PAD7.bind("<Button>", change_color6)
        self.PAD8.bind("<Button>", change_color7)
        self.PAD9.bind("<Button>", change_color8)
        self.PAD10.bind("<Button>", change_color9)
        self.PAD11.bind("<Button>", change_color10)
        self.PAD12.bind("<Button>", change_color11)
        self.PAD13.bind("<Button>", change_color12)
        self.PAD14.bind("<Button>", change_color13)
        self.PAD15.bind("<Button>", change_color14)
        self.PAD16.bind("<Button>", change_color15)
        self.PAD17.bind("<Button>", change_color16)
        self.PAD18.bind("<Button>", change_color17)
        self.PAD19.bind("<Button>", change_color18)
        self.PAD20.bind("<Button>", change_color19)
        self.PAD21.bind("<Button>", change_color20)
        self.PAD22.bind("<Button>", change_color21)

    # The Paint Atribute
    def paint(self,e):
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, e.x, e.y, width=self.penwidth, fill=self.color_fg,
                               capstyle=self.brush, smooth=False)

        self.old_x = e.x
        self.old_y = e.y

    # change Width of pen through slider
    def changeW(self, e):
        self.penwidth = e

    # reseting the position of brush in the canvas
    def reset(self, e):
        self.old_x = None
        self.old_y = None





# The Actual MainLoop

if __name__ == '__main__':
    root = Tk()
    main(root)
    root.geometry('1000x800')
    root.resizable(False,False)
    root.title('Paint Application')
    root.mainloop()