# 로또 번호 일부를 받아서 최고 최저 순위 구하기

# 1순위: 6개 모두 일치
# 2순위: 5개 일치
# 3순위: 4개 일치
# 4순위: 3개 일치
# 5순위: 2개 일치
# 6순위(낙첨): 그 외

# 당첨 가능한 최고 순위
# 당첨 가능한 최저 순위

lottos = [0, 0, 0, 0, 0, 0]
win_nums = [31, 10, 45, 1, 6, 19]

max_rank = 1
min_rank = 6
same_count, zero_count = 0

for i in lottos:
    if i == 0:
        zero_count += 1

    for j in win_nums:
        if i == j:
            same_count += 1

# 0을 제외한 일치하는 개수로 최저 순위 구하기
if same_count == 6:
    min_rank = 1
elif same_count == 5:
    min_rank = 2
elif same_count == 4:
    min_rank = 3
elif same_count == 3:
    min_rank = 4
elif same_count == 2:
    min_rank = 5
else:
    min_rank = 6

# 0을 포함하는 개수로 최고 순위 구하기
same_count += zero_count

if same_count == 6:
    max_rank = 1
elif same_count == 5:
    max_rank = 2
elif same_count == 4:
    max_rank = 3
elif same_count == 3:
    max_rank = 4
elif same_count == 2:
    max_rank = 5
else:
    max_rank = 6

result = [max_rank, min_rank]

print(result)

# 작은 수 큰수 정렬해서 각각 숫자를 비교해서 일치하는 숫자의 갯수를 카운트하면 되지 않을까?
# 0이 몇 개인지가 중요