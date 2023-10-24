from preImage import PreImage
from asciidata import get_asciiDataset

class Convert:

    def getImgRatio(self, pixel: int) -> float:
        if pixel != 0:
            return round(pixel / 255, 3)
        else:
            return 0.00
        
    def match(self, pixel: int) -> int:
        imgRatio = self.getImgRatio(pixel) # 한 pixel의 grayscale의 분포값
        dataSet = get_asciiDataset()
        
        minNum = 1
        asciiNum = 0
        
        for i, data in dataSet.items():
            absNum = abs(data-imgRatio) 

            if absNum < minNum:  #지금 차이가 전의 차이보다 작으면
                minNum = absNum  #지금 차이를 넣어준다.
                asciiNum = i

                if minNum == 0:     # 차이가 0 이라면 바로 ASCIINUM을 리턴
                    return asciiNum

        return asciiNum
    
    def getResult(self, pixels: list) -> list:
        result = []
        
        for item in pixels:
            result.append(chr(self.match(item)))

        return result

if __name__ == "__main__":
    a = PreImage("tests\\resources\\ROKMC.jpg")
    pixel_data = a.getPixel()
    b = Convert()