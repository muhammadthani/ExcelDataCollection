from tkinter import *
import pandas as pd
import time

def submit_fields():
    path = '/Users/apple/Downloads/excel.xlsx'
    df1 = pd.read_excel(path)
    SeriesA = df1['Name of Staff']
    SeriesB = df1['Extension']
    SeriesC = df1['Room Number']
    SeriesD = df1['Department']
    SeriesE = df1['Issue']
    SeriesF = df1['Brief Description of issue']
    SeriesG = df1['Assigned to']
    SeriesH = df1['Issue Status']
    A = pd.Series(entry1.get())
    B = pd.Series(entry2.get())
    C = pd.Series(entry3.get())
    D = pd.Series(entry4.get())
    E = pd.Series(entry5.get())
    F = pd.Series(entry6.get())
    G = pd.Series(entry7.get())
    H = pd.Series(entry8.get())
    SeriesA = SeriesA.append(A)
    SeriesB = SeriesB.append(B)
    SeriesC = SeriesC.append(C)
    SeriesD = SeriesD.append(D)
    SeriesE = SeriesE.append(E)
    SeriesF = SeriesF.append(F)
    SeriesG = SeriesG.append(G)
    SeriesH = SeriesH.append(H)
    df2 = pd.DataFrame({"Name of Staff":SeriesA, "Extension":SeriesB, "Room Number":SeriesC, "Department":SeriesD, "Issue":SeriesE, "Brief Description of issue":SeriesF, "Assigned to":SeriesG, "Issue Status":SeriesH})
    df2.to_excel(path, index=False)
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)
    entry8.delete(0, END)

master = Tk()

Label(master, text="Name of Staff").grid(row=0)
Label(master, text="Extension").grid(row=1)
Label(master, text="Room Number").grid(row=2)
Label(master, text="Department").grid(row=3)
Label(master, text="Issue").grid(row=4)
Label(master, text="Brief Description of issue").grid(row=5)
Label(master, text="Assigned to").grid(row=6)
Label(master, text="Issue Status").grid(row=7)

entry1 = Entry(master)
entry2 = Entry(master)
entry3 = Entry(master)
entry4 = Entry(master)
entry5 = Entry(master)
entry6 = Entry(master)
entry7 = Entry(master)
entry8 = Entry(master)

entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
entry3.grid(row=2, column=1)
entry4.grid(row=3, column=1)
entry5.grid(row=4, column=1)
entry6.grid(row=5, column=1)
entry7.grid(row=6, column=1)
entry8.grid(row=7, column=1)

Button(master, text='Quit', command=master.quit).grid(row=9,column=0, pady=4)
Button(master, text='Submit', command=submit_fields).grid(row=9,column=1, pady=4)
Label(master, text= (time.strftime("%d/%m/%Y"))).grid(row=10)
mainloop()