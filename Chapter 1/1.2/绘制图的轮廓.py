from PIL import Image
from pylab import *
data = array(Image.open('./2.jpg').convert('L'))
print(data.shape)
figure()
gray()
contour(data, origin='image')
axis("off")
axis("equal")
show()