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

SCOPES = ["https://www.googleapis.com/auth/calendar"]
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


'''adds event'''
# e = CAL.events().insert(calendarId="primary",sendNotifications=True, body=EVENT).execute()
# print('''*** %r event added:
#     Start: %s
#     End:   %s''' % (e["summary"].encode("utf-8"),
#         e["start"]["dateTime"], e["end"]["dateTime"]))


'''displays next 10 events'''
# now = datetime.datetime.utcnow().isoformat() + 'Z'
# events_result = CAL.events().list(calendarId='primary', timeMin=now,
#                                         maxResults=10, singleEvents=True,
#                                         orderBy='startTime').execute()
# events = events_result.get('items', [])

# for event in events:
#         start = event['start'].get('dateTime', event['start'].get('date'))
#         print(start, event['summary'])


'''deletes event by ID // more options, troubleshoot info'''
# CAL.events().delete(calendarId='primary', eventId='am94eme402tr17aokvba3nnlo4').execute()


'''shows event name and id'''
page_token = None
while True:
  events = CAL.events().list(calendarId='primary', pageToken=page_token).execute()
  for event in events['items']:
    print(event["summary"], event["id"])
  page_token = events.get('nextPageToken')
  if not page_token:
    break