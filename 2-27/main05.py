while True:  
  try:  
    l= '4'
    text=''
    for a in range(0,int(l)):
        text+="0"
    
    lenth=len(text)-1
    newer=list(text)
    count=0
    times=pow(2,int(l))/2
    left=lenth-1
    right=1
    while True:
        newer[left]=str(1-int(newer[left]))
        print(newer)
        count=0
        for a in range(lenth,0,-1):
            if (int(newer[a])):                
                right=a-1
                break
            else :
                count+=1
                if(count==3):
                    right=count-1
        print(right)
        newer[right]=str(1-int(newer[right]))
        print(newer)
        
        
        if(right):
            break

  except (EOFError):  
    break  