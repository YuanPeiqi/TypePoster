import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

template = [{'title': ['字体字号，文本框位置，文本框宽度，文字颜色，粗体斜体，行距']}]
font_shift = 10


class Poster:
    def __init__(self, title, time, location, reporter, inviter, meeting_num, abstract, introduction, photo_path,
                 bg_path='assets/img_resource/bg.png', logo_1_path='assets/img_resource/school_logo.png',
                 logo_2_path='assets/img_resource/department_logo.png', qrcode_path='assets/img_resource/qrcode.png'):
        """
        :param title: 报告主题
        :param time: 报告举办时间
        :param location: 报告举办地点
        :param reporter: 报告人
        :param inviter: 邀请人
        :param meeting_num: 腾讯会议号
        :param abstract: 报告摘要
        :param introduction: 讲者简介
        :param photo_path: 讲者相片
        :param bg_path: 背景图片
        :param logo_1_path: 学校标识
        :param logo_2_path: 系标识/讲堂标识
        """
        # 获取海报信息, 读取图像元素, 初始化海报面板
        self._title = title
        self._time = time
        self._location = location
        self._reporter = reporter
        self._inviter = inviter
        self._meeting_num = meeting_num
        self._abstract = abstract
        self._introduction = introduction
        self._bg = scale(cv2.imread(bg_path, cv2.IMREAD_UNCHANGED), 1920, 2560)
        self._photo = scale(cv2.imread(photo_path, cv2.IMREAD_UNCHANGED), 400, 600)
        self._logo_1 = cv2.imread(logo_1_path, cv2.IMREAD_UNCHANGED)
        self._logo_2 = cv2.imread(logo_2_path, cv2.IMREAD_UNCHANGED)
        self._qrcode = scale(cv2.imread(qrcode_path, cv2.IMREAD_UNCHANGED), 300, 300)
        self._canvas = np.full(fill_value=255, shape=self._bg.shape, dtype=np.uint8)
        self._layout = []

    def generate(self, save_path):
        # 调整背景透明度
        bg_alpha = 0.3
        self._canvas = cv2.addWeighted(self._bg, bg_alpha, self._canvas, 1 - bg_alpha, 1)

        # 添加矩形
        self._canvas = add_rect(self._canvas, 500, 600, 1870, 1200, (255, 255, 255), 0.6)
        self._canvas = add_rect(self._canvas, 50, 1300, 1870, 2510, (255, 255, 255), 0.6)
        self._canvas = add_rect(self._canvas, 100, 1900, 1820, 1910, (45, 89, 96), 1.0)

        # 叠加图片元素
        x1 = 50
        y1 = 50
        x2 = x1 + self._logo_1.shape[1]
        y2 = y1 + self._logo_1.shape[0]
        self._canvas = paste_img(self._canvas, self._logo_1, y1, y2, x1, x2)

        x1 = 1100
        y1 = 50
        x2 = x1 + self._logo_2.shape[1]
        y2 = y1 + self._logo_2.shape[0]
        self._canvas = paste_img(self._canvas, self._logo_2, y1, y2, x1, x2)

        x1 = 50
        y1 = 600
        x2 = x1 + self._photo.shape[1]
        y2 = y1 + self._photo.shape[0]
        self._canvas = paste_img(self._canvas, self._photo, y1, y2, x1, x2)
        cv2.imwrite('assets/temp/temp_poster.png', self._canvas)

        x1 = 1530
        y1 = 850
        x2 = x1 + self._qrcode.shape[1]
        y2 = y1 + self._qrcode.shape[0]
        self._canvas = paste_img(self._canvas, self._qrcode, y1, y2, x1, x2)
        cv2.imwrite('assets/temp/temp_poster.png', self._canvas)

        # 图像处理已经完成，剩余工作使用PIL库添加文字
        temp_canvas = Image.open('assets/temp/temp_poster.png')

        # 添加海报标题
        add_text(img=temp_canvas, text=self._title, max_width=1520, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=200, y=250, font_size=90, font_color=(45, 89, 96), bold=False)

        # 添加讲座基础信息
        info_font_size = 50
        add_text(img=temp_canvas, text='时间:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=550, y=650, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        add_text(img=temp_canvas, text=self._time, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
                 x=550 + 3 * info_font_size, y=650 + font_shift, font_size=info_font_size, font_color=(0, 0, 0), bold=True)
        add_text(img=temp_canvas, text='地点:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=550, y=750, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        add_text(img=temp_canvas, text=self._location, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
                 x=550 + 3 * info_font_size, y=750 + font_shift, font_size=info_font_size, font_color=(0, 0, 0), bold=True)
        add_text(img=temp_canvas, text='演讲人:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=550, y=850, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        add_text(img=temp_canvas, text=self._reporter, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
                 x=550 + 4 * info_font_size, y=850 + font_shift, font_size=info_font_size, font_color=(0, 0, 0), bold=True)
        add_text(img=temp_canvas, text='邀请人: ', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=550, y=950, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        add_text(img=temp_canvas, text=self._inviter, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
                 x=550 + 4 * info_font_size, y=950 + font_shift, font_size=info_font_size, font_color=(0, 0, 0), bold=True)
        add_text(img=temp_canvas, text='腾讯会议号:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=550, y=1050, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        add_text(img=temp_canvas, text=self._meeting_num, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
                 x=550 + 6 * info_font_size, y=1050 + font_shift, font_size=info_font_size, font_color=(0, 0, 0), bold=True)

        # 添加摘要与讲者介绍
        text_size = 45
        add_text(img=temp_canvas, text='Abstract:', max_width=1720, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=100, y=1330, font_size=info_font_size, font_color=(0, 0, 0), bold=False)
        add_text(img=temp_canvas, text=self._abstract, max_width=1720, font_path="C:\\Windows\\Fonts\\timesbd.ttf",
                 x=100, y=1410, font_size=text_size, font_color=(89, 89, 89), bold=False)
        add_text(img=temp_canvas, text='About the speaker:', max_width=1720, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
                 x=100, y=1950, font_size=info_font_size, font_color=(0, 0, 0), bold=False)
        add_text(img=temp_canvas, text=self._introduction, max_width=1720, font_path="C:\\Windows\\Fonts\\timesbd.ttf",
                 x=100, y=2030, font_size=text_size, font_color=(89, 89, 89), bold=False)

        # 保存最终版海报
        temp_canvas.save(save_path)

    def get_layout(self):
        return self._layout


def add_alpha_channel(img):
    """
    为jpg图像添加alpha通道
    """
    b_channel, g_channel, r_channel = cv2.split(img)  # 剥离jpg图像通道
    alpha_channel = np.ones(b_channel.shape, dtype=b_channel.dtype) * 255  # 创建Alpha通道
    img_new = cv2.merge((b_channel, g_channel, r_channel, alpha_channel))  # 融合通道
    return img_new


def paste_img(bg_img, element_img, y1, y2, x1, x2):
    """
    将png透明图像与jpg图像叠加
    y1,y2,x1,x2为叠加位置坐标值
    """
    # 判断jpg图像是否已经为4通道
    if bg_img.shape[2] == 3:
        bg_img = add_alpha_channel(bg_img)
    if element_img.shape[2] == 3:
        element_img = add_alpha_channel(element_img)
    """
    当叠加图像时，可能因为叠加位置设置不当，导致png图像的边界超过背景jpg图像，而程序报错
    这里设定一系列叠加位置的限制，可以满足png图像超出jpg图像范围时，依然可以正常叠加
    """
    yy1 = 0
    yy2 = element_img.shape[0]
    xx1 = 0
    xx2 = element_img.shape[1]

    if x1 < 0:
        xx1 = -x1
        x1 = 0
    if y1 < 0:
        yy1 = - y1
        y1 = 0
    if x2 > bg_img.shape[1]:
        xx2 = element_img.shape[1] - (x2 - bg_img.shape[1])
        x2 = bg_img.shape[1]
    if y2 > bg_img.shape[0]:
        yy2 = element_img.shape[0] - (y2 - bg_img.shape[0])
        y2 = bg_img.shape[0]

    # 获取要覆盖图像的alpha值，将像素值除以255，使值保持在0-1之间
    alpha_element = element_img[yy1:yy2, xx1:xx2, 3] / 255.0
    alpha_bg = 1 - alpha_element

    # 开始叠加
    for c in range(0, 3):
        bg_img[y1:y2, x1:x2, c] = (
                    (alpha_bg * bg_img[y1:y2, x1:x2, c]) + (alpha_element * element_img[yy1:yy2, xx1:xx2, c]))
    return bg_img


def split_text(text, max_width, font):
    ret = ''
    width = 0  # 当前行宽度, 单位为px
    for c in text:
        char_width, char_height = font.getsize(c)
        if c == '\n':
            width = 0
            ret += c
            continue
        if max_width < width + char_width:  # 剩余位置不够下一个字符
            width = char_width
            ret += '\n' + c
        else:
            width += char_width
            ret += c
    if ret.endswith('\n'):
        return ret
    return ret + '\n'


def add_text(img, text, font_path, x, y, max_width, font_size, font_color, bold):
    """
    在图片上添加粗体文字信息
    """
    font = ImageFont.truetype(font_path, font_size)
    _, char_height = font.getsize('A')
    spacing = round(0.5 * char_height)
    draw = ImageDraw.Draw(img)
    text = split_text(text, max_width, font)
    if bold:
        for j in range(-1, 2):
            for k in range(-1, 2):
                draw.text((x + j, y + k), text, font_color, font, spacing=spacing)
    else:
        draw.text((x, y), text, font_color, font, spacing=spacing)
    return img


def add_rect(img, x1, y1, x2, y2, color, opacity):
    x = x2-x1
    y = y2-y1
    blender = np.zeros(img[y1:y2, x1:x2].shape, dtype=np.uint8)
    cv2.rectangle(blender, (0, 0), (x, y), (color[2], color[1], color[0]), -1)
    img[y1:y2, x1:x2] = cv2.addWeighted(img[y1:y2, x1:x2], 1 - opacity, blender, opacity, 0)
    return img


def show_and_block(img):
    cv2.imshow("img_show", img)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()


def set_opacity(img, opacity=0.7):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    img[..., 3] = round(255 * opacity)
    return img


def cut_img(img, x0, y0, x1, y1):
    """
    (x0, y0)为截取图片的左上角坐标
    (x1, y1)为截取图片的右下角坐标
    """
    return img.crop((x0, y0, x1, y1))


def scale(img, target_width, target_height):
    """
    :param img: 需要缩小的图片对象
    :param target_width: 目标宽度
    :param target_height: 目标高度
    :return: 按比例缩小后的图片对象
    """
    img = cv2.resize(img, (target_width, target_height), interpolation=cv2.INTER_CUBIC)
    return img


if __name__ == '__main__':
    title = '文字到海报的端到端生成, 测试一下文字长度会不会超出海报'
    time = '2022年11月16日(周三) 9:30-11.30'
    location = '第一科研楼报告厅'
    reporter = '陈明 副教授/杜克大学'
    inviter = '原佩琦 学术垃圾/南方科技大学'
    meeting_num = '123-456-789'
    abstract = 'We present a novel method for blending hierarchical layouts with semantic labels. ' \
               'The core of our method is a hierarchical structure correspondence algorithm, ' \
               'which recursively finds optimal substructure correspondences, ' \
               'achieving a globally optimal correspondence between a pair of hierarchical layouts. ' \
               'This correspondence is consistent with the structures of both layouts, ' \
               'allowing us to define the union of the layouts’ structures. ' \
               'The resulting compound structure helps extract intermediate layout structures, ' \
               'from which blended layouts can be generated via an optimization approach.'
    introduction = 'We present a novel method for blending hierarchical layouts with semantic labels. ' \
                   'The core of our method is a hierarchical structure correspondence algorithm, ' \
                   'which recursively finds optimal substructure correspondences, ' \
                   'achieving a globally optimal correspondence between a pair of hierarchical layouts. ' \
                   'This correspondence is consistent with the structures of both layouts, ' \
                   'allowing us to define the union of the layouts’ structures. ' \
                   'The resulting compound structure helps extract intermediate layout structures, ' \
                   'from which blended layouts can be generated via an optimization approach.'
    bg_path = 'assets/img_resource/bg.png'
    logo_1_path = 'assets/img_resource/school_logo.png'
    logo_2_path = 'assets/img_resource/department_logo.png'
    photo_path = 'assets/img_resource/photo.png'
    poster = Poster(title=title, time=time, location=location, reporter=reporter, inviter=inviter,
                    meeting_num=meeting_num,abstract=abstract, introduction=introduction,
                    bg_path=bg_path, logo_1_path=logo_1_path, logo_2_path=logo_2_path,
                    photo_path=photo_path)
    poster.generate('assets/result/result.png')
