from __future__ import print_function
from Hiworks import *
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

def addGoogleEvent(startTime, endTime, title):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

    today = datetime.date.today().strftime('%Y-%m-%d')
    event = {
    'summary': title,
    'location': 'Test',
    'description': title,
    'start': {
        'dateTime': '%sT%s:00+09:00' % (today, startTime),
        'timeZone': 'Asia/Seoul',
    },
    'end': {
        'dateTime': '%sT%s:00+09:00' % (today, endTime),
        'timeZone': 'Asia/Seoul',
    },
    'recurrence': [
        'RRULE:FREQ=DAILY;COUNT=1'
    ],
    'attendees': [
    ],
    'reminders': {
        # 'useDefault': False,
        # 'overrides': [
        # {'method': 'email', 'minutes': 24 * 60},
        # {'method': 'popup', 'minutes': 10},
        # ],
    },
    }

    event = service.events().insert(calendarId='primary', body=event).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

def makeBook():
    guide = GuideToken('book', '/예약')
    commandToken = UserCommandToken('room', "%회의실명%")
    commandToken.allValues = ['S1','S2','S3','S4','S5','M','대 회의실']
    commandToken.canValues = ['S1','S2','S3']

    s1Token = UserCommandToken('time', "%예약할 시간%")
    s1Token.canValues = ["09:00-09:30", "09:30-10:00","10:00-10:30"]   

    guide.userCommandTokens = [commandToken, s1Token]
    return guide;

def makeVote():
    guide = GuideToken('voat', '/투표')
    commandToken = UserCommandToken('voat1', "%질문%")
    commandToken.contentOnly = True

    commandToken2 = UserCommandToken('voat2', "%후보1%")
    commandToken2.contentOnly = True

    commandToken3 = UserCommandToken('voat3', "%후보2%")
    commandToken3.contentOnly = True

    guide.userCommandTokens = [commandToken, commandToken2, commandToken3]

    return guide

def makeNotice():
    guide = GuideToken('notice', '/공지')
    commandToken = UserCommandToken('notice', "%공지할 내용%")
    commandToken.contentOnly = True

    guide.userCommandTokens = [commandToken]

    return guide

def makeBug():
    guide = GuideToken('bug', '/버그')
    commandToken = UserCommandToken('file', "%버그 발생 시점 및 현상%")
    commandToken.contentOnly = True
    guide.userCommandTokens = [commandToken]

    return guide

def run():
    guides = []
    

    guides.append(makeBook())
    guides.append(makeBug())
    guides.append(makeVote())
    guides.append(makeNotice())


    server = hiworksBotServer('dd7942ff-bd6a-4cdc-b367-7261a0f78e17')
    server.setGuides(guides)

    server.addHandler('book', book)
    server.addHandler('bug', bug)
    server.addHandler('voat', voat)
    server.addHandler('notice', notice)
    server.run()
    
def book():
    print(request.json)
    try:
        userCommandTokens = request.json['userCommandTokens']
        room = ''
        time = ''
        for token in userCommandTokens:
            if token['key'] == 'room':
                room = token['value']
            elif token['key'] == 'time':
                time = token['value']
        message = time.split('(')[0]
        times = message.split('-')
        startTime = times[0]
        endTime = times[1]
        addGoogleEvent(startTime, endTime, room)

        return '#BOT;clock;ok;예약이 완료 되었습니다.;미팅룸 ' + room + ' ' + startTime + '-' + endTime
    except:
        return '#BOT;exclamation-circle;fail;정확한 회의실 장소와 시각을 입력해주세요.'


def bug():
    print(request.json)

    return '#BOT;bug;ok;버그 리포팅이 완료 되었습니다.'

def voat():
    print(request.json)

    return '#BOT;poll-h;ok;투표 등록 되었습니다.'

def notice():
    print(request.json)

    return '#BOT;exclamation-circle;ok;공지 등록 되었습니다.'

run()
