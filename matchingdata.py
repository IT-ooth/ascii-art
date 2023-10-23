from PIL import Image
import numpy


class Image:

    def __init__(self, image_path, image_name):
        self.image_path = image_path
        self.image_name = image_name

    def image_crop(self, grid_w, grid_h):

        img = Image.open(self.image_path)
        image_w = img.size[0]
        image_h = img.size[1]

        for w in range(image_w):
            for h in range(image_h):
                box = (w * grid_w, h * grid_h, (w + 1) * grid_w, (h + 1) * grid_h)

        return



