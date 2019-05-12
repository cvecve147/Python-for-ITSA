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

            for c in range(getlong, length):
                if (int(i[3]) >= c and int(i[2]) <= c
                        or int(i[1]) >= c and int(i[0]) <= c):
                    print(c)
                    continue

    except (EOFError):
        break