# 함수
# 더하기 함수 1
def add(a, b):
    return a + b


print(add(3, 7))


# 더하기 함수 2
def add(a, b):
    print('힘수의 결과 : ', a + b)


add(3, 7)


# 파라미터 지정하기
def add(a, b):
    return a + b


print(add(a=3, b=7))

# global 키워드
# global 키워드로 변수를 지정하면 해당 함수에서는 지역 변수를 만들지 않고,
# 함수 바깥에 선언된 변수를 바로 참조하게 된다.
a = 0


def func():
    global a
    a += 1


for i in range(10):
    func()

print(a)

a = [1, 2, 3]


def func():
    a[2] += 7
    a[1] = 7


func()
print(a)


# 여러 개의 반환 값
def operator(a, b):
    return a + b, a - b, a * b, a / b


a, b, c, d = operator(3, 7)
print(a, b, c, d)

# 람타 표현식
print((lambda a, b: a + b)(3, 5))

# 람다 표현식 예시 : 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]


def my_key(x):
    return x[1]


print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1]))  # 점수를 기준으로 오름찻순 정렬

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = list(map(lambda a, b: a + b, list1, list2))  # map : 각 원소에 어떤 함수를 적용할지 설정

print(result)
