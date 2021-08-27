# 학점 계산기 
def grader(name, score):

    if score >= 95:
        grade = "A+"
    elif score >= 90:
        grade = "A"
    elif score >= 85:
        grade = "B+"
    elif score >= 80:
        grade = "B"
    elif score >= 75:
        grade = "C+"
    elif score >= 70:
        grade = "C"
    elif score >= 65:
        grade = "D+"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"학생이름: {name}")
    print(f"점수: {score}점")
    print(f"학점: {grade}")

name = input("이름: ")
score = int(input("점수: "))
grader(name, score)