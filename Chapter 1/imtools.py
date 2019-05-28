"""
存储一些经常使用的图像操作
"""
import os
from PIL import Image
from numpy import *

def get_imlist(path):
    """
    返回目录中所有JPG图像的文件名列表
    :param path:
    :return:
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


def imresize(im, sz):
    """
    图像缩放
    :param im: 图像对应的数据
    :param sz: 图像要缩放的大小
    :return:
    """
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(sz))

print(get_imlist('.'))