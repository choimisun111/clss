#판매가가 저장된 리스트가 있을때 부가세가 포함된 가격을 리스트로 반환하는 함수를 작성하시오.
#numbers = [100,200,300 ]
#print(vat(numbers))
#출력결과 [110,220,330]


numbers = [100,200,300 ]
def VAT(numbers):
    result = []
    for i in numbers :
        result.append(int(i*1.1))

    return result
print(VAT(numbers))



