import dropbox


class DropboxHandler(object):

    def __init__(self, config):
        self.config = config
        self.box = dropbox.Dropbox(self.config.KEY)

    def files(self, path=""):
        return [f.name for f in self.box.files_list_folder(path=path).entries]

    def upload_file_contents(self, upload_path, upload_file_name, file_contents):
        self.box.files_upload(file_contents, upload_path + '/' + upload_file_name)

    def upload_file(self, upload_path, file_name):
        with open(file_name, 'rb') as file_reference:
            contents = file_reference.read()
            self.upload_file_contents(upload_path, file_name, contents)

    def get_temporal_url(self, path, file_name):
        information = self.box.files_get_temporary_link(path + '/' + file_name)
        return information.link, information.metadata

