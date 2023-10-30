from tkinter import *
from tkinter import ttk

class mainWindow():
    
    root = Tk()

    def __init__(self):
        self.setupUI()
        
        self.root.mainloop()

    def setupUI(self):
        self.root.title = "mainWindow"
        self.root.geometry("300x100+2000+600")

        frame = Frame(self.root, bg="red")
        frame.pack(fill=BOTH, expand=True)

        txt = Entry(frame, width=50)
        txt.pack(side="left", fill=X)

        btn = Button(frame, overrelief="solid", text="convert")
        btn.pack(side="right", fill=X, padx=10)

        



class subWindow():
    pass


class Viewer():
    def __init__(self) -> None:
        pass

if __name__ == "__main__":
    a = mainWindow()
