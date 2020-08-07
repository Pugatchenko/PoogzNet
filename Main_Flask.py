from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates')

@app.route("/")
@app.route("/home")
def home():
    return render_template('home_layout.html')

@app.route("/personal")
def personal():
    return render_template('personal.html')

@app.route("/professional")
def professional():
    return render_template('professional.html')

@app.route("/projects")
def projects():
    return render_template('projects.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

if __name__=="__main__":
    app.run(debug=True)
