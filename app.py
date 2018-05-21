import requests
from flask import Flask, request

from embeddings import Embeddings
from loader import Loader
from serializer import EmbeddingSerializer

app = Flask(__name__)
embedding_model = None


@app.route('/', methods=['GET'])
def index():
    return "Vector service is working"


@app.route('/api/embedding', methods=['POST'])
def embedding():
    if request.is_json:
        content = request.get_json()
        serializer = EmbeddingSerializer(data=content)
        if serializer.is_valid():
            text = serializer.text
            redirected_url = serializer.redirected_url
            vector = Embeddings().build_sentence_vector(text).tolist()
            requests.post(url=redirected_url, json={'vector': vector})
            return "Embedding build"
    else:
        return 'Error'
    return 'OK'


@app.route('/api/setup', methods=['POST'])
def set_up():
    if request.is_json:
        content = request.get_json()
        if content['key'] == 'fox':
            Loader().download_all_models()
        if content['key'] == 'snake':
            embedding_model = Embeddings()
        if content['key'] == 'sitara':
            Loader().download_all_models()
            embedding_model = Embeddings()
        return 'All data is downloaded'


if __name__ == '__main__':
    app.run()
