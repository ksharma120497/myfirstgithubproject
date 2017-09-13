import tkinter
from tkinter import messagebox
top=tkinter.Tk()
i=1

def score(): 
        if(btn10['text']==btn20['text'] and btn20['text']==btn30['text'] and btn10['text']!="             " and btn20['text']!="             " and btn30['text']!="             "):
                winner=btn10['text']
                messagebox.showinfo("Winner",winner+" wins! ")
        elif(btn11['text']==btn21['text'] and btn21['text']==btn31['text'] and btn11['text']!="             " and btn21['text']!="             " and btn31['text']!="             "):
                winner=btn11['text']
                messagebox.showinfo("Winner",winner+" wins!")
        elif(btn12['text']==btn22['text'] and btn22['text']==btn32['text'] and btn12['text']!="             " and btn22['text']!="             " and btn32['text']!="             "):
                winner=btn12['text']
                messagebox.showinfo("Winner",winner+" wins!")
        elif(btn10['text']==btn11['text'] and btn11['text']==btn12['text'] and btn10['text']!="             " and btn11['text']!="             " and btn12['text']!="             "):
                winner=btn10['text']
                messagebox.showinfo("Winner",winner+" wins!")
        elif(btn20['text']==btn21['text'] and btn21['text']==btn22['text'] and btn20['text']!="             " and btn21['text']!="             " and btn22['text']!="             "):
                winner=btn20['text']
                messagebox.showinfo("Winner",winner+" wins! ")
        elif(btn30['text']==btn31['text'] and btn31['text']==btn32['text'] and btn30['text']!="             " and btn31['text']!="             " and btn32['text']!="             "):
                winner=btn30['text']
                messagebox.showinfo("Winner",winner+" wins! ")
        else:
                messagebox.showinfo("Draw","Match Draw")
        


def chng10():
        global i
        if i==1:
            btn10.config(text='X')
            btn10.config(state="disabled")
            i=0;
            score()
        else:
            btn10.config(text='O')
            btn10.config(state="disabled")
            i=1;
            score()
            
def chng11():
        global i
        if i==1:
            btn11.config(text='X')
            btn11.config(state="disabled")
            i=0;
            score()
        else:
            btn11.config(text='O')
            btn11.config(state="disabled")
            i=1;
            score()
def chng12():
        global i
        if i==1:
            btn12.config(text='X')
            btn12.config(state="disabled")
            i=0;
            score()
        else:
            btn12.config(text='O')
            btn12.config(state="disabled")
            i=1;
            score()
def chng20():
        global i
        if i==1:
            btn20.config(text='X')
            btn20.config(state="disabled")
            i=0;
            score()
        else:
            btn20.config(text='O')
            btn20.config(state="disabled")
            i=1;
            score()
def chng21():
        global i
        if i==1:
            btn21.config(text='X')
            btn21.config(state="disabled")
            i=0;
            score()
        else:
            btn21.config(text='O')
            btn21.config(state="disabled")
            i=1;
            score()
def chng22():
        global i
        if i==1:
            btn22.config(text='X')
            btn22.config(state="disabled")
            i=0;
            score()
        else:
            btn22.config(text='O')
            btn22.config(state="disabled")
            i=1;
            score()
def chng30():
        global i
        if i==1:
            btn30.config(text='X')
            btn30.config(state="disabled")
            i=0;
            score()
        else:
            btn30.config(text='O')
            btn30.config(state="disabled")
            i=1;
            score()
def chng31():
        global i
        if i==1:
            btn31.config(text='X')
            btn31.config(state="disabled")
            i=0;
            score()
        else:
            btn31.config(text='O')
            btn31.config(state="disabled")
            i=1;
            score()
def chng32():
        global i
        if i==1:
            btn32.config(text='X')
            btn32.config(state="disabled")
            i=0;
            score()
        else:
            btn32.config(text='O')
            btn32.config(state="disabled")
            i=1;
            score()
def newgame():
        global i
        i=1
        btn10.config(text="             ")
        btn11.config(text="             ")
        btn12.config(text="             ")
        btn20.config(text="             ")
        btn21.config(text="             ")
        btn22.config(text="             ")
        btn30.config(text="             ")
        btn31.config(text="             ")
        btn32.config(text="             ")
        btn10.config(state="normal")
        btn11.config(state="normal")
        btn12.config(state="normal")
        btn20.config(state="normal")
        btn21.config(state="normal")
        btn22.config(state="normal")
        btn30.config(state="normal")
        btn31.config(state="normal")
        btn32.config(state="normal")
    
btn10=tkinter.Button(top,text="             ",command=chng10)
btn10.grid(row=1,column=0)
btn11=tkinter.Button(top,text="             ",command=chng11)
btn11.grid(row=1,column=1)
btn12=tkinter.Button(top,text="             ",command=chng12)
btn12.grid(row=1,column=2)
btn20=tkinter.Button(top,text="             ",command=chng20)
btn20.grid(row=2,column=0)
btn21=tkinter.Button(top,text="             ",command=chng21)
btn21.grid(row=2,column=1)
btn22=tkinter.Button(top,text="             ",command=chng22)
btn22.grid(row=2,column=2)
btn30=tkinter.Button(top,text="             ",command=chng30)
btn30.grid(row=3,column=0)
btn31=tkinter.Button(top,text="             ",command=chng31)
btn31.grid(row=3,column=1)
btn32=tkinter.Button(top,text="             ",command=chng32)
btn32.grid(row=3,column=2)
btn1=tkinter.Button(top,text="New Game",command=newgame)
btn1.grid(row=6,column=1)
top.title("X & O")
top.mainloop()
