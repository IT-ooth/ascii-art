# module
import cv2
from PIL import Image


class img_map:
    def __init__(self, img):
        self.grayscaleImg = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
        self.img = Image.open(img).convert("L")

    def show(self):
        cv2.imshow("ROKMC_DOG", self.grayscaleImg)
        cv2.waitKey()
        cv2.destroyAllWindows()

    def getDataList(self):
        pixel_value = []
        (height, width) = self.grayscaleImg.shape

        for y in range(height):  # 모든 픽셀에 대한 grayScale을 가져옴
            t = []
            for x in range(width):
                t.append(self.grayscaleImg[y, x])
            pixel_value.append(t)

        return pixel_value

    def getData(self):
        data = self.img.getdata()
        return data

    def printDataList(self):  # 잘 작동하는지 확인
        t = self.getDataList()
        for y in range(len(t)):
            for x in range(len(t[0])):
                print("%3d" % t[y][x], end=" ")
            print()


# test
# a = img_map("img\\testImg.png")
# a.printDataList()
# a.show()
