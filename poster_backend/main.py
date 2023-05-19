import base64
import datetime
import os
import random
import uuid
from tqdm import tqdm

import layout_blending
import poster
from flask import Flask, request, jsonify, Response
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app, supports_credentials=True)


# 获取文件名
def random_filename(filename):
    ext = os.path.splitext(filename)[-1]
    return uuid.uuid4().hex + ext


@app.route("/save_preview", methods=['GET', 'POST'])
def save_preview():
    request_base64 = request.json['url']
    img = base64.b64decode(request_base64)
    filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    path = f'.\\static\\previews\\{filename}.png'
    with open(path, 'wb') as f:
        f.write(img)
    return f'http://localhost:5000/get_preview/{filename}.png'


@app.route("/save_layouts", methods=['GET', 'POST'])
def save_layouts():
    layout_list = request.values.get('layout_list')
    username = request.values.get('username')
    # TODO: 存入数据库中做保存
    return 'success'


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files.get('file')
    if file:
        print(file.filename)
        filename = random_filename(file.filename)
        filepath = os.path.join('.\\static\\images\\test_user\\', filename)
        file.save(filepath)

        file_url = f'http://localhost:5000/get_image/test_user/{filename}'
        return jsonify({'name': file.filename, 'url': file_url, 'msg': 'success'})
    return jsonify({'name': '', 'url': '', 'msg': 'error'})


@app.route('/blend', methods=['GET', 'POST'])
def blend_layouts():
    user_id = request.values.get('userid')
    lay1 = request.values.get('lay1')
    lay2 = request.values.get('lay2')
    bg1 = request.values.get('bg1')
    bg2 = request.values.get('bg2')
    style1 = bg1.split('/')[-1].split('.')[0]
    style2 = bg2.split('/')[-1].split('.')[0]
    info_form = {'title': request.values.get('title'), 'time': request.values.get('time'), 'location': request.values.get('location'),
                 'reporter': request.values.get('reporter'), 'inviter': request.values.get('inviter'), 'meeting_num': request.values.get('meeting_num'),
                 'abstract': request.values.get('abstract'), 'introduction': request.values.get('introduction')}
    blender = layout_blending.Blender(info_form, user_id)
    blending_results = blender.blend(lay1, lay2, bg1, bg2, style1, style2)
    blending_results[0]['show'] = True
    generator = poster.Poster()
    generator.layouts = blending_results
    if not os.path.exists(f'static/templates/{user_id}/blending_img_results'):
        os.mkdir(f'static/templates/{user_id}/blending_img_results')
    for index in range(len(generator.layouts)):
        generator.generate(f'static/templates/test_user/blending_img_results/template{index}.png', index)
        generator.layouts[index]['preview'] = f'http://localhost:5000/get_blending_img_result/{user_id}/template{index}.png/{random.randint(1, 1000000)}'
    return jsonify(generator.layouts)


@app.route('/submit_poster_info', methods=['GET', 'POST'])
def submit_poster_info():
    user_id = request.values.get('userid')
    title = request.values.get('title')
    location = request.values.get('location')
    time = request.values.get('datetime')
    reporter = request.values.get('reporter')
    inviter = request.values.get('inviter')
    abstract = request.values.get('abstract')
    introduction = request.values.get('introduction')
    meeting_num = request.values.get('meeting_num')
    logo_url = request.values.get('logo')
    photo_url = request.values.get('photo')
    qrcode_url = request.values.get('qrcode')
    info_list = {'time': time, 'location': location, 'reporter': reporter}
    if inviter:
        info_list['inviter'] = inviter
    if meeting_num:
        info_list['meeting_num'] = meeting_num
    generator = poster.Poster(title=title, info_list=info_list, abstract=abstract, introduction=introduction,
                              logo_url=logo_url, photo_url=photo_url, qrcode_url=qrcode_url)
    if not os.path.exists(f'static/templates/{user_id}'):
        os.mkdir(f'static/templates/{user_id}')
    for index in tqdm(range(len(generator.layouts))):
        generator.generate(f'static/templates/test_user/template{index}.png', index)
        generator.layouts[index]['preview'] = f'http://localhost:5000/get_poster_view/{user_id}/template{index}.png'
    return jsonify(generator.layouts)


@app.route("/get_poster_view/<userName>/<templateId>.png")
def get_poster_view(userName, templateId):
    if os.path.exists(f'static/templates/{userName}/{templateId}.png'):
        with open(f'static/templates/{userName}/{templateId}.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(f'static/templates/{userName}/template1.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


@app.route("/get_blending_img_result/<userName>/<templateId>.png/<random>")
def get_blending_img_result(userName, templateId, random):
    if os.path.exists(f'static/templates/{userName}/blending_img_results/{templateId}.png'):
        with open(f'static/templates/{userName}/blending_img_results/{templateId}.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(f'static/templates/{userName}/template1.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


@app.route("/get_image/<userName>/<imageId>.png")
def get_image(userName, imageId):
    if os.path.exists(f'static/images/{userName}/{imageId}.png'):
        with open(f'static/images/{userName}/{imageId}.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(f'static/images/{userName}/default_img.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


@app.route("/get_background/<userName>/<backgroundId>.png")
def get_background(userName, backgroundId):
    if os.path.exists(f'static/backgrounds/{userName}/{backgroundId}.png'):
        with open(f'static/backgrounds/{userName}/{backgroundId}.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(f'static/backgrounds/{userName}/default_bg.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


@app.route("/get_preview/<filename>.png")
def get_preview(filename):
    with open(f'static/previews/{filename}.png', 'rb') as f:
        image = f.read()
        resp = Response(image, mimetype="image/png")
        return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
