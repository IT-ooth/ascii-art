# ascii-dataset 가져오기
import yaml

def get_asciiDataset() -> dict:
    with open("ascii-art\\resources\\ascii-dataset.yml", 'r' , encoding='UTF8') as f:
        file = yaml.full_load(f)
        return file

if __name__ == "__main__":
    a = get_asciiDataset()
    for i, data in a.items():
        print(i, data)
