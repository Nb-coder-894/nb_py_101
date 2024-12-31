# [1, 5, 5, 1, 2, 5, 3]
# 
# 
# 
# 
# 
# 
# for a dictionary variable you add a key and value like dict variable name[key] = value 
# 
# my_dict = {}

# my_key = "ram"

# my_dict[my_key] = 1 

# print(my_dict)

# my_dict["ram"] += 1

# print(my_dict)

# my_dict[my_key] -= 1 

# print(my_dict)
input_lst = [1, 5, 5, 1, 2, 5, 3]
my_dict = {}
for i in input_lst:
    if i not in my_dict:
        my_dict[i] = 1
    else:
        my_dict[i] += 1
import json
print(f" my DERIVED dict -> {json.dumps(my_dict, indent=4)}")
for k,v in my_dict.items():
    if v == 1:
        continue
    else:
        print(f"Happy {k}")

           
    