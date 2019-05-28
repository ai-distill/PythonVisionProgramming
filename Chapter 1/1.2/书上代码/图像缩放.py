from PIL import Image
from numpy import *


def imresize(im, sz):
    """
    图像缩放
    :param im: 图像对应的数据
    :param sz: 图像要缩放的大小
    :return:
    """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))


from pylab import *
imshow(imresize(array(Image.open('empire.jpg'), (200, 200))))
show()