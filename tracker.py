from flask import Flask, render_template, url_for

app = Flask(__name__)

posts = [
    {
        'author': 'Chris collins',
        'title': 'Example',
        'content': 'Test content',
        'date_posted': '30/6/26'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)