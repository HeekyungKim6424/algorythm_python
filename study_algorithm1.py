#세 정수를 입력받아 최댓값 구하기
print('세 정수의 최댓값을 구합니다.')
a = int(input('정수 a의 값을 입력하세요.: '))
b = int(input('정수 b의 값을 입력하세요.: '))
c = int(input('정수 c의 값을 입력하세요.: '))

maximum = a
if b > maximum: maximum = b
if c > maximum: maximum = c
#maximum이라는 예약어가 따로 있는게 아니라 그냥 변수 이름을 저렇게 지어놓은것.
#그냥 thing으로 돌아갈껄?

print(f'최댓값은 {maximum}입니다.')

#이름을 받아 입력받아 인사하기
print('이름을 입력하세요.: ',end=' ')
name = input()
print(f'안녕하세요? {name} 님.')

#세 정수의 최댓값 구하기
def max3(a,b,c):
    """a,b,c의 최댓값을 구하여 반환""" #아마 함수를 입력할때 추가로 설명같은 란이 들어가는것 같다.
    maximum=a
    if b>maximum: maximum=b
    if c>maximum: maximum=c
    return maximum #최댓값 반환

print(f'max3(6,3,8)={max(6,3,8)}')
      
