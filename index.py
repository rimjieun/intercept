from flask import Flask, render_template, request, redirect, jsonify, session
from flask_pymongo import pymongo

app = Flask(__name__)


@app.route('/')
def hello_world():
    client = pymongo.MongoClient("mongodb://Admin:intercept@45.55.198.145/interceptDB")
    db = client.interceptDB
    quant = db.organizations.count()
    print(quant)
    return str(quant)

'''User login'''
@app.route('/login')
def login():
    '''below is admin functionality-  basically, if admin, redirect to an admin portal page, otherwise, render
    normal user experience html page'''
  '''if session.get("admin"):
        return redirect('/admin_portal')
    else:
        return render_template('login_page.html')'''


'''Handles POST action for Login, grab username/password from HTML form'''
@app.route('/login_submit', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']



'''We receive a JSON for this POST, so we handle it accordingly using Flask's JSON functionality'''
@app.route('/survey_submit', methods=['POST'])
def save_survey():
    json_Dictionary = request.get_json()
    '''do stuff with jsonDict- parse into format for DB insert'''
    print("test survey submit")


if __name__ == '__main__':
    app.run()