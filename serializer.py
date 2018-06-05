import requests
from flask import Flask, request
import json
from embeddings import Embeddings
from loader import Loader
from serializer import EmbeddingSerializer

app = Flask(__name__)
embedding_model = None


@app.route('/', methods=['GET'])
def index():
    return "Vector service is working"


# {
#     "text": "qwerty",
#     "token": "asdadasdasdasd"
# }
@app.route('/api/embedding', methods=['POST'])
def embedding():
    if request.is_json:
        content = request.get_json()
        serializer = EmbeddingSerializer(data=content)
        if not serializer.is_valid():
            return 'Error'
        text = serializer.text
        token = serializer.token
        vector = Embeddings().build_sentence_vector(text).tolist()
        data = json.dumps(
            {
                "vector": vector,
                "token": token
            }
        )
        return data



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
