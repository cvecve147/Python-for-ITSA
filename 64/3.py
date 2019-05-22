while True:
    try:
        text = ['Hi', 'Hello', 'How do you do', 'How are you']
        count = 0
        while True:
            s = input()
            if (text[0] == s or text[1] == s or text[2] == s or text[3] == s):
                print(text[count])
                count += 1
            else:
                print("Sorry")
                count = 0

            if (count == 4):
                count = 0

    except (EOFError):
        break
