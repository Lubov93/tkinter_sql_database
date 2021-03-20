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
        self.root.resizable(width=False, height=False)
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
        SearchFrame = Frame(MainFrame, bd=5, width=1320, height=50)
        SearchFrame.grid(row=1, column=0)



root = tk.Tk()
app = memberConnect(root)
root.mainloop()
