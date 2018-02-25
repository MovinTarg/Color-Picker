from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'movintarg'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/showColor', methods=['POST'])
def completedForm():
    red = request.form['red']
    green = request.form['green']
    blue = request.form['blue']

    return render_template('/index.html', red = red, green = green, blue = blue)

app.run(debug = True)