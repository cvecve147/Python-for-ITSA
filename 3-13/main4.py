def test(n):
    if(n==1):return 2
    return test(n-1)

print(test(10))