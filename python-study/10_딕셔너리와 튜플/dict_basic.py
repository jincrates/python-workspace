# Dictionary
# 여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능

# List는 삭제시 순서가 바뀌기 때문에 인덱스에 대한 값이 바뀐다.
# Dictionary는 key로 값을 가져오기 때문에 삭제 여부와 상관없다.
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}
#print(wintable['가위'])

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'
    
result = rsp('가위', '바위')
print(result)

messages = {
    'win':'이겼다!',
    'draw': '비겼네.',
    'lose': '졌어...'
}

print(messages[result])


# 이름표는 문자열 또는 숫자를 주로 사용하지만
# 값은 리스트를 포함해서 무엇이든 올 수 있습니다.
dict = {"이름표" : [1,2,3]}

print(dict["이름표"])


#전부 삭제
list.clear()
dict.clear()


def check_and_clear(box):
    if "불량품" in box.keys():
        box.clear()
        print("불량품이 있으면 box를 clear합니다.")
    else :
        print(box)

box1 = {"불량품" : 10}
check_and_clear(box1)
# {}가 출력되어야합니다.
print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
# {"정상품": 10}가 출력되어야합니다.
print(box2)