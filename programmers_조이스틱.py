from string import ascii_uppercase

up = list(ascii_uppercase)
down = sorted(list(ascii_uppercase), reverse=True)

def move(alphabet):
    if up.index(alphabet) == 0:   # means alphabet is A
        return (True,0)
    elif up.index(alphabet) < down.index(alphabet)+1:
        return (False,up.index(alphabet))
    else:
        return (False,down.index(alphabet)+1)
    
    
def choose_path(direction, current, total_cnt, visited):
    movement = {'left':-1, 'right':1}
    next_move=-1
    cnt=0
    while next_move!= current:
        next_move=(current+movement[direction])%total_cnt
        cnt +=1
        if visited[next_move] ==0:
            return cnt, next_move
    return 0, -1
    
    
def solution(name):
    init = [(move(alphabet)[0], move(alphabet)[1]) for alphabet in list(name)]
    answer = sum([move for (_,move) in init])
    visited = [visited for (visited,_) in init]
    start = 0
    visited[0]=True
    while not all(visited):
        left = (start-1) % len(name)
        right = (start+1) % len(name)
        if visited[left]!=0 and visited[right]==0:
            start = right
            answer+=1
            visited[start]=True
        elif visited[left]==0 and visited[right]!=0:
            start = left
            answer+=1
            visited[start]=True
        else:
            cnt_left, next_left = choose_path('left',start, len(name), visited)
            cnt_right, next_right = choose_path('right',start, len(name), visited)
            visited[start]=True
            if cnt_left < cnt_right:
                start = next_left
                answer+=cnt_left
                visited[start]=True
            else:
                start = next_right
                answer+=cnt_right
                visited[start]=True
    return answer