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
