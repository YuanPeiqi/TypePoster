import os
import copy
import warnings

from PIL import ImageFont
from poster_backend.config import font_path_global, style_list, English2Chinese, CONTENT_TYPE
warnings.filterwarnings("ignore")


def json2lay(layout, user):
    return f"static\\templates\\{user}\\layout_files\\{layout}"


def lay2json(output_dir, filename, bg1, bg2):
    layout_path = os.path.join(output_dir, filename)
    with open(layout_path, 'r') as f:
        _ = f.readline()
        node_num = int(f.readline().replace('\n', ''))
        node_attributes = {}
        for i in range(node_num):
            node = [int(str_num) for str_num in f.readline().replace('\n', '').split()]
            node_attributes[node[0]] = node
            if node[-1] in node_attributes.keys():
                node_attributes.pop(node[-1])
        id = int(float(filename[0:4]) * 100)
        data = [{'type': "background", 'opacity': 0.7, 'url': bg1 if id <= 50 else bg2}]
        title_flag = False
        for node in node_attributes.values():
            if CONTENT_TYPE[node[-2]] == 'title':
                temp = {'type': 'title', 'content': '', 'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6]}
                if title_flag:
                    temp['type'] = 'subtitle'
                    temp['y'] -= 10
                    temp['h'] -= 10
                else:
                    temp['h'] += 20
                data.append(temp)
                title_flag = True
            elif CONTENT_TYPE[node[-2]] == 'abstract':
                data.append({'type': "rect", 'rect_type': 'abstract',
                             'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6], 'content': []})
            elif CONTENT_TYPE[node[-2]] == 'introduction':
                data.append({'type': "rect", 'rect_type': 'introduction',
                             'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6], 'content': []})
            elif CONTENT_TYPE[node[-2]] == 'logo':
                data.append({'type': "img", 'img_type': 'logo', 'url': "http://localhost:5000/get_image/test_user/department_logo.png",
                             'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6]})
            elif CONTENT_TYPE[node[-2]] == 'info':
                data.append({'type': "rect", 'rect_type': 'info',
                             'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6], 'content': []})
            elif CONTENT_TYPE[node[-2]] == 'photo':
                data.append({'type': "img", 'img_type': 'photo', 'url': "http://localhost:5000/get_image/test_user/user_photo.png",
                             'x': node[3], 'y': node[4], 'w': node[5], 'h': node[6]})
        json = {
            'id': id,
            'show': False,
            'preview': '',
            'description': '',
            'layout_file': filename,
            'hover': False,
            'data': data
        }
        return json


def add_content(layouts, info_form, style1, style2):
    info_list = {'time': info_form['time'], 'location': info_form['location'], 'reporter': info_form['reporter']}
    if info_form['inviter']:
        info_list['inviter'] = info_form['inviter']
    if info_form['meeting_num']:
        info_list['meeting_num'] = info_form['meeting_num']
    count = 0
    for layout in layouts:
        count += 1
        for item in layout['data']:
            if count <= 5:
                style = copy.deepcopy(style_list[style1])
            else:
                style = copy.deepcopy(style_list[style2])
            if item['type'] == 'title':
                item['content'] = info_form['title']
                item['font'] = copy.deepcopy(style['title'])
            elif item['type'] == 'background':
                item['url'] = style['background']['url']
                item['opacity'] = style['background']['opacity']
            elif item['type'] == 'subtitle':
                item['content'] = '欢迎全校师生参加！'
                item['type'] = 'title'
                item['font'] = copy.deepcopy(style['title'])
            elif item['type'] == 'rect' and item['rect_type'] == 'info':
                content = []
                info_num = len(info_list)
                h = int(item['h'] / info_num)
                y = item['y']
                font_size = 1
                while True:
                    font = ImageFont.truetype(font_path_global['bold'], font_size)
                    char_width, char_height = font.getsize('中')
                    if char_height * 1.8 >= h or font_size >= 22:
                        style['info_title']['fontSize'] = f"{font_size}px"
                        style['info']['fontSize'] = f"{font_size}px"
                        break
                    font_size += 1
                for info_item in info_list:
                    w = len(English2Chinese[info_item]) * char_width
                    content.append({'type': "text", 'content': English2Chinese[info_item], 'info_type': 'default',
                                    'w': int(w * 1.6), 'h': h, 'x': item['x'], 'y': y, 'font': style['info_title']})
                    content.append({'type': "text", 'content': info_list[info_item], 'info_type': info_item,
                                    'w': item['w'] - w, 'h': h, 'x': item['x'] + w, 'y': y, 'font': style['info']})
                    y += h
                item['content'] = content
                item['backgroundColor'] = style['rect']['backgroundColor']
                item['opacity'] = style['rect']['opacity']
            elif item['type'] == 'rect' and item['rect_type'] == 'abstract':
                content = [{'type': "text", 'content': '报告摘要', 'info_type': 'default',
                            'w': item['w'], 'h': 40, 'x': item['x'], 'y': item['y'], 'font': copy.deepcopy(style['ab&intro_title'])},
                           {'type': "text", 'content': info_form['abstract'], 'info_type': 'abstract',
                            'w': item['w'], 'h': item['h'] - 40, 'x': item['x'] + 5, 'y': item['y'] + 35, 'font': copy.deepcopy(style['ab&intro'])}]
                item['content'] = content
                item['backgroundColor'] = style['rect']['backgroundColor']
                item['opacity'] = style['rect']['opacity']
            elif item['type'] == 'rect' and item['rect_type'] == 'introduction':
                content = [{'type': "text", 'content': '报告人简介', 'info_type': 'default',
                            'w': item['w'], 'h': 40, 'x': item['x'], 'y': item['y'], 'font': copy.deepcopy(style['ab&intro_title'])},
                           {'type': "text", 'content': info_form['introduction'], 'info_type': 'introduction',
                            'w': item['w'], 'h': item['h'] - 40, 'x': item['x'] + 5, 'y': item['y'] + 35, 'font': copy.deepcopy(style['ab&intro'])}]
                item['content'] = content
                item['backgroundColor'] = style['rect']['backgroundColor']
                item['opacity'] = style['rect']['opacity']
    return layouts


class Blender:
    def __init__(self, info_form, user):
        self.info_form = info_form
        self.user = user
        self.result_layouts = []

    def blend(self, lay1, lay2, bg1, bg2, style1, style2):
        self.result_layouts.clear()
        path1 = json2lay(layout=lay1, user=self.user)
        path2 = json2lay(layout=lay2, user=self.user)
        out_path = f"static\\templates\\{self.user}\\blending_results\\"
        os.system(f"layout_blending.exe {path1} {path2} {out_path}")
        layout_path_list = os.listdir(out_path)
        for index in range(0, len(layout_path_list)):
            json = lay2json(out_path, layout_path_list[index], bg1, bg2)
            self.result_layouts.append(json)
        self.result_layouts = add_content(self.result_layouts, self.info_form, style1, style2)
        return self.result_layouts


if __name__ == '__main__':
    b = Blender({
        'title': '文字到海报的端到端生成, 测试一下文字长度会不会超出海报',
        'time': '2022年11月16日(周三) 9:30-11.30',
        'location': '第一科研楼报告厅',
        'reporter': '陈明 副教授/杜克大学',
        'inviter': 'ypq',
        'meeting_num': '123-456-789',
        'abstract': 'We present a novel method for blending hierarchical layouts with semantic labels. ''The core of our method is a hierarchical structure correspondence algorithm, ''which recursively finds optimal substructure correspondences, ''achieving a globally optimal correspondence between a pair of hierarchical layouts. ''This correspondence is consistent with the structures of both layouts, ''allowing us to define the union of the layouts’ structures. ''The resulting compound structure helps extract intermediate layout structures, ''from which blended layouts can be generated via an optimization approach.',
        'introduction': 'We present a novel method for blending hierarchical layouts with semantic labels. ''The core of our method is a hierarchical structure correspondence algorithm, ''which recursively finds optimal substructure correspondences, ''achieving a globally optimal correspondence between a pair of hierarchical layouts. ''This correspondence is consistent with the structures of both layouts, ''allowing us to define the union of the layouts’ structures. ''The resulting compound structure helps extract intermediate layout structures, ''from which blended layouts can be generated via an optimization approach.'
    }, 'test_user')
    print(b.blend('template0.lay', 'template1.lay', "http://localhost:5000/get_image/test_user/bg1.png", "http://localhost:5000/get_image/test_user/bg2.png"))
