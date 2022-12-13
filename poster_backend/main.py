import os

from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import poster

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/submit_poster_info', methods=['GET', 'POST'])
def submit_poster_info():
    userid = request.values.get('userid')
    title = request.values.get('title')
    location = request.values.get('location')
    time = request.values.get('time')
    reporter = request.values.get('reporter')
    inviter = request.values.get('inviter')
    abstract = request.values.get('abstract')
    introduction = request.values.get('introduction')
    meeting_num = request.values.get('meeting_num')
    result = "hhh"
    bg_path = 'assets/img_resource/bg.png'
    logo_1_path = 'assets/img_resource/school_logo.png'
    logo_2_path = 'assets/img_resource/department_logo.png'
    photo_path = 'assets/img_resource/photo.png'
    generate_poster = poster.Poster(title=title, time=time, location=location, reporter=reporter, inviter=inviter,
                                    meeting_num=meeting_num, abstract=abstract, introduction=introduction,
                                    bg_path=bg_path, logo_1_path=logo_1_path, logo_2_path=logo_2_path,
                                    photo_path=photo_path)
    if not os.path.exists('static/test_poster/' + userid):
        os.mkdir('static/test_poster/' + userid)
    generate_poster.generate('static/test_poster/' + userid + '/result.png')
    return jsonify(result)


@app.route("/get_poster_view/<imageId>.png")
def get_poster_view(userid,imageId):
    # 图片上传保存的路径
    import os
    if os.path.exists('static/test_poster/'+userid+'{}.png'.format(imageId)):
        with open(r'static/test_poster/'+userid+'{}.png'.format(imageId), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(r'static/test_poster/{}.png'.format('template1'), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


@app.route("/get_image/<imageId>.png")
def get_image(imageId):
    # 图片上传保存的路径
    import os
    if os.path.exists(r'static/img_resource/{}.png'.format(imageId)):
        with open(r'static/img_resource/{}.png'.format(imageId), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(r'static/img_resource/{}.png'.format('img_resource/bg'), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
