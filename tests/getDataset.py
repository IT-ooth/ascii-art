from PIL import Image

def getDataset() -> list:
    dataset = [0.0 for _ in range(128)]

    for i in range(32,128):
        img = Image.open('tests\\resources\\ascii-data_img\\' + str(i) + '.png')
        img = img.convert("L")  # grayScale로 변경
        datas = img.getdata()   # img의 모든 픽셀값 가져오기

        img_size = img.size[0] * img.size[1]
        white_point = 0 # 글씨의 픽셀 수
        cutOff = 200    # white_pixel 값 = 204
        
        for item in datas:
            if item >= cutOff: # 204 = 흰색 12 = 검정
                white_point += 1
        
        dataset[i] = round(white_point / img_size / 0.357, 3)
    
    return dataset

if __name__ == "__main__":
    a = getDataset()
    print(max(a))
    # for i, k in enumerate(a):
    #     print(str(i) + " : "+ str(k) + ",")