# ----------------------Isaya"s update-------------------

def help():
    print("""
----- code clinics8 -----

To use the code clinics8 program; type cs8 [valid_command].
eg. cs8 view_slots

valid commands:

    register:    Enter the username of your Choice and Password which consist of six or more characters to register

    login:       Enter the registered username and password to access your account

    add_slots :  Add the slots NB: slots can't be duplicated

    view_slots:  check the available slots

    book_slots:  from the added slots book the available slot

""")

clinics_valid_argvs = ["login", "register", "view_slots", "book_slot", "help", "logout", "add_slot"]


basic = ["help", "login", "register"]


def process_command(arg):
    valid_ticket = ticket.get_the_diff()
    if valid_ticket and arg not in basic:
        # view_slots
        if arg == "view_slots":
            view_slots("all")

        # book availabe slots
        elif arg =="book_slots":
            book_slot()

        # add a new slot / slots
        elif  arg == "add_slot":
            add_slots("mzet")

        # logout of the current session and user account
        elif arg == "logout":
            print("....logged out of your account")

            # add functions here!

    # provide help
    elif arg == "help":
        help()

    # login to an existing account
    elif arg == "login":
        user_interface.user_login_menu()

    # add a new user
    elif arg == "register":
        user_interface.create_new_user_menu()


def one_session():
    
    if len(sys.argv) == 2:
        arg = sys.argv[1].lower()
        if arg in clinics_valid_argvs:
            process_command(arg)

        else:
            print("""
-invalid command!-

-use "cs8 help" for assistance -
""")

    # this is the home directory of the program, when a user doesn't provide an argument
    elif len(sys.argv) != 2:
        print("""
----- Welcome to code clinics --------

-use "cs8 help" for more information -
""")




if __name__ == "__main__":
    one_session()
    