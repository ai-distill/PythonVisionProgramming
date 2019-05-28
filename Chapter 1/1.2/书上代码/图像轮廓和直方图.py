from PIL import Image
from pylab import *

# 读取图像到数组中
im = array(Image.open('empire.jpg').convert('L'))

# 新建一个图像
figure()

# 不使用颜色信息
gray()

# 在原点的左上角显示轮廓图像
contour(im, origin='image')
axis('equal')
axis('off')




figure()
"""
hist() 函数的第二个参数指定小区间的数目。需要注意的是，因为 hist() 只接受一
维数组作为输入，所以我们在绘制图像直方图之前，必须先对图像进行压平处理。
flatten() 方法将任意数组按照行优先准则转换成一维数组
"""
hist(im.flatten(), 128)
show()