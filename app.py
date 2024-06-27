import flask 
from pymongo import MongoClient
from flask import render_template, request ,redirect, url_for
from bson import ObjectId

app = flask.Flask(__name__ ,template_folder='template')

client = MongoClient('localhost', 27017)


@app.route('/', methods=['GET' , 'POST'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('index'))
    all_todos = todos.find()
    return render_template('index.htm', todos=all_todos)

@app.post("/<id>/delete")
def delete(id):
    todos.delete_one({'_id':ObjectId(id)})
    return redirect(url_for('index'))

# Define the "todos" variable
db = client.flask_database
todos = db.todos

if __name__ == '__main__':
    app.run(debug=True)