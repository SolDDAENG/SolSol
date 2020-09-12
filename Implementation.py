# 구현(Implementation)
# 프로그래밍에서의 좌표계는 일반적인 대수학에서의 좌표계와 다른 의미를 가질 때가 많다.
# - 일반적으로 알고리즘 문제에서의 2차원 공간은 행렬(Matrix)의 의미로 사용된다.

for i in range(5):  # 행
    for j in range(5):  # 열
        print('(', i, ',', j, ')', end=' ')
    print()

# 완전 탐색 문제에서는 2차원 공간에서의 방향 벡터가 자주 활용된다.
# 동, 북, 서, 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# 현재 위치
x, y = 2, 2

for i in range(4):
    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    print(nx, ny)

# 문제1 : 시각 : 문제 설명  # 완전 탐색 유형 문제
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하세요.
# 예를 들어 1을 입력했을 때 다음은 3이 하나라도 포함되어 있으므로 세어야하는 시각입니다.
# - 00시 00분 03초
# - 00시 13분 30초
# 반면에 다음은 3이 하나라도 포함되어 있지 않으므로 세면 안 되는 시각입니다.
# - 00시 02분 55초
# - 01시 27분 45초

# 문제 조건
# 입력 조건 : 첫재 줄에 정수 N이 입력됩니다. (0 <= N <= 23)
# 출력조건 : 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 출력합니다.

# 문제 해결 아이디어
# 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다.
# 하루는 86,400초이므, 00시 00분 00초부터 23시 59분 59초까지의 모든 경우는 86,400가지 입니다.
# - 24 * 60 * 60 = 86,400
# 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
# 이러한 유형은 완전 탐색(Brute Forcing) 문제 유형이라고 불립니다.
# - 가능한 경우의 수를 모두 검사해보는 탐색 방법을 의미합니다.

# H 입력 받기
h = int(input())

count = 0
for i in range(h + 1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k):  # 시 분 초를 str로 묶어서 한번에 출력  # ex) 32020 이런식으로 출력
                count += 1

print(count)

# 문제2 : 상하좌우 : 문제 설명  # 시뮬레이션(Simulation) 유형
# 여행가 A는 N x N 크기의 정사각형 공간 위에 서 있습니다. 이 공간은 1 x 1 크기의 정사각형으로 나누어져 있습니다. 가장 왼쪽 위 좌표는 (1, 1)이며,
# 가장 오른쪽 아래 좌표는 (N, N)에 해당합니다. 여행가 A는 상, 하, 좌, 우 방향으로 이동할 수 있으며, 시작 좌표는 항상 (1, 1)입니다.  # ==> 좌표가 (1, 1)부터 시작하는지 (0, 0)부터 시작하는지 확인하기
# 우리 앞에는 여행가 A가 이동할 계획이 적힌 계획서가 놓여 있습니다.
# 계획서에는 하나의 줄에 띄어쓰기를 기준으로 하여 L, R, U, D중 하나의 문자가 반복적으로 적혀 있습니다. 각 문자의 의미는 다음과 같습니다.
# L : 왼쪽으로 한 칸 이동
# R : 오른쪽으로 한 칸 이동
# U : 위로 한 칸 이동
# D : 아래로 한 칸 이동

# 문제 설명
# 이때 여행가 A가 N x N 크기의 정사각형 공간을 벗어나는 움직임은 무시됩니다. 예를 들어 (1, 1)의 위치에서 L 혹은 U를 만나면 무시됩니다.

# 문제 조건
# 입력 조건 :
# - 첫째 줄에 공간의 크기를 나타내는 N이 주어집니다. (1 <= N <= 100)
# - 둘째 줄에 여행가 A가 이동할 계획서 내용이 주어집니다. (1 <= 이도 횟수 <= 100)

# 입력 예시
# 5
# R R R U D D

# 출력 조건 :
# - 첫째 줄에 여행가 A가 최종적으로 도착할 지점의 좌표 (X, Y)를 공백을 기준으로 구분하여 출력합니다.

# 출력 예시
# 3 4

# 문제 해결 아이디어
# 이 문제는 요구사항대로 충실히 구현하면 되는 문제입니다.

# N 입력 받기
n = int(input())
x, y = 1, 1
plans = input().split()

# L, R, U, D에 따른 이동 방향
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

# 이동 계획을 하나씩 확인하기
for plan in plans:
    # 이동 후 좌표 구하기
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
        # 공간을 벗어나는 경우 무시
        if nx < 1 or ny < 1 or nx > n or ny > n:
            continue
        # 이동 수행
        x, y = nx, ny

print(x, y)

# 문제3 : 문자열 재정렬 : 문제 설명
# 알파벤 대문자와 숫자(0 ~ 9)로만 구성된 문자열이 입력으로 주어집니다. 이때 모들 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 더한 값을 이어서 출력합니다.
# 예를 들어 K1KA5CB7이라는 값이 들어오면 ABCKK13을 출력합니다.

# 문제 조건
# 입력조건 : 첫째 줄에 하나의 문자열 S가 주어집니다. (1 <= S의 길이 <= 10,000)

# 입력 예시 1 : K1KA5CB7
# 입력 예시 2 : AJKDLSI412K4JSJ9D

# 출력 조건 :

# 출력 예시 1 : ABCKK13
# 출력 예시 2 : ADDIJJJKKLSS20

# 문제 해결 아이디어
# 요구사항대로 충실히 구현하면 되는 문제입니다.
# 문자열이 입력되었을 때 문자를 하나씩 확인합니다.
# - 숫자인 경우 따로 합계를 계산합니다.
# - 알파벳인 경우 별로의 리스트에 저장합니다.
# 결과적으로 리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답입니다.

data = input()
result = []
value = 0

# 문자를 하나씩 확인하며
for x in data:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():  # isalpha : 알파벳 확인
        result.append(x)
    # 숫자는 따로 떠하기
    else:
        value += int(x)

# 알파벳을 오름차순으로 정렬
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력
print(''.join(result))

# ----

arr = ['a', 'b', 'c']

# 'abc'

result1 = '/'.join(arr)
print(result1)