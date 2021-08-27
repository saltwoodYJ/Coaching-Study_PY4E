# 연봉 계산기
def calculte_yearly_payment(monthly_payment):

    # 세전 연봉 = 월급 * 12
    yearly_payment_b4_tax = monthly_payment * 12

    # 연봉 구간 별로 세금 구하기
    if yearly_payment_b4_tax <= 1200:
        tax = yearly_payment_b4_tax * 0.06  
    elif yearly_payment_b4_tax <= 4600:
        tax = yearly_payment_b4_tax * 0.15   
    elif yearly_payment_b4_tax <= 8800:
        tax = yearly_payment_b4_tax * 0.24
    elif yearly_payment_b4_tax <= 15000:
        tax = yearly_payment_b4_tax * 0.35
    elif yearly_payment_b4_tax <= 30000:
        tax = yearly_payment_b4_tax * 0.38
    elif yearly_payment_b4_tax <= 50000:
        tax = yearly_payment_b4_tax * 0.40
    else:
        tax = yearly_payment_b4_tax * 0.42

    # 세후 연봉 = 세전 연봉 - 세금
    yearly_payment_after_tax = yearly_payment_b4_tax - tax

    print(f"세전 연봉: {yearly_payment_b4_tax}만원")
    print(f"세후 연봉: {yearly_payment_after_tax}만원")

monthly_payment = int(input("월급 입력! : "))
calculte_yearly_payment(monthly_payment)