# module
import cv2


class img_map:
    def __init__(self, img):
        self.grayscaleImg = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

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


# test
# a = img_map("img\ROKMC_dog.jpg")
# a.show()
