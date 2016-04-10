#!/usr/bin/env python3
#-*-coding: utf-8-*-
from bottle import route, run, template, request, static_file, url, get, post
import sys, codecs
import hello
sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

@route('/')
def html_index():
	return template('index')

@get('/login')
def login():
	return """
		<form action='sayHello' method='post'>
			firstname: <input name='firstname' type='text' /> <br />
			lastname: <input name='lastname' type='text' /> <br />
			<input value='login' type='submit' />
		</form>
	"""

@post('/sayHello')
def sayHello():
	firstname = request.forms.get('firstname')
	lastname = request.forms.get('lastname')
	return hello.out(firstname, lastname)

run(host='localhost', port=8080, debug=True, reloader=True)
