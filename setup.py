import json
from util.client_secret import create_client_secret


def create_dot_env():
    pass

def main():

    with open('settings/client_secret.json.example') as secret_content:
        client_secrets_map_example = json.load(secret_content)

    create_client_secret(client_secrets_map_example)


if __name__ == "__main__":
    main()
