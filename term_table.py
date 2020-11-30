# from terminaltables import AsciiTable, SingleTable, DoubleTable
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import json
from prettytable import PrettyTable


t = PrettyTable(['Date', 'Time', 'Event'])
code_calendar = build("calendar", "v3", credentials=creds)
now = datetime.datetime.utcnow().isoformat() + 'Z'
elapsed = datetime.timedelta(days=7)
then = (datetime.datetime.utcnow() + elapsed).isoformat() + 'Z'
events_result = code_calendar.events().list(calendarId=CAL_ID, timeMax=then, timeMin=now,
                                        singleEvents=True,
                                        orderBy='startTime').execut
events = events_result.get('items', [])
print(events)
for event in events:
    # print(even
    start = event['start'].get('dateTime', event['start'].get('date'))
    start = start.replace("T", " ").replace("+02:00", "")
    t.add_row([date, time, event['summary']])
    event_details.write(start + event['summary']+'\n')