# 그리디 알고리즘(탐욕법) : 현재 상황에서 지금 당장 좋은 것만 고르는 방법
# 일반적인 그리디 알고리즘은 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 그리디 해법은 그 정당성 분석이 중요
# - 단순히 가장 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토해야한다.
# 상당수 그리디 문제는 탐욕법으로 얻은 해가 최적의 해라는 것을 추론할 수 있어야 풀리도록 출제된다.

# 문제1 : 거스름 돈 : 문제 설명
# 당신은 음식점의 계산을 도워주는 점원입니다. 카운터에서는 거스름돈으로 사용할 500원, 100원, 50원, 10원짜리 동전이 무한히 존재한다고 가정합니다.
# 손님에게 거슬러 주어야 할 돈이 N원일 때 거슬러 주어야 할 동전의 최소 개수를 구하세요. 단, 거슬러 줘야 할 돈 N은 항상 10의 배수입니다.

n = 1260
count = 0

# 큰 단위의 화폐부터 차례대로 확인하기
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin
#     몫을 구할 땐 //
#     나머지를 구할 땐 %

print(count)

# 문제2 : 1이 될때 까지
# 어떠한 수 N이 1이 될 때 까지 다음의 두 과정 중 하나를 반복적으로 선택하여 수행하려고 합니다.
# 단, 두 번째 연산은 N이 K로 나누어 떨어질 때만 선택할 수 있습니다.
# 1. N에서 1을 뺍니다.
# 2. N을 K로 나눕니다.

# 문제 해결 아이디어
# 주어진 N에 대하여 최대한 많이 나누기를 수행하면 된다.
# N의 값을 줄일 때 2 이상의 수로 나누는 작업이 1을 빼는 작업보다 수를 훨씬 많이 줄일 수 있다.

# 정당성 분석
# 가능하면 최대한 많이 나누는 작업이 최적의 해를 항상 보장할 수 있는가?
# N이 아무리 큰 수여도, K로 계속 나눈다면 기하급수적으로 빠르게 줄일 수 있다.
# 다시 말해 K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있다.
# 또한 N은 항상 1에 도달하게 된다. (최적의 해 성립)
# N, K공백을 기준으로 구분하여 입력 받기

n, k = map(int, input().split())
result = 0

while True:
    # N이 K로 나누어 떨어지는 수가 될 때 까지만 1씩 빼기
    target = (n // k) * k  # n을 k로 나눈 몫에다 다시 k를 곱해줌으로써 target이 항상 k의 배수가 되도록 한다.
    result += (n - target)
    n = target
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # K로 나누기
    result += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)

# 문제3 : 곱하기 혹은 더하기 : 문제 설명
# 각 자리가 숫자(0부터 9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며
# 숫자 사이에 'x' 혹은 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요.
# 단, +보다 x를 먼저 계산하는 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정합니다.
# 예를 들어 02984라는 문자열로 만들 수 있는 가장 큰 수는 ((((0 + 2) x 9) x 8) x 4) = 576 입니다.

# 문제 해결 아이디어
# 대부분의 경우 '+'보다는 'x'가 더 값을 크게 만든다.
# 다만 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기를 수행하는 것이 효율적.
# 따라서 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하며, 두 수가 모두 2 이상인 경우에는 곱하면 정답이다.

data = input()

# 첫 번째 문자를 순자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
