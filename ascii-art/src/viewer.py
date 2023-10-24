from functools import singledispatch
from abc import ABCMeta, abstractmethod

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

    def __init__(self) -> None:
        
        self.show = singledispatch(self.show)
        self.show.register(TUI, self.__showTUI)
    
    # show를 메서드 오버로딩해서 구성
    
    def show(self, arg: UI):pass

    def __showTUI(self, arg: TUI):

        with open(arg.getUrl() + "result.txt", "w") as file:
            for line in Convertor.getPixels():
                file.write("".join(line) + "\n")
