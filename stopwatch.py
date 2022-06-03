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

def start():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=100,y=300, width=150,height=50)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else: 
            time_elapsed1=0
            time_elapsed3+=1
            if time_elapsed3>=24:
                time_elapsed1=0
                time_elapsed2=0
                time_elapsed3=0
            else:
                time_elapsed3+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(1000,start)

def stop():
    global self_job
    if self_job is not None:
        root.after_cancel(self_job)
        self_job=None
    stop_button.place_forget()
    resume_button.place(x=100,y=300, width=150,height=50)
  
def resume():
    start_button.place_forget()
    resume_button.place_forget()
    stop_button.place(x=100,y=300, width=150,height=50)
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2
    time2=int(time.time())
    if time2!=time1:
        time1=time2
        if time_elapsed1<59:
            time_elapsed1+=1
            clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
        else: 
            time_elapsed1=0
            time_elapsed3+=1
            if time_elapsed3>=24:
                time_elapsed1=0
                time_elapsed2=0
                time_elapsed3=0
            else:
                time_elapsed3+=1
                clock_frame.config(text=(str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)))
    self_job=root.after(1000,start)

def clear():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,label,i,j
    try:
        stop()
    except:
        start()
        stop()
    clock_frame.config(text="00:00:00")
    time_elapsed1=0
    time_elapsed2=0
    time_elapsed3=0
    time1=0
    time2=0
    i=0
    j=0
    wig=root.winfo_children()
    for b in wig:
        b.place_forget()
        resume_button.place_forget()
        start_button.place(x=100,y=300, width=150,height=50)
        lap_button.place(x=730,y=300, width=150,height=50)
        reset_button.place(x=415,y=300, width=150,height=50)
        clock_frame.place(x=200,y=100, width=600,height=100)
        
def lap():
    global time_elapsed1,time_elapsed2,time_elapsed3,time1,self_job,time2,i,j
    if i <9:
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)),20+(110*i),400+(j*50))
    else:
        j+=1
        i=0
        create_label((str(time_elapsed3).zfill(2)+":"+str(time_elapsed2).zfill(2)+":"+str(time_elapsed1).zfill(2)),20+(110*i),400+(j*50))
    i+=1

clock_frame=Label(text="00:00:00",bg="white",fg="black",font=("default",100))
start_button=Button(text="START",bg="white",fg="black",font=("default",20),command=start)
stop_button=Button(text="STOP",bg="white",fg="black", font=("default",20),command=stop)
resume_button=Button(text="RESUME",bg="white",fg="black",font=("default",20),command=resume)
lap_button=Button(text="LAP",bg="white",fg="black",font=("default",20),command=lap)
reset_button=Button(text="RESET",bg="white",fg="black",font=("default",20),command=clear)

start_button.place(x=100,y=300, width=150,height=50)
lap_button.place(x=730,y=300, width=150,height=50)
reset_button.place(x=415,y=300, width=150,height=50)
clock_frame.place(x=200,y=100, width=600,height=100)

root.mainloop()
