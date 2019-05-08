from decimal import Decimal

while True:
    try:
        s = int(input())
        all = []
        for a in range(0, s):
            el = int(input())
            all.append(el)
        for e in all:
            ans = 0
            ans2 = 0
            while (e > 0):
                if (e >= 701):
                    ans += (e - 700) * 5.63
                    ans2 += (e - 700) * 4.50
                    e = 700
                elif (e >= 501):
                    ans += (e - 500) * 4.97
                    ans2 += (e - 500) * 4.01
                    e = 500
                elif (e >= 331):
                    ans += (e - 330) * 4.39
                    ans2 += (e - 330) * 3.61
                    e = 330
                elif (e >= 121):
                    ans += (e - 120) * 3.02
                    ans2 += (e - 120) * 2.68
                    e = 120
                else:
                    ans += e * 2.10
                    ans2 += e * 2.10
                    e = 0

            print("Summer months:" +
                  str(Decimal(ans).quantize(Decimal('0.00'))))
            print("Non-Summer months:" +
                  str(Decimal(ans2).quantize(Decimal('0.00'))))

    except (EOFError):
        break
