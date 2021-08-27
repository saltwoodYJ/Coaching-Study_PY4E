################
#a = "500629-2222222"
#check_id(a)
#50년06월 여자

#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o
#잘못된 번호입니다.
#올바른 번호를 넣어주세요

#a = "000629-2222222"
#check_id(a)
#2000년 이후 출생자 입니까? 맞으면 o 아니면 x : x
#00년06월 여자
####################

def check_id(a) :
  birth_date = a.split("-")[0]
  random_number = a.split("-")[1]
  sex = "none"
  if birth_date[0] == '0' or birth_date[1] == '1' :
    century = input("2000년 이후 출생자 입니까? 맞으면 o 아니면 x : o")
    if century == "o" :
      if random_number[0] == '3' :
        sex = "남자"
      elif random_number[0] == "4" :
        sex = "여자"
  else :
    if random_number[0] == '1' :
      sex = "남자"
    if random_number[1] == '2' :
      sex = "여자"

  if sex == "none" :
    print("잘못된 번호입니다.")
    print("올바른 번호를 넣어주세요")
    return
  else :
    print(f"{birth_date[0]}{birth_date[1]}년 {birth_date[2]}{birth_date[3]}월 {sex}")

a = input("주민등록번호를 '-'로 구분지어서 입력해주세요")
check_id(a)