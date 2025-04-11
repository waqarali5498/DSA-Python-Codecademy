def fibonacci(n):
    if  n==0: return 0
    if  n==1: return 1

    first=0
    second=1
    result=0

    for i in range(1,n,1):
        # print("First ", first)
        # print("Second ", second)
        result=first+second
        # print("Result ", result)
        first=second
        second=result

        # print("------------")
    
    return result


    # 0 1 1 2 3 5 8 13
  


print(fibonacci(3) == 2)
print(fibonacci(7) == 13)
print(fibonacci(0) == 0)