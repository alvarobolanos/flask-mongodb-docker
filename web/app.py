#app.py

from flask import Flask, render_template, redirect, url_for, request, jsonify
from flask_restful import Api, Resource

app = Flask(__name__) 						# Instantiate a Flask object.
api = Api(app)								# Instantiate an Api object.

# Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/work')
def work():
    return render_template('work.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup_validation')
def signup_validation():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    password = request.args.get('password')
    verify = request.args.get('verify')
    return render_template('thank_you.html',
							first_name=first_name,
							last_name=last_name,
							email=email,
							password=password,
							verify=verify)

@app.route('/thank_you')
def thank_you():
    first_name = request.args.get('first_name')
    last_name = request.args.get('last_name')
    email = request.args.get('email')
    return render_template('thank_you.html',
							first_name=first_name,
							last_name=last_name,
							email=email)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)
