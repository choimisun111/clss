#리스트 변수의 평균값 구하는 함수 작성.sum()함수 사용 불가능.

list = [1,2,3,4,5,6]

def average(list):
    a = 0
    for i in list:
        a = a + i


    result = a/len(list)
    return result
print(average(list))


def mean_list (x):
    result = 0
    for i in x:
        result = result + i
        avg = result / len(x)
        return avg

var = list(range(2, 99999))




var =[1,2,3,4,5]
result = 0
for i in var :
    result = result + i
    avg = result/len(var)