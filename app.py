from flask import Flask

from loader import Loader

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    loader = Loader().download_all_models()
    app.run()
