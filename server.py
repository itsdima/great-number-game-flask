from flask import Flask, redirect, render_template, session, request
import random

app = Flask(__name__)
app.secret_key = 'secret'

@app.route('/')
def home():
	num = random.randrange(1, 100)
	if 'num' not in session:
		session['num'] = num
	if 'guess' not in session:
		session['guess'] = ''
	print session['num']
	print session['guess']
	return render_template('index.html', num=session['num'], guess=session['guess'])

@app.route('/result', methods=['POST'])
def result():
	session['guess'] = int(request.form['guess'])

	return redirect('/')

@app.route('/playagain', methods=['POST'])
def playagain():
	session.pop('guess')
	session.pop('num')

	return redirect('/')

app.run(debug=True)