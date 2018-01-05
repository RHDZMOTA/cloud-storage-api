from settings import config
import base64
import json
import requests

VISION_KEY = config.client_secrets_map["google"]["cloud-vision"]
VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + VISION_KEY




class OCR(object):

    @staticmethod
    def get_text_from_file(file_name):
        with open(file_name, "rb") as file:
            contents = file.read()
        return OCR.get_text_from_bytes(contents)

    @staticmethod
    def get_text_from_bytes(file_bytes):
        r = requests.post(
            url=VISION_URL,
            data=OCR.base64_request_data(file_bytes),
            headers={'content-type': 'application/json'}
        )
        return r.json()["responses"][0]["fullTextAnnotation"]['text']

    @staticmethod
    def get_text_from_url(file_url):
        r = requests.post(
            url=VISION_URL,
            data=OCR.url_request_data(file_url),
            headers={'content-type': 'application/json'}
        )
        return r.json()["responses"][0]["fullTextAnnotation"]['text']

    @staticmethod
    def base64_request_data(file_bytes):
        return json.dumps(
            {
                "requests": [
                    {
                        "image": {
                            "content": base64.b64encode(file_bytes).decode("utf-8")
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION"
                            }
                        ]
                    }
                ]
            }
        )

    @staticmethod
    def url_request_data(file_url):
        return json.dumps(
            {
                "requests": [
                    {
                        "image": {
                            "source": {
                                "imageUri": file_url
                            }
                        },
                        "features": [
                            {
                                "type": "TEXT_DETECTION"
                            }
                        ]
                    }
                ]
            }
        )



OCR.get_text_from_file("temporal/plot.png")
OCR.get_text_from_url("https://myplotlib-api.appspot.com/function?func=x^2&start=-10&end=10")

import requests
import json

url1 = "https://rhdzmota-cloud-storage.herokuapp.com/cloud-vision/google-dropbox-ocr"
url2 = "http://127.0.0.1:8000/cloud-vision/google-dropbox-ocr"

r = requests.get(
    url=url1,
    params={
        "file_url":"https://myplotlib-api.appspot.com/function?func=x^2&start=-10&end=10"
    }
)

print(r.text)


r = requests.post(
    url=url2,
    headers = {"Content-Type": "application/json"},
    data=json.dumps({
        "file_url":"https://myplotlib-api.appspot.com/function?func=x^2&start=-10&end=10"
    })
)

print(r.text)

https://rhdzmota-cloud-storage.herokuapp.com/cloud-vision/google-dropbox-ocr?file_url=https://myplotlib-api.appspot.com/scatter?x=0,1,2,3,4,5&y=0,4,1,2,3,5