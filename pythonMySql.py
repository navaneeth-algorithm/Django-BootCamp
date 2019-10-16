from tkinter import *
import mysql.connector
import tkinter.messagebox
class DatabaseHandle:
    
    def __init__(self):
        
        self.mydb = mysql.connector.connect(host="localhost",user="root",passwd="Neethas@2504")
        self.cursor = self.mydb.cursor()
    def listDatabase(self):
        self.cursor.execute("SHOW DATABASES")
        self.databaselist = [i[0] for i in self.cursor] 
        return self.databaselist
        #print(self.databaselist)

    def selectDatabase(self,dbname):
        self.cursor.execute("USE "+dbname)

    def listTables(self):
        self.cursor.execute("SHOW TABLES")
        self.tablelist = [i[0] for i in self.cursor]
        return self.tablelist

class Application(Frame):
    global varButton
    def __init__(self,master):
        self.varButton = ''
        super().__init__(master)
        self.db = DatabaseHandle()
        self.master = master
        self.master.geometry("900x300")
        #self.master.resizable(False,False)
        self.master.title("DB Config")
        self.varText = StringVar()
        self.pack()
        self.topFrame = Frame(self.master)

        self.scrollbar = Scrollbar(self.topFrame)
        self.text = Text(self.topFrame)
        self.scrollbar.pack(side=RIGHT)
        self.text["width"] =230
        self.text["height"] = 5
        self.text["fg"] = "red"
        self.text["font"] =('Comic Sans MS', 12, 'bold italic')
        #self.text.config(state=DISABLED)
        self.text.pack(side=TOP)
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.topFrame.pack(side=TOP)

        self.dbName = StringVar()
        self.buttonName = StringVar()

        self.inputFrame = Frame(self.master)

        self.lableInput = Label(self.inputFrame)
        self.lableInput["text"]="Database Name:"
        self.lableInput.grid(row=0,column=0)

        self.inputDatabase = Entry(self.inputFrame)
        self.inputDatabase["textvariable"] = self.dbName
        self.inputDatabase.bind("<FocusIn>", self.callChangeButton)
        self.inputDatabase.grid(row=0,column=1)
        

        self.selectDb = Button(self.inputFrame)
        self.selectDb["text"] = "Select"
        self.selectDb["command"] = self.selectDbFunc
        #self.selectDb["textvariable"] = self.buttonName
        self.selectDb.grid(row=1,columnspan=25)
        self.inputFrame.pack()

        self.frameOne = Frame(self.master)
        self.buttonDb = Button(self.frameOne)
        self.buttonDb["text"] = "List Databases"
        self.buttonDb["command"] = lambda:self.setTextWidget(self.db.listDatabase())
        self.buttonDb.pack(side=LEFT)
        self.buttonTable = Button(self.frameOne)
        self.buttonTable["text"] = "List Tables"
        self.buttonTable["command"] = lambda:self.setTextWidget(self.db.listTables())
        self.buttonTable.pack(side=LEFT)
        self.frameOne.pack()

    def selectDbFunc(self):
        
        #print("Database "+self.dbName.get()+" Selected")
        dbname = self.dbName.get()
        if dbname == "":
            tkinter.messagebox.showerror("ERROR","No Database is given")
        else:
            self.db.selectDatabase(self.dbName.get())
            tkinter.messagebox.showinfo("Database Selected ","Now You Can List Tables of database "+self.dbName.get())

    def setTextWidget(self,value):
        valueStr = ','.join(value)
        self.text.insert(END,valueStr)
        #self.text.config(state=DISABLED)

    def changeButtonText(self,event):
        #print(event.keycode)
        if event.keycode>=24 and event.keycode<=58:
            self.varButton+=event.char
            self.buttonName.set(self.varButton)
        if event.keycode == 22:
            #print("BACK SPACE")
            lenButtonText = len(self.varButton)
            self.varButton = self.varButton[0:lenButtonText-1]
            self.buttonName.set(self.varButton)
            pass


        if event.keycode ==65:
            self.text.insert(END,"SPACE NOT ALLOWED")
            self.varButton = ""
        #self.buttonName.set("key-Code "+event.char+" Key-Char"+str(event.keycode))

    def callChangeButton(self,event):
        #print("Focus Came")
        self.inputDatabase.bind("<Key>",self.checkDbSpace)
        pass
        #
    def checkDbSpace(self,event):
        if event.keycode ==65:
            self.dbName.set("SPACENOTALLOWED")
        pass
if __name__=="__main__":
    window = Tk()
    app = Application(window)
    app.mainloop()
