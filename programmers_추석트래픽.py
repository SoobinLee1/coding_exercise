def start_end_time(lines):
    start_time = []
    end_time=[]
    for log in lines:
        time = log.split(" ")[1]
        duration =float(log.split(" ")[2][:-1])
        hour_sec = float(time.split(":")[0])*3600
        min_sec = float(time.split(":")[1])*60
        total_sec = hour_sec+min_sec+float(time.split(":")[2])
        end_time.append(total_sec)
        start_time.append((total_sec-duration)+0.001)
    return start_time,end_time


def count_work(time, start, end):
    cnt=0
    time = time
    for st, fin in zip(start,end):
        if fin<=time+1 and fin>=time:
            # fin 지점이 1초 구간 사이에 있을 때
            cnt+=1
        elif fin>time+1:
            if not st>=time+1:
                # start 지점이 1초 구간 사이에 있을 때
                cnt+=1
    return cnt


def solution(lines):
    start,end = start_end_time(lines)
    time=start[0]
    max_cnt = 0
    
    # O(N^2), 변화가 발생하는 양 끝 지점에 대해서만 탐색
    for st, fin in zip(start, end):
        cnt1 = count_work(st,start,end)
        cnt2=count_work(fin,start,end)
        if cnt1>max_cnt:
            max_cnt=cnt1
        if cnt2>max_cnt:
            max_cnt=cnt2
    return max_cnt