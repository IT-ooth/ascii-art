# module
from PIL import Image


class img_map:
    def __init__(self, img):
        self.__img = Image.open(img)

    def getPixel(self):
        return self.img.getdata()
    
    @property
    def img(self):
        return self.__img

# test code
if __name__ == "__main__":
    a = img_map("img\\testImg.png")
    print(type(a.img))
    print(type(Image.open("img\\testImg.png")))
    # for item in a.getPixel():
    #     print(item)