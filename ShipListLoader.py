# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 10:34:51 2017

@author: tastetf

Update 07/1/19 - Instead of using DC2 use 10.1.1.24. Server is virtualized and DNS routing to DC2 causes issues, so use IP instead
"""


from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QFileDialog
import sys
import ShipListLoader_UI

from PyQt5.QtWidgets import QMessageBox

import pyodbc
import sqlite3
import xlrd
import datetime
from datetime import date
import traceback


#from django.utils import timezone



class ShiplistDataLoader(QtWidgets.QMainWindow, ShipListLoader_UI.Ui_ShiplistDataLoader): 
    
    def __init__(self, parent=None): 
        super(ShiplistDataLoader, self).__init__(parent)
        self.setupUi(self)
        self.PB_ChooseList.clicked.connect(self.ChooseList)

    def printError(ex):
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
        traceback.print_exc()
    
    def ChooseList(self):

        listtype = self.CB_ListType.currentText()
        
        if listtype == "Preliminary List":
            datelist = date.today() + datetime.timedelta(days=1)
            
        elif listtype == "Today Ship List":
            datelist = date.today()   
            
        elif listtype == "Friday for Monday Ship List":
            datelist = date.today() + datetime.timedelta(days=3)
            
        elif listtype == "Saturday for Monday Ship List":
            datelist = date.today() + datetime.timedelta(days=2)
            
        
        fname = QFileDialog.getOpenFileName(self, 'Open file')
        path = fname[0]

        #Définition du fichier et des feuillesc
        try : 
            wb = xlrd.open_workbook(path)
        except FileNotFoundError:
            return
        
        sheet_names = wb.sheet_names()
        sh = wb.sheet_by_name(sheet_names[0])

        colone0 = sh.col_values(0)
#        print("colone0: ", sh.col_values(0))
        colone1 = sh.col_values(1)
        colone2 = sh.col_values(2)
        colone3 = sh.col_values(3)
#        print("colone3: ", sh.col_values(3))
        colone4 = sh.col_values(4)
#        print("colone4: ", sh.col_values(4))
        colone5 = sh.col_values(5)
        colone6 = sh.col_values(6)
        colone9 = sh.col_values(9)
        colone10 = sh.col_values(10)
        colone11 = sh.col_values(11)
        colone13 = sh.col_values(13)
        colone14 = sh.col_values(14)
        colone15 = sh.col_values(15)
        colone16 = sh.col_values(16)

        server = 'MSAVMFG1'
        database = 'VMLIVE'
        username = 'tastetf'
        password = 'Vi1234' 
        cnxn = pyodbc.connect('Driver={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password)
        cursor = cnxn.cursor()
        
        compteur = 0
        n=4
        while n <= len(colone1)-1:
            if colone1[n] == None or colone1[n] == "":
                if compteur == 3 :
                    break
                else :
                    compteur = compteur + 1
                    n= n + 3
                    
            elif colone1[n] != None or colone1[n] != "":
                
                wonumber = str(colone3[n])
#                print(wonumber)
                try :
#                    print("a")
                    won,lotsplit = wonumber.split("/")
#                    print("won", won)
#                    print("lotsplit", lotsplit)
                except :
#                    print("b")

                    QMessageBox.warning(self, "Error", "Oops, a mistake in the ship list has been detected, Please correct the work order : "+ wonumber +" to fit the following format : aa-aaaa/b.c , and reload the ship list.")
                    return
            
                try :
#                    print("c")

                    lot,split = lotsplit.split(".")
                except :
#                    print("d")

                    lot = lotsplit
                    split = '0'
                    wonumber = won+"/"+lot+"."+split
                
                cursor.execute("SELECT PART_ID FROM WORK_ORDER WHERE BASE_ID = ? AND LOT_ID = ? AND SPLIT_ID = ?",(won,lot,split,))
                test = cursor.fetchone()
                                              
                if test == None or test == "":
#                    print("e")

                    QMessageBox.warning(self, "Error", "!! "+wonumber+" does not exist in VISUAL!!, Please correct the work order : "+ wonumber +" , and reload the ship list.")
                    return
                         
            n=n+1
        cursor.close()
        

        buttonReply = QMessageBox.question(self, 'Warning', "You are about to load a : "+ listtype + " named " + sheet_names[0] + ".  If this is correct press Yes and wait until the confirmation message, if not press No.", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            # print("f")
            try:
#                conn = sqlite3.connect(r'\\DC2\\MSAIS\\db.sqlite3')
                conn = sqlite3.connect(r'\\10.1.1.24\\MSAIS\\db.sqlite3')
                cur = conn.cursor()
            except sqlite3.Error as e:
                print("Database error : %s" % e)
            except:
                print("BIG EXCEPTION")
            
            try:
                # print("g")

                cur.execute("UPDATE Shipping_Lot SET Value = ? WHERE Date = ?", (0, datelist,))
                conn.commit()
            except :
                 print("h")
                 bonbon = 1

                        
            # Insertion dans base de donnee 
            
            compteur = 0
            n=4
            while n <= len(colone1)-1:
                # print("i")

#                if colone1[n] == None or colone1[n] == "":
                if colone1[n] == None or colone1[n] == "":
                    if compteur == 3 :
                        break
                    else :
                        compteur = compteur + 1
                        n= n + 3
                        
#                elif colone1[n] != None or colone1[n] != "":
                elif colone1[n] != None and colone1[n] != "":   
                    Date = datelist
                    try:
                        PartNo = str(colone1[n])
                    except Exception as ex:
                        try:
                            print("check Part No for n:", colone2[n])
                        except:
                            print("Check for missing Part No in all part numbers, column B")
                        self.printError(ex)
                        sys.exit() #Data is missing
#                    print("PartNo colone1: ", colone1[n])
                    try:
                        PartId = int(colone2[n])
                    except Exception as ex:
                        try:
                            print("Check PartID for missing PartID near: ", colone1[n])
                        except:
                            print("Check PartIDs for missing PartID, column C")
                        self.printError(ex)
                        sys.exit() #Data is missing
#                    print("PartID colone2: ", colone2[n])
                    try:
                        LotNo = str(colone3[n])
                    except Exception as ex:
                        try:
                            print("Check LotNo for: ", colone1[n])
                        except:
                            print("Missing LotNo. Check column D")
                        self.printError(ex)
                        sys.exit() #Data is missing
#                    print("LotNo colone3: ", colone3[n])
                    
                    try :
                        lot,split = LotNo.split(".")
                        if split == 0 or split == "0" : 
                            LotNo = str(lot)
                            
                    except :
                        bonbon = 1 
                    
                    Rev = str(colone4[n])
                    Customer = str(colone5[n])
                    try :
                        ShipQty = float(colone9[n])
                    except : 
                        ShipQty = 0
                    try :   
                        UnitPrice = float(colone10[n])
                    except : 
                        UnitPrice = 0
                    try :       
                        Value = float(colone11[n])
                        Value = round(Value,2)
                    except :
                        Value = 0
                    
                    try :
                       
                        MiscCost = float(colone16[n])
                        print("Misc Cost Try: ", MiscCost)
                        MiscCost = round(MiscCost,2)
                        print("Misc Cost Try: ", MiscCost)
                    except : 
                        MiscCost = 0
            
                    Via = str(colone13[n])
                    Requirement = str(colone14[n])
                    Comment = str(colone15[n])
                    qe1 = False
                    qe2 = False
                    qe3 = False
                    qe4 = False
                    qe5 = False
                    qe6 = False
                    sh = False
                    iid = str(colone0[n])

                    ##New stuff
                    InShippingArea = False
                    InShippingTimeStamp = datetime.datetime.now()
                    IsPipeline = False
                    
                    if compteur == 0 :
                        if str(colone6[n]) == "FUTURES" :
                            cate = "FUTURE"
                        else :
                            cate = "WIP"
                    elif compteur == 1 :
                        cate = "WIP"
                    elif compteur == 2 :
                        cate = "FUTURE"
                    
                    try :
                        
                        print(LotNo,"Value: ", Value, "Misc: ", MiscCost)
                        
                        cur.execute("SELECT LotNo FROM Shipping_Lot WHERE Date = ? AND InternalId = ?", (Date, iid,))
                        choix = cur.fetchall()
                            
                        if choix == [] or choix == None:

                            #                            req = "INSERT INTO Shipping_Lot(Date,PartNo, PartId, LotNo, Revision, Customer, Category, ShipQty, ShipQtyOrigine, UnitPrice, Value, ValueOrigine, MiscCost, Via, QERequirement, Comment,QePendingFirstArticle,QePendingMaster,QePendingLab,QeStartWork,QeClose,QeReviewed,Shipped,InternalId) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            #                            cur.execute(req, (Date,PartNo, PartId, LotNo,Rev, Customer, cate, ShipQty, ShipQty, UnitPrice,Value, Value, MiscCost, Via, Requirement,Comment,qe1,qe2,qe3,qe4,qe5,qe6,sh,iid))

                            req = "INSERT INTO Shipping_Lot(Date,PartNo, PartId, LotNo, Revision, Customer, Category, ShipQty, ShipQtyOrigine, UnitPrice, Value, ValueOrigine, MiscCost, Via, QERequirement, Comment,QePendingFirstArticle,QePendingMaster,QePendingLab,QeStartWork,QeClose,QeReviewed,Shipped,InternalId, InShippingArea, InShippingTimeStamp, IsPipeline) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
                            cur.execute(req, (Date, PartNo, PartId, LotNo, Rev, Customer, cate, ShipQty, ShipQty, UnitPrice, Value, Value, MiscCost, Via, Requirement, Comment, qe1, qe2, qe3, qe4, qe5, qe6, sh, iid, InShippingArea, InShippingTimeStamp, IsPipeline))

                            conn.commit()
                        else :
                            cur.execute("UPDATE Shipping_Lot SET Value = ?, ShipQtyOrigine = ? WHERE Date = ? AND InternalId = ?", (Value,ShipQty,Date,iid,))
                            conn.commit()
                            
                        
                    except Exception as ex :
                        QMessageBox.warning(self, "Error", "Oops, an error occur during the loading at lot number :"+LotNo+", please try again !")
                        self.printError(ex)
                        return

                n = n + 1
                
            QMessageBox.about(self, "Confirmation", "Your ship list have been uploaded.")
            cur.close()
            
          
        else:
            return
            QMessageBox.about(self, "Operaation canceled", "You have decided to cancel the loading of the ship list.")


def main():
    app = QtWidgets.QApplication(sys.argv)
    form = ShiplistDataLoader()
    form.show()
    app.exec_()
    



if __name__ == '__main__':
    main()