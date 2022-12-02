from flask import Flask, request, jsonify
from flask_cors import CORS

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
    result = generate_basic()
    return jsonify(result)

def generate_basic():
    return 'success'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
