from user import User
from database import Database

Database().initialise(user="postgres",
                      password="Pcinderella12",
                      database="postgres",
                      host="localhost",
                      port="5433")

user1 = User('manu@hotmail.com', 'Manuel', 'Marquez', None)

user1.save_to_db()

user_from_database = User.load_from_db_by_email('manu@hotmail.com')

print(user_from_database)


