from google_drive_downloader import GoogleDriveDownloader as gdd
import os


class Loader:

    @staticmethod
    def load_embeddings():
        gdd.download_file_from_google_drive(
            file_id='1MmnHVzujbBD0scQ3xA273_W6PFTIejZA',
            dest_path='./data/Yelp_embedings'
        )

    @staticmethod
    def load_trainables():
        gdd.download_file_from_google_drive(
            file_id='1Xeet5uVs88uURxizwXQ-U3iPj7TGQRsa',
            dest_path='./data/Yelp_embedings.trainables.syn1neg.npy'
        )

    @staticmethod
    def load_vectors():
        gdd.download_file_from_google_drive(
            file_id='1V5q8M4rWdODUV4UU26yZQkamZAVabDFD',
            dest_path='./data/Yelp_embedings.wv.vectors.npy'
        )

    @staticmethod
    def load_check() -> bool:
        files = os.listdir('./data')
        if not files:
            return False
        return True

    def download_all_models(self):
        if not self.load_check():
            self.load_embeddings()
            self.load_trainables()
            self.load_vectors()