from flask import Flask, render_template, request, redirect, jsonify, session
from flask_pymongo import pymongo
from bson import json_util
import database.queries as queries



app = Flask(__name__)
client = pymongo.MongoClient("mongodb://admin:intercept@45.55.198.145/interceptDB")
db = client.interceptDB


'''Test to JSONIFY DB result of orgs'''


@app.route('/')
def db_tests1():
    services = ['Legal Services', 'Shelter', 'Food']
    populations = ['Minor', 'Male']
    user = queries.insert_record('Carrollton', populations, services, 'English')
    return user


@app.route('/test')
def db_tests():
    return list(queries.get_questions())


@app.route('/organization')
def organization():
    org_ID = request.args.get('id', default='*', type=str)

    the_org = queries.get_org_by_ID(org_ID)
    print(org_ID)
    print(the_org)
    return str(the_org)


'''User login'''
'''below is admin functionality-  basically, if admin, redirect to an admin portal page, otherwise, render
normal user experience html page'''


@app.route('/login')
def login():
    '''if session.get("admin"):
        return redirect('/admin_portal')
    else:
        return render_template('login_page.html')'''


'''Handles POST action for Login, grab username/password from HTML form'''


@app.route('/login_submit', methods=['POST'])
def user_login():
    username = request.form['username']
    password = request.form['password']
    print("test")


'''We receive a JSON for this POST, so we handle it accordingly using Flask's JSON functionality'''


@app.route('/survey_submit', methods=['POST'])
def save_survey():
    json_Dictionary = request.get_json()
    '''do stuff with jsonDict- parse into format for DB insert'''
    print("test survey submit")


if __name__ == '__main__':
    app.run()
