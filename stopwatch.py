import tkinter
from tkinter import *
import time

root=Tk()
root.configure(background=('white'))
root.title('Stopwatch')
root.geometry('980x480')

time_elapsed1=0
time_elapsed2=0
time_elapsed3=0
time1=0
time2=0
i=0
j=0

def create_label(text, _x,_y):
    label=Label(root, text=text, fg="white", bg="black", font=("default",10,"bold"))
    label.place(x=_x,y=_y, width=100,height=45)

