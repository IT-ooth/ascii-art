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

# 임시 컨버터 클래스, 컨버터 완성 시 삭제
class Convertor():

    ls = [
        ["1", "2"],
        ["2", "3"]
    ]

    @classmethod
    def getPixels(cls):
        return cls.ls
    
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
        from functools import singledispatch
from abc import ABCMeta, abstractmethod

class UI(metaclass = ABCMeta):
    url = "ascii-art/ascii-art/resources"

    @abstractmethod
    def getUrl(self) -> str:
        return self.url
    
class TUI(UI):

    def getUrl(self) -> str:
        return super().getUrl()

class Convertor():

    ls = [
        ["1", "2"],
        ["2", "3"]
    ]

    @classmethod
    def getPixels(cls):
        return cls.ls
    
class Viewer():

    def __init__(self) -> None:
        
        self.show = singledispatch(self.show)
        self.show.register(TUI, self.__showTUI)
    
    def show(self, arg: UI):pass

    def __showTUI(self, arg: TUI):

        with open(arg.getUrl() + "result.txt", "w") as file:
            for line in Convertor.getPixels():
                file.write("".join(line) + "\n")
        