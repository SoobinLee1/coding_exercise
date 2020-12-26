def GCD(a,b):
    if a<b:
        (a,b)=(b,a)
    while b!=0:
        (a,b)=(b,a%b)
    return a
        
def solution(w,h):
    answer = w*h-(w+h-GCD(w,h))
    return answer