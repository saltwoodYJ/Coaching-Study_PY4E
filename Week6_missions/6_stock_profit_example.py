def stock_profit(stocks, sells):
    stocks = stocks.split(',') # , 기준으로 분리
    stocks = [ s.split("/") for s in stocks ] # / 기준으로 분리
    
    # 종목명, 수량, 매수평균금액, 종목별수익률을 저장할 dict 생성
    profit_dict = dict()
    profits = [] # 종목별수익률을 저장할 리스트
    
    # stocks 리스트를 반복하며 dict로 데이터 옮기기
    for stock in stocks:
        # 없으면 키 생성하고 값을 리스트로 저장
        # 존재하면 리스트에 추가
        if profit_dict.get("종목명", "") == "":
            profit_dict["종목명"] = [stock[0]]
        else:
            profit_dict["종목명"].append(stock[0])
        
        if profit_dict.get("수량", 0) == 0:
            profit_dict["수량"] = [int(stock[1])]
        else:
            profit_dict["수량"].append(int(stock[1]))
            
        if profit_dict.get("매수평균금액", 0) == 0:
            profit_dict["매수평균금액"] = [int(stock[2])]
        else:
            profit_dict["매수평균금액"].append(int(stock[2]))
    # 수익률 = ((매도가 - 매수가) / 매수가) X 100    
    for i in range(len(sells)):
        profit = ((sells[i] - profit_dict["매수평균금액"][i]) / profit_dict["매수평균금액"][i]) * 100
        profits.append(profit)
    
    profit_dict["종목별수익률"] = profits
    
    # 종목명과 수익률만 저장할 dict생성
    answer_dict = dict()
    # 종목명에 수익률 대응시켜 저장
    i = 0
    for name in profit_dict["종목명"]:
        answer_dict[name] = profit_dict["종목별수익률"][i]
        i = i + 1
    # 정렬 
    answer_list = [(v, k) for (k,v) in answer_dict.items() ]
    answer_list = sorted(answer_list ,reverse=True)
    
    # 출력
    for i in answer_list:
        print(f"{i[1]}의 수익률 {i[0]:.3}")