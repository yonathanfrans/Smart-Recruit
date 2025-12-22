from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/assistant")
def assistant():
    return render_template("assistant.html")

@app.route("/register")
def register():
    return render_template("register.html", active_page=None)

@app.route("/candidate")
def candidate():
    return render_template("candidate.html", active_page="category")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/detail-candidate")
def detailCandidate():
    return render_template("detail-candidate.html", active_page="category")

if __name__ == '__main__':
    app.run(debug=True)
