#1부터 n까지 정수의 합 구하기(while문)

print('1부터 n까지 정수의 합을 구합니다.')
n= int(input('n값을 입력하세요: '))

sum=0
i=1

while i<=n: #i가 n보다 작거나 같은 동안 반복
    sum +=i #sum에 i를 더함
    i +=1 #i에 1을 더함

print(f'1부터 {n}까지의 정수의 합은 {sum}입니다.')


#1부터 n까지 정수의 합 구하기2(for문)

print('1부터 n까지 정수의 합을 구합니다,')
n= int(input('n값을 입력하세요.: '))

sum=0
for i in range(1,n+1):
    sum+=i

print(f'1부터 {n}까지 정수의 합은 {sum}입니다.')


#a부터 b까지 정수의 합 구하기(for문)

print('a부터 b까찌 정수의 합을 구합니다.')
a=int(input('정수 a를 입력하세요: '))
b=int(input('정수 b를 입력하세요: '))

if a>b:
    a,b=b,a

sum=0
for i in range(a,b+1):
    sum +=i

print(f'{a}부터 {b}까찌 정수의 합은 {sum} 입니다.')
