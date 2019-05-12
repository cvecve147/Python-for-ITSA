while True:
    try:
        pi = "3.14159265358979323846264338327950288419716939937510"
        times = int(input())
        for a in range(0, times):
            gets = input()
            getpostion = input().split(' ')
            for a in getpostion:
                print(pi[int(a) + 1])
    except (EOFError):
        break