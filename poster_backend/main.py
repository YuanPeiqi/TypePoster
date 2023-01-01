import os

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import poster, layout_blending

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/blend', methods=['GET', 'POST'])
def blend_layouts(layout1, layout2):
    blender = layout_blending.Blender(layout1, layout2)
    os.system(f"out.exe {path1} {path2}")
    return 'hello world'


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
    bg_path = 'static/images/test_user/bg.png'
    logo_1_path = 'static/images/test_user/school_logo.png'
    logo_2_path = 'static/images/test_user/department_logo.png'
    photo_path = 'static/images/test_user/photo.png'
    qrcode_path = 'static/images/test_user/qrcode.png'
    generator = poster.Poster(title=title, time=time, location=location, reporter=reporter, inviter=inviter, meeting_num=meeting_num,
                              abstract=abstract, introduction=introduction,
                              bg_path=bg_path, logo_1_path=logo_1_path, logo_2_path=logo_2_path, qrcode_path=qrcode_path, photo_path=photo_path)
    if not os.path.exists(f'static/templates/{user_id}'):
        os.mkdir(f'static/templates/{user_id}')
    for index in range(len(generator.layouts)):
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


@app.route("/get_image/<userName>/<imageId>.png")
def get_image(userName, imageId):
    if os.path.exists(f'static/images/{userName}/{imageId}.png'):
        with open(f'static/images/{userName}/{imageId}.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(f'static/images/{userName}/bg.png', 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
