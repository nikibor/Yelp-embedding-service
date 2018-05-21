class EmbeddingSerializer:

    def __init__(self, data):
        self.data = data
        self.text = ''
        self.redirected_url = ''

    def is_valid(self):
        if self.data:
            self.text = self.data['text']
            self.redirected_url = self.data['redirected_url']
            return True
        return False
