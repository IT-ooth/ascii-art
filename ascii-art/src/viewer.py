import tkinter.font
import tkinter

class Viewer(tkinter.Toplevel):

    def __init__(self, asciis: list) -> None:
        super().__init__()

        self.setUI(asciis)

        self.focus()
        self.grab_set()

        return None
    
    def setUI(self, asciis: list) -> None:
        menubar = tkinter.Menu(self)
        self.config(menu = menubar)

        font = tkinter.font.Font(family="MS Gothic", size = 2)
        label = tkinter.Label(self, text = self.listTotext(asciis), font = font)
        label.pack()
        fileMenu = tkinter.Menu(menubar)
        fileMenu.add_command(label = "Save", command = self.save)
        menubar.add_cascade(label = "File", menu = fileMenu)

    def save(self):
        pass

    def listTotext(self, asciis: list):
        string = str()

        for line in asciis:
            string += "".join(line) + "\n"
        
        return string