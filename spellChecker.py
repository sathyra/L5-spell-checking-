#Importing modules
from textblob import TextBlob
from tkinter import *


#Function to check the spelling and show the corrected spelling
def checkSpelling():
    a = text.get() #Getting the word user entered    
    b = TextBlob(a) #Getting the object for the word
    correctedText.set("The corrected word is: "+str(b.correct())) #Showing the corrected word
    
#Creating the window 
w= Tk() 
w.config(bg='white')

#Creating the variables to get the word and set the correct word
text=StringVar(w)

correctedText =StringVar(w)


#Getting the input of word from the user
Label(w, text='Please enter the word',font=('calibre',13,'normal'), anchor="e", justify=LEFT).place(x=20, y=70)

Entry(w,textvariable=text, width=35,font=('calibre',13,'normal')).place(x=20,y=110)

#Label to show the correct word
opLabel = Label(w, textvariable=correctedText,anchor="e",font=('calibre',13,'normal'), justify=LEFT).place(x=20, y=130)

#Button to do the spell check
Button(w, text="Click Me", bg='SlateGray4',font=('calibre', 13),
   command=checkSpelling).place(x=230, y=190)

#Runs the window till it is closed by the user
w.mainloop()
