#!/bin/env python3
# -*- coding: utf-8 -*-
"""
the url to handler route
"""
import tornado.web
from calendar_bot.callbackHandler import CallbackHandler
from calendar_bot.hellohandler import HelloHandler
from calendar_bot.constant import FILE_SYSTEM


def getRouter():
    """
    get the app with route info
    """
    return tornado.web.Application([
        (r"/callback", CallbackHandler),
        (r'/static/([a-zA-Z0-9\&%_\./-~-]*.([p|P][n|N][g|G]))',
            tornado.web.StaticFileHandler, 
            {"path": FILE_SYSTEM["image_dir"]}),
        (r'/hello', HelloHandler),
    ])
