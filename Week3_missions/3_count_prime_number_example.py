def count_prime_number(n, m):
    # n 이 반드시 더 작아야함
    count = 0
    for i in range(n, m):
        not_prime = 0
        if i < 2:
            continue
        
        for j in range(2, i):
            if i % j == 0:
                not_prime +=1
        if not_prime == 0:
            count +=1
            # 소수 출력
            # print(i)
            
    print(f"소수개수 {count}")

n = int(input("첫 번째 수 입력 : "))
m = int(input("두 번째 수 입력 : "))
count_prime_number(n, m)