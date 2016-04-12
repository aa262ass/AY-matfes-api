# coding=utf-8

from bottle import get, post, route, run, static_file, os, request

#ファイルアップロード
@get('/upload')
def upload():
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            Category:   <input type="text" name="category">
            Select a file:  <input type="file" name="upload">
        <input type="submit" value="start upload">
        </form>
    '''
@route('/upload', method='POST')
def do_upload():
    category = request.forms.get('category')
    upload   = request.files.get('upload')
    name, ext = os.path.splitext(upload.filename)
    if ext not in ('.png', '.jpg', '.jpeg'):
        return 'File extension not allowed.'
    save_path = "./Documents/{category}".format(category=category)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    file_path = "{path}/{file}".format(path=save_path, file=upload.filename)
    upload.save(file_path, overwrite=True)
    return 'OK'
def get_save_path_for_category(category):
    path = './Documents'
    return path


#サーバー起動
run(host='localhost', port=8080, debug=True)
