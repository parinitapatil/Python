# ✅ **Student Result Management System (Python – No Libraries)**

## 🎓 Student Result Management System (Mini Project)

This is a simple Python mini-project that stores student details, calculates grades, and prints passed/failed students.
The project uses **only core Python (no libraries)** — lists, dictionaries, loops, and conditions.

---

## ✨ Features

* Add multiple students
* Store:

  * Name
  * Roll Number
  * Marks
  * Grade
* Automatically calculate grades
* Print all students
* Print only passed students
* Print only failed students
* Clean and simple Python logic

---

## 📂 Data Structure

Each student is stored as a dictionary:

```python
{
    "Name": "Riya",
    "Roll Number": 12,
    "Marks": 87,
    "Grades": "B+"
}
```

All students go into a list:

```python
student_lst = []
```

---

## 🧾 Project Code

```python
# Count the number students
num_of_students = int(input("Enter Total Students: ")) 

# Data Store
student_lst = []
for i in range(num_of_students):
    print(i+1)
    name = input("Name: ")
    roll_num = int(input("Roll Number: "))
    Marks = int(input("Marks: "))

    # Grades Calculation
    if Marks >= 95:
        grades = 'A+'
    elif Marks >= 80:
        grades = 'B+'
    elif Marks >= 60:
        grades = 'C'
    else:
        grades = 'D'

    Students_Data = {
        'Name': name,
        'Roll Number': roll_num,
        'Marks': Marks,
        'Grades': grades
    }

    student_lst.append(Students_Data)

# Print Passed Students
print("\n----- PASSED STUDENTS -----")
for k in student_lst:
    if k['Marks'] >= 60:
        print(f"\nName : {k['Name']}\nRoll Number : {k['Roll Number']}\nMarks : {k['Marks']}\nGrades : {k['Grades']}")

# Print Failed Students
print("\n----- FAILED STUDENTS -----")
for k in student_lst:
    if k['Marks'] < 60:
        print(f"\nName : {k['Name']}\nRoll Number : {k['Roll Number']}\nMarks : {k['Marks']}\nGrades : {k['Grades']}")
```

---

## 🛠 Technologies Used

* Python (core)
* Lists
* Dictionaries
* Loops
* Conditions

---

## 🚀 How to Run

```
python student_result.py
```

---

## 📸 Sample Output

```
Enter Total Students: 2

1
Name: Ayesha
Roll Number: 10
Marks: 92

2
Name: Rahul
Roll Number: 21
Marks: 45

----- PASSED STUDENTS -----
Name: Ayesha
Roll Number: 10
Marks: 92
Grades: B+

----- FAILED STUDENTS -----
Name: Rahul
Roll Number: 21
Marks: 45
Grades: D
```

---

---

# ✅ **Sales Data Analysis (Python – No Libraries)**

## 📊 Sales Data Analysis (Python)

A beginner-friendly Sales Data Analysis project built using **pure Python only** — no Pandas or external libraries.
This project helps practice loops, dictionaries, conditions, and basic logic building.

---

## ✨ Features

* Input multiple sales records
* Store:

  * Product Name
  * Price
  * Quantity
  * Revenue
* Calculate:

  * Total Revenue
  * Highest Sale
  * Lowest Sale
  * Average Revenue
* Filter sales by revenue
* Search by product name

---

## 📂 Data Structure

Each sale:

```python
{
    "Product": "Laptop",
    "Price": 50000,
    "Quantity": 2,
    "Revenue": 100000
}
```

All sales:

```python
sales_data = []
```

---

## 🧾 Project Code

```python
# Number of sales entries
n = int(input("Enter number of sales records: "))
sales_data = []

# Input
for i in range(n):
    print(f"\nRecord {i+1}")
    product = input("Product Name: ")
    price = int(input("Price: "))
    quantity = int(input("Quantity: "))
    revenue = price * quantity

    record = {
        "Product": product,
        "Price": price,
        "Quantity": quantity,
        "Revenue": revenue
    }

    sales_data.append(record)

# Total Revenue
total_rev = 0
for s in sales_data:
    total_rev += s["Revenue"]

print("\nTotal Revenue:", total_rev)

# Highest & Lowest Revenue
highest = sales_data[0]
lowest = sales_data[0]

for s in sales_data:
    if s["Revenue"] > highest["Revenue"]:
        highest = s
    if s["Revenue"] < lowest["Revenue"]:
        lowest = s

print("\nHighest Sale:", highest)
print("Lowest Sale:", lowest)

# Average Revenue
avg_rev = total_rev / len(sales_data)
print("\nAverage Revenue:", avg_rev)

# Filter: Sales above a limit
limit = int(input("\nShow sales above revenue: "))
for s in sales_data:
    if s["Revenue"] > limit:
        print(s)

# Search by Product Name
search_item = input("\nSearch product: ")
for s in sales_data:
    if s["Product"].lower() == search_item.lower():
        print(s)
```

---

## 🛠 Technologies Used

* Python (built-in)
* Lists
* Dictionaries
* Loops
* Conditional logic

---

## 🚀 How to Run

```
python sales_analysis.py
```

---

## 📸 Sample Output

```
Enter number of sales records: 2

Record 1
Product Name: Laptop
Price: 50000
Quantity: 2

Record 2
Product Name: Mouse
Price: 500
Quantity: 10

Total Revenue: 110000
Highest Sale: {'Product': 'Laptop', 'Price': 50000, 'Quantity': 2, 'Revenue': 100000}
Lowest Sale: {'Product': 'Mouse', 'Price': 500, 'Quantity': 10, 'Revenue': 5000}
```

---

