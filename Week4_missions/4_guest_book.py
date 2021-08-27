def wrong_guest_book(guest_book) :
  for x in guest_book :
    check = 1
    phone_number = x[1]
    if len(phone_number) != 13 :
      check = 0
    elif phone_number[3] != '-' or phone_number[8] != '-' :
      check = 0
    elif phone_number[0] != '0' or phone_number[1] != '1' or phone_number[2] != '0' :
      check = 0

    if check == 0 :
      print(f'잘못쓴사람 : {x[0]} ')
      print(f'잘못쓴번호 : {x[1]}')
  
      

guest_book = [['김갑','123456789'],
['이을','010-1234-5678'],
['박병','010-5678-111'],
['최정','111-1111-11'],
['정무','010-3333-3333']]
wrong_guest_book(guest_book)