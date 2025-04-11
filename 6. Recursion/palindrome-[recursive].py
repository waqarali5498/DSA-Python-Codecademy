def is_palindrome(my_str):
    if len(my_str) < 2:
        return True
    print("length ", len(my_str))
    print("str[0] ", my_str[0])
    print("str[-1] ", my_str[-1])
    if my_str[0] != my_str[-1]:
        return False
    return is_palindrome(my_str[1:-1])


# test cases
print(is_palindrome("abba") == True)
# print(is_palindrome("abcba") == True)
# print(is_palindrome("") == True)
# print(is_palindrome("abcd") == False)




