from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# /// = relative path, //// = absolute path
# set some config parameters for our database, create the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# create a model class for our todo items: ID number, string title, completeness bool
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)


# todo app homepage
@app.route("/")
# homepage lists all the todos, rendered in HTML
def home():
    todo_list = Todo.query.all()
    return render_template("base.html", todo_list=todo_list)


# URL route for adding a to-do
@app.route("/add", methods=["POST"])
def add():
    # create new todo of Todo class with user-inputted title
    title = request.form.get("title")
    new_todo = Todo(title=title, complete=False)

    # add new todo to SQL database, commit current transaction
    db.session.add(new_todo)
    db.session.commit()

    # redirect to homepage
    return redirect(url_for("home"))


# URL route for updating a specific to-do
@app.route("/update/<int:todo_id>")
def update(todo_id):
    # fetch todo from database via unique todo_id, and toggle completeness
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete

    # commit the current transaction, redirect to homepage
    db.session.commit()
    return redirect(url_for("home"))


# URL route for deleting a specific to-do
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    # fetch todo from database via unique todo_id, and delete todo from DB
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)

    # commit the current transaction, redirect to homepage
    db.session.commit()
    return redirect(url_for("home"))

# For each url/route we want, we have to create a function and decorate it with @app.route('path/to/your/url'). In this case we only use a forward slash /because this is going to be our start page. Note that we set debug=True so we don't have to reload our server each time we make a change in our code.


if __name__ == "__main__":
    # kept getting a RunTime error that I was working outside the application context, with a
    # trace that started with the call to db.create_all so I added this line to set up
    # application context
    with app.app_context():
        db.create_all()
    # set debug to True so we don't have to reload server each time we change code
    app.run(debug=True)