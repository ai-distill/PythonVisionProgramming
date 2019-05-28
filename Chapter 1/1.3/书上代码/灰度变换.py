from PIL import Image
from pylab import *

im = array(Image.open('empire.jpg').convert('L'))
imshow(im)
title('原图')
show()
# 将图像进行反相化处理，图像反相化处理就是用255减去每一个RGB颜色值
im2 = 255 - im
imshow(im2)
title('图像反相化处理')
show()
# 将图像像素值变换到100....200之间
im3 = (100.0/255) * im + 100
imshow(im3)
title('像素值变化到100-200之间')
show()
# 对图像像素值求平方后得到的图像，对图像使用二次函数变换
im4 = 255.0 * (im / 255.0) ** 2
imshow(im4)
title('图像使用二次函数变换')
show()

print(im.min(), im.max())


# array() 变换的相反操作可以使用 PIL 的 fromarray() 函数完成
pil_im = Image.fromarray(im)
