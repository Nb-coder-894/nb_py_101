#### For Each Exercise Write a separate python file
#### Give them a meaningful name  
#### Test and Commit



Absolutely! Let’s rewind and take a proper **Day 3 class on `dictionaries`** — no rush, no skipping.

---

## 🏫 Welcome to Python Class: **Dictionaries 101**

Today’s Topic:
🔑 **Dictionaries** – a powerful way to store **related data** using **key-value pairs**.

---

## 🍎 What Is a Dictionary?

A **dictionary** is like a **real dictionary**:
You look up a **word (key)** to get the **definition (value)**.

In Python:

```python
my_dict = {
    "apple": "a fruit",
    "python": "a programming language",
    "sun": "a star"
}
```

* `"apple"`, `"python"` are **keys**
* `"a fruit"`, `"a programming language"` are **values**

---

## 🔍 Why Use a Dictionary?

Dictionaries are perfect when you want to:

* **Look things up** quickly (like a glossary)
* Store **info about something** (like a student or product)
* Group things together by **names or labels**

---

## 🛠 How to Create and Use Dictionaries

### 📦 1. Create a Dictionary

```python
student = {
    "name": "Alice",
    "age": 12,
    "grade": "7th"
}
```

### 🔑 2. Access a Value by Key

```python
print(student["name"])   # Output: Alice
print(student["age"])    # Output: 12
```

⚠️ If the key doesn’t exist, you’ll get an error.

### ✅ 3. Use `.get()` to avoid errors

```python
print(student.get("height"))       # Output: None (no error!)
print(student.get("height", "N/A"))  # Output: N/A
```

### 📝 4. Add or Change a Value

```python
student["age"] = 13         # change
student["hobby"] = "music"  # add new key-value
```

### ❌ 5. Remove a Key

```python
del student["grade"]
```

---

## 🧠 Example – Book Tracker

```python
book = {
    "title": "Harry Potter",
    "author": "J.K. Rowling",
    "pages": 500,
    "read": True
}

print("Book Title:", book["title"])
book["pages"] = 550
book["year"] = 1997
```

---

## 🌀 Looping Through a Dictionary

```python
for key in book:
    print(key, "->", book[key])
```

Or better:

```python
for key, value in book.items():
    print(f"{key}: {value}")
```

---

## 🧪 Try It Yourself

### ✏️ Exercise 1: Make a Dictionary of Your Favorite Animal

```python
animal = {
    "name": "Elephant",
    "color": "Gray",
    "weight": 5000
}
```

Now print the color.

---

### ✏️ Exercise 2: Add a Key for “continent”

Then print the whole dictionary.

---

### ✏️ Exercise 3: Student Database

Make a dictionary for 3 students:

```python
students = {
    "Alice": {"age": 12, "grade": 7},
    "Bob": {"age": 11, "grade": 6},
    "Clara": {"age": 13, "grade": 8}
}
```

Try printing:

```python
print(students["Bob"]["grade"])  # Output: 6
```

---

### 🧠 Bonus Challenge: Word Counter

```python
sentence = "apple banana apple mango banana apple"
words = sentence.split()
counter = {}

for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1

print(counter)
```

---

## 🧾 Summary

✅ Dictionaries use **key-value pairs**
✅ You can **access**, **add**, **change**, and **remove** entries
✅ Great for storing related info like a **profile** or **record**
✅ Use loops to go through them

---

Would you like me to quiz you a bit? Or do a small mini-project using dictionaries (like a phonebook or flashcard app)?
