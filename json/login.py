import json

# data =  {
#     "userId": 1,
#     "username": "sserakal@student.wethinkcode.co.za",
#     "password": "serendipity",
#     "active": "false"
#   }
# with open('user_account.json','w') as file:
#     json.dump(data,file)

def login(user):
    username = input("Name: ")
    password = input("Password: ")

    if username in usr.keys():
        if password == usr[uN]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else: 
        print("Hello, new person.")
        usr[username] = password

    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("user_account.json", "r") as f:
            return json.load(f)
    except IOError:
        return {}

def writeUsers(usr):
    with open("user_account.json", "w+") as f:
            json.dump(usr, f)

users = readUsers()
success = login(users)

while not success:
    success = login(users)