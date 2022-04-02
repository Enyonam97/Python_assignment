# Assignment 01
# write a python code that store the foolowing
# Employee Id
# First name
# Last Name
# Basic Salary
# Allowance
# Pension Scheme
# Tax
# Net Salary =((Basic Salary-Tax-Penseion Scheme) + Allowance)
# Print each variable

def calculateBasicSalary():
    EmployeeId = 12335546
    FirstName = "James"
    LastName = "Bond"
    NetSalary = 8000
    BasicSalary = 10000
    Allowance = 1500
    PensionScheme = 3000
    Tax = 500
    NetSalary = (BasicSalary- Tax - PensionScheme+ Allowance)
    print(EmployeeId)
    print(FirstName)
    print(LastName)
    print(NetSalary)
    print(BasicSalary)
    print(Allowance)
    print(PensionScheme)
    print(Tax)
    print(NetSalary)        
calculateBasicSalary()

# Assignment 02
#  Create a list of 10 users to add the following fields
# Id
# Name
# Email
# Phone Number
# Number of visits
# Posts:
#    - Post Id,
#    - Title,
#    - Summary

# Write a for loop to iterate through the list of users and print
# user = lackey
# print(number of visits)
# Print(number of posts)


my_list = [
    {
        "id": 1,
        "name": "Kwame",
        "email": "kwame@gmail.com",
        "phone_number": "547198658",
        "num_of_visits": 1000,
        "list_of_post": {"post_id": 2, "title": "feed", "summary": 500},
    },
    {
        "id": 2,
        "name": "Boakye",
        "email": "boakye@gmail.com",
        "phone_number": "545698650",
        "num_of_visits": 5000,
        "list_of_post": {"post_id": 3, "title": "fun", "summary": 600},
    },
    {
        "id": 3,
        "name": "Emmanuel",
        "email": "boakye@gmail.com",
        "phone_number": "545698650",
        "num_of_visits": 5000,
        "list_of_post": {"post_id": 4, "title": "food", "summary": 600},
    },
    {
        "id": 4,
        "name": "Caleb",
        "email": "caleb@gmail.com",
        "phone_number": "545692350",
        "num_of_visits": 5500,
        "list_of_post": {"post_id": 5, "title": "sweet", "summary": 400},
    },
    {
        "id": 5,
        "name": "Odafe",
        "email": "odafe@gmail.com",
        "phone_number": "549698340",
        "num_of_visits": 6400,
        "list_of_post": {"post_id": 6, "title": "love", "summary": 600},
    },
    {
        "id": 6,
        "name": "Malik",
        "email": "malik@gmail.com",
        "phone_number": "545808350",
        "num_of_visits": 500,
        "list_of_post": {"post_id": 7, "title": "honey", "summary": 60},
    },
    {
        "id": 7,
        "name": "Clement",
        "email": "clement@gmail.com",
        "phone_number": "205690650",
        "num_of_visits": 900,
        "list_of_post": {"post_id": 8, "title": "milo", "summary": 700},
    },
    {
        "id": 8,
        "name": "Frema",
        "email": "frema@gmail.com",
        "phone_number": "245698650",
        "num_of_visits": 30,
        "list_of_post": {"post_id": 9, "title": "strawberry", "summary": 600},
    },
    {
        "id": 9,
        "name": "Slim",
        "email": "slim@gmail.com",
        "phone_number": "275698650",
        "num_of_visits": 1500,
        "list_of_post": {"post_id": 10, "title": "red", "summary": 300},
    },
    {
        "id": 10,
        "name": "Elias",
        "email": "elias@gmail.com",
        "phone_number": "276608630",
        "num_of_visits": 200,
        "list_of_post": {"post_id": 11, "title": "black", "summary": 430},
    },
]

for dictionary in my_list:
    print("Username: " + str(dictionary["name"]))
    print("Number of visits: " + str(dictionary["num_of_visits"]))
    print("Title of post: " + str(dictionary["list_of_post"]["title"]))


# Assignment 03
# Taking into consideration MESt kitchen app, write a class to model the various objects:
# think of the real world and translate it to a class.

# A user class

class User():
  first_name = ''
  last_name = ''
  email_address = ''
  phone_number = ''
  alergies = ''
  gender = ''
  user_type = ''

    def __init__(self, first_name, last_name, email_address, phone_number, allergies, gender, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.allergies= allergies
        self.gender = gender
        self.user_type = user_type

class MealItem():
    meal_name = ''
    meal_description = ''
    serving_size = ''
    allergens = ''
    meal_image = ''

    def __init__(self, meal_name, meal_description, serving_sizes, allergens, meal_image):
        self.meal_name = meal_name
        self.meal_description = meal_description
        self.serving_sizes = serving_sizes
        self.allergens = allergens
        self.meal_image = meal_image

class Order():
    order_details = ''
    quantity = ''

    def __init__(self, order_details, quantity):
        self.order_details = order_details
        self.quantity = quantity

class Price():
    amount = ''
    balance = ''

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance

# Instantiate a user as an EIT
user_as_eit = User('Carol, 'Ofori','carol@ofori.com'
                   '+233547198658', 'female', 'none', 'EIT')

# Instantiate a user as an Staff
user_as_staff = User('John', 'Atta', 'john@atta.com',
                     '+2331234567', 'male', 'none', 'STAFF')


# Instantiate a meal object
new_meal = MealItem('Jollof with grilled pork',
                    'This is the regular jollof and grillled pork', '2 plate', '')


# Instantiate an order object
new_order = Order('jollof with grilled pork', 2)

print(user_as_eit.last_name)
print(user_as_staff.first_name)
print(new_meal.meal_name)
print(new_order.quantity)






