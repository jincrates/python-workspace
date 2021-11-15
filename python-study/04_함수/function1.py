#3
def print_sqrt():
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    
    print('해는 {} 또는 {}'.format(r1, r2))


#5
def print_root(a, b, c): #매개변수(parameter): 정의해서 사용하는 이름
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    print('해는 {} 또는 {}'.format(r1, r2))


#1
a = 1 
b = 2
c = -8

# a * x^2 + b * x + c = 0, a != 0인 x에 관한 2차 방정식에 대해,
# 근의 공식은
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는 {} 또는 {}'.format(r1, r2))


#2
a = 2 
b = -6
c = -8

# 한 번 더 구하려면
r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

print('해는 {} 또는 {}'.format(r1, r2))


#4
a = 2
b = -6
c = -8
print_sqrt()


#6
x = 2
y = -6
z = -8
print_root(x, y, z)  #실행인자(argument): 실행할 때 넘기는 값


#7
def print_round(number):
    rounded = round(number)
    print(rounded)

print_round(4.6)
print_round(2.2)
print_round(3.7)