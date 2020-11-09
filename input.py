from datetime import date
from datetime import time

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

def get_date(date): 
    """
    Validate date input in this format DD/MM/YYYY 
    """

    #input date
    input_date = date.split("/")

    #current date
    # current_time = str(date.today())
    # print(current_time, 'CURRENT TIME')
    # #current_date = current_date.split("-")

    # #month End date
    # Ending_31
    # Ending_30
    # Ending_30

    #check if months is valid
    return Trues