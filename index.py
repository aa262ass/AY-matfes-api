from bottle import route, run, template, request, static_file, HTTPResponse
import webbrowser as web
import os
import subprocess
import csv
from math import sqrt

csvPath = 'database/database.csv'
featsDim = 99120
dataSize = 500
dataset = []
dataname = []

def init():
  global dataset
  global dataname
  f = open(csvPath, 'r')
  reader = csv.reader(f)

  for myline in reader:
    mydata = map(float, myline[1:])
    norm = calcNorm(mydata)
    for i in range(featsDim):
      mydata[i] /= norm
    dataset.append(mydata)
    dataname.append(myline[0])


def calcNorm(mydata):
  s = 0.0
  for i in range(featsDim):
    s += mydata[i]**2
  return sqrt(s)


def calcSim(data1, data2):
  rtn = 0.0
  for i in range(featsDim):
    rtn += data1[i] * data2[i]
  return rtn


def cpp_exec(filename):
  cmd = ["./temp", "./image/"+filename]
  result = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
  return map(float, result.decode('utf-8').split(','))


@route('/title')
def title():
  return template('may')


@route('/result', method='POST')
def result():
  upload = request.files.get('bitmap')
  fname, extname = os.path.splitext(upload.filename)

  if (fname == ""):
      fname = "hogefile"

  if extname not in (".png", ".jpg"):
      return "The file extension is not allowed."

  upload.save("./image", overwrite=True)
  feats = cpp_exec(upload.filename)
  norm = calcNorm(feats)
  for i in range(featsDim):
    feats[i] /= norm

  maxSim = -1.0
  maxName = ''
  for i in range(dataSize):
    sim = calcSim(feats, dataset[i])
    if sim > maxSim:
      maxSim = sim
      maxName = dataname[i]

  body = maxName + '/' + str(maxSim)
  r = HTTPResponse(status=200, body=body)
  r.set_header('Content-Type', 'text/plain')
  return r


  #os.remove("./image/pic.png")

  #return template('show', name=fname)
  #return "Request permitted!"
  #here must be a number


if __name__ == '__main__':
  init()
  run(host = '0.0.0.0', port = 80)
