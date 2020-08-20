import json
import requests
import uuid
from flask_babel import _
from app import app


def translate(text, source_language, dest_language):
    # if 'MS_TRANSLATOR_KEY' not in app.config or \
    #         not app.config['MS_TRANSLATOR_KEY']:
    #     return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': '8d84e3a934024692abd29a3abc00881b',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())}
    body = [{
        'text': text
    }]
    r = requests.post('https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
        source_language, dest_language),
        headers=auth, json=body)
    if r.status_code != 200:
        return r.status_code
        # return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig'))


translate('hello', 'en', 'es')
