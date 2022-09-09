from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/aboutme")
def about_me():
    return render_template("about_me.html")

@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html")

@app.route("/portfolio/fakebook")
def fakebook():
    return render_template("/fakebook/fakebook.html")

@app.route("/portfolio/boogle")
def boogle():
    return render_template("/boogle/boogle.html")

@app.route("/portfolio/hairsalon")
def hair_salon():
    return render_template("/hair_salon/hair_salon.html")

if __name__ == '__main__':
    app.run(use_reloader=True)