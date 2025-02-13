from inventorycontents import amazon_dict
print("Welcome to the Amazon server. \n Here are the items, and here are their quantities.")
print (amazon_dict)
yOrN = input("would you like to add something type y or n? \n ")
if yOrN == "y":
    item_name = input("first please give the name of the item \n")
    amazon_dict[item_name] = None
    item_quantity = input("what is the quantity of the item \n")
    amazon_dict[item_name] = item_quantity
if item_name in amazon_dict:
 same_name_response = input("Okay this item is  already in Amazon. \n Would you like to change the quantity of the item? \n Type y for the quantity to update, type n for the quantity to stay the same. \n")    
if same_name_response == "y":
    print(f"change dict ->> {amazon_dict.items()}")    
# extension, make sure that if the item is already in the dict then change the value
    
        
    
                                                                                                                 