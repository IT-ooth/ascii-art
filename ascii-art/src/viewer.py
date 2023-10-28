from src.converter import Convert
from tkinter import messagebox, filedialog
from src.viewer import Viewer
import tkinter

# mainwindow
class Main(tkinter.Tk):

    def __init__(self) -> None:
        super().__init__()

        self.setUI()
        self.mainloop()

        return None
    
    # UI 구성
    def setUI(self) -> None:

        urlEntry = tkinter.Entry(self, width = 80)
        urlEntry.grid(row = 0, column = 0)

        def getpath(event:tkinter.Event) -> None:

            filename = filedialog.askopenfilename(
                filetypes = [
                    ("All Files", "*.*")
                ]
            )
            urlEntry.insert(0, filename)

        urlEntry.bind("<Button-1>", getpath)

        calBtn = tkinter.Button(self, text = "변환", command = lambda:self.show(urlEntry.get()))
        calBtn.grid(row = 0, column = 1)

        return None
        
    # ascii-art 출력
    def show(self, url:str) -> None:
        
        convertor = Convert()
        try: Viewer(convertor.getAsciis(url))
        except FileNotFoundError: 
            messagebox.showerror("오류", "파일 경로 오류")
        
        return None

if __name__ == "__main__":
    Main()
