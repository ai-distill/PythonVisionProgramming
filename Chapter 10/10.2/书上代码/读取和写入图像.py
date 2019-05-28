"""
下面这个简短的例子会载入一张图像，打印出图像大小，对图像进行转换并保存
为 .png 格式
"""
import cv2
# 读取图像,函数 imread() 返回图像为一个标准的 NumPy 数组
im = cv2.imread('empire.jpg')
# 打印图像大小
h, w = im.shape[:2]
print(h, w)
# 将图像转换为png格式并进行保存,
# 函数imwrite() 会 根据文件后缀自动转换图像
cv2.imwrite('empire.png', im)
