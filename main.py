import tkinter as tk

root = tk.Tk()
root.geometry("800x500")
root.title("First py")

def get_data():
    data = myentry.get()
    Label2.config(text= "Twoje dane to: " + data)

Label = tk.Label(root, text = "Wprowadź dane poniżej", font=("Arial", 20))
Label.pack(padx=20, pady=20) 

myentry = tk.Entry(root)
myentry.pack(padx=10, pady=10)

button_get_data = tk.Button(root, text="Pobież", command=get_data)
button_get_data.pack(padx=15, pady=15)

Label2 = tk.Label()
Label2.pack()



root.mainloop()