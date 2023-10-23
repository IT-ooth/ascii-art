# ascii-dataset 를 가져오기
import yaml

def get_asciiDataset() -> dict:
    with open("ascii-art\\resources\\ascii-dataset.yaml", 'r' , encoding='UTF8') as f:
        file = yaml.full_load(f)
        return file

if __name__ == "__main__":
    print(get_asciiDataset())
    