while True:  
  try:  
    text= input().split(' ') 
    print(len(text))
    context=[]
    for a in range(65,200):
      context.append(0)

    for a in text:
        for count in range(0,len(a)):
          temp=ord(a[count])-65
          if(temp>0 and temp<58):
            context[temp]+=1
          # print (context[temp])
          
    for a in range(0,32):
      if(context[a]!=0):        
        print(chr(a+65)+" : "+str(context[a]))
      if(context[a+32]!=0):
        print(chr(a+65+32)+" : "+str(context[a+32]))


  except (EOFError):  
    break  