from flask import Flask, render_template
app = Flask(name)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', subtitle='Home Page', text='This is the home page')

if name == 'main':
    app.run(debug=True, host="0.0.0.0")
