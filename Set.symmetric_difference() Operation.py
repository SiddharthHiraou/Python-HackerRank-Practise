n=int(input())
n1=list(input().split())
m=int(input())
m1=list(input().split())

s1=set(n1)
s2=set(m1)

print(len(s1.symmetric_difference(s2)))
