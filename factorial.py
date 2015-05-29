T=int(input())
for x in range(T):
    a=int(raw_input())
    k=1
    t=0
    while (5**k)<=a:
        t+=(a/(5**k))
        k=k+1
    print t
