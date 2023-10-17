#사진 데이터 전처리
#
#인데 아직 안 만들어져서 대충 옛날꺼 씀
# module
import cv2


class img_map:
    def __init__(self, img):

        self.grayscaleImg = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

    def show(self):
        cv2.imshow("", self.grayscaleImg)
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

    def printDataList(self):  # 잘 작동하는지 확인
        t = self.getDataList()
        for y in range(len(t)):
            for x in range(len(t[0])):
                print("%3d" % t[y][x], end=" ")
            print()

# test
#a = img_map("img/ROKMC_dog.jpg")


'''print(a.getDataList())
f = open("result.txt", "w")
f.write(str(a.getDataList()))
f.close()

a.show()'''
