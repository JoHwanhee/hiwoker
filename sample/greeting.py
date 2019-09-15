from Hiworks import *

def run():
    guides = []
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
    guides.append(guide)

    server = hiworksBotServer('')
    server.setGuides(guides)

    server.addHandler('book', book)
    server.run()

def book():
    print(request.json['key'])
    return 'ok'

run()