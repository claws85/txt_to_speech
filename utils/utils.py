import io
import requests

from gtts import gTTS
from bs4 import BeautifulSoup


class ArticleTextExtractor:
    def __init__(self, url):
        self.url = url

    def extract_text(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'html.parser')
        article_text = ''
        for paragraph in soup.find_all('p'):
            article_text += paragraph.text + '\n'

        return article_text


class TextConverter:
    def __init__(self, text):
        self.text = text
        self.tts = None

    def convert_to_speech_object(self):
        self.tts = gTTS(text=self.text, lang='en')

    def return_object_as_bytes(self):
        audio_bytes = io.BytesIO()
        self.tts.write_to_fp(audio_bytes)

        return audio_bytes
