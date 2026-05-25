#CREATIING CLASSES AND OBJECTS
class FirstClass:
    x = 5

obj1 = FirstClass()
obj2 = FirstClass()
obj3 = FirstClass()
print(obj1.x)
print(obj2.x)
print(obj3.x)


#SELF PARAMETER | CLASS METHODS
class User:

    def set_username(self, username:str):
        self.username = username
    
    def set_age(self, age:int):
        self.age = age
    
user1 = User()
user1.set_username("raman01")
user1.set_age(21)
print(user1.username)
print(user1.age)


# __init__() METHOD
class User:

    def __init__(self, username, age):
        self.username = username
        self.age = age

user1 = User("raman01", 22)
print(user1.username)
print(user1.age)


#STATIC METHOD
class User:
    
    def __init__(self, username, age):
        self.username = username
        self.age = age

    def edit_username(self, username):
        self.username = username
    
    @staticmethod
    def check_username(username):
        if len(username) > 0:
            print("Username is valid. Ready to proceed...")
        else:
            print("Username invalid.")
    

user1 = User("sandy5", 21)
User.check_username(user1.username)
user1.edit_username("")
User.check_username(user1.username)


#CLASS METHOD
class User:
    no_of_users = 0

    def __init__(self, username):
        self.username = username
        User.no_of_users += 1

    
    @classmethod
    def user_count(cls):
        print(f"Current no. of users: {cls.no_of_users}")

user1 = User("sandy5")
User.user_count()
user2 = User("raman1")
user3 = User("rehan2")
user4 = User("aviyan")
User.user_count()