import os
from os import environ, pardir
from os.path import join, dirname, abspath

import json
from util.client_secret import create_client_secret


PROJECT_DIR = abspath(join(dirname(__file__), pardir))
STATIC_DIR = join(PROJECT_DIR, 'app/static')



# Load client secret dictionary
def get_client_secret_json():
    if not os.path.isfile("settings/client_secret.json"):
        with open('settings/client_secret.json.example') as secret_content:
            client_secrets_map_example = json.load(secret_content)
        create_client_secret(client_secrets_map_example)
    with open('settings/client_secret.json') as secret_content:
        client_secrets_map = json.load(secret_content)
    return client_secrets_map

client_secrets_map = get_client_secret_json()
DEBUG = True



# Generic credential class
class Credentials:
    service = None

    def get_service(self):
        if not self.service:
            raise NotImplementedError("Service attribute missing.")
        return self.service

    def get_field(self, field):
        return client_secrets_map[self.get_service()].get(field)

    def get_user(self):
        return self.get_field("username")

    def get_email(self):
        return self.get_field("email")


# Dropbox configuration
class DropboxConfig(object):

    class DropboxCredentials(Credentials):
        service = "dropbox"

    credentials = DropboxCredentials()
    USER = credentials.get_user()
    EMAIL = credentials.get_email()
    KEY = credentials.get_field("access_key")


# Google configuration
class GoogleConfig(object):

    class GoogleCredentials(Credentials):
        service = "google"

    credentials = GoogleCredentials()
    USER = credentials.get_user()
    EMAIL = credentials.get_email()
    VISION_KEY = credentials.get_field("cloud-vision")
