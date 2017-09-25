import os
import json


def create_client_secret(client_secrets_map_example):

    if os.path.isfile("settings/client_secret.json"):
        return None

    client_secrets_map_example["dropbox"]["username"] = os.environ.get("DROPBOX_USERNAME")
    client_secrets_map_example["dropbox"]["email"] = os.environ.get("DROPBOX_EMAIL")
    client_secrets_map_example["dropbox"]["access_key"] = os.environ.get("DROPBOX_KEY")

    with open('settings/client_secret.json', 'w') as file:
        json.dump(client_secrets_map_example, file)
