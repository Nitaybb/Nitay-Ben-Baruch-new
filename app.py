from flask import Flask, redirect, url_for, request, session
from flask import render_template

app = Flask(__name__)
app.secret_key = '123'

my_users = {'user1': {'first_name': 'Nitay', 'last_name': 'Ben Baruch', 'email': 'user1@Xmail.com'},
            'user2': {'first_name': 'Itzik', 'last_name': 'Hagever', 'email': 'user2@Xmail.com'},
            'user3': {'first_name': 'Yosi', 'last_name': 'Ben Baruch', 'email': 'user3@Xmail.com'},
            'user4': {'first_name': 'Neta', 'last_name': 'nice girl', 'email': 'user4@Xmail.com'},
            'user5': {'first_name': 'Arsani', 'last_name': 'WEB', 'email': 'user5@Xmail.com'},
            'user6': {'first_name': 'Volley', 'last_name': 'Ball', 'email': 'user6@Xmail.com'}
            }


# Assignment 9
@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9():
    # search form
    if 'name' in request.args:
        name = request.args['name']
        if name == '':
            return render_template('assignment9.html', users_list=my_users)

        for key, value in my_users.items():
            if value.get('first_name') == name:
                return render_template('assignment9.html',
                                       user_first_name=value.get('first_name'),
                                       user_last_name=value.get('last_name'),
                                       user_email=value.get('email'))

    # Registration form
    if request.method == 'POST':
        new_user = request.form['new_user']
        session['new_user'] = new_user
    return render_template('assignment9.html')


@app.route("/logout_assignment9")
def logout_assignment9():
    session['new_user'] = '' # removing the global variable
    return render_template('assignment9.html') # returns to the log in page


# Assignment 8


@app.route('/')
def home_page():
    return render_template('home_page.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        name = request.form['nickname']
        password = request.form['password']
        # DB
        session['username'] = name
        return render_template('login.html')


@app.route('/logout')
def logout():
    session['username'] == ''
    return redirect(url_for('login'))


@app.route('/assignment8')
def assignment8():
    if session['username'] == '':
        return render_template('assignment8.html')
    else:
        return render_template('assignment8.html',
                               uni='Ben Gurion University',
                               profile={'First name': 'Nitay',
                                        'Last name': 'Ben Baruch'},
                               hobbies=['Volleyball', 'Beach', 'Dogs']
                               )


@app.route('/about')
def about():
    return render_template('about.html')


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


# Naama Assignments

@app.route('/PUG')
def PUG():
    return render_template('PUG.html')


@app.route('/CVgrid')
def CVgrid():
    return render_template('CVgrid.html')


@app.route('/exercise2')
def exercise2():
    return render_template('exercise2.1.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/GRID')
def GRID():
    return render_template('GRID.html')


@app.route('/JSintro')
def JSintro():
    return render_template('JSintro.html')


if __name__ == '__main__':
    app.run(debug=True)
