from mysqlconnection import connectToMySQL


# make a class for the single items from table you want to pull from
class User():
#create initialization method for individual dictionary you will pull from the database to turn into an item
    def __init__(self, data):
# The KEY is the column from db, the value is the entry
# Create a translation into python from MySQL for EACH column you hope to pull data from
# The KEY ['id'] or ['first_name'] MUST match collumn in the database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# Create CLASS METHODS that will interact with the db on our behalf
# CLASS METHODS return INSTANCES of the class from the db as results
    @classmethod
    def get_all_users(cls):
# This is the literal query being run in MySQL, you can and should test them in MySQL if they are complicated
        query = "SELECT * FROM users;"

        results = connectToMySQL('users').query_db(query)

        users = []

        for item in results:
# You can use cls OR the name of the actual class above
            users.append(User(item))

        return users

# The creates the new user in the db by interacting directly with MySQL
    @classmethod
# The data being passed in here comes from the @app.route('/users/create') function create_user via the call to request.form
# Normally this has the parameters (cls, data), but if your FORM matches your data you can just SKIP inputting data ={} below
    def create_user(cls, data):
# It is best to test your query in MySQL then copy it in here
# the %(data)s formatting helps prevent SQL Injection of malicious code
        query = 'INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);'
# This is ONLY necessary if your FORM fields are different from your query fields
        # data = {
        #     'first_name': form['first_name'],
        #     'last_name': form['last_name'],
        #     'email': form['email']
        # }
# This connects to MySQL to run our query and pull our data
# For this project we don't have to 'return' but it is good practice
        return connectToMySQL('users').query_db(query, data)
