#문자메시지 길이 20 이하 50원, 20 초과시 100원. 사용자로부터 문자메시지 입력받아 문자요금
#반환하는 코드를 작성하시오.

#1.문자 메시지의 길이를 파악
x = "내가 입력하는 문자 메시지"
print(len(x))
#2.문자 메시지의 길이 <=20,50원
if len(x)<=20:
    print("50원")
#3. 문자 메시지의 길이 > 20, 100원
elif len(x) > 20 :
    print("100원")

#4. 사용자로부터 문자 메시지 입력 받아
text=input("문자 메시지를 입력해주세요.")
#5. 함수로 만들어서 요금을 반환

def find_len(x):
    print(x)

var = find_len("이건 제가 함수 호출할 때 넣은 임의의 값입니다.")
print(var)




#
# x = input("문자메세지를 입력하세요.")
# if len(x)<=20:
#     print("문자요금은 50원입니다.")
# elif len(x)>20:
#     print("문자요금은 100원입니다.")


