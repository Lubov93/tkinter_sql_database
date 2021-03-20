import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
import pymysql
import random


class memberConnect:

    def __init__(self,root):
        self.root = root
        self.root.title("MySql Database Connector")
        self.root.resizable(width=True, height=True)
        self.root.geometry("1360x700+0+0")

        MemID = tk.StringVar()
        Firstname = tk.StringVar()
        Surname = tk.StringVar()
        Address = tk.StringVar()
        PoBox = tk.StringVar()
        Gender = tk.StringVar()
        Mtype = tk.StringVar()
        Mobile = tk.StringVar()
        Email = tk.StringVar()

        Search = tk.StringVar()
        MemIDBar = tk.StringVar()


        MainFrame = Frame(self.root, bd=10, width=1350, height=700,  bg='royal blue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1320, height=100)
        TitleFrame.grid(row=0, column=0)

        TitleFrames = Frame(TitleFrame, bd=7, width=1320, height=100,  bg='royal blue')
        TitleFrames.grid(row=0, column=0)

        SearchFrames = Frame(MainFrame, bd=5, width=1330, height=50)
        SearchFrames.grid(row=1, column=0)


        #===============================================================================
        MidFrame = Frame(MainFrame, bd=5, width=1340, height=500, bg='royal blue')
        MidFrame.grid(row=3, column=0)

        InnerFrame = Frame(MidFrame, bd=5, width=1340, height=180, padx=24, pady=4)
        InnerFrame.grid(row=0, column=0)

        ButtonFrame = Frame(MidFrame, bd=7, width=1340, height=50, bg='royal blue')
        ButtonFrame.grid(row=1, column=0)

        ThreeviewFrame = Frame(MidFrame, bd=5, width=1340, height=400, padx=4)
        ThreeviewFrame.grid(row=2, column=0, padx=5, pady=0)

        #===============================================================================
        self.lblTitle = Label(TitleFrames, font=('arial', 40, 'bold'), text="MySql Connection", bg="royal blue", fg='white')
        self.lblTitle.grid(row = 0, column = 0, padx=90)

        self.lblHunter = Label(TitleFrames, font=('C39HrP24DlTt', 60, 'bold'), text="By Luba R", bg="royal blue",
                              fg='white')
        self.lblHunter.grid(row=0, column=1, padx=152)
        # ===============================================================================
        self.lblBarCode = Label(SearchFrames, font=('arial', 12, 'bold'), text="BarCode")
        self.lblBarCode.grid(row=0, column=0, padx=4, sticky='w')
        self.txtBarCode = Entry(SearchFrames, font=('CCode39', 13),  width=26,  textvariable=MemIDBar, justify='center')
        self.txtBarCode.grid(row=0, column=1, padx=39)
        # ===============================================================================
        self.txtSearch = Entry(SearchFrames, font=('CCode39', 13), width=33, textvariable=Search, justify='center')
        self.txtSearch.grid(row=0, column=2)
        self.btnSearch = Button(SearchFrames, pady=1, bd=4, font=('arial',12,'bold'), text="Search", width=9, height=1)

        # ===============================================================================




root = tk.Tk()
app = memberConnect(root)
root.mainloop()
