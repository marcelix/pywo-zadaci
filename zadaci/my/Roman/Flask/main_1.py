from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/hello")
def hello():
    return render_template('hello.html')


if __name__ == '__main__':
    app.run(debug=True)