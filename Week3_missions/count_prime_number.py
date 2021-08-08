def isPrime (num) :
  devide = 2
  while devide < num : # 2부터 num - 1 까지 나누기
    if num % devide == 0 : # 나누어떨어진다면 반복문 탈출
      break
    devide = devide + 1
  if devide == num : # 현재 devide가 num과 같다면 소수판정, 1반환
    return 1
  else : # 소수가 아니라면 0반환
    return 0

def count_prime_number(n, m) :
  numbers = [ i for i in range(n,m+1)]
  count = 0
  for i in numbers :
    if isPrime(i) : # 소수가 맞다면(반환값) 카운트
      count = count + 1 
  print("소수개수 " + str(count))

flag = 1 
while flag :
  n = int(input("첫 번째 수 입력 : "))
  m = int(input("두 번째 수 입력 : "))
  if n <= m : # 숫자 범위가 맞으면 flag 0으로 설정후 반복문 탈출
    flag = 0
  else : # 숫자 범위가 오류났으면 에러메세지 출력후 while문 반복
    print("숫자의 범위가 잘못됐습니다. 다시 입력해주세요")

count_prime_number(n, m)