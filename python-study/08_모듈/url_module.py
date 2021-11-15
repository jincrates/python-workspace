# 모듈: 미리 만들어진 코드를 가져와 쓰는 방법
# import <모듈 이름>
def get_web(url):
    """URL을 넣으면 페이지 내용을 올려주는 함수"""
    import urllib.request
    response = urllib.request.urlopen(url)
    data = response.read()
    decoded = data.decode('utf-8')
    return decoded

url = input('웹 페이지 주소? ') #https://example.com/
content = get_web(url)
print(content)


import math
print("파이의 값은 {}입니다.".format(math.pi))