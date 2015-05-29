N= int(input())
def rev(num):
    rev=0
    while num!=0:
        rev=(rev*10)+(num%10)
        num=num/10
    return rev
for x in range(N):
    a,b=raw_input().split(' ')
    a=int(a)
    b=int(b)

    s=rev(a)+rev(b)
    print rev(s)
