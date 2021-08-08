birth = int(input("생일이 지났습니까? 맞으면 0 아니면 -1 :"))
age = int(input("한국 나이를 입력해 주세요 :" ))
if birth == 0:
    age = age - 1;
else :
    age = age - 2;
print("미국 나이 : " + str(age))