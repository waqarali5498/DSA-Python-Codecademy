def sum_digits(num):
    if num < 1:
        return 0
    return num%10 + sum_digits(num//10)


# test cases
print(sum_digits(12) == 3)
print(sum_digits(552) == 12)
print(sum_digits(123456789) == 45)



# def sum_digits(n):
#   if n < 0:
#     ValueError("Inputs 0 or greater only!")
#   result = 0
#   while n is not 0:
#     result += n % 10
#     n = n // 10
#   return result + n