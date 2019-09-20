from Hiworks import *

def makeBugGuide():
    guide = GuideToken('bug', '/버그')
    commandToken = UserCommandToken('bug', '%버그 발생 시점 및 현상%')
    commandToken.contentOnly = True

    guide.userCommandTokens = [commandToken]
    return guide

def makeBookGuide():
    guide = GuideToken('book', '/예약')
    commandToken = UserCommandToken('room', "%회의실명%")
    commandToken.allValues = ['S1','S2','S3','S4','S5','M','대 회의실']
    commandToken.canValues = ['S1','S2','S3']

    s1Token = UserCommandToken('time_1', "%예약할 시간%")
    s1Token.containsKey = 'room'
    s1Token.containsValue = 'S1'
    s1Token.allValues = ["09:00~09:30", "10:00~10:30","10:30~11:00"]
    s1Token.canValues = ["09:00~09:30"]

    s2Token = UserCommandToken('time_2', "%예약할 시간%")
    s2Token.containsKey = 'room'
    s2Token.containsValue = 'S2'
    s2Token.allValues = ["09:00~09:30", "10:00~10:30","10:30~11:00"]
    s2Token.canValues = ["09:00~09:30", "10:00~10:30","10:30~11:00"]

    s3Token = UserCommandToken('time_3', "%예약할 시간%")
    s3Token.containsKey = 'room'
    s3Token.containsValue = 'S3'
    s3Token.allValues = ["09:00~09:30", "10:00~10:30","10:30~11:00"]
    s3Token.canValues = ["09:00~09:30", "10:30~11:00"]

    guide.userCommandTokens = [commandToken, s1Token, s2Token, s3Token]
    return guide

def makeVoteGuide():
    guide = GuideToken('vote', '/투표')
    commandToken = UserCommandToken('room', "%[질문]%")
    commandToken.contentOnly = True

    s1Token = UserCommandToken('time_1', "%후보%")
    s1Token.contentOnly = True

    guide.userCommandTokens = [commandToken, s1Token]
    return guide

def makeNoticeGuide():
    guide = GuideToken('notice', '/공지')
    commandToken = UserCommandToken('notice', "%공지할내용%")
    commandToken.contentOnly = True
    
    guide.userCommandTokens = [commandToken]
    return guide

def makeGuides():
    guides = []
    guides.append(makeBugGuide())
    guides.append(makeBookGuide())
    guides.append(makeVoteGuide())
    guides.append(makeBookGuide())

    return guides

def run():
    server = hiworksBotServer('')
    server.setGuides(makeGuides())

    server.addHandler('book', book)
    server.addHandler('bug', bug)
    server.addHandler('vote', vote)
    server.addHandler('notice', notice)
    server.run()

def book():
    print(request.json['key'])
    return '예약 되었습니다!!!'
def bug():
    print(request.json['key'])
    return '버그 접수 되었습니다.'
def vote():
    print(request.json['key'])
    return '투표 기능은 개발즁입니다..'
def notice():
    print(request.json['key'])
    return '공지 기능은개발중입니다..'

run()