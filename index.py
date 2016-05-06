from bottle import route, run, template, request, static_file, HTTPResponse
from datetime import datetime
import webbrowser as web
import numpy as np
import os, subprocess

dataPath = 'database/database.npz'
featsDim = 99120
category = ['allData', 'mElse', 'mActor', 'mArtist', 'mShowman', \
                'fElse', 'fActor', 'fArtist', 'fShowman']
categorySize = len(category)
dataSet = []
dataID = []


def init():
  global dataSet
  global dataID
  tmpData = np.load(dataPath)

  for key in category:
    dataSet.append(tmpData[key])

  dataID.append(range(1001,1089)+range(1101,1153)+range(1201,1242)+range(1301,1369) \
                      +range(2001,2053)+range(2101,2182)+range(2201,2254)+range(2301,2328))
  dataID.append(range(1001, 1089))
  dataID.append(range(1101, 1153))
  dataID.append(range(1201, 1242))
  dataID.append(range(1301, 1369))
  dataID.append(range(2001, 2053))
  dataID.append(range(2101, 2182))
  dataID.append(range(2201, 2254))
  dataID.append(range(2301, 2328))


def cpp_exec(filename):
  cmd = ["./temp", "./image/"+filename]
  result = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
  if len(result) == 0:
    return np.array([])
  return np.array(map(float, result.decode('utf-8').split(',')))


@route('/title')
def title():
  return template('may')


@route('/result', method='POST')
def result():
  # time1 = datetime.now()
  upload = request.files.get('bitmap')
  '''
  fname, extname = os.path.splitext(upload.filename)

  upload.filename = 'test' + extname

  if extname not in (".png", ".jpg"):
      return "The file extension is not allowed."
  '''
  upload.save("./image", overwrite=True)
  # time2 = datetime.now()
  feats = cpp_exec(upload.filename)

  # time3 = datetime.now()
  if feats.size == 0:
    body = ','.join(['0']*categorySize)
  else:
    feats = feats.reshape(featsDim, 1)
    body = '' 
    for i in xrange(categorySize):
      body += ',' if i != 0 else ''
      body += str(dataID[i][np.argmax(dataSet[i].dot(feats))])

  #time4 = datetime.now()

  '''
  body += '\n'
  body += str(time2-time1) + '\n'
  body += str(time3-time2) + '\n'
  body += str(time4-time3) + '\n'
  '''
  r = HTTPResponse(status=200, body=body)
  r.set_header('Content-Type', 'text/plain')
  return r


if __name__ == '__main__':
  init()
  run(host = '0.0.0.0', port = 80)
