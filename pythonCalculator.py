from tkinter import *

class Application(Frame):
    global fieldValue
    def __init__(self,master):
        super().__init__(master)        
        self.master = master
        self.fieldValue = ''
        self.master.geometry("300x300+440+40")
        self.master.title("CALCI PYTHO")
        self.master.resizable(False,False)
        self.pack()
        self.inputVar = StringVar()
        self.create_widgets()

    def create_widgets(self):
        self.label = Label(self)
        self.label["text"] = "CALCULATOR"
        self.label["fg"] = "red"
        self.label.pack(side=TOP)
        self.input = Entry(self)
        self.input["textvariable"] = self.inputVar
        self.input.config(state=DISABLED)
        self.input.config(disabledforeground="red")
        self.input.pack(ipadx=90,ipady=10)
        self.operationFrame = Frame(self.master)
        self.buttonAdd = Button(self.operationFrame)
        self.buttonAdd["text"] = "+"
        self.buttonAdd["command"] = lambda:self.onClick(self.buttonAdd)
        self.buttonAdd.pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonSub = Button(self.operationFrame)
        self.buttonSub["text"] = "-"
        self.buttonSub["command"] = lambda:self.onClick(self.buttonSub)
        self.buttonSub.pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonDiv = Button(self.operationFrame)
        self.buttonDiv["text"] = "/"
        self.buttonDiv["command"] = lambda:self.onClick(self.buttonDiv)
        self.buttonDiv.pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonMul = Button(self.operationFrame)
        self.buttonMul["text"] = "*"
        self.buttonMul["command"] = lambda:self.onClick(self.buttonMul)
        self.buttonMul.pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonBack = Button(self.operationFrame)
        self.buttonBack["text"] = "C"
        self.buttonBack["command"] = lambda:self.onClick(self.buttonBack)
        self.buttonBack.pack(side=LEFT,ipadx=10,ipady=10)
        self.buttonNumber = ["0","1","2","3","4","5","6","7","8","9"]

        self.operationFrame.pack()
        #print(self.buttonObject)
        self.firstFrame = Frame(self.master)
        self.buttonObject = [Button(self.firstFrame) for i in range(0,5)]

        self.buttonObject[0]["text"] = self.buttonNumber[0]
        self.buttonObject[0]["command"] = lambda:self.onClick(self.buttonObject[0])
        self.buttonObject[0].grid(row=0,column=0,ipadx=10,ipady=10)

        self.buttonObject[1]["text"] = self.buttonNumber[1]
        self.buttonObject[1]["command"] = lambda:self.onClick(self.buttonObject[1])
        self.buttonObject[1].grid(row=0,column=1,ipadx=10,ipady=10)

        self.buttonObject[2]["text"] = self.buttonNumber[2]
        self.buttonObject[2]["command"] = lambda:self.onClick(self.buttonObject[2])
        self.buttonObject[2].grid(row=0,column=2,ipadx=10,ipady=10)


        self.buttonObject[3]["text"] = self.buttonNumber[3]
        self.buttonObject[3]["command"] = lambda:self.onClick(self.buttonObject[3])
        self.buttonObject[3].grid(row=0,column=3,ipadx=10,ipady=10)


        self.buttonObject[4]["text"] = self.buttonNumber[4]
        self.buttonObject[4]["command"] = lambda:self.onClick(self.buttonObject[4])
        self.buttonObject[4].grid(row=0,column=4,ipadx=10,ipady=10)
        self.firstFrame.pack(padx=0,pady=0)

        self.secondFrame = Frame(self.master)
        self.buttonObjectSecond = [Button(self.secondFrame) for i in range(0,5)]

        self.buttonObjectSecond[0]["text"] = self.buttonNumber[5]
        self.buttonObjectSecond[0]["command"] = lambda:self.onClick(self.buttonObjectSecond[0])
        self.buttonObjectSecond[0].pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonObjectSecond[1]["text"] = self.buttonNumber[6]
        self.buttonObjectSecond[1]["command"] = lambda:self.onClick(self.buttonObjectSecond[1])
        self.buttonObjectSecond[1].pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonObjectSecond[2]["text"] = self.buttonNumber[7]
        self.buttonObjectSecond[2]["command"] = lambda:self.onClick(self.buttonObjectSecond[2])
        self.buttonObjectSecond[2].pack(side=LEFT,ipadx=10,ipady=10)

        self.buttonObjectSecond[3]["text"] = self.buttonNumber[8]
        self.buttonObjectSecond[3]["command"] = lambda:self.onClick(self.buttonObjectSecond[3])
        self.buttonObjectSecond[3].pack(side=LEFT,ipadx=10,ipady=10)


        self.buttonObjectSecond[4]["text"] = self.buttonNumber[9]
        self.buttonObjectSecond[4]["command"] = lambda:self.onClick(self.buttonObjectSecond[4])
        self.buttonObjectSecond[4].pack(side=LEFT,ipadx=10,ipady=10)
        self.secondFrame.pack()

        self.lastFrame = Frame(self.master)
        self.dotButton = Button(self.lastFrame)
        self.dotButton["text"] = "."
        self.dotButton["command"] = lambda:self.onClick(self.dotButton)
        self.dotButton.pack(side=LEFT,ipadx=20,ipady=10)

        self.answerButton = Button(self.lastFrame)
        self.answerButton["text"] = "ANSWER"
        self.answerButton["command"] = lambda:self.onClick(self.answerButton)
        self.answerButton.pack(side=LEFT,ipadx=20,ipady=10)

        self.clearButton = Button(self.lastFrame)
        self.clearButton["text"] = "CLEAR"
        self.clearButton["command"] = lambda:self.onClick(self.clearButton)
        self.clearButton.pack(side=LEFT,ipadx=10,ipady=10)

        self.lastFrame.pack()

    def onClick(self,button):
        if button["text"] == 'C':
            self.fieldValue = self.fieldValue[0:len(self.fieldValue)-1]
        elif button["text"]=="CLEAR":
            self.fieldValue = ""
        elif button["text"]=="ANSWER":
            try:
                self.fieldValue = str(eval(self.fieldValue))
            except Exception:
                self.fieldValue = "Unidentified Expression"

        else:
            if self.fieldValue =="Unidentified Expression":
                self.fieldValue = ""
            self.fieldValue+=button["text"]
        self.inputVar.set(self.fieldValue)


if __name__=="__main__":
    window = Tk()
    app = Application(window)
    app.mainloop()

