import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)


@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    data = []
    with open('data/company.json', 'r') as json_data:
        data = json.load(json_data)
    tasks=mongo.db.tasks.find()
    return render_template("tasks.html", page_title="tasks.html", tasks=tasks, company=data) 

    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", page_title="addrecipe.html", categories=mongo.db.categories.find())
    
    
@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)