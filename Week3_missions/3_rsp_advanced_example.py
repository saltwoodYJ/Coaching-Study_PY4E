import random

def rsp_advanced(games):

    # 전적 기록 판
    my_win, my_lose = 0, 0
    computer_win, computer_lose = 0, 0
    draw = 0

    for i in range(games):

        while True:
            my = input("가위 바위 보 : ")
            if my not in ["0", "1", "2", "가위", "바위", "보"]:
                print("똑바로 내세요!")
                continue
            else:
                break
        
        # 나의 입력이 숫자로 들어오면 한글로 바꿔줌
        if my == "0":
            my = "가위"
        elif my == "1":
            my = "바위"
        elif my == "2":
            my = "보"
        
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
            print(f"{i+1} 번째 판 비김!")
            draw += 1 # draw = draw + 1
        # 비기는 것을 제외하고 가위바위보 경우의 수 비교
        elif my == "가위" and computer == "바위":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 컴퓨터 승리!")
            computer_win += 1
            my_lose += 1
        elif my == "가위" and computer == "보":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 나의 승리!")
            computer_lose += 1
            my_win += 1
        elif my == "바위" and computer == "가위":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 나의 승리!")
            computer_lose += 1
            my_win += 1
        elif my == "바위" and computer == "보":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 컴퓨터 승리!")
            computer_win += 1
            my_lose += 1
        elif my == "보" and computer == "가위":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 컴퓨터 승리!")
            computer_win += 1
            my_lose += 1
        elif my == "보" and computer == "바위":
            print(f"나: {my}")
            print(f"컴퓨터: {computer}")
            print(f"{i+1} 번째 판 나의 승리!")
            computer_lose += 1
            my_win += 1
        # 칸 띄우기 용 공백 프린트    
        print()

    print()
    print(f"나의 전적: {my_win}승 {draw}무 {my_lose}패")
    print(f"컴퓨터의 전적: {computer_win}승 {draw}무 {computer_lose}패")

# 몇 판을 진행 할 것인가?
games = int(input("몇 판을 진행하시겠습니까? : "))
rsp_advanced(games)