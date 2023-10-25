# 사진 전처리 데이터
from PIL import Image


class PreImage:
    def __init__(self, path: str, size_ratio=1):
        self.__img = self.setImage(path, size_ratio)

    @property
    def img(self):
        return self.__img

    # 이미지 세팅 ( 그레이스케일 값 )
    def setImage(self, path: str, size_ratio: float) -> Image.Image:
        img = Image.open(path)

        # 이미지 사이즈 조절
        def resize(img, size_ratio):
            x, y = img.size
            return img.resize((int(x*size_ratio), int(y*size_ratio)))

        # grayScale 으로 변환
        img = resize(img, size_ratio).convert("L")

        return img

    # 이미지의 grayScale 데이터 -> iterator
    def getPixel(self) -> list:
        return self.img.getdata()


# test code
if __name__ == "__main__":
    a = PreImage("tests\\resources\\ROKMC.jpg", 0.5)
    print(type(a.getPixel()))
    a.img.show()
