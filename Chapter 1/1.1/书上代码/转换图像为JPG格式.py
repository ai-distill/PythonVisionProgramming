from PIL import Image
import os

file_path = input('请输入文件绝对路径：')
if os.path.splitext(file_path)[1] != '.jpg':
    try:
        infile_image = Image.open(file_path)
        outfile_image = os.path.splitext(file_path)[0] + ".jpg"
        # save方法用于保存图像到指定文件名的文件
        infile_image.save(outfile_image)
    except IOError:
        print("转换失败")
