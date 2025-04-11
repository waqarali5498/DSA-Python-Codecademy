def multiplication(num1,num2):
    print(num1,num2)
    if num2==0:
        return num2
    return num1 + multiplication(num1,num2-1)


print(multiplication(3, 7))
print(multiplication(3, 7) == 21)
print(multiplication(5, 5) == 25)
print(multiplication(0, 4) == 0)