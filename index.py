from bottle import route, run, template, request, static_file
import webbrowser as web
import os
import subprocess
import csv
from math import sqrt

csvPath = 'database/database.csv'
dataset = {}

def init():
  global dataset
  f = open(csvPath, 'r')
  reader = csv.reader(f)
  for row in reader:
    tmp = row
    dataset[tmp[0]] = map(float, tmp[1:])


def calcSim(data1, data2):
  sum1 = sum2 = 0.0
  rtn = 0.0
  for val1, val2 in zip(data1, data2):
    sum1 += val1**2
    sum2 += val2**2
    rtn += val1 * val2
  return rtn / (sqrt(sum1)*sqrt(sum2))


@route('/title')
def title():
  return template('may')


def cpp_exec(filename):
  cmd = ["./temp", "./image/" + filename]
  result = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
  return map(float, result.decode('utf-8').split(','))


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

  global dataset
  maxSim = 0.0
  maxName = ''
  for mykey, mydata in dataset.items():
    tmp = calcSim(feats, mydata)
    if tmp > maxSim:
      maxSim = tmp
      maxName = mykey

  return maxName + '/' + str(maxSim)


  #os.remove("./image/pic.png")

  #return template('show', name=fname)
  #return "Request permitted!"
  #here must be a number


if __name__ == '__main__':
  init()
  run(host = '0.0.0.0', port = 80)
