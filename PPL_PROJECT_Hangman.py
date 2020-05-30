from tkinter import *
from tkinter import messagebox
from string import ascii_uppercase
import random



global x
x=0
window1=Tk()
window1.title("Hangman")
window1.config(bg="pink")
word_list=["parrot","eagle","sparrow","pigeon","crow","kite","kiwi","kingfisher","crane","duck","peacock","cuccoo","swallow","swan"]

photos=[PhotoImage(file="images/hang0.png"),PhotoImage(file="images/hang1.png"),PhotoImage(file="images/hang2.png"),
        PhotoImage(file="images/hang3.png"),PhotoImage(file="images/hang4.png"),PhotoImage(file="images/hang5.png"),
        PhotoImage(file="images/hang6.png"),PhotoImage(file="images/hang7.png"),PhotoImage(file="images/hang8.png"),
        PhotoImage(file="images/hang9.png"),PhotoImage(file="images/hang10.png"),PhotoImage(file="images/hang11.png")]
def setx1():
    x=1
    newgame1()
def setx2():
    x=2
    newgame2()

def newgame1():
    e1.set("")
    word=random.choice(word_list)
    word=word.upper()
    global the_word_withspaces
    global no_guesses
    no_guesses=0
    imgLabel.config(image=photos[0])
    the_word=word
    the_word_withspaces=" ".join(the_word)
    lblword.set(" ".join("_"*len(the_word)))

def newgame2():
    word = e1.get()
    e1.set("")
    for i in word:
        if i.isdigit():
            messagebox.showwarning("Error","Input a valid word")
    word=word.upper()
    global the_word_withspaces
    global no_guesses
    no_guesses=0
    imgLabel.config(image=photos[0])
    the_word=word
    the_word_withspaces=" ".join(the_word)
    lblword.set(" ".join("_"*len(the_word)))

def guess(alphabet):
    global no_guesses
    if no_guesses<11:
        txt=list(the_word_withspaces)
        guessed=list(lblword.get())

        if the_word_withspaces.count(alphabet)>0:
            for c in range(len(txt)):
                if(txt[c])==alphabet:
                    guessed[c]=alphabet
                lblword.set("".join(guessed))
                if lblword.get()==the_word_withspaces:
                    messagebox.showinfo("Hangman","You Guessed it!!")
        else:
            no_guesses+=1
            imgLabel.config(image=photos[no_guesses])
            if no_guesses==11:
                messagebox.showwarning("Hangman","GameOver")


imgLabel=Label(window1,width=100,height=150)
imgLabel.grid(row=0,column=0,columnspan=3,padx=10,pady=40)
imgLabel.config(image=photos[0])
lblword=StringVar()
word=StringVar()
Label(window1,textvariable=lblword,font=("courier",22,'italic','bold'),fg="green").grid(row=0,column=3,columnspan=6,padx=10,pady=5)


n=0
for c in ascii_uppercase:
    Button(window1,text=c,command=lambda c=c: guess(c), font=("seriff"),width=4,bg="black",fg="white").grid(row=1+n//9,column=n%9)
    n+=1
def new():
    messagebox.showinfo("Press button","Choose 1 or 2 players")

e1=StringVar()
Button(window1,text="New\nGame",command=lambda:new(),font=("seriff",6),bg="blue",fg="white").grid(row=3,column=8,sticky="NSWE")
Button(window1,text="1 Player",command=lambda:setx1(),font=("seriff",8),bg="blue",fg="white").grid(row=4,column=0)
Button(window1,text="2 Player",command=lambda:setx2(),font=("seriff",8),bg="blue",fg="white").grid(row=4,column=2)
Label(window1,text="Enter Your Word : ",command=None,font=("seriff",10,'bold'),fg="White",bg="orange").grid(row=5,column=0,columnspan=4,padx=10,pady=10)
Entry(window1,width=25,textvariable=e1).grid(row=5,column=4,columnspan=4,padx=10,pady=10,)


window1.mainloop()
