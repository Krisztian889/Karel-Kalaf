from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def about():
    return render_template('about.html')

@app.route("/index/")
def index():
    return render_template('index.html')

@app.route("/contact/")
def contact():
    return render_template('contact.html')

@app.route("/hire/")
def hire():
    return render_template('hire.html')   

@app.route("/playing_styles/")
def playing_styles():
    return render_template('playing_styles.html')

@app.route("/guitar_tut/")
def guitar_tut():
    return render_template('guitar_tut.html')      



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

