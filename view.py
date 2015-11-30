__author__ = 'Goldsmitd'

import tkinter as tk
from tkinter import ttk
from time import gmtime, strftime
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

markG=None
class BuyBaseApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.container = tk.Frame(self)
        self.container.pack(side='top')

        # CREATING MENU
        menubar = tk.Menu(self.container, bg='grey')
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save settings")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label="File", menu=filemenu)
        optmenu = tk.Menu(menubar, tearoff=0)
        optmenu.add_command(label='Configuration',
                            command=lambda: self.show_frame(ConfigurationPage))
        optmenu.add_command(label='About',
                            command=lambda: self.show_frame(AboutPage))
        menubar.add_cascade(label='Options', menu=optmenu)



        tk.Tk.config(self, menu=menubar)



       #CREATING WINDOWS
        self.frames ={}
        for F in (HomePage, ConfigurationPage, AboutPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')
        #displaying start page
        self.show_frame(HomePage)



    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        markG=1
        tk.Frame.__init__(self, parent)
        self.leftCont = tk.Frame(self)
        self.rightCont = tk.Frame(self, width=300, height=100)
        self.leftCont.pack(side='left')
        self.rightCont.pack(side='right')

        #--------------
        #LEFT CONTAINER
        #--------------

        #LABELS=============================================

        self.nameL = ttk.Label(self.leftCont, text='name:')
        self.kindL = ttk.Label(self.leftCont, text='kind:')
        self.buyerL = ttk.Label(self.leftCont, text='buyer:')
        self.storeL = ttk.Label(self.leftCont, text='store:')
        self.priceL = ttk.Label(self.leftCont, text='price:')
        self.dateL = ttk.Label(self.leftCont, text='date:')

        self.nameL.grid(row=0, column=0, pady=5, padx=5)
        self.kindL.grid(row=1, column=0, pady=5, padx=5)
        self.buyerL.grid(row=2, column=0, pady=5, padx=5)
        self.storeL.grid(row=3, column=0, pady=5, padx=5)
        self.priceL.grid(row=4, column=0, pady=5, padx=5)
        self.dateL.grid(row=5, column=0, pady=5, padx=5)

        # ENTRIES====================================
        self.nameE = ttk.Entry(self.leftCont)
        self.kindE = ttk.Entry(self.leftCont)
        self.buyerE = ttk.Entry(self.leftCont)
        self.storeE = ttk.Entry(self.leftCont)
        self.priceE = ttk.Entry(self.leftCont)
        self.dateE = ttk.Entry(self.leftCont)

        self.nameE.grid(row=0, column=1, pady=5, padx=5)
        self.kindE.grid(row=1, column=1, pady=5, padx=5)
        self.buyerE.grid(row=2, column=1, pady=5, padx=5)
        self.storeE.grid(row=3, column=1, pady=5, padx=5)
        self.priceE.grid(row=4, column=1, pady=5, padx=5)
        self.dateE.grid(row=5, column=1, pady=5, padx=5)
        #insert current data
        self.dateE.insert(0, strftime("%Y-%m-%d %H:%M:%S", gmtime()))

        #BUTTONS=====================================
        self.addB = ttk.Button(self.leftCont, text='add')
        self.empty1L = ttk.Label(self.leftCont)
        self.clearB = ttk.Button(self.empty1L, text='clear')
        self.deleteB = ttk.Button(self.empty1L, text='delete')

        self.addB.grid(row=6, column=0, pady=5, padx=5)
        self.empty1L.grid(row=6, column=1, pady=5, padx=5)
        self.clearB.grid(row=0, column=0, pady=5, padx=5)
        self.deleteB.grid(row=0, column=1, pady=5, padx=5)


        #-----------------|
        # RIGHT CONTAINER |
        #-----------------|

        #---------------
        #creating table
        self.table = ttk.Treeview(self.rightCont,selectmode="extended",columns=("A","B","C","D","E","F"))
        self.table.heading("#0", text="id")
        self.table.column("#0",minwidth=0,width=100, stretch='no', anchor='center')
        self.table.heading("A", text="name")
        self.table.column("A",minwidth=0,width=100, stretch='no', anchor='center')
        self.table.heading("B", text="kind")
        self.table.column("B",minwidth=0,width=100, anchor='center')
        self.table.heading("C", text="buyer")
        self.table.column("C",minwidth=0,width=100, anchor='center')
        self.table.heading("D", text="store")
        self.table.column("D",minwidth=0,width=100, anchor='center')
        self.table.heading("E", text="price")
        self.table.column("E",minwidth=0,width=100, anchor='center')
        self.table.heading("F", text="date")
        self.table.column("F",minwidth=0,width=100, anchor='center')

        # self.table.insert("" , 0, text="2", values=("22","1b","22","1b","1b","1b"))
        # self.table.insert("" , 0, text="3", values=("22","1b","22","1b","1b","1b"))


        #scrollbar
        self.vsb = ttk.Scrollbar(self.rightCont,
						orient="vertical",
						command = self.table.yview
						)
        #link scrollbar to table
        self.table.configure( 	yscrollcommand=self.vsb.set)

        #packing table and scrollbar
        self.vsb.pack(side  = tk.RIGHT	, fill = tk.Y)
        self.table.pack(expand=True, fill=tk.BOTH)


class ConfigurationPage(tk.Frame):
    def __init__(self, parent, controller):
        markG=2
        tk.Frame.__init__(self, parent)
        #LABELS
        self.userL = ttk.Label(self, text='user name:')
        self.passL = ttk.Label(self, text='password:')
        self.hostL = ttk.Label(self, text='host:')
        self.dataL = ttk.Label(self, text='databse:')
        self.userL.grid(row=0, column=0, pady=5, padx=5)
        self.passL.grid(row=1, column=0, pady=5, padx=5)
        self.hostL.grid(row=2, column=0, pady=5, padx=5)
        self.dataL.grid(row=3, column=0, pady=5, padx=5)
        #ENTRIES
        self.userE = ttk.Entry(self)
        self.passE = ttk.Entry(self)
        self.hostE = ttk.Entry(self)
        self.dataE = ttk.Entry(self)
        self.userE.grid(row=0, column=1, pady=5, padx=5)
        self.passE.grid(row=1, column=1, pady=5, padx=5)
        self.hostE.grid(row=2, column=1, pady=5, padx=5)
        self.dataE.grid(row=3, column=1, pady=5, padx=5)
        #setting data in entries
        self.userE.insert(0, 'root')
        self.passE.insert(0, '')
        self.hostE.insert(0, 'localhost')
        self.dataE.insert(0, 'buybook')

        #BUTTONS
        self.connB = ttk.Button(self, text='connect')
        self.clearB = ttk.Button(self, text='clear')
        self.closB = ttk.Button(self, text='close')
        self.connB.grid(row=4, column=0, pady=5, padx=5)
        self.clearB.grid(row=4, column=1, pady=5, padx=5)
        self.closB.grid(row=4, column=2, pady=5, padx=5)


    def clear_click(self):
        self.userE.delete(0,'end')
        self.passE.delete(0,'end')
        self.hostE.delete(0,'end')
        self.dataE.delete(0,'end')


class AboutPage(tk.Frame):
    def __init__(self, parent, controller):
        markG=3
        tk.Frame.__init__(self, parent)
        #FRAMES-------------------------
        self.rightFrame = tk.Frame(self)
        self.leftFrame = tk.Frame(self)
        #pack
        self.leftFrame.grid(row=0, column=0)
        self.rightFrame.grid(row=0, column=1)

        #---------------------------------

        #  LEFT FRAME  |
        #--------------|



        # var1 = tk.StringVar()
        # self.rCheck = ttk.Checkbutton(self.leftFrame, text="rafal", variable=var1).grid(row=0, sticky=tk.W)
        # var2 = tk.StringVar()
        # self.lCheck = ttk.Checkbutton(self.leftFrame, text="paulina", variable=var2).grid(row=1, sticky=tk.W)

        #  self.rRadioB = ttk.Radiobutton(self.leftFrame, text="rafal", variable=v1, value=1
       #                                 ).pack(anchor='w')
       #  self.pRadioB = ttk.Radiobutton(self.leftFrame, text="paulina", variable=v2, value=2
       #                                 ).pack(anchor='w')
       # # self.pRadioB
        # f = Figure(figsize=(3,3), dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
        #
        #
        #
        # canvas = FigureCanvasTkAgg(f, self)
        # canvas.show()
        # canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #
        # toolbar = NavigationToolbar2TkAgg(canvas, self)
        # toolbar.update()
        # canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


#
#
# myapp = BuyBaseApp()
# myapp.mainloop()