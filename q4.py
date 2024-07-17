#학점변환기 함수. 사용자로부터 SCORE를 입력받아 학점ㅇ로 환산하여 반환하는 함수를 작성

def 점수 (a) :
    result = "잘못 입력하셨습니다."
    if 80 < a < 100 :
        result = "A"
    elif 61 < a < 80 :
        result = "B"
    elif 41 < a < 60 :
        result = "C"
    elif 21 < a < 40 :
        result = "D"
    elif 0 <  a < 20 :
        result = "E"

    else:
        print("올바른 점수를 입력하세요.")
    return result

text=input("점수를 입력하세요.")
print(점수(int(text)))

