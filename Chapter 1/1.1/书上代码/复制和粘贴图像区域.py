from PIL import Image

img = Image.open('./1.jpg')

# 使用 crop() 方法可以从一幅图像中裁剪指定区域
# 区域使用四元组来指定。四元组的坐标依次是（左，上，右，下）。PIL 中指定
# 坐标系的左上角坐标为（0，0）
box = (100,100,400,400)
region = img.crop(box)
# 旋转上面代码中获取的区域，然后使用
# paste() 方法将该区域放回去
region = region.transpose(Image.ROTATE_180)
img.paste(region, box)
img.save('4.jpg')
