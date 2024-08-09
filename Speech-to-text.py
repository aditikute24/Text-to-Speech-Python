## import libraries
from tkinter import *
import pyttsx3

################### Initialized window ####################

root = Tk()
root.geometry('350x300')
root.resizable(0, 0)
root.config(bg='ghost white')
root.title('ADITI KUTE - TEXT_TO_SPEECH')

## heading
Label(root, text='TEXT_TO_SPEECH', font='Helvetica 20 bold', bg='white smoke').pack()
Label(root, text='ADITI_KUTE', font='Helvetica 15 bold', bg='white smoke').pack(side=BOTTOM)

# label
Label(root, text='Enter Text', font='Helvetica 15 bold', bg='white smoke').place(x=20, y=60)

## text variable
Msg = StringVar()

# Entry
entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

################### define function ##############################

def Text_to_speech():
    Message = entry_field.get()
    engine = pyttsx3.init()

    # Set properties for the speech (optional, but can help simulate a male voice)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # 0 for male, 1 for female
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level 0.0 to 1.0

    engine.say(Message)
    engine.runAndWait()

def Exit():
    root.destroy()

def Reset():
    Msg.set("")

# Buttons
Button(root, text="PLAY", font='Helvetica 15 bold', command=Text_to_speech, width=4).place(x=25, y=140)
Button(root, text='EXIT', font='Helvetica 15 bold', command=Exit, bg='OrangeRed1').place(x=100, y=140)
Button(root, text='RESET', font='Helvetica 15 bold', command=Reset).place(x=175, y=140)

# infinite loop to run program
root.mainloop()
