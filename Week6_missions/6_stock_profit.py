member_names = ["갑돌이", "갑순이", "을돌이", "을순이", "병돌이", "병순이"]
member_records = [[4,5,3,5,6,5,3,4,1,3,4,5],[2,3,4,3,1,2,0,3,2,5,7,2], [1,3,0,3,3,4,5,6,7,2,2,1],[3,2,9,2,3,5,6,6,4,6,9,9],[8,7,7,5,6,7,5,8,8,6,10,9],[7,8,4,9,5,10,3,3,2,2,1,3]]
stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]

def stock_profit(stocks, sells) :
  stocks_information = stocks.split(",") # ","로 주식별 정보를 나누기
  revenue_dict = dict() # 빈 딕셔너리 생성

  for x in stocks_information :
    index = stocks_information.index(x) # 탐색할 인덱스 저장
    information = x.split("/") # "/" 로 이름, 수량, 평균금액 나누기
    Name = information[0]
    average = int(information[2])
    revenue_dict[Name] = (sells[index] - average) / average * 100 #딕셔너리에 이름과 수익률 계산해서 저장
  
  sorted_d = sorted(revenue_dict, key= lambda x : revenue_dict[x], reverse = True) # 밸류값을 기준으로 내림차순 정렬하여 키값을 저장한 배열생성

  for Name in sorted_d :
    print(f"{Name}의 수익률 {revenue_dict[Name]:.3}") # 정렬된 순서대로 출력

stock_profit(stocks, sells)