import json
import requests
import uuid
import time
from flask_babel import _
# from app import app

def translate(text, source_language, dest_language):
    time.sleep(2)
    return f'Translated {text} from {source_language} to {dest_language}'

def translate_old(text, source_language, dest_language):
    # if 'MS_TRANSLATOR_KEY' not in app.config or \
    #         not app.config['MS_TRANSLATOR_KEY']:
    #     return _('Error: the translation service is not configured.')
    auth = {'Ocp-Apim-Subscription-Key': '7ddc301f6bfc49b98929c1298e4b2337',
            'Content-type': 'application/json',
            'X-ClientTraceId': str(uuid.uuid4())
            }
    body = [{
        'text': text
    }]
    r = requests.post(
        'https://api.cognitive.microsofttranslator.com/translate?api-version=3.0&from={}&to={}'.format(
            source_language, dest_language),
        headers=auth, json=body)
    response = r.json()
    print(json.dumps(response, sort_keys=True, indent=4,
                     ensure_ascii=False, separators=(',', ': ')))
    # if r.status_code != 200:
    #     return r.status_code
    #     return _('Error: the translation service failed.')
    # return json.loads(r.content.decode('utf-8-sig'))
