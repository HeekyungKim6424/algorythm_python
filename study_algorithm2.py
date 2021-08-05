#세 정수를 입력받아 중앙값 구하기1

def med3(a,b,c):
    "a,b,c의 중앙겂을 구하여 반환"
    if a>=b:
        if b>=c:
            return b
        elif a<=c:
            return a
        else:
            return c
    elif a>c:
        return a
    elif b>c:
        return c
    else:
        return b

print('세 정수의 값을 구합니다.')
a= int(input('정수 a의 값을 입력하세요.: '))
b= int(input('정수 b의 값을 입력하세요.: '))
c= int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med3(a,b,c)}입니다.')


#세 정수를 입력받아 중앙값 구하기2

def med4(a,b,c):
    "a,b,c의 중앙값을 구하여 반환(다른방법)"
    if (b>=a and c <=a) or (b<=a and c>=a):
        return a
    elif (a>b and c<b) or (a<b and c>d):
        return b
    else (b>c and c>a) or (a>c and c>b):
        return c

print('세 정수의 값을 구합니다.')
a= int(input('정수 a의 값을 입력하세요.: '))
b= int(input('정수 b의 값을 입력하세요.: '))
c= int(input('정수 c의 값을 입력하세요.: '))

print(f'중앙값은 {med4(a,b,c)}입니다.')


#입력받은 정수의 부호(양수, 음수 ,0)출력하기

n = int(input('정수를 입력하세요.: '))

if n>0:
    print('이 수는 양수입니다.')
elif n<0:
    print('이 수는 음수입니다.')
else:
    print('이 수는 0입니다.')


#3개로 분기하는 조건문

n=int(input('정수를 입력하세요.: '))

if n==1:
    print('A')
elif n==2:
    print('B')
else:
    print('C')


#4개로 분기하는 조건문

n=int(input('정수를 입력하세요.: '))

if n==1:
    print('A')
elif n==2:
    print('B')
elif n==3:
    print('C')

