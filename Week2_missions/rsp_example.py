import random

# 가위 바위 보 게임
def rsp(my):

    # 나의 입력이 숫자로 들어오면 한글로 바꿔줌
    if my == "0":
        my = "가위"
    elif my == "1":
        my = "바위"
    else:
        my =="보"

    computer = random.randint(0, 2)
    # 컴퓨터는 한글을 모르기 때문에 숫자를 한글로 바꿔줌
    if computer == 0:
        computer = "가위"
    elif computer == 1:
        computer = "바위"
    else:
        computer ="보"

    # 가위 바위 보 대결
    # 같은 것을 내면 비김
    if my == computer:
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("비김!")
    # 비기는 것을 제외하고 가위바위보 경우의 수 비교
    elif my == "가위" and computer == "바위":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("컴퓨터 승리!")
    elif my == "가위" and computer == "보":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("나의 승리!")
    elif my == "바위" and computer == "가위":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("나의 승리!")
    elif my == "바위" and computer == "보":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("컴퓨터 승리!")
    elif my == "보" and computer == "가위":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("컴퓨터 승리!")
    elif my == "보" and computer == "바위":
        print(f"나: {my}")
        print(f"컴퓨터: {computer}")
        print("나의 승리!")
    
my = input("가위 바위 보 : ")
rsp(my)