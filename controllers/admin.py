# coding=utf-8

from .base import BaseHandler


class AdminHandler(BaseHandler):
    def get(self):
        self.render("admin.html")
