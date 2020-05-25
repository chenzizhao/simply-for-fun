from flask import Flask, render_template

app = Flask(__name__)


experiences = [
    {
        'company':'SOCAAR, University of Toronto',
        'role':'Research Assistant',
        'time':'March 2019 - August 2019',
    },

    {
        'company':'Faculty of Law, University of Toronto',
        'role':'IT Help Desk Analyst',
        'time':'October 2019 - April 2020',
    },

    {
        'company':'Google',
        'role':'STEP Intern',
        'time':'May 2020 - August 2020',
    }
]



@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html", experiences=experiences)

if __name__ == "__main__":
    app.run(debug=True)