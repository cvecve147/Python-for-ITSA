import itertools

def position(l,ans):
    for temp in range(3,len(l)):
        if(int(l[temp])==ans):
            return temp-3

while True:
    try:
        l = input().split(',')
        count = list(map(int, l[3:]))
        pre = list(itertools.permutations(count, int(l[1])))

        for a in pre:
            addtemp=0
            for temp in a:
                addtemp+=temp
            if(addtemp==int(l[0])):
                lenth=0
                for temp in a:
                    lenth+=1
                    if(lenth!=len(a)):
                        print("k"+ str(position(l,temp)),end=',')
                    else:
                        print("k" + str(position(l, temp)))
                break

    except (EOFError):
        break
