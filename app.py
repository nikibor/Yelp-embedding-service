from flask import Flask, request

from embeddings import Embeddings
from loader import Loader
from serializer import EmbeddingSerializer

app = Flask(__name__)


@app.route('/api/embedding', methods=['POST'])
def embedding():
    if request.is_json:
        content = request.get_json()
        serializer = EmbeddingSerializer(data=content)
        if serializer.is_valid():
            text = serializer.text
            redirected_url = serializer.redirected_url
            vector = embedding_model.build_sentence_vector(text)
    else:
        pass
    return 200


if __name__ == '__main__':
    loader = Loader().download_all_models()
    embedding_model = Embeddings()
    app.run()
