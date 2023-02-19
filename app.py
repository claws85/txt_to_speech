from flask import Flask, request, render_template, jsonify

from utils.utils import (
    ArticleTextExtractor,
    TextConverter
)
import base64


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert-to-audio', methods=['POST'])
def convert_to_audio():
    data = request.get_json()
    article_url = data['articleUrl']

    extractor = ArticleTextExtractor(article_url)
    article_text = extractor.extract_text()

    converter = TextConverter(article_text)
    converter.convert_to_speech_object()
    audio_bytes = converter.return_object_as_bytes()

    audio_base64 = base64.b64encode(audio_bytes.getvalue()).decode('utf-8')
    return jsonify({'audioData': audio_base64})


if __name__ == '__main__':
    app.run(debug=True)