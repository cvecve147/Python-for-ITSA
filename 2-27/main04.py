while True:
    try:
        l = input()
        ans1=int(l)
        ans2=0

        for a in range(0,len(l)):
            for times in range(0,(len(l)-a-1)):
                ans1 -= int(str(ans1)[a]) * pow(10, times)

        for a in range(0, len(str(ans1))):
            ans2 += ans1//pow(10,a)

        if(ans2==int(l)):
            print(ans1)
        else:
            print('-1')
    except (EOFError):
        break
