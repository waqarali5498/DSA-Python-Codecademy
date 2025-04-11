# define your linear_search() below...
def linear_search(search_list,target_value):
  for idx in range(len(search_list)):
    if search_list[idx] == target_value:
      return idx
  raise ValueError(f"{target_value} not in list")



# uncomment the lines below to test...
values = [54, 22, 46, 99]
print(linear_search(values, 22))