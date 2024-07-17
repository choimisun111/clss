#홀수 짝수 판별기 함수. 매개변수 입력에 따라 홀수 또는 짝수를 자동으로 판별하는 함수를 작성.
#반환되는 값은 홀수 또는 짝수이다.

def 홀수짝수(x):
    if x % 2 == 0 :
        result = "짝수"
    elif x % 2 == 1 :
        result = "홀수"
    return result


x=int(input("숫자를 입력하세요."))
print(홀수짝수(x))



var = 1233
def find_odd_even (var) :
    result = ""
    if var %2 == 0 :
        result= "홀수"
        return result
nes = find_odd_even(123456789)
print()