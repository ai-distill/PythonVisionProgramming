import os
from PIL import Image

image = Image.open('./1.jpg')
# 获得图像的尺寸
print(image.size)
#  thumbnail() 方法接受一个元组参数
# （该参数指定生成缩略图的大小），然后将图像转换成符合元组参数指定大小的缩略图
image.thumbnail((128,128))
image.save('3.jpg')
