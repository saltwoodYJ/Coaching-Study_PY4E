import random 

def bs31():
  print("wefwef")
  number = 0
  flag = 0
  while flag == 0 :
    my = input("My turn - 숫자를 입력하세요: ")
    answer = my.split()

    count = 0
    now_number = number
    for x in answer :
      count = count + 1
      next_number = now_number + 1
      if count == 4 or int(x) != next_number :
        print("잘못 입력하셨습니다. 다시 입력해주세요.")
        now_number = number
        break
      else : 
        now_number = int(x)
        flag = 1
  number = now_number

  computer_turn_num = random.randint(1,3)
  number = number +
  print(f"현재 숫자 : {now_number}")

bs31()