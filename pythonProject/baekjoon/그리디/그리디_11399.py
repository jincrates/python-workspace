# https://www.acmicpc.net/problem/11399

# n: 사람의 수
# p: 인출하는데 걸리는 시간
# result; 돈을 인출하는데 필요한 시간의 합
n = int(input()) # 사람 수
p = list(map(int, input().split())) # 인출하는데 걸리는 시간
result = [];
time = 0
p.sort()  # 낮은 순으로 정렬

for i in range(n):
    time += p[i];
    result.append(time)

print(result)
print(sum(result))



