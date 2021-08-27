def make_comma(number) :
  answer = ""
  strnum = str(number) 
  strlen = len(strnum)
  comma = strlen % 3 # 콤마를 시작할 자릿수 계산
  if comma == 0 : # 나누어 떨어질경우 첫자리 콤마 제외
    comma = 3

  index = 0 # 문자열 탐색할 인덱스
  for x in strnum :
    if(index == comma) : 
      answer = answer + ',' # 콤마 추가
      comma = comma + 3 # 콤마 갱신
    index = index + 1 # 인덱스 갱신
    answer = answer + x # 숫자 추가
  print(answer) # 숫자 출력


###################test###################
print("########test#########")
test = 1
while test <= 1000000000000000000 :
  make_comma(test)
  print(f"{test:,}")
  test = test * 10
print("########test#########")
###################test###################