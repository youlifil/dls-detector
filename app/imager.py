from flask import request, current_app
from werkzeug.utils import secure_filename
import os

class Imager:
    def __init__(self):
        pass

    def _upload_path(self, fname):
        return os.path.join(current_app.root_path, current_app.config['UPLOAD_PATH'], secure_filename(fname))
    
    def _flush_upload_folder(self):
        # TODO: тереть прошлые файлы по дате
        pass

    def validate(self, file):
        def _issue(err):
            return { 'err':err }

        if file.filename == '':
            return _issue("empty-file")
        file_ext = os.path.splitext(file.filename)[1]
        if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
            return _issue("wrong-ext")

        # TODO: добавить валидацию контента через imghdr https://blog.miguelgrinberg.com/post/handling-file-uploads-with-flask
        return None

    def upload(self, file):
        self._flush_upload_folder()
        path = self._upload_path(file.filename)
        file.save(path)
        return path

