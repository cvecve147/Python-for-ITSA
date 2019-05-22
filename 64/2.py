while True:
    try:
        s = int(input())
        for a in range(s, 0, -1):
            count = 0
            for b in range(2, a):
                if (a % b == 0):
                    break
                else:
                    count += 1
            if (count == a - 2):
                print(a)
                break
    except (EOFError):
        break