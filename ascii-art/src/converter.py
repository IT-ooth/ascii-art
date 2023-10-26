from preImage import PreImage
from asciidata import get_asciiDataset

class Convert:
    
    dataset = get_asciiDataset()

    #ascii-dataset.yml의 값이 0~255이라서 이거를 0~1 스케일로 변경
    def getImgRatio(self, pixel: int) -> float:
        if pixel != 0:
            return round(pixel / 255, 3)
        else:
            return 0.00
        
    #픽셀 하나의 grayscale 받아서 그것에 맞는 아스키 문자 반환
    def matchByOne(self, pixel: int) -> int:
        #imgRatio = self.getImgRatio(pixel) # 한 pixel의 grayscale의 분포값
        imgRatio = pixel

        minNum = 255
        asciiNum = 0
        
        
        for key, data in self.dataset.items():
            absNum = abs(data-imgRatio) 

            if absNum < minNum:     #지금 차이가 전의 차이보다 작으면
                minNum = absNum     #지금 차이를 넣어준다.
                asciiNum = key

                if minNum == 0:     # 차이가 0 이라면 바로 ASCIINUM을 리턴
                    return asciiNum
        return asciiNum
    
    #1차원 리스트로 된 픽셀의 grayscale을 아스키 코드로 된 1차원 리스트 반환
    def matchByList(self, pixels: list) -> list:
        result = []
        
        for item in pixels:
            result.append(chr(self.matchByOne(item)))

        return result

    #사진의 경로를 받아서 아스키 코드로 된 2차원 리스트 반환
    def getAsciis(self, img_path: str, img_size: int = 1) -> list:
        converting_image = PreImage(img_path, img_size)
        image_pixels = converting_image.getPixel()
        x, y = converting_image.size

        one_dim = self.matchByList(image_pixels)
        two_dim = []

        for i in range(y):
            two_dim.append(one_dim[i*x:(i+1)*x])

        return two_dim
    
       

if __name__ == "__main__":
    # 테스트용 함수들
    def writeResult(result):
        with open("result.txt", 'w', encoding='ASCII') as f:
            for i in result:
                for j in i:
                    # 정석적인 출력 방식. 대신 텍스트 파일로 보면 줄이 밀려있음
                    f.write(str(j)+' ')

                    # 결과를 예쁘게 보고 싶을 때
                    #f.write(j+j+j+'\t')
                f.write("\n")
    a = Convert()
    writeResult(a.getAsciis("tests/resources/pepe.jpg",0.2))
    #writeResult(a.getPixels("../../tests/resources/ROKMC.jpg"))
