# pixel 값과 ascii 값을 대조 ( 단 제어문자는 제외 )
# 32~127 까지 ascii  값 사용

# 해상도 비교 ( 경향성 X ) ( *해상도 = 20x20 안에 글씨를 쓰기 위한 검정 점이 얼마나 찍혀있는가 )
# 단순하게 일정한 범위 안에 검정 픽셀이 얼마나 찍혀있는지를 기준으로
from PIL import Image

path = "img\\ascii_code\PNG\\"
dataSet = [0 for _ in range(128)]  # ascii 코드 값이 가지는 해상도의 집합

# 각 ascii-code 들이 가지는 해상도를 구해서 dataSet에 추가
for code in range(32, 127):
    img_path = path + str(code) + ".png"  #  ascii_code 값을 하나씩 꺼냄
    img = Image.open(img_path)

    datas = img.getdata()

    cutOff = 103  # 배경이 지워지는 정도
    black_point = 0  # 20x20 크기의 사진 안에 검정색이 몇개가 있는가

    for item in datas:
        if item <= cutOff:  # 배경의 검정이 아닌 글씨의 검정일 때
            black_point += 1  # 점 하나씩 더하기

    dataSet[code] = black_point

# 이미지 파일의 해상도와 비교해서 넣기
img = Image.open("img\ROKMC_dog.jpg")

datas = img.convert("L").getdata()

# 매칭
# for item in datas:
#     if
