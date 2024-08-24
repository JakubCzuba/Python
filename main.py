import tkinter as tk
import random

root = tk.Tk()
root.geometry("800x500")
root.title("First py")



frametop = tk.Frame(root, bg="linen")
frametop.place(relwidth=1, relheight=0.2)

labelhead = tk.Label(frametop, text = "Wprowadź dane", font=("Arial", 20), bg="linen") 
labelhead.place(relx=0.45, rely=0.4)



ranodomint = random.randint(1,2)



frameleft = tk.Frame(root, bg="powder blue")
frameleft.place(relx=0, rely=0.2, relwidth=0.33, relheight=1)

labelguess = tk.Label(frameleft, bg="powder blue", text="Zgadnij liczbę:")
labelguess.grid(row=0, column=0, pady=10, padx=5)

myentry:int = tk.Entry(frameleft)
myentry.grid(row=0, column=1, padx=10, pady=10)



def get_data():
    dataint:int = myentry.get()
    labelLiczba.config(text= "Twoje odpowiedź to: " + dataint)
    if dataint == ranodomint: 
        return labeltrue.config(text="Brawo, wygrałeś"), labelfalse.config(text="")                
    else:
        return labelfalse.config(text="Przegrałeś"), labeltrue.config(text="")

button_get_data = tk.Button(frameleft, text="Zatwierdź", command=get_data, bg="linen")
button_get_data.grid(row=1, column=0, padx=10, pady=10)



labeltest = tk.Label(frameleft, bg="powder blue", text= ranodomint)
labeltest.grid(row=5, column=0, padx=10, pady=10)

labeltrue = tk.Label(frameleft, bg="powder blue")
labeltrue.grid(row=2, column=0, padx=10, pady=10)

labelfalse = tk.Label(frameleft, bg="powder blue")
labelfalse.grid(row=2, column=1, padx=10, pady=10)


labelLiczba = tk.Label(frameleft, bg="powder blue")
labelLiczba.grid(row=1, column=1)



root.mainloop()