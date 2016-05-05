from bottle import route, run, template, request, static_file
import webbrowser as web
import os
import subprocess

@route('/title')
def title():
    return template('may')

def cpp_exec(filename):
  cmd = "./a.out " + "./image/" + filename
  result = subprocess.Popen(cmd.split(' '), stdout=subprocess.PIPE).communicate()[0]
  return result.decode('utf-8')

@route('/result', method='POST')
def resuelto():
    upload = request.files.get('bitmap')
    fname, extname = os.path.splitext(upload.filename)

    if (fname == ""):
        fname = "hogefile"

    if extname not in ".png":
        return "The file extension is not allowed."

    upload.save("./image", overwrite=True)
#    text = cpp_exec(upload.filename)

#    os.remove("./image/pic.png")

#    return template('show', name=fname)
    return "Request permitted!"
    #here must be a number
run(host = '0.0.0.0', port = 80)

