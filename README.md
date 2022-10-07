I built this prototype using the [tutorial linked](https://www.python-engineer.com/posts/flask-todo-app/) on the Canvas assignment!

# How to run
1. Clone this repo and open the repository in your IDE of choice.
2. Open a terminal, navigate to the repo, and run `python3 -m venv venv`.
3. Run `. venv/bin/activate` on Mac, `venv\Scripts\activate` on Windows.
4. Install Flask and Flask-SQLAlchemy if not already installed (`pip install Flask` and `pip install Flask-SQLAlchemy` respectively)
5. Run the app with `python app.py`.


# Reflection
*What are the significant software concepts that this combination of technologies has that each previous set of technologies did not? Or that they handle significantly differently?*

A huge difference between other technologies we've used (ObservableHQ, React) is that Flask is a lightweight framework that's independent of external libraries. We can write the logic for both our frontend and our backend with the help of the open source `sqlite3` module that's built into Python. We also see that we can build CRUD logic directly into the Flask framework without having to use a 3rd-party DB browser UI like MongoDB, in which the code is .
