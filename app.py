from tkinter import *
import pyshorteners

root = Tk()
root.title('Link Shortener')
root.geometry("500x500")

def shorten():
    if linkBox.get():
        linkBox.delete(0, END)
    
    if myEntry.get():
        # Convert to tinyurl
        s = pyshorteners.Shortener()
        url = s.tinyurl.short(myEntry.get())
        linkBox.insert(END, url)

        print(pyshorteners.Shortener().tinyurl.expand(url))

        myEntry.delete(0,END)

myLabel = Label(root, text="Enter Link To Shorten", font=("Havettica", 30))
myLabel.pack(pady=20)

myEntry = Entry(root, font=('Havettica', 20))
myEntry.pack(pady=20)

myButton = Button(root, text="Shorten Link", command=shorten, font=('Havettica', 24))
myButton.pack(pady=20)

shortLabel = Label(root, text="Shortened Link", font=('Havettica', 20))
shortLabel.pack(pady=50)

linkBox = Entry(root, font=('Havettica', 24), justify=CENTER, width=30, bd=0, bg="systembuttonface")
linkBox.pack(pady=5)


root.mainloop()

