import warnings

import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

font = {'bold': 'C:\\Windows\\Fonts\\msyhbd.ttc', 'normal': 'C:\\Windows\\Fonts\\msyh.ttc'}
font_shift = 10
warnings.filterwarnings("ignore")


class Poster:
    def __init__(self, title, time, location, reporter, inviter, meeting_num, abstract, introduction,
                 canvas_width=680,
                 canvas_height=907,
                 photo_path='static/images/test_user/photo.png',
                 bg_path='static/images/test_user/bg.png',
                 logo_1_path='static/images/test_user/school_logo.png',
                 logo_2_path='static/images/test_user/department_logo.png',
                 qrcode_path='static/images/test_user/qrcode.png'):
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
        self._bg = scale(cv2.imread(bg_path, cv2.IMREAD_UNCHANGED), canvas_width, canvas_height)
        self._logo_1 = cv2.imread(logo_1_path, cv2.IMREAD_UNCHANGED)
        self._logo_2 = cv2.imread(logo_2_path, cv2.IMREAD_UNCHANGED)
        self._qrcode = scale(cv2.imread(qrcode_path, cv2.IMREAD_UNCHANGED), 300, 300)
        self._canvas_width = canvas_width
        self._canvas_height = canvas_height
        self._canvas = np.full(fill_value=255, shape=(self.canvas_height, self.canvas_width, 4), dtype=np.uint8)
        self._layouts = [
            {
                'id': 1,
                'preview': '',
                'description': '模板1',
                'hover': False,
                'data': [
                    {'type': "background", 'opacity': 0.7, 'url': "http://localhost:5000/get_image/test_user/bg.png"},
                    {'type': "rect", 'backgroundColor': '#FFFFFF', 'opacity': 0.6, 'w': 646, 'h': 427, 'x': 17, 'y': 463},
                    {'type': "rect", 'backgroundColor': '#FFFFFF', 'opacity': 0.6, 'w': 485, 'h': 212, 'x': 178, 'y': 213},
                    {'type': "rect", 'backgroundColor': '#000000', 'opacity': 1, 'w': 612, 'h': 4, 'x': 34, 'y': 671},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/department_logo.png", 'w': 265, 'h': 55, 'x': 390, 'y': 17},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/school_logo.png", 'w': 212, 'h': 55, 'x': 17, 'y': 17},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/photo.png", 'w': 140, 'h': 212, 'x': 17, 'y': 214},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/qrcode.png", 'w': 106, 'h': 106, 'x': 542, 'y': 300},
                    {
                        'type': "title", 'content': '',
                        'font': {
                            'fontSize': '34px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '158%'
                        },
                        'w': 560, 'h': 120, 'x': 60, 'y': 76
                    },
                    {
                        'type': "text", 'content': "时间:", 'info_type': 'default',
                        'font': {
                            'fontSize': '18px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 70, 'h': 35, 'x': 185, 'y': 225
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'time',
                        'font': {
                            'fontSize': '18px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 400, 'h': 35, 'x': 238, 'y': 225
                    },
                    {
                        'type': "text", 'content': "地点:", 'info_type': 'default',
                        'font': {
                            'fontSize': '18px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 70, 'h': 35, 'x': 185, 'y': 260
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'location',
                        'font': {
                            'fontSize': '18px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 186, 'h': 35, 'x': 238, 'y': 260
                    },
                    {
                        'type': "text", 'content': "报告人:", 'info_type': 'default',
                        'font': {
                            'fontSize': '18px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 90, 'h': 35, 'x': 185, 'y': 295
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'reporter',
                        'font': {
                            'fontSize': '18px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 220, 'h': 35, 'x': 256, 'y': 295
                    },
                    {
                        'type': "text", 'content': "邀请人:", 'info_type': 'default',
                        'font': {
                            'fontSize': '18px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 90, 'h': 35, 'x': 185, 'y': 330
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'inviter',
                        'font': {
                            'fontSize': '18px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 290, 'h': 35, 'x': 256, 'y': 330
                    },
                    {
                        'type': "text", 'content': "腾讯会议号:", 'info_type': 'default',
                        'font': {
                            'fontSize': '18px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 130, 'h': 35, 'x': 185, 'y': 365
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'meeting_num',
                        'font': {
                            'fontSize': '18px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 220, 'h': 35, 'x': 290, 'y': 365
                    },
                    {
                        'type': "text", 'content': "Abstract:", 'info_type': 'default',
                        'font': {
                            'fontSize': '19px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 120, 'h': 50, 'x': 25, 'y': 465
                    },
                    {
                        'type': "text", 'content': "About the speaker:", 'info_type': 'default',
                        'font': {
                            'fontSize': '19px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '158%'
                        },
                        'w': 220, 'h': 50, 'x': 25, 'y': 678
                    },
                    {
                        'type': "text",
                        'content': '',
                        'info_type': 'abstract',
                        'font': {
                            'fontSize': '14px',
                            'fontFamily': '"Times New Roman",Georgia,Serif',
                            'color': '#595959',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '135%'
                        },
                        'w': 625,
                        'h': 170,
                        'x': 26,
                        'y': 495
                    },
                    {
                        'type': "text",
                        'content': '',
                        'info_type': 'introduction',
                        'font': {
                            'fontSize': '14px',
                            'fontFamily': '"Times New Roman",Georgia,Serif',
                            'color': '#595959',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '135%'
                        },
                        'w': 625,
                        'h': 170,
                        'x': 26,
                        'y': 708
                    },
                ]
            },
            {
                'id': 2,
                'preview': '',
                'description': '模板2',
                'hover': False,
                'data': [
                    {'type': "background", 'opacity': 1, 'url': "http://localhost:5000/get_image/test_user/bg2.png"},
                    {'type': "rect", 'backgroundColor': '#FFFFFF', 'opacity': 0.6, 'w': 646, 'h': 200, 'x': 17, 'y': 320},
                    {'type': "rect", 'backgroundColor': '#FFFFFF', 'opacity': 0.6, 'w': 646, 'h': 350, 'x': 17, 'y': 540},
                    {'type': "rect", 'backgroundColor': '#FFFFFF', 'opacity': 0.6, 'w': 480, 'h': 230, 'x': 180, 'y': 76},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/department_logo.png", 'w': 265, 'h': 55, 'x': 390, 'y': 10},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/school_logo.png", 'w': 212, 'h': 55, 'x': 10, 'y': 10},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/photo.png", 'w': 150, 'h': 230, 'x': 17, 'y': 76},
                    {'type': "img", 'url': "http://localhost:5000/get_image/test_user/qrcode.png", 'w': 106, 'h': 106, 'x': 542, 'y': 190},
                    {
                        'type': "title", 'content': '',
                        'font': {
                            'fontSize': '22px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '158%'
                        },
                        'w': 460, 'h': 60, 'x': 180, 'y': 76
                    },
                    {
                        'type': "text", 'content': "时间:", 'info_type': 'default',
                        'font': {
                            'fontSize': '16px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 70, 'h': 35, 'x': 185, 'y': 155
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'time',
                        'font': {
                            'fontSize': '16px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 330, 'h': 35, 'x': 238, 'y': 155
                    },
                    {
                        'type': "text", 'content': "地点:", 'info_type': 'default',
                        'font': {
                            'fontSize': '16px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 70, 'h': 35, 'x': 185, 'y': 183
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'location',
                        'font': {
                            'fontSize': '16px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 166, 'h': 35, 'x': 238, 'y': 183
                    },
                    {
                        'type': "text", 'content': "报告人:", 'info_type': 'default',
                        'font': {
                            'fontSize': '16px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 80, 'h': 35, 'x': 185, 'y': 211
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'reporter',
                        'font': {
                            'fontSize': '16px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 200, 'h': 35, 'x': 256, 'y': 211
                    },
                    {
                        'type': "text", 'content': "邀请人:", 'info_type': 'default',
                        'font': {
                            'fontSize': '16px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 80, 'h': 35, 'x': 185, 'y': 239
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'inviter',
                        'font': {
                            'fontSize': '16px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 270, 'h': 35, 'x': 256, 'y': 239
                    },
                    {
                        'type': "text", 'content': "腾讯会议号:", 'info_type': 'default',
                        'font': {
                            'fontSize': '16px',
                            'color': '#2D5960',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 120, 'h': 35, 'x': 185, 'y': 267
                    },
                    {
                        'type': "text", 'content': '', 'info_type': 'meeting_num',
                        'font': {
                            'fontSize': '16px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 200, 'h': 35, 'x': 290, 'y': 267
                    },
                    {
                        'type': "text", 'content': "Abstract:", 'info_type': 'default',
                        'font': {
                            'fontSize': '19px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '100%'
                        },
                        'w': 120, 'h': 50, 'x': 25, 'y': 323
                    },
                    {
                        'type': "text", 'content': "About the speaker:", 'info_type': 'default',
                        'font': {
                            'fontSize': '19px',
                            'color': '#000000',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '158%'
                        },
                        'w': 220, 'h': 50, 'x': 25, 'y': 535
                    },
                    {
                        'type': "text",
                        'content': '',
                        'info_type': 'abstract',
                        'font': {
                            'fontSize': '14px',
                            'fontFamily': '"Times New Roman",Georgia,Serif',
                            'color': '#595959',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '158%'
                        },
                        'w': 625,
                        'h': 165,
                        'x': 26,
                        'y': 353
                    },
                    {
                        'type': "text",
                        'content': '',
                        'info_type': 'introduction',
                        'font': {
                            'fontSize': '14px',
                            'fontFamily': '"Times New Roman",Georgia,Serif',
                            'color': '#595959',
                            'fontWeight': 'bold',
                            'textAlign': 'left',
                            'fontStyle': '',
                            'letterSpacing': 0,
                            'lineHeight': '135%'
                        },
                        'w': 625,
                        'h': 310,
                        'x': 26,
                        'y': 565
                    },
                ]
            },
            {'id': 3, 'preview': '', 'description': '模板3', 'hover': False, 'data': []},
            {'id': 4, 'preview': '', 'description': '模板4', 'hover': False, 'data': []},
            {'id': 5, 'preview': '', 'description': '模板5', 'hover': False, 'data': []}
        ]
        for layout in self._layouts:
            for item in layout['data']:
                if item['type'] == 'title':
                    item['content'] = title
                elif item['type'] == 'text' and item['info_type'] == 'time':
                    item['content'] = time
                elif item['type'] == 'text' and item['info_type'] == 'location':
                    item['content'] = location
                elif item['type'] == 'text' and item['info_type'] == 'reporter':
                    item['content'] = reporter
                elif item['type'] == 'text' and item['info_type'] == 'inviter':
                    item['content'] = inviter
                elif item['type'] == 'text' and item['info_type'] == 'meeting_num':
                    item['content'] = meeting_num
                elif item['type'] == 'text' and item['info_type'] == 'abstract':
                    item['content'] = abstract
                elif item['type'] == 'text' and item['info_type'] == 'introduction':
                    item['content'] = introduction

    @property
    def layouts(self):
        return self._layouts

    @property
    def canvas_width(self):
        return self._canvas_width

    @property
    def canvas_height(self):
        return self._canvas_height

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, value):
        self._canvas = value

    def generate(self, save_path, layout_index):
        # 调整背景透明度
        template_data = self._layouts[layout_index]['data']
        if not template_data:
            return
        self._canvas = np.full(fill_value=255, shape=(self.canvas_height, self.canvas_width, 3), dtype=np.uint8)
        if template_data[0]['type'] == 'background':
            bg_alpha = template_data[0]['opacity']
            url_list = template_data[0]['url'].split('/')
            bg_img = del_alpha_channel(scale(cv2.imread(f'static/images/{url_list[-2]}/{url_list[-1]}', cv2.IMREAD_UNCHANGED), self.canvas_width, self.canvas_height))
            self._canvas = np.full(fill_value=255, shape=bg_img.shape, dtype=np.uint8)
            self._canvas = cv2.addWeighted(bg_img, bg_alpha, self._canvas, 1 - bg_alpha, 1)

        # 添加矩形
        for item in template_data:
            if item['type'] == 'rect':
                self._canvas = add_rect(self._canvas, item['x'], item['y'], item['x'] + item['w'],
                                        item['y'] + item['h'], hex2RGB(item['backgroundColor']), item['opacity'])

        # 叠加图片元素
        for item in template_data:
            if item['type'] == 'img':
                x1 = item['x']
                y1 = item['y']
                x2 = item['x'] + item['w']
                y2 = item['y'] + item['h']
                url_list = item['url'].split('/')
                img = scale(cv2.imread(f'static/images/{url_list[-2]}/{url_list[-1]}', cv2.IMREAD_UNCHANGED), item['w'], item['h'])
                self._canvas = paste_img(self._canvas, img, y1, y2, x1, x2)

        # x1 = 50
        # y1 = 50
        # x2 = x1 + self._logo_1.shape[1]
        # y2 = y1 + self._logo_1.shape[0]
        # self._canvas = paste_img(self._canvas, self._logo_1, y1, y2, x1, x2)
        #
        # x1 = 1100
        # y1 = 50
        # x2 = x1 + self._logo_2.shape[1]
        # y2 = y1 + self._logo_2.shape[0]
        # self._canvas = paste_img(self._canvas, self._logo_2, y1, y2, x1, x2)
        #
        # x1 = 50
        # y1 = 600
        # x2 = x1 + self._photo.shape[1]
        # y2 = y1 + self._photo.shape[0]
        # self._canvas = paste_img(self._canvas, self._photo, y1, y2, x1, x2)
        # cv2.imwrite('assets/temp/temp_poster.png', self._canvas)
        #
        # x1 = 1530
        # y1 = 850
        # x2 = x1 + self._qrcode.shape[1]
        # y2 = y1 + self._qrcode.shape[0]
        # self._canvas = paste_img(self._canvas, self._qrcode, y1, y2, x1, x2)
        cv2.imwrite('assets/temp/temp_poster.png', self._canvas)

        # 图像处理已经完成，剩余工作使用PIL库添加文字
        self._canvas = Image.open('assets/temp/temp_poster.png')

        # 添加海报标题与讲座基础信息
        for item in template_data:
            if item['type'] == 'title' or item['type'] == 'text':
                font_path = font['bold'] if item['font']['fontWeight'] == 'bold' else font['normal']
                font_size = add_text(img=self._canvas, text=item['content'], max_width=item['w'], max_height=item['h'], font_path=font_path,
                                     x=item['x'], y=item['y'], font_size=int(item['font']['fontSize'][:-2]),
                                     font_color=hex2RGB(item['font']['color']))
                item['font']['fontSize'] = f'{font_size}px'
        # 添加讲座基础信息
        # info_font_size = 50
        # add_text(img=temp_canvas, text='时间:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=550, y=650, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        # add_text(img=temp_canvas, text=self._time, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
        #          x=550 + 3 * info_font_size, y=650 + font_shift, font_size=info_font_size, font_color=(0, 0, 0),
        #          bold=True)
        # add_text(img=temp_canvas, text='地点:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=550, y=750, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        # add_text(img=temp_canvas, text=self._location, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
        #          x=550 + 3 * info_font_size, y=750 + font_shift, font_size=info_font_size, font_color=(0, 0, 0),
        #          bold=True)
        # add_text(img=temp_canvas, text='报告人:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=550, y=850, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        # add_text(img=temp_canvas, text=self._reporter, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
        #          x=550 + 4 * info_font_size, y=850 + font_shift, font_size=info_font_size, font_color=(0, 0, 0),
        #          bold=True)
        # add_text(img=temp_canvas, text='邀请人: ', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=550, y=950, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        # add_text(img=temp_canvas, text=self._inviter, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
        #          x=550 + 4 * info_font_size, y=950 + font_shift, font_size=info_font_size, font_color=(0, 0, 0),
        #          bold=True)
        # add_text(img=temp_canvas, text='腾讯会议号:', max_width=1100, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=550, y=1050, font_size=info_font_size, font_color=(45, 89, 96), bold=False)
        # add_text(img=temp_canvas, text=self._meeting_num, max_width=1100, font_path="C:\\Windows\\Fonts\\simfang.ttf",
        #          x=550 + 6 * info_font_size, y=1050 + font_shift, font_size=info_font_size, font_color=(0, 0, 0),
        #          bold=True)
        #
        # # 添加摘要与讲者介绍
        # text_size = 45
        # add_text(img=temp_canvas, text='Abstract:', max_width=1720, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=100, y=1330, font_size=info_font_size, font_color=(0, 0, 0), bold=False)
        # add_text(img=temp_canvas, text=self._abstract, max_width=1720, font_path="C:\\Windows\\Fonts\\timesbd.ttf",
        #          x=100, y=1410, font_size=text_size, font_color=(89, 89, 89), bold=False)
        # add_text(img=temp_canvas, text='About the speaker:', max_width=1720, font_path="C:\\Windows\\Fonts\\msyhbd.ttc",
        #          x=100, y=1950, font_size=info_font_size, font_color=(0, 0, 0), bold=False)
        # add_text(img=temp_canvas, text=self._introduction, max_width=1720, font_path="C:\\Windows\\Fonts\\timesbd.ttf",
        #          x=100, y=2030, font_size=text_size, font_color=(89, 89, 89), bold=False)
        #

        # 保存最终版海报
        self._canvas.save(save_path)


def hex2RGB(hex_code):
    return tuple(int(hex_code[i:i + 2], 16) for i in (1, 3, 5))


def del_alpha_channel(img):
    """
    为jpg图像删除alpha通道
    """
    if img.shape[2] == 3:
        return img
    b_channel, g_channel, r_channel, _ = cv2.split(img)  # 剥离图像通道
    img_new = cv2.merge((b_channel, g_channel, r_channel))  # 融合通道
    return img_new


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


def split_text(text, max_width, font_path, font_size):
    ret = ''
    width = 0  # 当前行宽度, 单位为px
    font = ImageFont.truetype(font_path, font_size)
    char_width, char_height = font.getsize('A')
    max_width = max_width - 2 * char_width
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
    return ret + '\n', char_width, char_height


def add_text(img, text, font_path, x, y, max_width, max_height, font_size, font_color):
    """
    在图片上添加粗体文字信息
    """
    draw = ImageDraw.Draw(img)
    text_slice, char_width, char_height = split_text(text, max_width, font_path, font_size)
    # 调大字体
    if 1.5 * char_height * text_slice.count('\n') < 0.6 * max_height:
        font_size = int(font_size * 1.3)
        text_slice, char_width, char_height = split_text(text, max_width, font_path, font_size)
    spacing = round(0.5 * char_height)
    font = ImageFont.truetype(font_path, font_size)
    draw.text((x + char_width, y + spacing), text_slice, font_color, font, spacing=spacing)
    return font_size


def add_rect(img, x1, y1, x2, y2, color, opacity):
    x = x2 - x1
    y = y2 - y1
    blender = np.zeros(img[y1:y2, x1:x2].shape, dtype=np.uint8)
    cv2.rectangle(blender, (0, 0), (x, y), color, -1)
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
    bg_path = 'static/images/test_user/bg.png'
    logo_1_path = 'static/images/test_user/school_logo.png'
    logo_2_path = 'static/images/test_user/department_logo.png'
    photo_path = 'static/images/test_user/photo.png'
    qrcode_path = 'static/images/test_user/qrcode.png'
    poster = Poster(title=title, time=time, location=location, reporter=reporter, inviter=inviter,
                    meeting_num=meeting_num, abstract=abstract, introduction=introduction,
                    bg_path=bg_path, logo_1_path=logo_1_path, logo_2_path=logo_2_path, qrcode_path=qrcode_path,
                    photo_path=photo_path)
    for index in range(len(poster.layouts)):
        poster.generate(f'static/templates/test_user/template{index}.png', index)
        poster.layouts[index]['preview'] = f'http://localhost:5000/get_poster_view/test_user/template{index}.png'
