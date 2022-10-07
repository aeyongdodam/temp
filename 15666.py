def rec(i):
    if i==m:
        print(" ".join(map(str, ans)))
        return
    for j in range(len(num)):
        if i==0 or ans[-1] <= num[j]:
            ans.append(num[j])
            rec(i+1)
            ans.pop()
import sys
n,m=map(int, sys.stdin.readline().split())
num=list(set(map(int,sys.stdin.readline().split())))
num.sort()
ans=[]
rec(0)
