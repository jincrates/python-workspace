list1 = ['가위', '바위', '보']
list2 = [37, 23, 10, 33, 29, 40]

print(list1)
print(list2)

print(list1[0])
print(list1[1])
print(list1[2])

list1[0] = '바위'
print(list1[0])
print(list1)
print(list1[-1])
print(list1[-2])


rainbow=['빨강','주황','노랑','초록','파랑','남색','보라']
#rainbow를 이용해서 last_color에 값을 저장하세요
last_color = rainbow[-1]
print('무지개의 마지막 색은 {}이다'.format(last_color) )