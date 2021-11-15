# 딕셔너리와 반복문
seasons = ['봄', '여름', '가을', '겨울']

for season in seasons:
    print(season)


ages = {"Tod" : 35, "Jane" : 23, "Paul" : 62}
print(ages)

for key in ages.keys():
    print(key)

for value in ages.values():
    print(value)


# 딕셔너리는 순서와 상관없이 for문 진행
for key in ages.keys():  #.keys() 생략 가능
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

for key in ages:
    print('{}의 나이는 {}입니다.'.format(key, ages[key]))

for key, value in ages.items():
    print('{}의 나이는 {}입니다.'.format(key, value))
