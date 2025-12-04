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


Here you go — **a clean, ready-to-upload README.md** that includes your entire explanation + all 10 solutions exactly as you wrote them.

This is formatted professionally for GitHub.
Just copy–paste into your `README.md`.

---

# 📊 Sales Data Analysis Using Pure Python

This project solves **10 important data analysis queries** using **ONLY core Python** (lists, loops, dictionaries).
No pandas. No numpy. Perfect for beginners learning Python logic & data processing.

---
📝 Important Note

⚠ The .ipynb Jupyter Notebook code may not appear correctly on GitHub sometimes.
If it doesn’t load, you can read the full code directly from this README.

## 📁 Dataset

Assuming your cleaned data `newData` looks like this:

```python
newData = [
 ['1001', '2023-02-17', 'Rohit Gupta', 'Chair', 'Furniture', 2, 1999],
 ['1002', '2023-03-04', 'Amit Sharma', 'Marker', 'Stationery', 4, 35],
 ['1003', '2023-08-31', 'Rahul Mehta', 'Headphones', 'Electronics', 2, 1299]
]
```

Where:

| Index | Meaning  |
| ----- | -------- |
| 0     | OrderID  |
| 1     | Date     |
| 2     | Customer |
| 3     | Product  |
| 4     | Category |
| 5     | Quantity |
| 6     | Price    |

---

# ✅ 1. **Total revenue from all sales**

Revenue = Quantity × Price

```python
total_revenue = 0
for row in newData:
    total_revenue += row[5] * row[6]

print(total_revenue)
```

---

# ✅ 2. **Total orders placed**

```python
total_orders = len(newData)
print(total_orders)
```

---

# ✅ 3. **Total quantity sold**

```python
total_quantity = 0
for row in newData:
    total_quantity += row[5]

print(total_quantity)
```

---

# ✅ 4. **Total revenue by each category**

```python
category_revenue = {}

for row in newData:
    cat = row[4]
    revenue = row[5] * row[6]

    if cat not in category_revenue:
        category_revenue[cat] = 0
    category_revenue[cat] += revenue

print(category_revenue)
```

---

# ✅ 5. **Total revenue by each product**

```python
product_revenue = {}

for row in newData:
    product = row[3]
    revenue = row[5] * row[6]

    if product not in product_revenue:
        product_revenue[product] = 0
    product_revenue[product] += revenue

print(product_revenue)
```

---

# ✅ 6. **Product with highest quantity sold**

```python
product_quantity = {}

for row in newData:
    product = row[3]
    qty = row[5]

    if product not in product_quantity:
        product_quantity[product] = 0
    product_quantity[product] += qty

max_product = max(product_quantity, key=product_quantity.get)

print(max_product, product_quantity[max_product])
```

---

# ✅ 7. **Customer who spent the most**

```python
customer_spend = {}

for row in newData:
    customer = row[2]
    revenue = row[5] * row[6]

    if customer not in customer_spend:
        customer_spend[customer] = 0
    customer_spend[customer] += revenue

top_customer = max(customer_spend, key=customer_spend.get)

print(top_customer, customer_spend[top_customer])
```

---

# ✅ 8. **Total revenue per date**

```python
date_revenue = {}

for row in newData:
    date = row[1]
    revenue = row[5] * row[6]

    if date not in date_revenue:
        date_revenue[date] = 0
    date_revenue[date] += revenue

print(date_revenue)
```

---

# ✅ 9. **Total revenue between two dates**

Example input:

```python
start_date = "2023-03-01"
end_date = "2023-08-31"
```

Code:

```python
total = 0

for row in newData:
    date = row[1]

    if start_date <= date <= end_date:
        total += row[5] * row[6]

print(total)
```

---

# ✅ 10. **Export 'Electronics' category to CSV (without pandas)**

```python
electronics = []

for row in newData:
    if row[4] == "Electronics":
        electronics.append(row)

with open("electronics.csv", "w") as f:
    f.write("OrderID,Date,Customer,Product,Category,Quantity,Price\n")
    for row in electronics:
        line = ",".join([str(item) for item in row])
        f.write(line + "\n")
```

---

# 🎉 Done!


