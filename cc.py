# 기본 입출력
a = [1, 2, 3]
a.append(0)  # append는 맨 뒤에 붙는다.
print(a)

a = {1, 2, 3}
a.add(0)
print(a)

# 자주 사용되는 표준 입력 방법
# input() : 한 줄의 문자열을 입력 받는 함수.
# map() : 리스트의 모든 원소에 각각 특정한 함수를 적용할 때 사용.

# 데이터의 개수 입력
# 입력 : 1 2 3 4 5
# input().split() : ['1', '2', '3', '4', '5']
# map(int, input().split()): map([1, 2, 3, 4, 5])

a = list(map(int, input().split()))

print(a)

# 데이터의 개수 입력
n = list(input())
# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

print(n)
print(data)

'''
3
4
0 0 0 0
0 0 0 0
0 0 0 0
'''
n = int(input())
m = int(input())

arr = []
for i in range(n):
    arr.append((list(map(int, input().split()))))

# 빠르게 입력 받기
import sys

data = sys.stdin.readline().rstrip()
print(data)

# print() 줄 안바꾸고 출력하기
print(8, end=' ')
print(10)

# 출력을 위한 전형적인 소스코드
# 출력할 변수들
a = 7
print('정답은 ' + str(a))  # str(a)를 하지 않고 그냥 a를 출력하면 에러가 발생한다.
