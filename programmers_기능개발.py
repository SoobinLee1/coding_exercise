import math

def solution(progresses, speeds):
    deadlines = [math.ceil((100-progress)/speed) for progress, speed in zip(progresses,speeds)]
    print(deadlines)
    answer = []
    while deadlines:
        current = deadlines.pop(0)
        cnt=1
        if not deadlines:
            answer.append(cnt)
            break
        print(current)
        while deadlines:
            if deadlines[0]<=current:
                deadlines.pop(0)
                cnt+=1
            else:
                answer.append(cnt)
                break
            if not deadlines:
                answer.append(cnt)
    return answer