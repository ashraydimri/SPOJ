test=raw_input()
test=int(test)
for i in range(test):
    s=0
    raw_input()
    n=raw_input()
    n=int(n)
    for j in range(n):
        num=raw_input()
        num=int(num)
        s+=num

    if s%n==0: print "YES"
    else : print "NO"
