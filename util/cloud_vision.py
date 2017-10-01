from settings import config
from util.DropboxFileManager import DropBoxFileManager
import requests
import base64
import json


VISION_URL = "https://vision.googleapis.com/v1/images:annotate?key=" + config.GoogleConfig.VISION_KEY


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
        return OCR.extract_text(r)

    @staticmethod
    def get_text_from_url(file_url, user="temp"):
        DFM = DropBoxFileManager(user, file_url)
        DFM.upload_url_file()
        new_url = DFM.get_temporal_url()
        r = requests.post(
            url=VISION_URL,
            data=OCR.url_request_data(new_url),
            headers={'content-type': 'application/json'}
        )
        return OCR.extract_text(r)

    @staticmethod
    def extract_text(response):
        response.raise_for_status()
        try:
            return str(response.json()["responses"][0]["fullTextAnnotation"]['text'])
        except Exception as e:
            print(str(e))
            return "Warning: no text detected."

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

