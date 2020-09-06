# 문자열 자료형
data = 'Hello World'
print(data)

data = "Don't you know \"Python\"?"
print(data)

a = "Hello"
b = "World"
print(a + ' ' + b)

a = 'String'
print(a * 3)

a = "ABCDEF"
print(a[2: 5])

# 사전 자료형
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

a = dict()
a['사과'] = 'Apple'
a['바나나'] = 'Banana'

print(a)

print(a.keys())
print(a.values())

print(list(a.keys()))
print(list(a.values()))

# 집합 자료형
# 중복을 허용하지 않고 순서가 없다. ==> 인덱싱을 사용할 수 없다.

# 집합 자료형 초기화 방법1
data = set([1, 1, 2, 3, 4, 4, 5])
print(data)

# 집합 자료형 초기화 방법2
data = {1, 1, 2, 3, 4, 4, 5}
print(data)

a = {1, 2, 3}

a.add(3)

print(a)
print(1 in a)

# 리스트나 튜플 같은 경우 데이터의 갯수만큼 복잡도가 필요하다.
a = [1, 2, 3, 4, 5, 6]
print(3 in a)

a = {1, 2, 3, 4, 5, 6}
print(3 in a)

# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])

# 합집합
print((a | b))

# 교집합
print(a & b)

# 차집합
print(a - b)

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

# 새로운 원소 추가
data.add(4)
print(data)

data.update([5, 6])
print(data)

# 특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)

a = ['H', 'e', 'l', 'l', 'o']

print(set(a))
