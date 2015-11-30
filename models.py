__author__ = 'Goldsmitd'
from mysql.connector import errorcode
import mysql.connector
import matplotlib.pyplot as plt
import pandas
import datetime as dt
from datetime import date
from datetime import datetime


class Model:
    def __init__(self, inUser, inPass, inHost, inDabe):
        self.cnn = mysql.connector.connect(user=inUser, password=inPass, host=inHost, database=inDabe)
        self.cursor = self.cnn.cursor()
        self.args_to_creating_chceckbox()






    def create_table(self, inTabNam, inName, inKind, inBuyer, inStore, inPrice, inDate):

        stmt_create = """
        CREATE TABLE %s (
        id INT  NOT NULL AUTO_INCREMENT,
        %s VARCHAR(255) DEFAULT '' NOT NULL,
        %s VARCHAR(255) DEFAULT '' NOT NULL,
        %s VARCHAR(255) DEFAULT '' NOT NULL,
        %s VARCHAR(255) DEFAULT '' NOT NULL,
        %s REAL  NOT NULL,
        %s DATE  NOT NULL,
        PRIMARY KEY (id)
        )ENGINE=InnoDB""" %(inTabNam, inName, inKind, inBuyer, inStore, inPrice, inDate)
        self.cursor.execute(stmt_create)
        self.cnn.commit()


    def add_data(self, inTabName, inName, inKind, inBuyer, inStore, inPrice, inDate):
        # evidence = (  (inName,), (inKind,), (inBuyer,), (inStore,), (inPrice,), (inDate,) )
        # insertCom = "INSERT INTO aa (name, kind, buyer, store, price, date) VALUES (%s)"
        # self.cursor.executemany(insertCom, evidence)
        # self.cnn.commit()

        self.cursor.execute("ALTER TABLE %s MODIFY `id` INT(11) NOT NULL AUTO_INCREMENT" % inTabName)
        self.cursor.execute("INSERT INTO %s (name, kind, buyer, store, price, date) VALUES \
                            ('%s', '%s', '%s', '%s', '%s','%s')"\
                            % ( inTabName, inName, inKind, inBuyer, inStore, inPrice, inDate))
        self.cnn.commit()


    def close_database(self):
         self.cursor.close()
         self.cnn.close()

    def arguments_plot(self, buyerField):
        # this is the query when one checkbutton is marked
        if buyerField[1] == 1:
            query = """
            SELECT price, date
            FROM aa
            WHERE date >= "2015-11-01"
              AND date < "2015-11-30"
              AND buyer = '%s';
            """ % buyerField[0]
            # Data pulling from mysql
            self.cursor.execute(query)
        # this is the query when two checkbuttons are marked
        elif buyerField[1] == 2:
            query = """
            SELECT price, date
            FROM aa
            WHERE date >= "2015-11-01"
              AND date < "2015-11-30";
            """
            # Data pulling from mysql
            self.cursor.execute(query)
        dates = []
        prices = []
        for (price, date) in self.cursor:
            # date = dt.datetime.strptime(date,'%m/%d/%Y').date()
            # regard = '%Y-%m-%d %H:%M:%S'
            # date = date.strftime(regard)

            date = datetime.combine(date, datetime.min.time())


            dates.append(date)
            prices.append(price)

        return dates, prices

    def args_to_creating_chceckbox(self):
        i=0
        nameL = []
        kindL = []
        storeL = []
        query = """
            SELECT name, kind, store
            FROM aa
            WHERE date >= "2015-11-01"
            AND date < "2015-11-30";
            """
        self.cursor.execute(query)

        for name, kind, store in self.cursor:
            # if i == 0:
            #     print('tak')
            #     kindL.append(kind)
            #     buyerL.append(buyer)
            #     storeL.append(store)
            # elif i>0:
            #     if kindL[i] == kind:
            #         kindL.append(kind)
            #     if buyerL[i] == buyer:
            #         buyerL.append(buyer)
            #     if storeL[i] == store:
            #         storeL.append(store)
            # i=i+1
            if nameL.count(name) == 0:
                nameL.append(name)
            if kindL.count(kind) == 0:
                kindL.append(kind)
            if storeL.count(store) == 0:
                storeL.append(store)
                

        print(nameL, kindL, storeL)

                    



    # def self_call(self, inUser, inPass, inHost, inDabe):
    #     return Model(inUser, inPass, inHost, inDabe)



    # def create_table(self, tableName):
    #     self.cursor.execute("CREATE TABLE %s (Id INT PRIMARY KEY,Name TEXT,Kind TEXT,Buyer TEXT,Store TEXT,Price FLOAT,Date TEXT)" % (tableName))
    #
    # def add_data(self, inTablename,inId, inName, inKind, inBuyer,
    #              inStore, inPrice, inDate):
    #     self.cursor.execute("INSERT INTO %s VALUES (%s,%s,%s,%s,%s,%s,%s)" %
    #                         (inTablename,inId,inName, inKind, inBuyer, inStore,
    #                         inPrice, inDate))
    #
    #



