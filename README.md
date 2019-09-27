# hiwoker
하이웍스 메신져 챗봇 서버 소스입니다. 

## Installation
```
pip install hiworker
```

## Usage

0. API Key 발급 [하이웍스 메신져](https://www.hiworks.com/cs/download)에서 APIKey를 받을 받을 수 있습니다.
<img src="./cb.png" width="300">


1. Guide 생성
```python
def makeBugGuide():
    guide = GuideToken('bug', '/버그')
    commandToken = UserCommandToken('bug', '%버그 발생 시점 및 현상%')
    commandToken.contentOnly = True

    guide.userCommandTokens = [commandToken]
    return guide
```

