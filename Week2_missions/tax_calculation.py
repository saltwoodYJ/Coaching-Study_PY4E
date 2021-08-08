def yearly_payment(m_payment):
  yearly_before = int(m_payment)*12
  if yearly_before <= 1200 :
    yearly_after = int(yearly_before * 0.94)
  elif yearly_before <= 4600 :
    yearly_after = int(yearly_before * 0.85)
  elif yearly_before <= 8800 :
    yearly_after = int(yearly_before * 0.76)
  elif yearly_before <= 15000 :
    yearly_after = int(yearly_before * 0.65) 
  elif yearly_before <= 30000 :
    yearly_after = int(yearly_before * 0.62)
  elif yearly_before <= 50000 :
    yearly_after = int(yearly_before * 0.60)
  else :
    yearly_after = int(yearly_before * 0.58)
  print("세전 연봉: "+ str(yearly_before) + "만원")
  print("세후 연봉: "+ str(yearly_after) + "만원")


monthly_payment = input("월급을 입력하세요")
yearly_payment(monthly_payment)