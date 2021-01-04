def solution(n):
    import math

    answer = 0

    for a in range(0,(n//2)+1):
        if a ==0 or n-2*a==0:
            answer+=1
        else:
            answer += ((math.factorial(n-a)) // ((math.factorial(n-2*a))*(math.factorial(a))))
            answer %= 1000000007
    return answer