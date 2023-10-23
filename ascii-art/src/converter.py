from preImage import PreImage
from asciidata import get_asciiDataset

class Convert:
    def getImgRatio(self, pixel: int) -> float:
        if pixel != 0:
            return round(pixel / 255, 3)
        else:
            return 0.00
        
    def match(self, pixel) -> int:
        imgRatio = self.getImgRatio(pixel) # 한 pixel의 grayscale의 분포값
        dataSet = get_asciiDataset()
        
        minNum = 1
        asciiNum = 0
        
        for i, data in dataSet.items():
            absNum = abs(data-imgRatio) 

            if absNum < minNum:  #지금 차이가 전의 차이보다 작으면
                minNum = absNum  #지금 차이를 넣어준다.
                # nearNum = data     #근사값에 지금 데이터를 넣어준다.
                asciiNum = i
        
        return asciiNum
    
    def getResult(self, pixels):
        result = []
        for item in pixels:
            self.match(item)


if __name__ == "__main__":
    a = PreImage("tests\\resources\\ROKMC.jpg")
    b = Convert()
    print(b.getImgRatio(240))