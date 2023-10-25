from preImage import PreImage
from asciidata import get_asciiDataset

class Convert:
    def __init__(self):
        self.dataset = get_asciiDataset()

    def getImgRatio(self, pixel: int) -> float:
        if pixel != 0:
            return round(pixel / 255, 3)
        else:
            return 0.00

    
    def match(self, pixel: int) -> int:
        imgRatio = self.getImgRatio(pixel) # 한 pixel의 grayscale의 분포값
        #dataSet = get_asciiDataset()
        
        minNum = 1
        asciiNum = 0
        
        for key, data in self.dataset.items():
            #print("comparing [{}][{}]".format(key, data))
            absNum = abs(data-imgRatio) 

            if absNum < minNum:  #지금 차이가 전의 차이보다 작으면
                minNum = absNum  #지금 차이를 넣어준다.
                asciiNum = key

                if minNum == 0:     # 차이가 0 이라면 바로 ASCIINUM을 리턴
                    return asciiNum
        return asciiNum
    
    def matchbyList(self, pixels: list) -> list:
        result = []
        
        for item in pixels:
            result.append(chr(self.match(item)))

        return result

    
    def getPixels(self, img_path: str) -> list:

        converting_image = PreImage(img_path, 0.7)
        image_pixels = converting_image.getPixel()

        one_dim = self.matchbyList(image_pixels)
        two_dim = []

        x, y = converting_image.img.size
        
        for i in range(y):
            two_dim.append(one_dim[i*x:(i+1)*x])

        return two_dim

if __name__ == "__main__":
    a = Convert()
