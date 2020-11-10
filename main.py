import time
import get_input
# All accounts
users = {
    "root": {
        "password": "gucci-mane",
        "group": "admin",
        "slots": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not get_input.get_username(username):
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not get_input.get_password(password):
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        return session(username)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username*: ")
        if not get_input.get_username(username):
            print("Username can't be blank!!!")
            continue
        else:
            break
    while True:
        password = input("New password*: ")
        if not get_input.get_password(password):
            print("Password can't be blank!!!")
            continue
        else:
            break
    while True:
        email = input("User-email*: ")
        if not get_input.get_email(email):
            print("User-email can't be blank!!!")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["slots"] = []
    time.sleep(1)
    print("Account has successfully been created")


def help_me():
    help1 = """
        register:   Enter the username of your Choice and Password which consist of six or more characters to register
        login:      Enter the registered username and password to access your account
        exit:       Exit the program as it shutdown
    """
    return help1

def help_me2():
    help2 = """
        add slots:  Add the slots NB: slots can't be duplicated
        check slots:check the available slots
        book slots: from the added slots book the available slot
        exit:       Exit the program as it shutdown
    """

    return help2

def add_slots(username):
    while True:
        topic = input("Topic > ")
        if not len(topic) > 0:
            print("Topic can't be blank")
            continue
        else:
            break
    while True:
        time1 = input("Time > ")
        if not len(time1) > 0:
            print("Time can't be blank")
            continue
        else:
            break
    while True:
        name = input("Username > ")
        if not len(name) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        status = input("Status > ")
        if not len(status) > 0:
            print("Status can't be blank")
            continue
        else:
            break
    print("adding slot...")
    users[username]["slots"].append(["Topic: " + topic, "Time: " + time1, "Status: " + status])
    time.sleep(2)
    print("slot has been added successfully")


# User session
def session(username):
    print("Welcome to your account " + username)
    print("Menu: check slots | add slots | book slots | delete slots | logout | help")
    if users[username]["group"] == "admin":
        print("")
    while True:
        option = input(username + " > ")
        if option == "logout":
            print("Logging out...")
            break
        elif option == "check slots":
            print("Available slots:")
            for i in users[username]["slots"]:
                print(i)
        elif option == "add slots":
            print("function not available")
            add_slots(username)
        elif option == "book slots":
            print("function not available")
        elif option == "delete slots":
            print("function not available")
        elif option == "help":
            print(help_me2())
        else:
            print(option + " is not an option")

# On start
print("Welcome to the system. Please register or login.")
print("Menu: register | login | help | exit")
while True:
    option = input("> ")
    if option == "login":
        login()
    elif option == "register":
        register()
    elif option == "help":
        print(help_me())
    elif option == "exit":
        break

    else:
        print(option + " is not an option")

# On exit
print("Shutting down...")
time.sleep(1)

