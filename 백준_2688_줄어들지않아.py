T = int(input())

def dfs(depth, cur_num, n, dp):
  if depth == n:
    return 1
  if dp[depth][cur_num]!=-1:
    return dp[depth][cur_num]
  dp[depth][cur_num]=0
  for num in range(cur_num,10):
    dp[depth][cur_num]+=dfs(depth+1, num, n, dp)
  return dp[depth][cur_num]

answer = [0]*T
for t in range(0,T):
  n = int(input())
  dp = [[-1]*10 for _ in range(n)]
  answer[t]=dfs(0,0,n,dp)

print(answer)
