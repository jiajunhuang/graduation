# coding=utf-8

import os
import uuid
from config import Config
from .base import BaseHandler


class FileHandler(BaseHandler):
    def get(self):
        self.render("file_upload.html")

    def post(self):
        """
        @apiDescription 文件上传, 请访问 ``/upload/?`` 或参照 ``templates/file_upload.html``
        @api {post} /upload/? 文件上传
        @apiGroup file
        """
        fileinfo = self.request.files['filearg'][0]
        fname = fileinfo['filename']
        extn = os.path.splitext(fname)[1]
        cname = str(uuid.uuid4()) + extn
        fh = open(os.path.join(Config().img_path, cname), 'wb')
        fh.write(fileinfo['body'])
        self.write(dict(
            filename=cname,
        ))
