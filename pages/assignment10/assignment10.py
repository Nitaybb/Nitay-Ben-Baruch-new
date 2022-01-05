from flask import redirect, render_template, request, Blueprint
from interact_db import interact_db


change_message = ""

assignment10 = Blueprint('assignment10', __name__, static_folder='static', static_url_path='/assignment10', template_folder='templates')


@assignment10.route("/assignment10", methods=['GET', 'POST'])
def assignment10s():
    global change_message
    change_message = ""
    return render_template('assignment10.html')


#### Insert new user to users table ####
@assignment10.route('/insert_new_user', methods=['POST'])
def insert_new_users():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    query = "INSERT INTO users(email, first_name, last_name) VALUES ('%s', '%s', '%s')" % (email, first_name, last_name)
    interact_db(query=query, query_type='commit')
    global change_message
    change_message = "The user "+first_name + " " + last_name+" is add to users table"
    return redirect('/users_list')


#### Update user email by first & last neme ####
@assignment10.route('/update_user_email', methods=['POST'])
def update_users():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_email = request.form['new_email']
    query = "update users set email = '%s' where first_name = '%s' and last_name = '%s';" % (new_email, first_name, last_name)
    interact_db(query=query, query_type='commit')
    global change_message
    change_message = "The email of the user "+first_name + " is updated to " + new_email + "."
    return redirect('/users_list')


#### Delete user by first & last name ####
@assignment10.route('/delete_user', methods=['POST'])
def delete_users():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    query = "DELETE FROM users where first_name = '%s' and last_name = '%s';" % (first_name, last_name)
    interact_db(query, query_type='commit')
    global change_message
    change_message = "The user: " + first_name + " " + last_name + " was deleted"
    return redirect('/users_list')


#### Print user list ####
@assignment10.route('/users_list')
def user_lists():
    query = "select * from users"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('assignment10.html', user_list=query_result, change_message=change_message)
