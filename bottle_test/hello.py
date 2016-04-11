#!/usr/bin/env python3
#-*-coding: utf-8-*-
from bottle import route, run, template, request, static_file, url, get, post
import sys, codecs, os
import hello
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

@get('/')
def login():
	return """
<p>
	<form action='sayHello' method='post'>
		firstname: <input name='firstname' type='text' /> <br />
		lastname: <input name='lastname' type='text' /> <br />
		<input value='login' type='submit' />
	</form>
</p>

<p>
	<form action="/readTxt" method="post" enctype="multipart/form-data">
		<div class="form-group">
			<label class="control-label" for="upload">Select a txt file:
			<input type="file" name="upload">
		</div>
		<div class="form-group">
			<input type="submit" value="Upload" class="btn btn-primary">
		</div>
	</form>
</p>
"""


@post('/sayHello')
def sayHello():
	firstname = request.forms.get('firstname')
	lastname = request.forms.get('lastname')
	return '<p>%s</p>' % hello.out(firstname, lastname)


@post('/readTxt')
def readTxt():
	upload = request.files.get('upload')
	name, ext = os.path.splitext(upload.filename)

	if ext != '.txt':
		return '<p>"%s" is not txt file.</p>' % upload.filename

	upload.save('./txt', overwrite=True)
	return "<p>%s</p>" % hello.mycat('./txt/'+upload.filename).replace('\n','<br>\n')


run(host='localhost', port=8080, debug=True)
