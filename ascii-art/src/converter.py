from src.asciidata import get_asciiDataset

class Convert:
    
    dataset = get_asciiDataset()

    
    
    # 픽셀의 grayscale(1차원)을 아스키 코드 리스트(2차원)로 반환
    @classmethod
    def getAsciis(cls, pixels: list, img_size: tuple) -> list:

        # 픽셀 하나의 grayscale을 아스키 문자로 반환
        def match(dataset: dict,pixel_imgRatio: int) -> int:
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
            one_dim.append(chr(self.match(cls.dataset, item)))

        # ascii(1차) -> ascii(2차)
        for i in range(y):
            two_dim.append(one_dim[i*x:(i+1)*x])

        return two_dim
       

# if __name__ == "__main__":
#     # 테스트용 함수들
#     def writeResult(result):
#         with open("result.txt", 'w', encoding='ASCII') as f:
#             for i in result:
#                 for j in i:
#                     # 정석적인 출력 방식. 대신 텍스트 파일로 보면 줄이 밀려있음
#                     f.write(str(j)+' ')

#                     # 결과를 예쁘게 보고 싶을 때
#                     # f.write(j+j+j+'\t')
#                 f.write("\n")

#     a = PreImage("tests\\resources\\ROKMC.jpg")
#     b = Convert()

#     writeResult(b.getAsciis(a.getPixel(), a.size))
