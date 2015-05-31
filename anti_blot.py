t=int(input())
for x in range(t):
    raw_input()
    n=raw_input().split(' ')
    tot=0
    num=[0,2,4]
    for y in num:
        for z in range(len(n[y])):
            if n[y][z]=='m':
                tot=y
    num.remove(tot)
    a=int(n[num[0]])
    b=int(n[num[1]])
    if tot==4:
        print a,"+",b,"=",(a+b)
    elif tot==2:
        print a,"+",(b-a),"=",b
    else:
        print (b-a),"+",a,"=",b
