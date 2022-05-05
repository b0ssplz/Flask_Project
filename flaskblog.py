from flask import Flask, render_template, url_for

app = Flask(__name__)


posts = [
    {
        'author': 'Marcin Wis',
        'title': 'First post',
        'content': 'forst post content',
        'date_posted': '4 May 2022'
    },
    {
        'author': 'Ala Pep',
        'title': 'First post2',
        'content': 'forst post content2',
        'date_posted': '3 May 2022'
    }
    ]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


if __name__ == '__main__':
    app.run(debug=True)
