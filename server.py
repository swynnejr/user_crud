from flask import Flask, render_template, request, redirect
# from user.py import class User
from user import User

app = Flask(__name__)
app.secret_key = 'user cr'

# This is what happens when the website is visited
@app.route('/')
def index():
# This calls on the Class to utilize its method that contains a function established to query our database
    users = User.get_all_users()
# FUNCTIONALITY TEST ONLY: For each entry in our column
    for user in users:
# This is an early test that should spit our user id's from the database in the terminal to make sure we are connecting to db and that our query works properly
        print(user.id)
# This will tell our homepage ('/') to use index.html to render a template and users in green is the data we are passing it, from user in pink that got its value passed to it from User.get_all_users()
    return render_template('index.html', users = users)

@app.route('/create')
def create_form():
    return render_template('create.html')

# This function is called when the URL is visited. Since it is uses methods POST you don't actually see this page, when the function is run it REDIRECTS to another page where we have a template to show the data
@app.route('/users/create', methods=['POST'])
def create_user():
    # print(request.form) FUNCTIONALITY TEST ONLY: Use this to check your terminal to see if your dictionary is being recieved by your form
# This is what calls the method inside of our User class to request the data from our "create user" form
    User.create_user(request.form)
#  REDIRECT IS REQUIRED FOR methods=['POST']
    return redirect('/show/<int:user.id>')

@app.route('/users/<int:user.id>/delete')
def delete_user(user_id):
    data = {
        'id': user_id
    }
    User.delete_user(data)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)