# hiwoker
하이웍스 메신져 챗봇 서버 소스입니다. 메신져에서 API Key를 발급받은 후 사용하시면 하이웍스 메신져에 채팅 봇을 추가하여 만들 수 있습니다.

## Installation
```
pip install hiworker
```

## Usage

#### API Key 발급   
- [하이웍스 메신져](https://www.hiworks.com/cs/download)에서 APIKey를 받을 수 있습니다.
<img src="./cb.png" width="300">

#### API Key 등록 및 서버 생성
```python
server = hiworksBotServer('a4d83710-5905-465a-ae32-26d7eac9035c')
```

#### Guide 생성 - 컨텐트만 받는 경우
```python
def makeBugGuide():
    guide = GuideToken('bug', '/버그')
    commandToken = UserCommandToken('bug', '%버그 발생 시점 및 현상%')
    commandToken.contentOnly = True

    guide.userCommandTokens = [commandToken]
    return guide
```

#### Guide 생성 - 변수와 함께 받는 경우
```python
def makeBookGuide():
    guide = GuideToken('book', '/예약')
    commandToken = UserCommandToken('room', "%회의실명%")
    commandToken.allValues = ['S1','S2','S3','S4','S5','M','대 회의실']
    commandToken.canValues = ['S1','S2','S3']

    commandToken2 = UserCommandToken('time', "%예약할 시간%")
    commandToken2.allValues = ["09:00~09:30", "10:00~10:30","10:30~11:00"]
    commandToken2.canValues = ["09:00~09:30"]

    guide.userCommandTokens = [commandToken, commandToken2]
    return guide
```

#### Guide 등록
```python
server.setGuides(makeBugGuide())
```

#### Http Handler 등록
```python
server.addHandler('bug', bug)

def bug():
    print(request.json['key'])
    return '버그 접수 되었습니다.'
```

#### Sample
```python
from Hiworks import *

def makeBugGuide():
    guide = GuideToken('bug', '/버그')
    commandToken = UserCommandToken('bug', '%버그 발생 시점 및 현상%')
    commandToken.contentOnly = True

    guide.userCommandTokens = [commandToken]
    return guide
    
def makeGuides():
    guides = []
    guides.append(makeBugGuide())
    
    return guides

def run():
    server = hiworksBotServer('a4d83710-5905-465a-ae32-26d7eac9035c')
    server.setGuides(makeGuides())

    server.addHandler('bug', bug)
    server.run()

def bug():
    print(request.json['key'])
    return '버그 접수 되었습니다.'

run()
```

