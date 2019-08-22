import os
import json
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId 


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'task_manager'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')


mongo = PyMongo(app)


# recipe card display information 
@app.route('/')
@app.route('/get_tasks')
def get_tasks():
    tasks=mongo.db.tasks.find()
    return render_template("tasks.html", page_title="tasks.html", tasks=tasks) 


# add recipe html page    
@app.route('/add_recipe')
def add_recipe():
    return render_template("addrecipe.html", page_title="addrecipe.html", categories=mongo.db.categories.find())

# insert recipe function from add_recipe.html to tasks.html  
@app.route('/insert_recipe', methods=["GET", "POST"])
def insert_recipe():
    tasks = mongo.db.tasks
    tasks.insert_one(request.form.to_dict())
    return redirect(url_for('get_tasks'))


# edit tasks.html info function
@app.route('/edit_recipe/<task_id>')
def edit_recipe(task_id):
    the_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    all_categories = mongo.db.categories.find()
    return render_template("editrecipe.html", page_title="editrecipe.html", task=the_task, categories=all_categories)
    

# update function to save edited data
@app.route('/confirm_task/<task_id>', methods=["POST"])
def confirm_task(task_id):
    tasks = mongo.db.tasks
    tasks.update({'_id': ObjectId(task_id)},
    {
        'category_name':request.form.get('category_name'),
        'task_name':request.form.get('task_name'),
        'task_description':request.form.get('task_description'),
        'task_note':request.form.get('task_note'),
        'task_instructions':request.form.get('task_instructions')
    })
    return redirect(url_for('get_tasks'))
    
   

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)