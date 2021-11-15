list2 = [37, 23, 10, 33, 29, 40]
print(list2)

#list2.append(16)
#print(list2)

#새로운 리스트를 만들어 낸다.
list3 = list2 + [16]
print(list3)


list4 = list2 + list3
print(list4)

n = 12
ownership = n in list3  #리스트에 해당 값이 있는지 확인 in
print(ownership)

n = 10
if n in list3:
    print('{}은 있어!'.format(n))

print(list4)
del(list4[12]) #리스트의 12번째 값을 지워라

print(list4)
list4.remove(40) #리스트에 40이라는 값이 있는 경우 삭제, 여러개의 경우 가장 앞에 있는 하나만 지워짐

print(list4)