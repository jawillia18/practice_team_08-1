import datetime
import os


# global var
time_difference_capture = datetime.datetime.today()

# create a new ticket
def create_ticket():

    # add current time to the ticket.txt file
    ticket = open("app_data/ticket.txt", "a+")
    ticket.write(f"{datetime.datetime.today()}\n")
    ticket.close()

    print("Your Token will expire in 30 minutes from now")




def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `-.,:/`
    :return: a list of words from splitting text using the delimiters
    """

    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_time_to_list(datetime_stamp):
    return list(filter(lambda x: x != '', split("-.,:/ ", datetime_stamp)))


def get_the_diff():
    global time_difference_capture


    unwanted = ['\n']
    usable_ticket = ''
    # open and read the tickets file
    tickets_file = open("app_data/ticket.txt", "r")
    tickets = tickets_file.readlines()
    tickets_file.close()

    # get the latest ticket
    latest_ticket = tickets[len(tickets)-1]
    

    # filter the ticket to remove the \n chars
    latest_ticket_filtered = list(filter(lambda char: char not in unwanted, latest_ticket))
    
    for char in latest_ticket_filtered:
        usable_ticket += char

    # get the current time and convert it to a list
    now = datetime.datetime.today()
    

    # calculate the difference between the latest ticket and the current time
    ticket_time = datetime.datetime.strptime(usable_ticket, '%Y-%m-%d %H:%M:%S.%f')
    time_diff = now - ticket_time
    
    time_diff = convert_time_to_list(str(time_diff))

    if len(time_diff) == 4:
        if int(time_diff[0]) > 0 or int(time_diff[1]) > 30:
            print("Your last ticket expired, please login")
            if os.path.exists("token.pickle"):
                os.remove("token.pickle")
            return False
        else:
            return True

    elif len(time_diff) > 4:
        print("Your last ticket expired, please login")
        return False
    
    print("something went wrong with the programme files, please contact the developer for assistance")
    return False
