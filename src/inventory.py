from inventorycontents import amazon_dict
print (amazon_dict)
yOrN = input("would you like to add something type y or n? \n ")
if yOrN == "y":
    item_name = input("first please give the name of the item \n")
    amazon_dict[item_name] = None
    item_quantity = input("what is the quantity of the item \n")
    amazon_dict[item_name] = item_quantity
print(f"change dict ->> {amazon_dict.items()}")

# extension, make sure that if the item is already in the dict then change the value    
        
    
                                                                                                                 