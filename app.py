from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/')
def index():
    # return "<p>Hello, World!</p>"
    return 'Index Page'


@app.route('/hello')
def hello():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


# if __name__ == '__main__':
#     app.run(port=5000)

# $ flask --app app run
# $ flask run --host=0.0.0.0
# $ flask --app app run --debug
# $ pip freeze > requirements.txt
# $ pip install gunicorn
