from flask import Flask, redirect, url_for
from flask import render_template

app = Flask(__name__)


# Assignment 8

@app.route('/')
@app.route('/nitay_cv')
def nitay_cv():
    return render_template('my_cv.html')


# Assignment 7

@app.route('/first_seen')
def first_seen():
    return render_template('first_seen.html')


@app.route('/first')
def redirect_url_for():
    return redirect(url_for('first_seen'))




@app.route('/second_seen')
def second_seen():
    return render_template('second_seen.html')


@app.route('/second')
def x():
    return redirect('/second_seen')


# Assignment 8



if __name__ == '__main__':
    app.run(debug=True)
