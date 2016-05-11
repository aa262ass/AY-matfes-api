from bottle import route, run, template, request, static_file, HTTPResponse
import webbrowser as web
import numpy as np
import os, subprocess
import json

dataPath = './database3.npy'
featsDim = 99120

'''
allData,
male, female
mElse, mActor, mArtist, mShowman,
fElse, fActor, fArtist, fShowman
'''

dataSet = np.load(dataPath)
dataID = [
  range(1001,1089)+range(1101,1153)+range(1201,1242)+range(1301,1369) \
  +range(2001,2053)+range(2101,2182)+range(2201,2254)+range(2301,2328),
  range(1001,1089)+range(1101,1153)+range(1201,1242)+range(1301,1369),
  range(2001,2053)+range(2101,2182)+range(2201,2254)+range(2301,2328),
  range(1001, 1089), range(1101, 1153), range(1201, 1242), range(1301, 1369),
  range(2001, 2053), range(2101, 2182), range(2201, 2254), range(2301, 2328),
]
#dataTag = ["allData","male","female","mElse","mActor","mArtist", "mShowman","fElse", "fActor", "fArtist", "fShowman"]
categoryIndex = [
  [0,462], [0,249], [249,462],
  [0,88], [88,140], [140,181], [181,249],
  [249,301], [301,382], [382,435], [435,462]
]
categorySize = len(categoryIndex)


def cpp_exec(filename):
  cmd = ["./extractFeats", "./image/"+filename]
  result = subprocess.Popen(cmd, stdout=subprocess.PIPE).communicate()[0]
  if len(result) == 0:
    return np.array([])
  return np.array(map(float, result.decode('utf-8').split(',')))


@route('/title')
def title():
  return template('may')


@route('/result', method='POST')
def result():
  upload = request.files.get('upfile')
  upload.save("./image", overwrite=True)
  feats = cpp_exec(upload.filename)

  if feats.size == 0:
    body = {}
    for i in xrange(categorySize):
      body[i] = 0
  else:
    feats = feats.reshape(featsDim, 1)
    body = {}
    for i in xrange(categorySize):
      body[i] = dataID[i][np.argmax(dataSet[categoryIndex[i][0]:categoryIndex[i][1]].dot(feats))]

  r = HTTPResponse(status=200, body=json.dumps(body))
  r.set_header('Content-Type', 'text/plain')
  return r


if __name__ == '__main__':
  run(host = '0.0.0.0', port = 80)
