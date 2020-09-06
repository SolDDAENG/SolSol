array = [i for i in range(100)]

print(array)

# 0부터 19까지의 수 중에서 홀수만 포함하는 리스트
aa1 = [i for i in range(20) if i % 2 == 1]
print(aa1)

aa2 = []
for i in range(20):
    if i % 2 == 1:
        aa2.append(i)
print(aa2)

# 1부터 9까지의 수들의 제곱 값을 포함하는 리스트
bb = [i * i for i in range(1, 10)]
print(bb)

# N * M 크기의 2차원 리스트 초기화
n = 4
m = 3
array = [[0] * m for _ in range(n)]
print(array)

# N * M 크기의 2차원 리스트 초기화 (잘못된 방법)
n = 4
m = 3
array = [[0] * m] * n
print(array)

array[1][1] = 5
print(array)