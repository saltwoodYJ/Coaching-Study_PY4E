monthly_dates = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ["월", "화", "수", "목", "금", "토", "일"]

def after_100(month, date, day) :
  now_month = month
  count = 0

  while count < 99 - 31 :
    if count == 0 :
      count = count + monthly_dates[now_month] - date
    else :
      count = count + monthly_dates[now_month]
    now_month = now_month + 1
    if now_month == 13 :
      now_month = 1

  now_date = 99 - count
  if days.index(day) + 1 == 7 :
    now_day = days[0]
  else :  
    now_day = days[days.index(day) + 1]

  print(f"{month}월 {date}일 {day}요일부터 100일 뒤는 {now_month}월 {now_date}일 {now_day}요일")


after_100(6,21,"월")