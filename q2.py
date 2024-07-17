#구구단 함수를 작성. 매개변수 입력에 따라 해당 구구단을 화면에 출력하는 함수를 작성

# def 구구단(num):
#     for i in range(1,10):
#         num2 = num * i
#         print(num, "x", i, "=",num2)
#
# b = int(input('숫자를 입력하시오.'))
# 구구단(b)

# def aa(a):
#     for b in range(1,10):
#         print(a,"x" , b, "=", a*b)
# aa(3)

def print_mul_table(x):
    print(x)
    for i in range(1,10):
        print(x,"x", i ,"=", x * i)

print_mul_table(4)