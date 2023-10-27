from tkinter.font import Font
from tkinter import filedialog
import tkinter

# sub window
class Viewer(tkinter.Toplevel):

    def __init__(self, asciis: list) -> None:
        super().__init__()

        self.setUI(asciis)

        self.focus()
        self.grab_set()

        return None

    # UI 구성    
    def setUI(self, asciis: list) -> None:
        menubar = tkinter.Menu(self)
        self.config(menu = menubar)

        font = Font(family="MS Gothic", size = 2)
        label = tkinter.Label(self, text = self.listTotext(asciis), font = font)
        label.pack()
        fileMenu = tkinter.Menu(menubar)
        fileMenu.add_command(label = "Save", command = lambda:self.save(asciis))
        menubar.add_cascade(label = "File", menu = fileMenu)

    # txt 파일로 저장

    def save(self, asciis: list) -> None:
        
        filename = filedialog.asksaveasfilename(
            initialfile = "result.txt",
            defaultextension = ".txt",
            filetypes = [
                ("All Files", "*.*"),
                ("Text Document", "*.txt")
                ]
            )
        
        with open(filename, 'w', encoding = "utf-8") as txt_file:
            txt_file.write(self.listTotext(asciis))

        return None

    # list[][] -> str로 변경
    def listTotext(self, asciis: list):
        string = str()

        for line in asciis:
            string += "".join(line) + "\n"
        
        return string