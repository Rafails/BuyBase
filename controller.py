__author__ = 'Goldsmitd'
import tkinter as tk
import view
import models


class Cont:
    def __init__(self):
        self.cview = view.BuyBaseApp()
        try:
            self.cmod = models.Model(self.cview.frames[view.ConfigurationPage].userE.get(),
                                 self.cview.frames[view.ConfigurationPage].passE.get(),
                                 self.cview.frames[view.ConfigurationPage].hostE.get(),
                                 self.cview.frames[view.ConfigurationPage].dataE.get())
        except:
            print('EROOR')
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





if __name__ == '__main__':
    contOP = Cont()
    contOP.cview.mainloop()
   


