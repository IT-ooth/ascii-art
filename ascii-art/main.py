from src.converter import Convert
import src.viewer
import tkinter



class Main(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.setUI()
        self.mainloop()

        return None
    
    def setUI(self) -> None:

        urlEntry = tkinter.Entry(self, width = 80)
        urlEntry.grid(row = 0, column = 0)
        
        calBtn = tkinter.Button(self, text = "변환", command = lambda:self.show(urlEntry.get()))
        calBtn.grid(row = 0, column = 1)
    
        return None

    def show(self, url:str) -> None:
        
        convertor = Convert()
        try: src.viewer.Viewer(convertor.getAsciis(url))
        except FileNotFoundError: pass
        


a = Main()
