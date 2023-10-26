from PIL import Image
import yaml

START = 32
END = 127

#0~1 사이의 값으로 각 사진의 흑백비율을 리스트로 반환
def getDataset() -> list:
    dataset = [0.0 for _ in range(END)]

    for i in range(START,END):
        img = Image.open('tests\\resources\\ascii-data_img\\' + str(i) + '.png')
        img = img.convert("L")  # grayScale로 변경
        datas = img.getdata()   # img의 모든 픽셀값 가져오기

        img_size = img.size[0] * img.size[1]
        white_point = 0 # 글씨의 픽셀 수
        cutOff = 200    # white_pixel 값 = 204
        
        for item in datas:
            if item >= cutOff: # 204 = 흰색 12 = 검정
                white_point += 1
        
        dataset[i] = float(white_point / img_size)

    return dataset

# 0~1 스케일의 리스트를 0~255로 바꿈
# 이때 0:가장 흰색이 많은 사진, 255 : 배경색이 가장 많은 사진 기준
def changeScale(raw_dataset: list) -> list:
    max_val = max(raw_dataset[START:END])
    min_val = min(raw_dataset[START:END])

    dataset = list(raw_dataset)
    for ascii_num in range(START, END):
        dataset[ascii_num] = round((dataset[ascii_num] - min_val) / (max_val - min_val) * 255, 3)

    return dataset

if __name__ == "__main__":
    a = getDataset()
    a = changeScale(a)

    dic = dict()
    for key, value in enumerate(a[START:]):
        dic[int(key+START)] = value
    #print(dic)
    with open("ascii-art/resources/ascii-dataset.yml", 'w' , encoding='UTF8') as f:
        yaml.dump(dic, f)
        
    # for i, k in enumerate(a):
    #     print(str(i) + " : "+ str(k) + ",")