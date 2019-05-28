"""
存储一些经常使用的图像操作
"""
import os


def get_imlist(path):
    """
    返回目录中所有JPG图像的文件名列表
    :param path:
    :return:
    """
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith('.jpg')]


print(get_imlist('.'))