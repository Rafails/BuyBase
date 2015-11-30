__author__ = 'Goldsmitd'




#----------------------------------------------
#-----------------------------------------------
# ODSIWEZYC TEGO PLOTA xD






from tkinter import ttk
import tkinter as tk
import view
import models
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from matplotlib.dates import  DateFormatter
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import matplotlib.pyplot as plt
from matplotlib.dates import DayLocator, HourLocator, DateFormatter, drange
from numpy import arange

class Cont:
    def __init__(self):
        self.cview = view.BuyBaseApp()

        self.cmod = models.Model(self.cview.frames[view.ConfigurationPage].userE.get(),
                                 self.cview.frames[view.ConfigurationPage].passE.get(),
                                 self.cview.frames[view.ConfigurationPage].hostE.get(),
                                 self.cview.frames[view.ConfigurationPage].dataE.get())

        # adding data method
        self.cview.frames[view.HomePage].addB.config(command=self.add_dataV)
        self.display_data()
        # CONFIGURATTION PAGE----------------------------------------------------------------------------------------------
        # connect with database in configurationPage
        self.cview.frames[view.ConfigurationPage].connB.config(command=self.cmod_call)
        # clearing data in configuration page
        self.cview.frames[view.ConfigurationPage].clearB.config(command=self.cview.frames[view.ConfigurationPage].clear_click)
        # closing configuration page
        self.cview.frames[view.ConfigurationPage].closB.config(command=lambda: self.cview.show_frame(view.HomePage))
        #making a checkbuttons
        self.making_check()
        #making plot
        self.make_plot()
    def add_dataV(self):
        self.cmod.add_data('aa',
                           self.cview.frames[view.HomePage].nameE.get(),
                           self.cview.frames[view.HomePage].kindE.get(),
                           self.cview.frames[view.HomePage].buyerE.get(),
                           self.cview.frames[view.HomePage].storeE.get(),
                           self.cview.frames[view.HomePage].priceE.get(),
                           self.cview.frames[view.HomePage].dateE.get())
        #clearing and adding data. it is a way to avoid doubling data
        self.cleat_data()
        self.display_data()


    def display_data(self):
        self.cmod.cursor.execute('SELECT * FROM aa')
        for (id, name, kind, buyer, store, price, date) in self.cmod.cursor:
            #self.lix.insert('end', ('%d  ||  %s  ||  %s  ||  %s  ||  %s  ||  %s') % (id, gname, surname, adress, mobile, email))
            self.cview.frames[view.HomePage].table.insert("" , 0, text="%d" % id, values=("%s" % name,
                                                                                    "%s" % kind,
                                                                                    "%s" % buyer,
                                                                                    "%s" % store,
                                                                                    "%s" % price,
                                                                                    "%s" % date))
    def cleat_data(self):
        for row in self.cview.frames[view.HomePage].table.get_children():
            self.cview.frames[view.HomePage].table.delete(row)

    def cmod_call(self):
        self.cmod = models.Model(self.cview.frames[view.ConfigurationPage].userE.get(),
                                 self.cview.frames[view.ConfigurationPage].passE.get(),
                                 self.cview.frames[view.ConfigurationPage].hostE.get(),
                                 self.cview.frames[view.ConfigurationPage].dataE.get())

    def make_plot(self):
        #plot gets arguments
        dates, prices = self.cmod.arguments_plot(buyerField=self.argCH_plot())
        print(dates)
        print(prices)
        #creating plot
        dates = np.array(dates)#converting list
        prices = np.array(prices)#converting list
        fig, self.plotTK = plt.subplots()
        s = np.argsort(dates)#hang price to date
        f = np.argsort(prices)#hang price to date
        self.plotTK.plot_date(dates[s], prices[f], 'bo-')

        self.plotTK.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        self.plotTK.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
        fig.autofmt_xdate()
        #merge plot and tkinter
        self.canvas = FigureCanvasTkAgg(fig, self.cview.frames[view.AboutPage].leftFrame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
        #creating toolbar
        toolbar = NavigationToolbar2TkAgg(self.canvas, self.cview.frames[view.AboutPage].leftFrame)
        toolbar.update()
        #packing plot
        self.canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    #funckion is creating widgets in leftframe
    def making_check(self):
        
         #name-------------------------------------------------------
        self.nameMB = ttk.Menubutton(self.cview.frames[view.AboutPage].rightFrame, text="name")#, relief='RAISED' )
        self.nameMB.grid(row=0, column=0)
        self.nameMB.menu = tk.Menu(self.nameMB, tearoff =0)
        self.nameMB["menu"] = self.nameMB.menu
        self.creating_checkbox()




        #kind--------------------------------------------------
        self.kindMB = ttk.Menubutton(self.cview.frames[view.AboutPage].rightFrame, text="kind")#, relief='RAISED' )
        self.kindMB.grid(row=0, column=1)
        self.kindMB.menu = tk.Menu(self.kindMB, tearoff=0)
        self.kindMB["menu"] = self.kindMB.menu
        self.creating_checkbox()

        #buyer
        self.buyerMB = ttk.Menubutton (self.cview.frames[view.AboutPage].rightFrame, text="buyer")#, relief='RAISED' )
        self.buyerMB.grid(row=0, column=2)
        self.buyerMB.menu = tk.Menu(self.buyerMB, tearoff =0)
        self.buyerMB["menu"] = self.buyerMB.menu
        self.varRafal = tk.IntVar()
        self.varPaulina = tk.IntVar()

        self.buyerMB.menu.add_checkbutton(label="rafal",
                          variable=self.varRafal)
        self.buyerMB.menu.add_checkbutton(label="paulina",
                          variable=self.varPaulina)
       

        #store-------------------------------------------------------
        self.storeMB = ttk.Menubutton(self.cview.frames[view.AboutPage].rightFrame, text="store")#, relief='RAISED' )
        self.storeMB.grid(row=0, column=3)
        self.storeMB.menu = tk.Menu(self.storeMB, tearoff =0)
        self.storeMB["menu"] = self.storeMB.menu
        self.creating_checkbox()

        # #price------------------------------------------------------------
        # self.priceMB = ttk.Menubutton(self.cview.frames[view.AboutPage].rightFrame, text="price")#, relief='RAISED' )
        # self.priceMB.grid(row=0, column=3)
        # self.priceMB.menu = tk.Menu(self.priceMB, tearoff =0)
        # self.priceMB["menu"] = self.nameMB.menu
        # self.creating_checkbox()
        #
        # #date--------------------------------------------------------------
        # self.dateMB = ttk.Menubutton(self.cview.frames[view.AboutPage].rightFrame, text="date")#, relief='RAISED' )
        # self.dateMB.grid(row=0, column=4)
        # self.dateMB.menu = tk.Menu(self.dateMB, tearoff =0)
        # self.dateMB["menu"] = self.nameMB.menu
        # self.creating_checkbox()

        
        # self.rCheck = ttk.Checkbutton(self.cview.frames[view.AboutPage].rightFrame, text="rafal",
        #                               variable=self.var1, state=tk.ACTIVE
        #                               ).grid(row=0, sticky=tk.W)
        #
        # self.lCheck = ttk.Checkbutton(self.cview.frames[view.AboutPage].rightFrame, text="paulina",
        #                               variable=self.var2, state=tk.ACTIVE
        #                               ).grid(row=1, sticky=tk.W)
        self.refreshB = ttk.Button(self.cview.frames[view.AboutPage].rightFrame, text='Refresh plot', command=self.refresh_plot
                                 ).grid(row=2, sticky=tk.W)

    #function gives an argumenr buyerField to making_plot in file models
    def argCH_plot(self):
        buyer=['','']
        mark = self.varRafal.get() + self.varPaulina.get()
        if (self.varRafal.get() == 1 and
            self.varPaulina.get() == 0):
            buyer=['rafal',mark]
        elif (self.varRafal.get() == 0 and
            self.varPaulina.get() == 1):
            buyer=['paulina',mark]
        elif (self.varRafal.get() == 1 and
            self.varPaulina.get() == 1):
            buyer=['',mark]
        else:
            print('ERROR')

        return buyer

    def refresh_plot(self):
        #deleting plot
        self.canvas.get_tk_widget().destroy()
        #creating refreashed plot
        #-------------------
        #plot gets arguments
        dates, prices = self.cmod.arguments_plot(buyerField=self.argCH_plot())
        print(dates)
        print(prices)
        #creating plot
        dates = np.array(dates)#converting list
        prices = np.array(prices)#converting list
        fig, self.plotTK = plt.subplots()
        s = np.argsort(dates)#hang price to date
        f = np.argsort(prices)#hang price to date
        self.plotTK.plot_date(dates[s], prices[f], 'bo-')

        self.plotTK.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
        self.plotTK.fmt_xdata = DateFormatter('%Y-%m-%d %H:%M:%S')
        fig.autofmt_xdate()
        #merge plot and tkinter
        self.canvas = FigureCanvasTkAgg(fig, self.cview.frames[view.AboutPage].leftFrame)
        self.canvas.show()
        self.canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

    def creating_checkbox(self):
        pass


if __name__ == '__main__':
    contOP = Cont()
    contOP.cview.mainloop()

