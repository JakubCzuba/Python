import tkinter as tk
import random

root = tk.Tk()
root.geometry("800x500")
root.title("Stupid game")



frametop = tk.Frame(root, bg="linen")
frametop.place(relheight=0.2, relwidth=1)

labeltop = tk.Label(frametop, text="Witaj w grze", bg="linen")
labeltop.place(relx=0.45, rely=0.4)



randomint = random.randint(1,4)



frameleft = tk.Frame(root, bg="powder blue")
frameleft.place(relx=0, rely=0.2, relwidth=0.33, relheight=1)

labelleft = tk.Label(frameleft, text="Zgadnij liczbę:", bg="powder blue")
labelleft.grid(row=0, column=0, pady=10, padx=5)

entryfield= tk.Entry(frameleft, bg="linen")
entryfield.grid(row=1, column=1, pady=10, padx=5)



def getdata():
    guess = entryfield
    if guess == "1" or guess == "2":
        return labelend.config(text="Twoja liczba to: " + guess), labelgood.config(text="Brawo, odgadnąłeś liczbę!"), labelbad.config(text="")
    else: 
        return labelend.config(text="Twoja liczba to: " + guess), labelgood.config(text=""), labelbad.config(text="Brawo, odgadnąłeś liczbę!")



buttondata = tk.Button(labelleft, bg="Linen", text="Zapisz", command=getdata)
buttondata.grid(row=2, column=0, padx=10, pady=10)

labelend = tk.Label(frameleft, bg="powder blue")
labelend.grid(row=3, column=1)

labelgood = tk.Label(frameleft, bg="powder blue")
labelgood.grid(row=3, column=0, padx=10, pady=10)

labelbad = tk.Label(frameleft, bg="powder blue")
labelbad.grid(row=4, column=1, padx=10, pady=10)

labeltest = tk.Label(frameleft, bg="powder blue", text= randomint)
labeltest.grid(row=10, column=0, padx=10, pady=10)


root.mainloop()