def sales_management(names, records):
    
    record_dict = dict() # 멤버의 실적을 기록할 dict 생성
    # 실적 기록
    for i in range(len(names)):
        record_dict[names[i]] = records[i]
    
    # 실적을 평균으로 바꿔서 저장
    for (k,v) in record_dict.items():
        total = 0
        for i in v:
            total = total + i
        mean = total / len(v)
        record_dict[k] = mean
    # 평균 실적이 높은 순서대로 저장
    ranking = [ (v,k) for k,v in record_dict.items() ]
    ranking = sorted(ranking, reverse=True)
    
    # 예비 보너스, 면담 대상자 저장
    bonus_names = (ranking[0][1], ranking[1][1])
    counsel_name = (ranking[4][1], ranking[5][1])
    
    # 5보다 작으면 보너스 대상자 제외
    for bn in bonus_names:
        if record_dict[bn] < 5:
            continue
        print(f"보너스 대상자 {bn}")
    print()
    
    # 3보다 높으면 면담 대상자 제외
    for cn in counsel_name:
        if record_dict[cn] > 3:
            continue
        print(f"면담 대상자 {cn} ")