def find_even_number(n, m) :
  numbers = [ i for i in range(n,m+1)]
  for i in numbers :
    if i % 2 == 0 :
      print(str(i) + " 짝수")
      if i == (n + m) / 2  :
        print(str(i) + " 중앙값")

flag = 1 
while flag :
  n = int(input("첫 번째 수 입력 : "))
  m = int(input("두 번째 수 입력 : "))
  if n <= m : # 숫자 범위가 맞으면 flag 0으로 설정후 반복문 탈출
    flag = 0
  else : # 숫자 범위가 오류났으면 에러메세지 출력후 while문 반복
    print("숫자의 범위가 잘못됐습니다. 다시 입력해주세요")
find_even_number(n, m)