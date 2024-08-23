import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("First py")

def get_data():
    data = myentry.get()
    Label2.config(text= "Twoje dane to: " + data)



frametop = tk.Frame(root, bg="linen")
frametop.pack(side="top", fill="x")

Label = tk.Label(frametop, text = "Wprowadź dane poniżej", font=("Arial", 20), bg="linen")
Label.pack(padx=20, pady=20) 



frameleft = tk.Frame(root, bg="powder blue")
frameleft.pack(side="left", fill="y")

button_get_data = tk.Button(root, text="Zatwierdź", command=get_data, bg="linen")
button_get_data.pack(padx=15, pady=15)

myentry = tk.Entry(frameleft)
myentry.pack(padx=10, pady=10)

Label2 = tk.Label(frameleft, bg="powder blue")
Label2.pack()



root.mainloop()