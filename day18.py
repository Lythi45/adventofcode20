def parse(s,p):   
    nu=0
    rr='+'
    while s[p]!=')':       
        if s[p]=='+':
            rr='+'
        elif s[p]=='*':
            rr='*'
        else:
            if s[p]=='(':
                p,num=parse(s,p+1)
            else:
                 num=int(s[p])
            if rr=='+':
                nu+=num
            else:
                nu*=num
        p+=1
    return p,nu
           
su=0
for line in open("input18.txt",'r').readlines():
    line=('('+line.strip()+')').replace('(','( ').replace(')',' )').split()
    su+=parse(line,1)[1]
print(su)

def parse2(s,p,mo):   
    nu=0    
    while s[p]!=')':      
        if s[p]=='+':
            rr='+'
        elif s[p]=='*':
            if mo:              
                return(p-1,nu)
            else:
                p,num=parse2(s,p+1,True)              
                nu*=num
                rr='*'               
        else:
            if s[p]=='(':
                p,num=parse2(s,p+1,False)             
            else:
                 num=int(s[p])
            nu+=num
        p+=1
    return (p-1,nu) if mo else (p,nu)

su=0
for line in open("input18.txt",'r').readlines():
    line=('('+line.strip()+')').replace('(','( ').replace(')',' )').split()
    su+=parse2(line,1,False)[1]
   
print(su)