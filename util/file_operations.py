from urllib.request import urlopen


def download_file(file_url, file_name=None, file_path=None):
    file_path = "temporal/" if file_path is None else file_path
    file_name = file_path + ("temp" if file_name is None else file_name)
    with urlopen(file_url) as response, open(file_name, 'wb') as file:
        file_contents = response.read()
        file.write(file_contents)
    return {
        "file_name": file_name,
        "file_contents": file_contents
    }

