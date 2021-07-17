# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:47:39 2021

@author: hp
"""

from tkinter import *
from tkinter import ttk
from tkinter import font
#import datetime

#global count
count=0
count1=0
count2=0

    
#def returner():
#    return (count, count1, count2)

'''def clock_count():
    lefttime = endtime - datetime.datetime.now()
    lefttime = lefttime - datetime.timedelta(microseconds = lefttime.microseconds)
    if lefttime.seconds<=0:
        quit_()
    txt.set(lefttime)
    root.after(1, clock_count)
    #print(lefttime)'''

def counting():
    global count
    count+=1
    #print(count)

def counting1():
    global count1
    count1 += 1

def counting2():
    global count2
    count2 += 1

def sensors():
    root = Tk()
    root.geometry("1536x864")#"1366x768")
    root.attributes("-fullscreen", True)
    root.configure(background='green')
    def quit_(*args):
        root.destroy()
    root.bind("x", quit_)
    #root.after(1, clock_count)
    txt = StringVar()
    #endtime = datetime.datetime(2021, 6, 2, 15, 0, 0)
    fnt = font.Font(family='Helvetica', size=120, weight='bold')
    #txt = StringVar()
    #lbl = ttk.Label(root, textvariable=txt, font=fnt, foreground="pink", background="green")
    #lbl.place(relx=0.5, rely=0.5, anchor=CENTER)
    
    button1 = Button(root, text="Sensor1", command=counting)
    button1.pack(pady=10)
    button2 = Button(root, text="Sensor2", command=counting)
    button2.pack(pady=10)
    button3 = Button(root, text="Sensor3", command=counting)
    button3.pack(pady=10)
    button4 = Button(root, text="Sensor4", command=counting1)
    button4.pack(pady=10)
    button5 = Button(root, text="Sensor5", command=counting1)
    button5.pack(pady=10)
    button6 = Button(root, text="Sensor6", command=counting1)
    button6.pack(pady=10)
    button7 = Button(root, text="Sensor7", command=counting2)
    button7.pack(pady=10)
    button8 = Button(root, text="Sensor8", command=counting2)
    button8.pack(pady=10)
    button9 = Button(root, text="Sensor9", command=counting2)
    button9.pack(pady=10)
    #button10 = Button(root, text="Sensor10", command=quit_)
    #button0 = Button(root, text="Exit", command=quit_)
    exit_button = Button(root, text="Finish & Exit", command=quit_)
    exit_button.pack(pady=10)
    
    root.mainloop()
    return count, count1, count2