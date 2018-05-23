class EmbeddingSerializer:

    def __init__(self, data):
        self.data = data
        self.text = ''
        self.redirected_url = ''
        self.hashkey = ''

    def is_valid(self):
        if self.data:
            self.text = self.data['text']
            self.redirected_url = self.data['redirected_url']
            self.hashkey = self.data['hashkey']
            return self.text != '' and self.redirected_url != '' and self.hashkey != ''
        return False
