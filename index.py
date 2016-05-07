from bottle import route, run, template, request, static_file, HTTPResponse
from datetime import datetime
import webbrowser as web
import numpy as np
import os, subprocess

dataPath = 'database/database3.npy'
featsDim = 99120

'''
データは
allData,
mElse, mActor, mArtist, mShowman,
fElse, fActor, fArtist, fShowman
の順
'''

dataSet = np.load(dataPath)
dataID = [
  range(1001,1089)+range(1101,1153)+range(1201,1242)+range(1301,1369) \
  +range(2001,2053)+range(2101,2182)+range(2201,2254)+range(2301,2328),
  range(1001, 1089), range(1101, 1153), range(1201, 1242), range(1301, 1369),
  range(2001, 2053), range(2101, 2182), range(2201, 2254), range(2301, 2328),
]
categoryIndex = [
  [0,462], [0,88], [88,140], [140,181], [181,249],
  [249,301], [301,382], [382,435], [435,462]
]
categorySize = len(categoryIndex)


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
  time1 = datetime.now()
  upload = request.files.get('bitmap')
  '''
  fname, extname = os.path.splitext(upload.filename)

  upload.filename = 'test' + extname

  if extname not in (".png", ".jpg"):
      return "The file extension is not allowed."
  '''
  upload.save("./image", overwrite=True)
  time2 = datetime.now()
  feats = cpp_exec(upload.filename)

  time3 = datetime.now()
  if feats.size == 0:
    body = ','.join(['0']*categorySize)
  else:
    feats = feats.reshape(featsDim, 1)
    body = '' 
    for i in xrange(categorySize):
      body += ',' if i != 0 else ''
      body += str(dataID[i][np.argmax(dataSet[categoryIndex[i][0]:categoryIndex[i][1]].dot(feats))])

  time4 = datetime.now()

  body += '\n'
  body += str(time2-time1) + '\n'
  body += str(time3-time2) + '\n'
  body += str(time4-time3) + '\n'
  r = HTTPResponse(status=200, body=body)
  r.set_header('Content-Type', 'text/plain')
  return r


if __name__ == '__main__':
  run(host = '0.0.0.0', port = 80)
