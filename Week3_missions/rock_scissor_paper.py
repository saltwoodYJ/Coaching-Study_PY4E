import random

def printcmp(computer) :
  if computer == 0 :
    print("컴퓨터 : 가위")
  elif computer == 1 :
    print("컴퓨터 : 바위")
  elif computer == 2 : 
    print("컴퓨터 : 보")

def rcp(my):
  computer = random.randint(0, 2) # 0 : 가위 1 : 바위 2 : 보
  printcmp(computer)
  
  if my == '가위' :
    myint = 0
  elif my == '바위' :
    myint = 1
  elif my == '보' :
    myint = 2;
  
  if myint == computer : #무승부 처리
    my = input("무승부입니다. 다시입력하세요")
    rcp(my)

  elif myint == 0: #내가 가위
    if computer == 2 : #컴퓨터가 보
      print("내가 승리!")
    else :  #컴퓨터가 바위
      print("컴퓨터가 승리!")
  elif myint == 1: #내가 바위
    if computer == 0 : #컴퓨터가 가위
      print("내가 승리!")
    else : #컴퓨터가 보
      print("컴퓨터가 승리!")
  elif myint == 2: #내가 보
    if computer == 1 : #컴퓨터가 바위
      print("내가 승리!")
    else : #컴퓨터가 가위
      print("컴퓨터가 승리!")

my = input("가위 바위 보")
rcp(my)