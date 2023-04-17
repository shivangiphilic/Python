cp = int(input())
r = int(input())
sp = int(input())
tc = cp+r
delta = sp-tc
p = abs((delta/tc)*100)
print(round(p,2))