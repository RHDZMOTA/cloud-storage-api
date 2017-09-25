import os
import json
from util.client_secret import create_client_secret

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

    def get_user(self):
        return client_secrets_map[self.get_service()].get("username")

    def get_email(self):
        return client_secrets_map[self.get_service()].get("email")

    def get_key(self):
        return client_secrets_map[self.get_service()].get("access_key")


# Dropbox configuration
class DropboxConfig(object):

    class DropboxCredentials(Credentials):
        service = "dropbox"

    credentials = DropboxCredentials()
    USER = credentials.get_user()
    EMAIL = credentials.get_email()
    KEY = credentials.get_key()


