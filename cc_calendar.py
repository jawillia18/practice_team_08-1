
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
from prettytable import prettytable

SCOPES = ["https://www.googleapis.com/auth/calendar"]

CAL_ID = "c_if5tihbg7n7a5k5261np66o514@group.calendar.google.com"

# The file token.pickle stores the user's access and refresh tokens, and is
# created automatically when the authorization flow completes for the first
# time.
creds = None
if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)
# If there are no (valid) credentials available, let the user log in.
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secret.json', SCOPES)
        creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open('token.pickle', 'wb') as token:
        pickle.dump(creds, token)


code_calendar = build("calendar", "v3", credentials=creds)


def convert_to_RFC_datetime(year=2020, month=1, day=1, hour=0, minute=0):
    dt = datetime.datetime(year, month, day, hour, minute, 0).isoformat() + 'Z'
    return dt


# def get_calendar():


def add_slot(summary, start_time, end_time, email):
    '''
    Creates event on Google calendar
    '''
    slot_details = {
    "summary": summary,
    "start": {"dateTime": start_time},
    "end":   {"dateTime": end_time},
    "attendees": [{"email": email}, 
                  {"email": "codeclinic@mail"}],
    }
    slot = code_calendar.events().insert(calendarId=CAL_ID,sendNotifications=True, body=slot_details).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (slot["summary"].encode("utf-8"),
            slot["start"]["dateTime"], slot["end"]["dateTime"]))


def book_slot(eventID, email):
    '''
    Books available slot by adding user email to created event
    '''
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    event["attendees"].append({"email": email})
    updated_event = code_calendar.events().update(calendarId=CAL_ID, eventId=event['id'], sendNotifications=True, body=event).execute()


def display_slots():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    events = events_result.get('items', [])
    print(events)
    t = PrettyTable(['Date', 'Time', 'Event'])
    for event in events:
        # print(event)
        
        start = event['start'].get('dateTime', event['start'].get('date'))
        start = start.replace("T", " ").replace("+02:00", "")
        t.add_row([date, time, event['summary']])
        event_details.write(start + event['summary']+'\n')
        # print(start, event['summary'], event["id"])

# Delete event by ID
def cancel_slot(eventID):
    code_calendar.events().delete(calendarId=CAL_ID, eventId=eventID).execute()


def cancel_booking(eventID):
    event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
    email = get_user_email()
    for attendee in range(len(event["attendees"]) - 1):
        if event["attendees"][attendee]["email"] == email:
            event["attendees"].pop(attendee)
    code_calendar.events().update(calendarId=CAL_ID, eventId=event['id'], body=event).execute()


def store_calendar_details():
    '''
    Creates calendar.json which stores the calendar information in py dictionary.
    '''
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()

    if events_result == []:
        return

    if os.path.exists("calendar.json"):
        with open("calendar.json") as open_calendar:
            calendar_data = json.load(open_calendar)
        if calendar_data == events_result["items"]:
            return
    with open("calendar.json", 'w') as calendar_out:
        json.dump(events_result["items"], calendar_out, indent=4)

    # events_result.


# def get_attendees(eventID):
#     '''
#     creates a list of attendees
#     '''
#     event = code_calendar.events().get(calendarId=CAL_ID, eventId=eventID).execute()
#     attendee_list = []
#     if len(event["attendees"]) == 0:
#         return None
#     for attendee in event["attendees"]:
#         attendee_list.append(attendee["email"])

#     return attendee_list


def get_user_email():
    calendar = code_calendar.calendars().get(calendarId='primary').execute()
    return calendar["id"]
    

'''
Calls the function that stores calendar data; is called when program is run
'''
store_calendar_details()
get_user_email()
