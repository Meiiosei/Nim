import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
bg = '#C3C3C3'
root.title("Jeu de Nim")
root.geometry("1280x720")
root.minsize(1280, 720)
root.maxsize(1280, 720)
root.config(background=bg)
Font = ("Comic Sans MS", 20, "bold")


# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

def clickFunction(event):
    print ("test")
def test (event):
    print(event)
# username
j1_label = ttk.Label(root, text="Joueur 1", font = Font)
j1_label.grid(column=0, row=0, sticky=tk.NW)




# password
score_label = ttk.Label(root, text = "score", font = Font)
score_label.grid(column=1, row=0, sticky=tk.N)
def test_ ():
    print ("dnzqndozq")

j2_label = ttk.Label(root, text = "Joueur 2", font = Font)
j2_label.grid(column=2, row=0, sticky=tk.NE)

# login button

login_button = ttk.Label(root, text="Login",font=Font)
login_button.grid(column=0, row=4, sticky=tk.W, padx=5, pady=5)
login_button.bind("<Button-1>", test)

login_button2 = ttk.Label(root, text="Login",font=Font)
login_button2.grid(column=0, row=5, sticky=tk.W, padx=5, pady=5)
login_button2.bind("<Button-1>", test)

root.mainloop()