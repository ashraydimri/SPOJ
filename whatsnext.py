while 1:
    x,y,z = raw_input().split(' ')
    x=int(x)
    y=int(y)
    z=int(z)
    if x==0 and y==0 and z==0:
        break
    else:
        if (y-x)==(z-y):
            print "AP",(z+(z-y))
        else:
            print "GP",(z*(z/y))
            
