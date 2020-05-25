from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author':'Zoe Chen',
        'title':'first post',
        'content':'Today I learned Flask',
        'date_posted':'May 24, 2020',
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", title="Home Page")

@app.route("/about")
def about():
    return render_template("about.html", posts=posts)

if __name__ == "__main__":
    app.run(debug=True)