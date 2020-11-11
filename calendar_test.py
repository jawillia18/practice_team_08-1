'''To create vitual environment and install necessary packages:
        python3 -m venv vcalendar
        source /goinfre/rsamdaan/practice_team_08/vcalendar/bin/activate
        pip install google-api-python-client
        pip install --upgrade oauth2client
'''

from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import datetime

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

'''TODO get code clinic token'''

SCOPES = ["https://www.googleapis.com/auth/calendar"]

# storage.json stores user login
store = file.Storage("storage.json")
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets("client_secret.json", SCOPES)
    creds = tools.run_flow(flow, store, flags) \
        if flags else tools.run(flow, store)

CAL = build("calendar", "v3", http=creds.authorize(Http()))

GMT_OFF = "+02:00"
EVENT = {
    "summary": "This thang",
    "start": {"dateTime": "2020-11-11T09:00:00%s" % GMT_OFF},
    "end":   {"dateTime": "2020-11-11T11:00:00%s" % GMT_OFF},
    "attendees": ["roderick.t.samdaan@gmail.com"],
}


'''Adds event
time needs to be string of format 2020-11-11T09:00:00+02:00'''
def add_event(summary, start_time, end_time, email):
    EVENTS = {
    "summary": summary,
    "start": {"dateTime": start_time},
    "end":   {"dateTime": end_time},
    "attendees": ["mail@gmail.com"],
    }
    e = CAL.events().insert(calendarId="c_if5tihbg7n7a5k5261np66o514@group.calendar.google.com",sendNotifications=True, body=EVENTS).execute()

    print('''*** %r event added:
        Start: %s
        End:   %s''' % (e["summary"].encode("utf-8"),
            e["start"]["dateTime"], e["end"]["dateTime"]))


'''Displays next 7 days'''
def display_event():
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    elapsed = datetime.timedelta(days=7)
    then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'

    events_result = CAL.events().list(calendarId='c_if5tihbg7n7a5k5261np66o514@group.calendar.google.com', timeMax=then, timeMin=now,
                                            singleEvents=True,
                                            orderBy='startTime').execute()
    events = events_result.get('items', [])

    for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])

    # TODO add code to store data


'''
Deletes event by ID
'''
def cancel_event(eventID):
    CAL.events().delete(calendarId='primary', eventId=eventID).execute()


'''shows event name and id'''
def show_id():
    page_token = None
    now = datetime.datetime.utcnow().isoformat() + 'Z'

    while True:
        events = CAL.events().list(calendarId='primary',timeMin=now, pageToken=page_token).execute()
        for event in events['items']:
            print(event["summary"], event["id"])
        page_token = events.get('nextPageToken')
        if not page_token:
            break


# add_event("Recursion", "2020-11-14T09:00:00+02:00", "2020-11-14T11:00:00+02:00", "roderick@mail")
display_event()

# creating calendar??
# calendar = {
#     "summary": "Code Clinics",
#     "timeZone": "America/Los_Angeles"
# }

# created_calendar = CAL.calendars().insert(body=calendar).execute()
# print(created_calendar['id'])
