import tkinter
import tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
import pymysql
import random
from tkinter import ttk

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
        self.txtSearch = Entry(InnerFrame, font=('CCode39', 13), width=33, textvariable=Search, justify='center')
        self.txtSearch.grid(row=0, column=2)
        self.btnSearch = Button(InnerFrame, pady=1, bd=4, font=('arial',12,'bold'),
                                text="Search", width=9, height=1, bg="royalblue", padx=29).grid(row=0, column=3, padx=1)

        # ===============================================================================
        self.lblmemberID = Label(InnerFrame, font=('arial', 12, 'bold'), text="Member ID", bd=7, justify='left')
        self.lblmemberID.grid(row=0, column=0, padx=5, sticky='w')
        self.txtmemberID = Entry(InnerFrame, font=('arial', 12, 'bold'), width=35, textvariable=MemID, bd=7, justify='left')
        self.txtmemberID.grid(row=0, column=1, padx=39)
        # ===============================================================================
        self.lblFirstname = Label(InnerFrame, font=('arial', 12, 'bold'), text="Firstname", bd=7, justify='left')
        self.lblFirstname.grid(row=1, column=0, padx=5, sticky='w')
        self.txtFirstname = Entry(InnerFrame, font=('arial', 12, 'bold'), width=35, textvariable=MemID,bd=5, justify='left')
        self.txtFirstname.grid(row=1, column=1)
        # ===============================================================================
        self.lblSurname = Label(InnerFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, justify='left')
        self.lblSurname.grid(row=2, column=0, padx=5, sticky='w')
        self.txtSurname = Entry(InnerFrame, font=('arial', 12, 'bold'),bd=5, width=35, textvariable=MemID,
                                  justify='left')
        self.txtSurname.grid(row=2, column=1)
        # ===============================================================================
        self.lblAddress = Label(InnerFrame, font=('arial', 12, 'bold'), text="Address", bd=7, justify='left')
        self.lblAddress.grid(row=0, column=2, padx=5, sticky='w')
        self.txtAddress = Entry(InnerFrame, font=('arial', 12, 'bold'), bd=5, width=35, textvariable=Address,
                                justify='left')
        self.txtSurname.grid(row=0, column=3)
        # ===============================================================================
        self.lblPOBox = Label(InnerFrame, font=('arial', 12, 'bold'), text="PO Box", bd=5, justify='left')
        self.lblPOBox.grid(row=0, column=4, padx=5, sticky='w')
        self.txtPOBox = Entry(InnerFrame, font=('arial', 12, 'bold'), bd=5, width=35, textvariable=PoBox,
                                justify='left')
        self.txtPOBox.grid(row=0, column=5)
        # ===============================================================================
        self.lblGender = Label(InnerFrame, font=('arial', 12, 'bold'), text="Gender", bd=5, justify='left')
        self.lblGender.grid(row=1, column=2, padx=5, sticky='w')
        self.cboGender = ttk.Combobox(InnerFrame,width=33, font=('arial', 12, 'bold'), state='readonly', textvariable=Gender)
        self.cboGender['values'] = ('', 'Female', 'Male')
        self.cboGender.current(0)
        self.cboGender.grid(row=1, column=3)
        # ===============================================================================
        self.lblEmail = tk.Label(InnerFrame, font=("Arial", 12, "bold"), text="Email", bd=7)
        self.lblEmail.grid(row=1, column=4, sticky='w', padx=5)
        self.txtemail = tk.Entry(InnerFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                                 textvariable=Email)
        self.txtemail.grid(row=1, column=5)

        # ===============================================================================
        self.lblMobile = tk.Label(InnerFrame, font=("Arial", 12, "bold"), text="Mobile", bd=7)
        self.lblMobile.grid(row=2, column=2, sticky='w', padx=5)
        self.txtMobile = tk.Entry(InnerFrame, font=("Arial", 12, "bold"), bd=5, width=35, justify="left",
                                  textvariable=Mobile)
        self.txtMobile.grid(row=2, column=3, sticky='w')

        self.lblType = tk.Label(InnerFrame, font=("Arial", 12, "bold"), text="Type", bd=7)
        self.lblType.grid(row=2, column=4, sticky='w', padx=5)


        # ===============================================================================
        self.cboType = ttk.Combobox(InnerFrame, width=33, font=("Arial", 12, "bold"), state="readonly",
                                    textvariable=Mtype)
        self.cboType["values"] = ("Member Type", "Annual Member", "Quatererly", 'Monthly')
        self.cboType.current(0)
        self.cboType.grid(row=2, column=5)


root = tk.Tk()
app = memberConnect(root)
root.mainloop()
