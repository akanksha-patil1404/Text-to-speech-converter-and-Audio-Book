import tkinter as tk
import pyttsx3
import PyPDF2
from tkinter.filedialog import *

print("enter 1. if you want to convert text to speech")
print("enter 2. if you want an audiobook")
n=int(input("Enter choice:"))

if(n==1):
    x=pyttsx3.init()
    
#speaknow function converts text to speech using pyttsx3 library
    def speaknow():
        x.say(textv.get())
        x.runAndWait()
        x.stop()
    
    root=Tk() # initialisation of tkinter library

    textv=StringVar() #user input variable

    #designing gui for pop up window
    obj=LabelFrame(root,text="Text to Speech Converter", font=20, bd=1)
    obj.pack(fill="both", expand="yes", padx=10, pady=10)
    
    lbl=Label(obj,text="Text", font=30)
    lbl.pack(side=tk.LEFT,padx=5)

    text=Entry(obj,textvariable=textv,font=30, width=25, bd=5)
    text.pack(side=tk.LEFT, padx=10)

    btn=Button(obj, text="Speak", font=20, bg="black", fg="white", command=speaknow)
    btn.pack(side=tk.LEFT, padx=10)

    root.title("Text to Speech Converter")
    root.geometry("400x200")
    root.resizable(False,False)
    root.mainloop()

elif(n==2):
    print("Select a pdf file")

    #opening a file selection window
    book= askopenfilename()
    pdfreader=PyPDF2.PdfFileReader(book)
    pages=pdfreader.numPages
    
    for i in range(0,pages):
        page=pdfreader.getPage(i)
        text=page.extractText()
        player=pyttsx3.init()
        player.say(text)
        player.runAndWait()
else:
    print("invalid entry")
    

