from functools import singledispatch
from abc import ABCMeta, abstractmethod
from tkinter import ttk
import tkinter
import converter

# UI 추상클래스
class UI(metaclass = ABCMeta):
    url = "ascii-art/resources"

    @abstractmethod
    def getUrl(self) -> str:
        return self.url
    
class TUI(UI):

    def getUrl(self) -> str:
        return super().getUrl()

class GUI(UI):

    def getUrl(self) -> str:
        return super().getUrl()
    
class Viewer():

    convertor = converter.Convert()
    tk = tkinter.Tk()

    def __init__(self) -> None:
        
        self.show = singledispatch(self.show)
        self.show.register(TUI, self.__showTUI)
        self.show.register(GUI, self.__showGUI)

        self.setUI()

        self.tk.mainloop()

    # show를 메서드 오버로딩해서 구성
    
    # GUI 구성
    def setUI(self):
        self.selectUIcombo = ttk.Combobox(self.tk, height = 2, values = ["GUI", "TUI"], state = "readonly")
        self.selectUIcombo.current(0)
        self.selectUIcombo.grid(row = 0, column = 0)

        self.urlEntry = tkinter.Entry(self.tk, width = 80)
        self.urlEntry.grid(row = 0, column = 1)
        
        self.calBtn = tkinter.Button(self.tk, text = "변환", command = lambda: self.show(UI))
        self.calBtn.grid(row = 0, column = 2)
        
        self.textbox = tkinter.Text(self.tk, font = ("Times", 9))
        self.textbox.grid(row = 1, column = 0, columnspan = 10)

    def show(self, arg: UI):

        if self.selectUIcombo.get() == "GUI":
            self.show(GUI())
        
        elif self.selectUIcombo.get() == "TUI":

            self.show(TUI())

    def __showTUI(self, arg: TUI):

        with open(arg.getUrl() + "result.txt", "w") as file:
            for line in self.convertor.getPixels(self.urlEntry.get()):
                file.write("".join(line) + "\n")

    def __showGUI(self, arg: GUI):

        for line in self.convertor.getPixels(self.urlEntry.get()):
            self.textbox.insert("end", "".join(line))


        

a = Viewer()

