import json 
input_dict = {
    "korfu" : "dog",
    "meow" : "mouse",
    "adam" : "dog",
    "pinky" : "dog",
    "neptune" : "cat",
    "moustache" : "cat",
    "purugly" : "cat"

}






input_dict["blahblahblah"] = 3000


print(f" AFTER CHANnge --> {json.dumps(input_dict, indent=4)}\n\n ========\n ")

counting_dict = {}

for key, value in input_dict.items():
    if value not in counting_dict:
        counting_dict[value] = 1
    else:
        counting_dict[value] += 1
print(counting_dict)  
print("\n==========================\n")            