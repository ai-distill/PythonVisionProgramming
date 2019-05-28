from PIL import Image
img = Image.open('1_1.jpg')
# 要调整一幅图像的尺寸，我们可以调用 resize() 方法。该方法的参数是一个元组，用来指定新图像的大小
print(img.size)
img = img.resize((128, 128))
img.save('1_1.jpg')
print(img.size)
# 要旋转一幅图像可以逆时针表示旋转角度，然后用rotate()方法
img = Image.open('1.jpg')
img.rotate(90)
img = img.save('1_2.jpg')

