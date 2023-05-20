from tkinter import *
from Nim_variante_part3_Naumova_Silva import *
from Text import *


# ----------------------------------
wind = Tk()

# ----------------------------------
bg = '#C3C3C3'
wind.title("Jeu de Nim")
wind.geometry("850x760")
wind.minsize(1280, 720)
wind.config(background=bg)
Font = ("Comic Sans MS", 20, "bold")
lab = Label(wind, text='', font=Font, bg='#95C8F0')


def gagne():
    delete()
    gg = Label(wind, text='VOUS AVEZ GAGNER',
               font=Font, bg='#95C8F0')
    gg.pack(expand=YES)


def regles():
    global lab
    lab.destroy()
    lab = Label(wind, text=commande['rules'], font=Font, bg=bg)
    lab.place(x=0, y=600)



def TG():
    global lab
    lab.destroy()
    lab = Label(wind, text='TG FLORIAN', font=Font, bg=bg)
    lab.place(x=0, y=600)


def wd_destroy():
    wind.destroy()


def delete():
    for c in wind.winfo_children():
        c.destroy()


def menu():
    frame_start = Frame(wind, bg=bg)

    tire = Label(wind, text="\nLE JEU DE NIM MARIENBAD",
                 font=Font, bg=bg)
    tire.pack()
    sous_tire = Label(frame_start, text="Voulez vous commencer le jeu?\nCliqez sur START\n", font=
        Font, bg=bg)
    sous_tire.pack()
    frame_start.pack(expand=YES)
    start = Button(frame_start, text='START', font=Font, bg='azure',
                   fg='black', command=run).pack(expand=YES, ipady=10, padx=10, pady=10)
    bt_quit = Button(frame_start, text='Quitter', font=Font, bg='azure', fg='black',  command=wd_destroy).pack(expand=YES)


def run():
    delete()
    cnv = Canvas(wind, width=450, height=600,
                 bg=bg, bd=0, highlightthickness=0)
    cnv.place(x=0, y=0)
    photo(cnv)
    cmd()
def allu ():
    print ("test")

def photo(cnv):
    test = PhotoImage(file="placeholder.gif")
    cnv.test = test
    h = 65
    for i in range(len(tab)):
        r = tab[i]
        l = 20
        s = 0
        while s <= r:
            cnv.create_image(l, h, image=test)
            l = l+50
            s = s+1
        h = h+150
    Button(wind, image=test,command=allu).pack(side=TOP)

def cmd():
    def setTextOnMouseOver(self):
        button.config(text=commande['rules'])

    def setTextOnMouseLeave(self):
        button.config(text="Régles")
    frame1 = Frame(wind, bg='#95C8F0')

    sous_tire = Label(frame1, text="Parametres du jeu",
                      font=Font, bg='#95C8F0')
    sous_tire.pack()
    frame1.place(x=550, y=0)
    button = Button(wind, text="Régles", font=Font,
                    bg='azure', fg='black', command=regles)
    button.place(x=700, y=70)
    button2 = Button(wind, text="EXIT", font=Font,
                     bg='azure', fg='black', command=wd_destroy)
    button2.place(x=720, y=140)
    button3 = Button(wind, text="TG", font=Font,
                     bg='azure', fg='black', command=TG)
    button3.place(x=715, y=210)


def console(event):
    frame = Frame(wind, bg='#95C8F0')
    if event == regles:
        sous_tire = Label(frame, text=commande['rules'], font=Font, bg='#95C8F0')
        sous_tire.pack()

    frame.place(fill=X, x=0, y=600)


menu()
wind.mainloop()
