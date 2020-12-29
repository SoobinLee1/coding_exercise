from itertools import product
from itertools import chain

def solution(N, number):
    if N ==number:
        return 1
    for i in range(1,8):
        operators = product(['','+','-','*','/'], repeat=i)
        operators = list(operators)
        for o in operators:     
            # operators 의 각 원소들 자체가 배열일 때,
            # 각 원소들 내부의 최종 원소를 string 화하는 작업
            str_operators = list(map(str,o))
            evaluation = ''
            evaluation+=str(N)
            
            for oo in str_operators:
                evaluation+=str(oo)
                evaluation+=str(N)
            
            if eval(evaluation)==number:   
                print(evaluation)
                return i+1
    answer = -1
    return answer