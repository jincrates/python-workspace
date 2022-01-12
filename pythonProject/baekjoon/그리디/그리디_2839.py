# sugar: 배달해야하는 설탕 무게
# kg: 봉지 무게 단위 3, 5
# bag: 배달에 필요한 최소 봉지수(딱 나누어 떨어지지 않으면 -1)

sugar = int(input())

bag = 0

while sugar >= 0:
    if sugar % 5 == 0: # 5의 배수면
        bag += (sugar // 5)
        print(bag)
        break

    sugar -= 3
    bag += 1
else:
    print(-1)