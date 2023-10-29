from src.asciidata import get_asciiDataset
from src.preImage import PreImage

class Convert:
    
    dataset = get_asciiDataset()

    
    
    # 픽셀의 grayscale(1차원)을 아스키 코드 리스트(2차원)로 반환
    @classmethod
    def getAsciis(cls, url = str) -> list:

        converting_image = PreImage(url)
        img_size = converting_image.size
        pixels = converting_image.getPixel()

        # 픽셀 하나의 grayscale을 아스키 문자로 반환
        def match(pixel_imgRatio: int) -> int:

            minNum = 255
            asciiNum = 0
        
            for key, data in cls.dataset.items():
                absNum = abs(data-pixel_imgRatio) 

                if absNum < minNum:     #지금 차이가 전의 차이보다 작으면
                    minNum = absNum     #지금 차이를 넣어준다.
                    asciiNum = key

                    if minNum == 0:     # 차이가 0 이라면 바로 ASCIINUM을 리턴
                        return asciiNum
                
            return asciiNum


        
        x, y = img_size

        one_dim = []
        two_dim = []
        
        # pixel(1차) -> ascii(1차)
        for item in pixels:
            one_dim.append(chr(match(item)))

        # ascii(1차) -> ascii(2차)
        for i in range(y):
            two_dim.append(one_dim[i*x:(i+1)*x])

        return two_dim
       

