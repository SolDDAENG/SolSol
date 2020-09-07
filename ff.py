# 유용한 표준 라이브러리
# 내장함수
# itertools : 파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 라이브러리를 제공.
# heapq : 힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용.
# bisect : 이진 탐색(Binary Search) 기능을 제공하는 라이브러리.
# collections : 덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리.

# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval() : 중위 표기법. 입력이 들어왔을 때 실행한 결과를 반환  # 코테에서 많이 쓰인다.
result = eval('(3 + 5) * 7')
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4])
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True)
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 35), ('이순신', 75), ('아무개', 50)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합
# 순열 : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열하는것
#   {'A', 'B', 'C'}에서 세 개를 선택하여 나열하는 경우 : 'ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA'
from itertools import permutations

data = ['A', 'B', 'C']  # 데이터 준비

result = list(permutations(data, 3))  # 모든 순열 구하기
print(result)

# 조합 : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택하는 것
#   {'A', 'B', 'C'}에서 순서를 고려하지 않고 두 개를 뽑는 경우 : 'AB', 'AC', 'BC'
from itertools import combinations

data = ['A', 'B', 'C']  # 데이터 준비

result = list(combinations(data, 2))  # 2개를 뽑는 모든 조합 구하기
print(result)

# 중복 순열
from itertools import product

data = ['A', 'B', 'C']  # 데이터 준비

result = list(product(data, repeat=2))  # 2개를 뽑는 모든 순열 구하기 (중복 허용)
print(result)

# 증복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']  # 데이터 준비

result = list(combinations_with_replacement(data, 2))  # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
