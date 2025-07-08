"""
Keep checking the stock price
Use a fucntion to decide whether to sell or not
Keep looping until you decide to stop
"""
import time
print("Now running day_5.py\n")
time.sleep(0.01)
print("Financial checker code\n")
previous_price = 9999   
def check_price(current_price, previous_price):
    print(f"My current price -> {current_price}\n")
    print(f"My previous price -> {previous_price} \n")
    print(f"{'='*100}")
    if current_price < previous_price:
        return "DO NOT SELL"
    elif current_price > previous_price:
        pricedif = current_price - previous_price
        return "YES YOU CAN SELL\n UR PROFIT IS..." + str(pricedif)
    else:
        return "NO CHANGE"
while True:
    current_price = int(input("Please input the current AAPL stock price. \n"))
    print(check_price(current_price, previous_price))
    end_rqst = input("Do you want to end y or n")
    end_rqst = end_rqst.lower()
    if end_rqst == "y":
        print("Gudbye")
        break
    else:
        previous_price = current_price
    

 
