from collections import deque
dy,dx=[-2,-2,-1,1,2,2,-1,1],[-1,1,2,2,-1,1,-2,-2]
def bfs(y,x):
	dq=deque()
	mapp[y][x]=1
	dq.append([y,x])
	while dq:
		y,x=dq.popleft()
		if y==end[0] and x==end[1]:
			return mapp[y][x]-1
		for i in range(8):
			ny,nx=y+dy[i],x+dx[i]
			if 0<=ny<a and 0<=nx<a and mapp[ny][nx]==0:
				mapp[ny][nx]=mapp[y][x]+1
				dq.append([ny,nx])
a=int(input())
start=list(map(int, input().split()))
end=list(map(int, input().split()))
mapp=[[0]*a for _ in range(a)]
print(bfs(start[0],start[1]))