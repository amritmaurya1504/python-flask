from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
import pymongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from datetime import datetime

app = Flask(__name__)

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db_connect = myclient["iot_server"]  # database name
db_collection = db_connect["sensor_data"]  # collection name

@app.route("/")
def home():
    return jsonify("Flask Server")

@app.route("/add", methods=['POST'])
def add_user():
    _json = request.get_json()
    _name = _json['name']
    _note = _json['note']
    _date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    data = {
        "name" : _name,
        "note" : _note,
        "date" : _date
    }

    if _name and _note and request.method == 'POST':
        name = db_collection.find_one({'name' : _name})
        # print(type(name))
        if name is None:
            _id = db_collection.insert_one(data)
            resp = jsonify("User Added successfully")
            resp.status_code = 200
            return resp
        else:
            if(name.get('name') == _name):
                return jsonify("User Already exist")
            else:
                _id = db_collection.insert_one(data)
                resp = jsonify("User Added successfully")
                resp.status_code = 200
                return resp
    else:
        return not_found()

@app.route("/get-users", methods=['GET'])
def getUsers():
    users = db_collection.find()
    # print(dumps(users[0]["name"]))
    resp = dumps(users)
    return resp

@app.route("/update/<id>", methods=['PATCH'])
def update(id):
    try:
        print(id)
        db_collection.update_one(
            {'_id' : ObjectId(id)},
            {'$set' : {'name' : "Huheuhuehhhe"}}
        )
        return var
    except Exception as ex:
        print(ex)
        return ex

@app.route("/users/<int:id>/<string:name>")
def user(id,name):
    # print(id,name)
    user = db_collection.find_one({'_id' : ObjectId(id)})
    resp = dumps(user)
    print(resp["name"])
    return "hehe"

@app.route("/search")
def search():
    #geting url variables and converting it into dist
    q = request.args.to_dict()
    print(q['sensor-data'])
    print(q.get("key"))
    return q

@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status' : 404,
        'message' : 'Not Found ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == "__main__":
    app.run(debug=True)