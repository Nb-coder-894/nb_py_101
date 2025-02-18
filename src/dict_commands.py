from inventorycontents import amazon_dict
print(amazon_dict)
number_request = int(input("Welcome to workspace number 2. Please input 1, 2, 3, or 4 \n"))
if number_request == 1:
    input_request_1 = input("please give the name of the item you would like to give.\n")
    amazon_dict[input_request_1] = None
    quantity_request_1 = input("now please give the quantity of the object. \n")
    amazon_dict[input_request_1] = quantity_request_1
elif number_request == 2:
    input_request_2 = input("Please give the name of the item you would like to give. \n")
    amazon_dict[input_request_2] = None
    quantity_request_2 = input("please give the quantity of the item. \n")
    amazon_dict[input_request_2] = quantity_request_2
    print("Now updating inventory \n")
    print(amazon_dict)
elif number_request == 3:
    item_search_3 = input("please give the name of the object \n")
    if item_search_3 not in amazon_dict:
        print("item not in dict. thank you")
    else:
        recieved_value = amazon_dict.get(item_search_3)
        print(f"alright this is in the inventory. the quantity will be {recieved_value}. ")
else:
    print(amazon_dict.items())                
