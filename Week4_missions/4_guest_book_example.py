def wrong_guest_book(guest_book):
		# text 파일 저장
    text_save = open("guest_book.txt","w", encoding="UTF8")
    text_save.write(guest_book)
    text_save.close()
    
		# 파일 불러오기
    file = open("guest_book.txt")
    for line in file:
				# 이름과 전화번호 구분
        name = line[:2]
        phone_number = line[3:].strip()
				# 조건을 만족하면 continue 아니면 출력
        if len(phone_number) == 13 and phone_number.find("-") != -1 and phone_number.startswith("010") == True:
            continue
        else:
            print(f"잘못 쓴 사람: {name}")
            print(f"잘못 쓴 번호: {phone_number}")
            print()