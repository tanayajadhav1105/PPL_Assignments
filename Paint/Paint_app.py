from tkinter import *
from tkinter import ttk,colorchooser

class paint():
    def __init__(self,root):
        self.root=root
        self.root.title("Paint")
        self.root.geometry("1000x600")
        self.root.configure(background='white')
        self.root.resizable(1,1)

        self.penColor="black"
        self.bgColor="white"

        self.m_frame = LabelFrame(self.root, text="Palette", font=("seriff,14"), bd=5, relief=RIDGE, bg="white")
        self.m_frame.place(x=0, y=0, width=120, height=595)

        self.color_frame = LabelFrame(self.m_frame,text="Colors",font =("seriff,13"),bd =5,relief=RIDGE,bg="silver")
        self.color_frame.place(x=0,y=0,width=85,height=190)
        self.color_frame.grid(row=0,column=1,padx=12)

        colors = ["black","white","red","green","blue","yellow","pink","orange","brown","violet","grey","magenta"]
        i=j=0
        for color in colors:
            Button(self.color_frame,bg=color,bd=2,relief=RIDGE,width=4,command=lambda col=color:self.selectColor(col)).grid(row=i,column=j)
            j+=1
            if j==2:
                j=0
                i+=1
        self.brushcolor=Button(self.m_frame, text="More Colors", bg="silver", bd=3, relief=RIDGE, command=self.more_colors,width=11)
        self.brushcolor.place(x=0,y=195)
        self.brushcolor.grid(row=2, column=1, padx=12)

        self.p_frame = LabelFrame(self.m_frame, text="Tools", font=("seriff,13"), bd=5, relief=RIDGE, bg="white")
        self.p_frame.place(x=0, y=225, width=85, height=200)
        self.p_frame.grid(row=3, column=1, padx=12)
        self.eraser=Button(self.p_frame,text="Eraser",bg="silver",bd=3,relief=RIDGE,command=self.eraser,width=9).grid(row=1,column=1)
        self.clear=Button(self.p_frame,text="Clear",bg="silver",bd=3,relief=RIDGE,command=lambda :self.canvas.delete(ALL),width=9).grid(row=2,column=1)
        self.bgcolor=Button(self.p_frame, text="BgColor", bg="silver", bd=3, relief=RIDGE, command=self.bg_color, width=9).grid(row=3, column=1)


        self.size_frame = LabelFrame(self.m_frame, text="Size", font=("seriff,13"), bd=5, relief=RIDGE, bg="white")
        self.size_frame.place(x=0, y=380, width=85, height=180)
        self.size_frame.grid(row=4, column=1, padx=12)
        self.size=Scale(self.size_frame,orient=VERTICAL,from_=50,to=1,length = 150)
        self.size.set(1)
        self.size.grid(row=0,column=1,padx=27)

        self.canvas = Canvas(self.root,bg="white",bd=5,relief=GROOVE,height = 585,width=860)
        self.canvas.place(x=125,y=0)

        self.canvas.bind("<B1-Motion>",self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)
        self.x1=None
        self.y1=None

    def paint(self, e):
        if self.x1 and self.y1:
            self.canvas.create_line(self.x1,self.y1, e.x, e.y, width=self.size.get(), fill=self.penColor,capstyle=ROUND, smooth=True)
        self.x1 = e.x
        self.y1 = e.y

    def reset(self,e):
        self.x1 = None
        self.y1 = None

    def selectColor(self,col):
        self.penColor=col

    def more_colors(self):
        self.penColor = colorchooser.askcolor(color=self.penColor)[1]

    def eraser(self):
        self.penColor="white"

    def bg_color(self):
        self.bgColor = colorchooser.askcolor(color=self.bgColor)[1]
        #color=colorchooser.askcolor()
        self.canvas['bg']=self.bgColor


if __name__=="__main__":
    root = Tk()
    p = paint(root)
    root.mainloop()