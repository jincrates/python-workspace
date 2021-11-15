for i in [0, 1, 2, 3, 4]:
    print(i)

# 0부터 9까지
for i in range(10): 
    print(i)

names = ['철수', '영희', '바둑이', '귀도', '비단뱀']

for i in range(5):
    name = names[i]
    print('{}번: {}'.format(i + 1, name))

for i, name in enumerate(names):
    print('{}번: {}'.format(i + 1, name))

for i in range(11172):
    print(chr(44032 + i), end='')


rainbow=["빨","주","노","초","파","남","보"]
for i in range(len(rainbow)) :
    color = rainbow[i]
    print('{}번째 색은 {}'.format(i + 1, color))

for i,color in enumerate(rainbow):
    print('{}번째 색은 {}'.format(i + 1, color))

days = [31,29,31,30,31,30,31,31,30,31,30,31]
for i in range(len(days)):
    print('{}월의 날짜수는 {}일 입니다.'.format(i + 1, days[i]))