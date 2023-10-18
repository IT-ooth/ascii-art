# 사진 전처리 데이터
from PIL import Image


class PreImage:
    def __init__(self, path: str):
        self.__img = self.setImage(path)

    @property
    def img(self):  # img 불러오기
        return self.__img

    @property
    def size(self) -> tuple:  # 주어진 이미지의 사이즈
        return self.img.size

    @property
    def area(self) -> int:  # 주어진 이미지의 넓이
        w, h = self.img.size
        return w * h

    def setImage(path):  # 경로에 있는 이미지를 객체로 반환
        return Image.open(path)

    def getGrayscale(self):  # 이미지를 grayScale로 만듦
        return self.img.convert("L")

    def getPixel(self):  # 이미지의 grayScale 데이터 받아오기
        return self.getGrayscale().getdata()


# test code
if __name__ == "__main__":
    a = PreImage("img\\ROKMC_dog.jpg")
    print(a.getPixel())
