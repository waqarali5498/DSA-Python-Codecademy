def find_min(my_list,current_min=None):
    
    if len(my_list)==0:  return current_min
    if current_min is None or my_list[0]< current_min:
        current_min=my_list[0]
    print(current_min)

    return find_min(my_list[1:],current_min)


    
    


print(find_min([42, 17, 2, -1, 67]) == -1)
print("---------------------")
print(find_min([]) == None)
print("---------------------")

print(find_min([13, 72, 19, 5, 86]) == 5)




# def find_min(my_list):
#   min = None
#   for element in my_list:
#     if not min or (element < min):
#       min = element
#   return min



