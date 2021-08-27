# 버스요금 계산기
def calculate_bus_fare(age, types):

    if types == "현금":
        if age < 8:
            bus_fare = 0
        elif age >= 8 and age < 14:
            bus_fare = 450 
        elif age >= 14 and age < 20:
            bus_fare = 1000
        elif age >= 20 and age < 75:
            bus_fare = 1300
        elif age >= 75:
            bus_fare = 0
    elif types == "카드":
        if age < 8:
            bus_fare = 0
        elif age >= 8 and age < 14:
            bus_fare = 450 
        elif age >= 14 and age < 20:
            bus_fare = 720
        elif age >= 20 and age < 75:
            bus_fare = 1200
        elif age >= 75:
            bus_fare = 0
    
    if bus_fare == 0:
        bus_fare = "무료"
    
    print(f"나이: {age}세")
    print(f"지불유형: {types}")
    print(f"버스요금: {bus_fare}")

age = int(input("나이 입력: "))
types = input("지불유형 입력: ")
calculate_bus_fare(age, types)