#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route, run, template, request, static_file
import webbrowser as web
import os

print("Content-type: text/html\n")
print("<html><body>Python is awesome !</body></html>")
#/
@route('/')
def title():
    # views/may.tplを呼ぶ
    return template('may')

#/tmp
@route('/tmp', method='POST')
def men():
    upload = request.files.get('upload')
    fname, extname = os.path.splitext(upload.filename)

    # Controller部 =======================================
    if (fname == ""):
        fname = "hogefile"

    if extname not in ".txt":
        return "The file extension is not allowed."

    upload.save("/tmp", overwrite=True)

    # View部 =============================================
    #return static_file("sample.txt", root='/tmp')
    # views/show.tplを呼ぶ
    return template('show', name=fname, ext=extname)
# ビルドインサーバの実行
run(server='cgi')
