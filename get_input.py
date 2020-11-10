from datetime import datetime

def get_username(username):

    if isinstance(username, int):
        return False
    try:
        username = username.lower()
    except:
        pass   
    for i in username:
        try:
            int(i)
            return False
        except:
            pass
        if i >= 'a' and i <= 'z':
            pass
        else:
            return(False)
    if len(username) > 0:
        return True
    else:
        return False

def get_date(date_input): 
    """
    Validate date input in this format DD/MM/YYYY 
    """

    #split input date
    try:
        input_date = date_input.split("/")
    except:
        return False

    #check if input format is valid
    try:
        datetime.date(int(input_date[2]), int(input_date[1]), int(input_date[0]))
    except:
        return False
      

    #split current date
    current_date = str(datetime.date.today())
    current_date = current_date.split("-")
    print(current_date, 'CURRENT TIME', date_input, "Date input")

    #compare dates
    if current_date[0] <= input_date[2]:
        if current_date[1] <= input_date[1] :
            if current_date[2] <= input_date[2]:
                return True
        if current_date[1] >= input_date[1]:
            if current_date[0] < input_date[2]:
                return True
    return False

def get_time(time, date):
    """
    Validate time in this format HH:MM over 24h circle
    """

    input_time = time.split(":")

    time = str(datetime.now()).split()
    time = time[1].split(":")
    print("time",time)
    
    # if date == 
    #     if time[0] >= input_time[0]:
    #         if time[1] > input_time[1]:
    #             return True

def get_email(get_email):
    return True

def get_password(get_password):
    return True

