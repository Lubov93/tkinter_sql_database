
from  tkinter import *
from tkinter import ttk
import  tkinter as tk
from tkinter import messagebox
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from tkinter import Scrollbar
from tkinter import VERTICAL
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

        TreeviewFrame = Frame(MidFrame, bd=5, width=1340, height=400, padx=4)
        TreeviewFrame.grid(row=2, column=0, padx=5, pady=0)

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
        self.txtFirstname = Entry(InnerFrame, font=('arial', 12, 'bold'), width=35, textvariable=Firstname,bd=5, justify='left')
        self.txtFirstname.grid(row=1, column=1)
        # ===============================================================================
        self.lblSurname = Label(InnerFrame, font=('arial', 12, 'bold'), text="Surname", bd=7, justify='left')
        self.lblSurname.grid(row=2, column=0, padx=5, sticky='w')
        self.txtSurname = Entry(InnerFrame, font=('arial', 12, 'bold'),bd=5, width=35, textvariable=Surname,
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

        def ShowRecord(self):
            sqlCon = pymysql.cursors.connect(host="localhost",
                                             user="root",
                                             password="",
                                             database="Member")
            cursors = sqlCon.cursors()
            cursors.execute("SELECT* FROM Member")
            results = cursors.fetchall()
            if len(results) != 0:
                self.member_record.delete(*self.member_record.get_children())
                for row in results:
                    self.member_record.insert("", END, values=row)
                    sqlCon.commit()

            sqlCon.close()

        def MemberInfo(ev):
            viewInfo = self.member_records.focus()
            learnerData = self.member_records.item(viewInfo)
            row = lea['values']

            MemID.set(row[0])
            Firstname.set(row[1])
            Surname.set(row[2])
            Address.set(row[3])
            PoBox.set(row[4])
            Gender.set(row[5])
            Mobile.set(row[6])
            Email.set(row[7])
            Mtype.set(row[8])


        # ===============================================================================
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, fg='black', font=("Arial", 16, "bold"), text="Add New", width=11,
                                height=1, bg='royal blue',padx=29).grid(row=0, column=0, padx=1)
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, fg='black', font=("Arial", 16, "bold"), text="Show record", width=11,
                                height=1, bg='royal blue', padx=29).grid(row=0, column=1, padx=1)
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4,fg='black',  font=("Arial", 16, "bold"), text="Update", width=11,
                                height=1, bg='royal blue', padx=29).grid(row=0, column=2, padx=1)
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4,fg='black', font=("Arial", 16, "bold"), text="Delete", width=11,
                                height=1, bg='royal blue', padx=29).grid(row=0, column=3, padx=1)
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4,fg='black', font=("Arial", 16, "bold"), text="Reset", width=11,
                                height=1, bg='royal blue', padx=29).grid(row=0, column=4, padx=1)
        self.btnAddNew = Button(ButtonFrame, pady=1, bd=4, fg='black', font=("Arial", 16, "bold"), text="Exit", width=11,
                                height=1, bg='royal blue', padx=29).grid(row=0, column=5, padx=1)
        # ===============================================================================

        # ===============================================================================


        #================================================================


        scroll_y = Scrollbar(TreeviewFrame, orient=VERTICAL)
        self.member_records = ttk.Treeview(TreeviewFrame, columns=("memid", "firstname", "surname", "address", "pobox", "gender", "mobile", "email", "mtype"), yscrollcommand = scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.member_records.heading("memid", text="MemberID")
        self.member_records.heading("firstname", text="Firstname")
        self.member_records.heading("surname", text="Surname")
        self.member_records.heading("address", text="Address")
        self.member_records.heading("pobox", text="PO Box")
        self.member_records.heading("gender", text="Gender")
        self.member_records.heading("mobile", text="Mobile")
        self.member_records.heading("email", text="Email")
        self.member_records.heading("mtype", text="Member Type")

        self.member_records['show'] = 'headings'

        self.member_records.column("memid", width=148)
        self.member_records.column("firstname", width=148)
        self.member_records.column("surname", width=148)
        self.member_records.column("address", width=148)
        self.member_records.column("pobox", width=148)
        self.member_records.column("gender", width=148)
        self.member_records.column("mobile", width=148)
        self.member_records.column("email", width=148)
        self.member_records.column("mtype", width=148)

        self.member_records.pack(fill=BOTH, expand=1)
        self.member_records.bind("<ButtonRelease-1>", MemberInfo)

        ShowRecord









root = tk.Tk()
app = memberConnect(root)
root.mainloop()
