def fact(num):
    ans=1
    if num!=0:
        ans*=num *fact(num-1)
    return ans

T=int(input())
for x in range(T):
    a=int(input())
    print fact(a)
