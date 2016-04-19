#!/usr/bin/env python3

from bottle import route, run, template, request, static_file
import webbrowser as web
import os
import subprocess


print("Content-type: text/html\n")
print("<html><body>Python is awesome !</body></html>")

# localhost:8080
@route('/')
def title():
    # views/may.tplを呼ぶ
    return template('may')

def main(filename):
  text = "gspr"
  cmd = "./a.out " + "./tmp/" + filename
  result = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE).communicate()[0]
  return result.decode('utf-8')

# localhost:8080/result
@route('/result', method='POST')
def men():
    upload = request.files.get('upload')
    fname, extname = os.path.splitext(upload.filename)

    if (fname == ""):
        fname = "hogefile"

    if extname not in ".txt":
        return "The file extension is not allowed."

    upload.save("./tmp", overwrite=True)

    text = "init"


    if __name__ == '__main__':
      text = main(upload.filename)

    # views/show.tplを呼ぶ
    return template('show', name=fname, contents=text)

web.open('http://localhost:8080')
# ビルドインサーバの実行
run(host='localhost', port=8080, debug=True)
