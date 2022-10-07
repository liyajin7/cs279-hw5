I built this prototype using the [tutorial linked](https://www.python-engineer.com/posts/flask-todo-app/) on the Canvas assignment!

# How to run
1. Clone this repo and open the repository in your IDE of choice.
2. Open a terminal, navigate to the repo, and run `python3 -m venv venv`.
3. Run `. venv/bin/activate` on Mac, `venv\Scripts\activate` on Windows.
4. Install Flask and Flask-SQLAlchemy if not already installed (`pip install Flask` and `pip install Flask-SQLAlchemy` respectively)
5. Run the app with `python app.py`.


# Reflection
*What are the significant software concepts that this combination of technologies has that each previous set of technologies did not? Or that they handle significantly differently?*

A huge difference between other technologies we've used (ObservableHQ, React) is that Flask is a lightweight framework that's independent of external libraries. With the help of Python’s default libraries ,we really only needed to write two files of code: `app.py` and `base.html`.

We were also easily able to create the backend <—> frontend logic with the help of the open source `SQLAlchemy` module that's built into Python.

There are some similarities to our MongoDB app in that we again use “routing” to control functionality and generally segment app functionality, occasionally passing in information like `todo_id` through the URL. The simplicity, however, of using the `SQLAlchemy` module is far less lift than setting a separate backend on MongoDB in which we had to design a mongoose schema, connect to MongoDB separately, store a connection string in a `.env` file, etc. In our Flask app, all we had to do to connect and instantiate our database was configure our app with a SQLAlchemy URI in 3 lines of code, all in `app.py`. Flask combines and greatly simplifies many of the more standardly complex database connection technologies we’ve ground out so far. 

A small note, but Semantic UI was also a huge simplification of styling: we were able to do all of our styling in `base.html` with predefined Semantic UI style classes!
