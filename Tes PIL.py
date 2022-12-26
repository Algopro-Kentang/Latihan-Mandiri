from PIL import Image

class testing(object):
    def __init__(self, file_name):
        self.open = Image.open(file_name)
    def show(self):
        self.open.show()
    def image_rotate(self):
        rotate = self.open.rotate(90, expand=True)
        rotate.show()
    def image_flip_horizontal(self):
        flip = self.open.transpose(6)
        flip.show()
    def image_flip_vertical(self):
        flip = self.open.transpose(3)
        flip.show()

gambar = testing("1000126.jpg")
gambar.image_flip_horizontal()