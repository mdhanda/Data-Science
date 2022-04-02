# Task:
# 1. Write a function to fetch data from SQL Table via API (postman)
# 2. Write a function to fetch data from MongoDB table via API (postman)

from flask import Flask, request, jsonify
import pymongo
import mysql.connector as connection
from bson.json_util import dumps


app = Flask(__name__)

@app.route('/sql/listdbnames', methods=['GET', 'POST'])
def sql_db_names():
    mydb = connection.connect(host="localhost", user="root", passwd="admin", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "SHOW DATABASES"

    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(str(result))

@app.route('/sql/students', methods=['GET', 'POST'])
def sql_students():
    mydb = connection.connect(host="localhost", user="root", passwd="admin", use_pure=True)
    # check if the connection is established
    print(mydb.is_connected())

    query = "SELECT * FROM testdb.StudentDetails"

    cursor = mydb.cursor()  # create a cursor to execute queries
    cursor.execute(query)
    result = cursor.fetchall()
    return jsonify(str(result))

@app.route('/mongo/listdbnames', methods=['GET', 'POST'])
def mongo_db_names():
    DEFAULT_CONNECTION_URL = "mongodb+srv://mongodb:mongodb@cluster0.2wjy8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    result = client.list_database_names()
    return jsonify(str(result))

@app.route('/mongo/list', methods=['GET', 'POST'])
def mongo_db_names_list():
    DEFAULT_CONNECTION_URL = "mongodb+srv://mongodb:mongodb@cluster0.2wjy8.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    client = pymongo.MongoClient(DEFAULT_CONNECTION_URL)
    db = client['sudh']
    coll = db['ineuron_collection']
    cursor = coll.find()
    list_cur = list(cursor)
    json_data = dumps(list_cur)
    
    return json_data


if __name__ == '__main__':
    app.run()