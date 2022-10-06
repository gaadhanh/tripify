def count():
    r=open('count.txt','r')
    n=r.read()
    m=str(int(n)+1)
    r.close()
    r=open('count.txt','w')
    r.write(m)
    r.close()
    return n
    
