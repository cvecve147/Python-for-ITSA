while True:  
  try:  
    text= input()
    context=[]
    count=0
    add=0
    last=99
    for a in range(0,10):
        context.append(0)
    for a in range(0,len(text)):
      print(text[a])

    # for a in text:
    #     count+=1        
    #     if(count==1):continue
    #     if(int(text[count-2])>=int(a)):              
    #         if(last>int(a)):        
    #             if(add==0):
    #                 context[int(text[count-2])]+=1
    #                 print(int(text[count-2]),end="")
    #                 context[int(a)]+=1
    #                 add+=1
    #             print(int(a),end="")
    #             last=int(a)
    # print()

  except (EOFError):  
    break