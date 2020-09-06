# 조건문과 반복문
x = 15

if x > 7:
    print(x)
    print('출력 완료')

print('조건문 끝')

score = 85

if score >= 90:
    print('학점 : A')
elif score >= 80:
    print('학점 : B')
elif score >= 70:
    print('학점 : C')
else:
    print('학점 F')


score = 80

if score >= 70:
    print('성적이 70점 이상입니다.')
    if score >= 90:
        print('우수한 성적입니다.')

else:
    print('성적이 70점 미만입니다.')
    print('조금 더 분발하세요')

print('프로그램을 종료합니다.')

# 비교 연산자
a = 5
print(a == 5)

# 논리 연산자
a = 10

if 0 <= a and a <= 10:
    print('a는 0 이상 10 이하 입니다,')
