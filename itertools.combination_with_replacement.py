from itertools import combinations_with_replacement as comb
s,n=input().split()
s,n=sorted(s),int(n)
li=comb(s,n)
for i in li:
    print(''.join(i))