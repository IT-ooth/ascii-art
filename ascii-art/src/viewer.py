from functools import singledispatch
from abc import ABCMeta, abstractmethod
from PyQt5 import QtWidgets, uic
import converter
import yaml
import sys

# UI 추상클래스
class UI(metaclass = ABCMeta):
    url = "ascii-art/resources"

    @abstractmethod
    def getUrl(self) -> str:
        return self.url
    
class TUI(UI):

    def getUrl(self) -> str:
        return super().getUrl()


class Viewer():

    convertor = converter.Convert()

    def __init__(self) -> None:
        
        self.show = singledispatch(self.show)
        self.show.register(TUI, self.__showTUI)
    
    # show를 메서드 오버로딩해서 구성
    
    def show(self, arg: UI):pass

    def __showTUI(self, arg: TUI):
        
        with open(arg.getUrl() + "result.txt", "w") as file:
            for line in self.convertor.getPixels(arg.getUrl()):
                file.write("".join(line) + "\n")


window_form = uic.loadUiType("ascii-art/resources/window_UI.ui")[0]


# 미완성
class MainWindow(QtWidgets.QMainWindow, window_form):

    def __init__(self):
        super().__init__()
        
        self.setupUi()
        
        self.initUI()
    
    def initUI(self):
        
        self.setUIoption()

        self.setWindowTitle(self.data["title"])
        self.resize(self.data["size"][0], self.data["size"][1])
        self.center()
        self.show()
        
    
    def setUIoption(self):

        with open("ascii-art/resources/window_config.yml", encoding = 'utf-8') as file:
            
            self.__data = yaml.load(file, Loader = yaml.FullLoader)
    

    def center(self):

        qr = self.frameGeometry()
        qr.moveCenter(QtWidgets.QDesktopWidget().availableGeometry().center())

        self.move(qr.topLeft())

    @property
    def data(self): 
        return self.__data