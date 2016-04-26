import bottle

def calc(datafile):
    #ここでベクトルの計算処理を行う
    result = 1.23456789
    return result

@bottle.route('/result')
def result():
    #upload = bottle.request.files.get('bitmap')
    n =   calc(1)
    body = str(n)
    r = bottle.HTTPResponse(status=200, body=body)
    r.set_header('Content-Type', 'text/plain')
    return r

bottle.run(host='localhost', port=8080)
