from PIL import Image
from pylab import *
im = array(Image.open('empire.jpg'))
# <class 'numpy.ndarray'>
print(type(im))
# 每行的第一个元组表示图像数组的大小（行、列、颜色通道）
print(im.shape, im.dtype)

# 对图像进行灰度化处理，并且在创建数组时使用额外的参数“f”；
# 该参数将数据类型转换为浮点型
im = array(Image.open('empire.jpg').convert('L'), 'f')
print(im.shape, im.dtype)


# 数组中的元素可以使用下标访问。
# 位于坐标 i、j，以及颜色通道 k 的像素值可以使用如下方式访问
value = im[i, j, k]


# 将第 j 行的数值赋值给第 i 行
im[i, :] = im[j, :]
# 将第 i 列的所有数值设为 100
im[:, i] = 100
# 计算前 100 行、前 50 列所有数值的和
im[:100,:50].sum()
# 50~100 行，50~100 列（不包括第 100 行和第 100 列）
im[50:100, 50:100]
# 第 i 行所有数值的平均值
im[i, :].mean()
# 最后一列
im[:, -1]
# 倒数第二行
im[-2, :] or im[-2]


# 如果仅使用一个下标，则该下标为行下标