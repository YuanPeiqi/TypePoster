import os
from PIL import Image


def image_processing():
    #  待处理图片路径下的所有文件名字
    all_file_names = os.listdir('E:\\h5-editor-master\\poster_backend\\static\\test_poster')
    for file_name in all_file_names:
        #  待处理图片路径
        img_path = Image.open(f'E:\\h5-editor-master\\poster_backend\\static\\test_poster\\{file_name}')
        #  resize图片大小，入口参数为一个tuple，新的图片的大小
        img_size = img_path.resize((1920, 2560))
        img_size = img_size.convert('RGB')  # 为防止报png图片通道数不对的错误
        #  处理图片后存储路径，以及存储格式
        img_size.save(f'E:\\h5-editor-master\\poster_backend\\static\\test_poster\\{file_name}', 'PNG')


if __name__ == '__main__':
    image_processing()
