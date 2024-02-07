from tkinter import *


langas = Tk()

def spausdinti():
    ivesta = ivedimo_laukas.get()
    rezultatas["text"] = (f"Labas, {ivesta}!")
    status["text"] = "Sukurta"

def isvalyti():
    rezultatas["text"] = ""
    status["text"] = "Išvalyta"
def atkurti():
    spausdinti()
    status["text"] = "Atkurta"

def iseiti():
    langas.destroy()

langas.title("My first program!")
langas.iconbitmap(r'cpu_uls_icon.ico')
langas.geometry("330x105")
langas.resizable(False, False)
vardo_ivestis = Label(langas, text="Įveskite vardą: ")
mygtukas1 = Button(text="Patvirtinti", command=spausdinti)
langas.bind("<Return>", lambda event: spausdinti())
langas.bind("<Escape>", lambda event: iseiti())
ivedimo_laukas = Entry(langas)
rezultatas = Label(langas, text="")
meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff = 0)
status = Label(langas, text="", bd=1, relief=SUNKEN, anchor=W)


vardo_ivestis.grid(row=0, column=0)
mygtukas1.grid(row=0, column=2)
ivedimo_laukas.grid(row=0, column=1)
rezultatas.grid(row=1, columnspan=3)
status.grid(row=3, columnspan=4, sticky=W+E)

meniu.add_cascade(label="Meniu", menu=submeniu)
submeniu.add_command(label="Išvalyti", command=isvalyti)
submeniu.add_command(label="Atkurti", command=atkurti)
submeniu.add_separator()
submeniu.add_command(label="Išeiti", command=lambda: langas.destroy())

langas.mainloop()

# Padaryti paleidžiamąjį failą iš 11 paskaitos 4 programos
# (pilna programa su vartotojo sąsaja)
# Programa turi turėti programos lango ikoną ir norimą pavadinimą
# Paleidžiamasis failas turi turėti norimą ikoną