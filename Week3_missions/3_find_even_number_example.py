def find_even_number(n, m):
    # n과 m 사이의 숫자 리스트 만들기
    numbers = [ i for i in range(n, m+1) ]
    for i in numbers:
        # 2로 나눠서 나머지가 없으면 짝수
        if i % 2 == 0:
            print(f"{i} 짝수")
        # n+m를 2로 나누면 중앙값
        if i % 2 == 0 and (n+m) // 2 == i:
            print(f"{i} 중앙값")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
find_even_number(n, m)