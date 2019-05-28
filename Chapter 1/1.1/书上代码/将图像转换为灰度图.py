from PIL import Image
# 读取图像
pil_im = Image.open('./1.jpg')
# 将读取到的图像转换为灰度图
pil_im_L = pil_im.convert('L')

print(pil_im_L.save(']./2.jpg'))