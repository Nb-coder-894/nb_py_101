## Day 5 - Should You Sell Your AAPL Stock?
### Your mission:
You're a junior stock trader watching the price of **AAPL** **(AAPL Inc.)** stock.

Your goal:
* Keep checking the stock price
* Use a **function** to decide: *Should you sell or not?*
* Keep looping until you decide to stop

### What You'll Learn Today:
* How to create and use a **function**
* How to build a **while loop** that repeats a task
* How to compare prices using ``` if, elif, else ```
* How to use ```input()``` and ```float()``` for numbers

### What You Need to Build
1. Start with a ```previous_price``` **set to a very large number,** like 9999.
That way, on the first round, it will definitely say **"Do Not Sell"**, and the user will ahve to enter a second price to see what happens next. *(This is just to make sure the loop runs at least twice!)*
2. **Create a function** called something like ``` check_price(current_price, previous_price)```
Inside the function:
* If the current privce is **less than** the previous &rarr; return or print **"Do Not Sell"
* If the current price is **greater** &rarr; calculate **profit**, return or print **"Yes You Can Sell"** and show the profit
* If price is **the same** &rarr; return or print something like **"No Change"**
3. Use a ```while``` **loop** to:
* Ask for the **current AAPL** price
* Call your function and show the result
* Ask the user: *"Do you want to check again?"*, and if they say "no", stop the loop and say gudbye!
* Remember to update ```previous_price``` tot he new ```current_price``` so it compares correctly next time.
## Hints:
* Use ```float(input(...)) ``` to get decimal price values
* Make your function return a string like ```"Do Not Sell"``` or ```"Yes You Can Sell"```
* You can ```print()``` things inside the function too
* Don't forget to update your ```previous_price``` each time through the loop
## Optional Fun:
* Add emojis to your messages **like** ":dollar: 
* Try to keep track of total profit (a stretch goal)
