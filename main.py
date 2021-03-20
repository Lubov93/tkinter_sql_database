import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Text
from tkinter import Label
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


        MainFrame = Frame(self.root, bd=10, width=1350, height=700,  bg='cadetblue')
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=7, width=1320, height=100)
        TitleFrame.grid(row=0, column=0)

        TitleFrames = Frame(TitleFrame, bd=7, width=1320, height=100,  bg='cadetblue')
        TitleFrames.grid(row=0, column=0)

        SearchFrames = Frame(MainFrame, bd=5, width=1330, height=50)
        SearchFrames.grid(row=1, column=0)


        #===============================================================================
        MidFrame = Frame(MainFrame, bd=5, width=1340, height=500, bg='cadetblue')
        MidFrame.grid(row=3, column=0)

        InnerFrame = Frame(MidFrame, bd=5, width=1340, height=180, padx=24, pady=4)
        InnerFrame.grid(row=0, column=0)

        ButtonFrame = Frame(MidFrame, bd=7, width=1340, height=50, bg='cadetblue')
        ButtonFrame.grid(row=1, column=0)

        ThreeviewFrame = Frame(MidFrame, bd=5, width=1340, height=400, padx=4)
        ThreeviewFrame.grid(row=2, column=0, padx=5, pady=0)

        #===============================================================================




root = tk.Tk()
app = memberConnect(root)
root.mainloop()
