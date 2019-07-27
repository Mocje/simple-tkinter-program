from tkinter import *


class App:
    def __init__(self, parent):
        parent.geometry('355x231')

        self.mainContainer = Frame(parent)
        self.mainContainer.pack()

        self.namelb = Label(self.mainContainer, text="Name")
        self.namelb.pack()

        self.nameEntry = Entry(self.mainContainer)
        self.nameEntry.pack()

        self.passContainer = Frame(parent)
        self.passContainer.pack()

        self.passlb = Label(self.passContainer, text="Password")
        self.passlb.pack()

        self.passEntry = Entry(self.passContainer)
        self.passEntry['show'] = '*'
        self.passEntry.pack()

        self.btnContainer = Frame(parent)
        self.btnContainer.pack()

        self.btn = Button(self.btnContainer)
        self.btn['text'] = 'Login'
        self.btn['command'] = self.verify
        self.btn.pack()

    def verify(self):
        passw = self.passEntry.get()
        user = self.nameEntry.get()
        self.result = Frame(root)
        self.result.pack()


        if user == "dev" and passw == "devMan":

            self.resultlb = Label(self.result, text="Logged In!")
            self.resultlb.pack()

        else:
            self.resultlb = Label(self.result, text="Could not log in :(")
            self.resultlb.pack()

root = Tk()
App(root)
root.mainloop()