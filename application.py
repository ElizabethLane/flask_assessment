from flask import Flask, render_template
from flask import request
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")


@app.route("/application-form")
def application_form():
    """Application Page"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def application():
    """Application Response"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job_title = request.form.get("jobtype")


    return render_template("application-response.html", 
                            name=first_name,
                            lastname=last_name,
                            monies=salary,
                            job=job_title)

if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")



#When I ran the server I saw this error in the console:

# (env)vagrant@vagrant-ubuntu-trusty-64:~/src/flask$ python application.py
# Traceback (most recent call last):
#   File "application.py", line 2, in <module>
#     from flask_debugtoolbar import DebugToolbarExtension
# ImportError: No module named flask_debugtoolbar

#I FIGURED THIS OUT! I had to pip install flask_debugtoolbar
#ALSO I realized I had to import request from flask
#Duh

#I commented out anything to do with the DebugToolbarExtension and the server
#was then able to run
