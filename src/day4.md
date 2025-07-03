## Day 4 plan functions

### Today, we will learn how to make ur own commands, cald functions
### They help us to avoid repeating code, organize our programs, and to think like real programmers.

## What is a function?
### A function is like a reusable box of code. Here's an example.
```
def say_hello():
   print("Hello there!)
```   
### In this case, your defined a function called say_hello. 
### To run this function, you must type:
```
say_hello()
```
## Functions with Parameters

Let's say that we want to greet someone by name:
```
def greet(name):
   print("hi",name)
```
Now you can call it with different names:
```
greet("Alice")
greet("Bob")
```
## Function That Returns A Value
```
def add(a,b):
  return a + b
```
This returns a result--but it doesn't print it. You can print or save the result.
```
result = add(3,4)
print("The sum is", result)
```
## Try this yourself:
Please make a different python document for each one.
### Exercise 1 : Make a function called welcome() that prints:
```
# Welcome to Python class!
```
### Exercise 2 : Make a function called square(n) that returns the square of a numbers, such as square(5) = 25.

### Exercise 3: Make a function called is_even(n) that returns True if the number is even, otherwise False.

### Bonus challenge: Mini quiz game.
```
def ask_question(question, correct_answer):
   answer = input(question + " ")
   if answer.lower() = correct_answer.lower():
      print("Correct!")
    else:
    print("Oops! The right answer was", correct_answer)
```
Try calling it:
ask_question("What is the capital of France?" , "Paris")
ask_question("What is 2+2", "4")
### Explain 2 Hada what this code is doing.      
