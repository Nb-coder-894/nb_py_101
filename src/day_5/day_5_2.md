

## 🧠 Day 5 - Python: Functions & Power-Ups!
🎮 “Think of a function like a secret move or power-up in a game.”
### 📘 Part 1: What Is a Function?
👾 Imagine you're building your own video game.
 You want to make a special move—like "Fireball Attack" or "Health Restore".
Do you want to write the same code again and again every time the hero attacks?
 Nope! You just want to call the move whenever needed.
That’s exactly what a function is in Python.
📦 It's a little box of code you can reuse again and again.
 🕹️ You give it inputs (like ammo, target, or energy)
 🎯 And it gives you a result (like damage, success, or score)
🎮 Example:
def fireball(power):
    print("🔥 Fireball launched!")
    return power * 10

# Use the move!
damage = fireball(5)
print("Enemy takes", damage, "damage!")

✅ You just made your own attack function!

### ⚔️ Part 2: Your Turn — Build a Math Wizard Power
You're going to build a magic formula generator for a wizard.
🧙 The wizard combines two numbers to make a quadratic spell.
📐 The spell is in the form:
x^2 + (num1 + num2)x + (num1 * num2)

For example:
make_quad(2, -3)

Would return:
x^2 - 1x - 6

🛠️ What To Do:
Write a function called make_quad(num1, num2)


Inside it, calculate:


a = num1 + num2


b = num1 * num2


Build a string like: "x^2 + {a}x + {b}" (but be careful with minus signs!)


Return that string


Try it with both positive and negative numbers


🎯 Challenge: Can you make it so that:
If a is negative, it says - ax (not + -ax) (e.g it returns sign correctly)


If b is negative, it says - b (not + -b)



📬 Paste your code here when you're done and I’ll review it!
Have fun being a Math Wizard! 🧙‍♂️✨

