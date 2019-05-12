while True:
    try:
        s = int(input())
        for a in range(0, s):
            i = []
            length = int(input())
            n = int(input())
            for b in range(0, n):
                geti = input().split(' ')
                i += geti

            # process
            getlong = 0
            for b in (0, n):
                if (getlong < (int(i[b + 1]) - int(i[b]))):
                    getlong = (int(i[b + 1]) - int(i[b]))
            getlong += 1
            ans = 0
            for c in range(getlong, length):
                allc = c
                count = 0
                if (ans > 0):
                    break
                while (allc < length):
                    if (int(i[3]) > allc and int(i[2]) < allc
                            or int(i[1]) > allc and int(i[0]) < allc):
                        count += 1
                        break
                    else:
                        allc += c
                        if (allc > length and count == 0):
                            ans = c
                            print(c)

    except (EOFError):
        break