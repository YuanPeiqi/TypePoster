import os

from flask import Flask, request, jsonify, Response
from flask_cors import CORS

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
CORS(app, supports_credentials=True)


@app.route('/')
def hello_world():
    return 'hello world'


@app.route('/submit_poster_info', methods=['GET', 'POST'])
def submit_poster_info():
    title = request.values.get('title')
    location = request.values.get('location')
    start_time = request.values.get('start_time')
    end_time = request.values.get('end_time')
    reporter = request.values.get('reporter')
    inviter = request.values.get('inviter')
    abstract = request.values.get('abstract')
    introduction = request.values.get('introduction')
    meeting_num = request.values.get('meeting_num')
    result = "hhh"
    return jsonify(result)


@app.route("/get_poster_view/<imageId>.png")
def get_poster_view(imageId):
    # 图片上传保存的路径
    import os
    if os.path.exists('static/test_poster/{}.png'.format(imageId)):
        with open(r'static/test_poster/{}.png'.format(imageId), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp
    else:
        with open(r'static/test_poster/{}.png'.format('template1'), 'rb') as f:
            image = f.read()
            resp = Response(image, mimetype="image/png")
            return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
