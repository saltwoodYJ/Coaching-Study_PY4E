def timetable(time) :
  multiply = 1;
  while multiply < 10 :
    if time * multiply <= 50 : # 두번째 조건, 값이 50이하인 것만 출력
      print(str(time) + " X " + str(multiply) + " = " + str(time * multiply))
    multiply = multiply + 2 # 첫번째 조건, 1 부터 2씩 더해 홀수번만 연산하도록

flag = 1
while flag :
  time = int(input("몇 단? :"))
  if 0 < time or time < 10 : # 숫자 범위가 맞으면 flag 0으로 설정후 반복문 탈출
    flag = 0;
  else : # 숫자 범위가 오류났으면 에러메세지 출력후 while문 반복
    print("구구단 숫자를 잘못 입력하셨습니다. 다시 입력해주세요")
    
timetable(time)