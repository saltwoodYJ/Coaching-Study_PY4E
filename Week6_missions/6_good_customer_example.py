def good_customer(info):
    # ,를 기준으로 분리
    info = info.split(",")
    # 정보를 담을 dict 생성
    info_dict = dict()
    # 정보 6개가 반복되므로 6으로 나눈 나머지를 이용하여 항목 구분하여 저장
    for i in range(len(info)):
        if i % 6 == 0:
            if info_dict.get("아이디", "") == "":
                info_dict["아이디"] = [info[i]]
            else:
                info_dict["아이디"].append(info[i])

        elif i % 6 == 1:
            if info_dict.get("나이", "") == "":
                info_dict["나이"] = [info[i]]
            else:
                info_dict["나이"].append(info[i])

        elif i % 6 == 2:
            if info_dict.get("전화번호", "") == "":
                info_dict["전화번호"] = [info[i]]
            else:
                info_dict["전화번호"].append(info[i])

        elif i % 6 == 3:
            if info_dict.get("성별", "") == "":
                info_dict["성별"] = [info[i]]
            else:
                info_dict["성별"].append(info[i])
        elif i % 6 == 4:
            if info_dict.get("지역", "") == "":
                info_dict["지역"] = [info[i]]
            else:
                info_dict["지역"].append(info[i])
        elif i % 6 == 5:
            if info_dict.get("구매횟수" , "") == "":
                info_dict["구매횟수"] = [int(info[i])]
            else:
                info_dict["구매횟수"].append(int(info[i]))

    index = [] # 전화번호가 없는 회원의 인덱스 저장
    buy = [] # 구매횟수가 8회 이상인 회원 인덱스 저장
    for i in range(len(info_dict["전화번호"])):
        if info_dict["전화번호"][i] == "x":
            index.append(i)
            info_dict["전화번호"][i] = "000-0000-0000"
        if info_dict["구매횟수"][i] >= 8:
            buy.append(i)
    # 구매횟수가 8회 넘는 회원 중에 전화번호가 있는 회원 인덱스 저장 
    true_index = []
    for i in buy:
        if i not in index:
            true_index.append(i)
    info_list = list(info_dict.items())
    
    # 정보 출력
    print(info_dict)
    for i in true_index:
        print(f"할인 쿠폰을 받을 회원정보 아이디:{info_list[0][1][i]}, 나이:{info_list[1][1][i]}, 전화번호:{info_list[2][1][i]}, 성별:{info_list[3][1][i]}, 지역:{info_list[4][1][i]}, 구매횟수: {info_list[5][1][i]}")