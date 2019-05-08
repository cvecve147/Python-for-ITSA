while True:
    try:
        a = input()   
        if(int(a)>10 or int(a)<1):
            break
        x=0
        for item in  range(0,999):
            x+=4*(pow(-1,item)/(2*item+1))
            # print (x)     
        s=input().split(' ')
        x=str(x)
        for item in range(0,int(a)):
            if(int(s[item])<1 or int(s[item])>18):
                break
            print(x[int(s[item])+1])
        
    except (EOFError):
        break