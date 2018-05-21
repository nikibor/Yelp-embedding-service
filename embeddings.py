from gensim.models import Word2Vec
import numpy as np

class Embeddings:

    def __init__(self):
        self.embedding_model = Word2Vec.load('./data/Yelp_embeddings')

    def build_sentence_vector(self, sentence):
        words = sentence.split()
        result = np.zeros(100)
        size = 0
        for word in words:
            if word in self.embedding_model.wv.vocab:
                result += self.embedding_model.wv[word]
                size += 1
        if size == 0:
            size = 1
        result /= size
        return result
