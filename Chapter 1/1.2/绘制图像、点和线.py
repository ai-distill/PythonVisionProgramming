from pylab import *
from PIL import Image

img = Image.open('./书上代码/empire.jpg')
data = array(img)

imshow(data)

x = [100, 100, 400, 400]
y = [200, 500, 200, 500]

plot(x, y, 'r*')

plot(x[:2], y[:2])

# 坐标轴不显示
axis("off")

title('Practical')
show()
