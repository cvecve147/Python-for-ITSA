while True:
    try:
        s = int(input())
        text = []
        Coin = {'1': 0, '5': 0, '10': 0, '50': 0}
        for a in range(0, s):
            all = input().split(',')
            text.append(all)
        for a in text:
            a[0] = int(a[0])
            a[1] = int(a[1])
            a[2] = int(a[2])
            if (a[1] == 1):
                a[0] -= 17 * a[2]
            else:
                a[0] -= 25 * a[2]
            while (a[0] > 0):
                if (a[0] >= 50):
                    a[0] -= 50
                    Coin['50'] += 1
                elif (a[0] >= 10):
                    a[0] -= 10
                    Coin['10'] += 1
                elif (a[0] >= 5):
                    a[0] -= 5
                    Coin['5'] += 1
                else:
                    a[0] -= 1
                    Coin['1'] += 1

            while (Coin['1'] or Coin['5'] or Coin['10'] or Coin['50']):
                print("Coin ", end="")
                if (Coin['1'] > 0):
                    print("1:" + str(Coin['1']), end="")
                    Coin['1'] = 0
                elif (Coin['5'] > 0):
                    print("5:" + str(Coin['5']), end="")
                    Coin['5'] = 0
                elif (Coin['10'] > 0):
                    print("10:" + str(Coin['10']), end="")
                    Coin['10'] = 0
                elif (Coin['50'] > 0):
                    print("50:" + str(Coin['50']), end="")
                    Coin['50'] = 0
                if (Coin['1'] or Coin['5'] or Coin['10'] or Coin['50']):
                    print(",", end="")
            print()

    except (EOFError):
        break
