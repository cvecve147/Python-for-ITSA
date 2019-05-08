while True:
    try:
        x=0
        for item in  range(0,1000170):
            x+=4*(pow(-1,item)/(2*item+1))
        times=int(input())
        for times2 in range(0,times):
            a = input()   
            if(int(a)>10 or int(a)<1):
                break
            s= input().split(' ')            
            x=str(x)
            for item in range(0,int(a)):
                if(int(s[item])<1 or int(s[item])>18):
                    break
                print(x[int(s[item])+1])
    
    except (EOFError):
        break