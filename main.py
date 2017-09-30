from flask import Flask, request
from pymongo import MongoClient
from json import dumps
from flask_restful import Resource, Api
from bson.json_util import dumps
import jsonify


# App object instance. 
app = Flask(__name__)

# Main entry point for application, instance it with Flask app.
api = Api(app)

# MongoClient instance.
client = MongoClient('localhost:27017')

# DB creation.
db = client.chicago_employees


class Chicago_department(Resource):

    def get(self):
        # Perform query and return data.
        query = db.salary.find({})
        data = dumps(query)
        return data

class Department_salary(Resource):

    def get(self, department_name):
        dep = department_name.upper()
        print dep
        #query = db.salary.find({Department: dep})
        query = db.salary.find({'Department': {'$regex': dep, '$options': 'i'}})
        print query
        return dumps(query)


class HelloWorld(Resource):

    def get(self):
        return {'hello': 'world'}


@app.route('/index')
@app.route('/')
def home():
    return 'Hello api'


api.add_resource(Chicago_department, '/api/v1.0/departments')
api.add_resource(Department_salary, '/api/v1.0/<string:department_name>')
api.add_resource(HelloWorld, '/api/v1.0/home')

if __name__ == '__main__':
    app.run(debug=True)
