def gugudan(number):
    n = 1
    print(f"{number} 단")
    # 구구단은 9까지만
    while n <= 9:
        # 홀수 번째이면서 값이 50보다 작은 수 찾기
        if n % 2 != 0 and number * n <= 50:
            print(f"{number} X {n} = {number * n}")
        # 9를 넘어가면 반복문을 탈출하도록 하는 코드
        n += 1 

number = int(input("몇 단? : "))
gugudan(number)