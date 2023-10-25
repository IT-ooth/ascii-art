# 사진 전처리 데이터
from PIL import Image


class PreImage:
    def __init__(self, path: str, size_ratio):
        self.__img = self.setImage(path, size_ratio)

    @property
    def img(self):  # img 불러오기
        return self.__img

    # img setting
    def setImage(self, path: str, size_ratio=1):
        img = Image.open(path)

        # img resize
        def resize(img, size_ratio):
            x, y = img.size
            return img.resize((int(x*size_ratio), int(y*size_ratio)))
    
        return resize(img, size_ratio)
    
    def getGrayscale(self):  # 이미지를 grayScale로 만듦
        return self.img.convert("L")

    def getPixel(self):  # 이미지의 grayScale 데이터 -> iterator
        return self.getGrayscale().getdata()


# test code
if __name__ == "__main__":
    a = PreImage("tests\\resources\\ROKMC.jpg", 0.5)
    a.img.show()
