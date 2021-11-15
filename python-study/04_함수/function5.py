def root(a, b, c): 
    r1 = (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)
    r2 = (-b - (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)

    return r1, r2  #쉼표 구분을 통해 여러 값을 반환

x = 2
y = -6
z = -8

r1, r2 = root(x, y, z) 
print('근은 {}와 {}입니다.'.format(r1, r2))


