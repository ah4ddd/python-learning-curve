# **🔥 Python Lists – Complete Recap**

---

## **1️⃣ Grouping Data in Lists**

**Concept:** A list is a collection of items. Can hold numbers, strings, or even other lists.

```python
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4]
mixed = ["apple", 10, True]
```

* **Indexing:** Access by position

  ```python
  print(fruits[0])  # apple
  print(numbers[2]) # 3
  ```
* **Negative indexing:** Count from the end

  ```python
  print(fruits[-1]) # orange
  ```
* **Nested lists:** Lists inside lists

  ```python
  nested = [[1, 2], [3, 4]]
  print(nested[1][0]) # 3
  ```

**Memory view:** Each element has a slot in the list object; nested lists are references to other lists.

---

## **2️⃣ Changing Data in Lists**

* Replace elements using index:

```python
fruits[0] = "mango"
print(fruits)  # ['mango', 'banana', 'orange']
```

* Add items: `.append()` adds one item at end

```python
fruits.append("grape")
```

* Add multiple items: `.extend()` adds elements of another list

```python
fruits.extend(["kiwi", "pineapple"])
```

* Insert at specific index:

```python
fruits.insert(1, "pear")  # index 1
```

* Remove items:

```python
fruits.remove("banana")
popped_item = fruits.pop()  # removes last element
```

---

## **3️⃣ Updating Lists**

* **Slicing to update multiple elements**

```python
numbers = [1, 2, 3, 4, 5]
numbers[1:3] = [20, 30]  # replace 2 and 3
```

* **Clear entire list**

```python
numbers.clear()
```

* **Copy list**

```python
copy_numbers = numbers.copy()
```

---

## **4️⃣ Organizing Data 1 & 2 (Practice + Supercharge)**

* **Sorting**

```python
numbers = [4, 2, 9, 1]
numbers.sort()  # in-place sort
print(numbers)  # [1, 2, 4, 9]

sorted_numbers = sorted(numbers)  # returns a new sorted list
```

* **Reverse**

```python
numbers.sort(reverse=True)
```

* **Custom sort (lambda)**

```python
players = [["Alice", 50], ["Bob", 30]]
players.sort(key=lambda x: x[1], reverse=True)
# sorts by second element (score)
```

* **Min / Max**

```python
print(min(numbers))  # 1
print(max(numbers))  # 9
```

---

## **5️⃣ Looping over Lists**

* Simple loop

```python
for fruit in fruits:
    print(fruit)
```

* Loop with index

```python
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

* Nested loops for nested lists

```python
matrix = [[1,2],[3,4]]
for row in matrix:
    for col in row:
        print(col)
```

---

## **6️⃣ Deciding with Lists**

* Check membership

```python
if "apple" in fruits:
    print("Yes, apple exists")
```

* Conditional inside loops

```python
for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even")
```

---

## **7️⃣ Finding Extreme Data**

* **Min/Max on list**

```python
scores = [50, 80, 90, 70]
print(max(scores))  # 90
print(min(scores))  # 50
```

* **Manual way (loop)**

```python
max_score = scores[0]
for s in scores:
    if s > max_score:
        max_score = s
```

---

## **8️⃣ Sorting Data**

* In-place sort with `sort()`
* Out-of-place with `sorted()`
* Reverse with `reverse=True`
* Custom key with lambda: `key=lambda x: x[1]`

**Memory:** `sort()` changes the list in memory, `sorted()` makes a copy.

---

## **9️⃣ Summing Data**

* **Simple sum**

```python
numbers = [1, 2, 3]
total = sum(numbers)  # 6
```

* **Nested lists**

```python
sales = [[5, 10], [3, 7]]
overall_total = sum(sum(day) for day in sales)
```

* **Conditional sum**

```python
numbers = [1, 2, 3, 4]
even_total = sum(x for x in numbers if x % 2 == 0)
```

---

## **🔟 Using Lists 1 (Practice + Supercharge)**

* Combining different skills:

  * Indexing
  * Loops
  * Sum / Max / Min
  * Conditional operations

---

## **1️⃣1️⃣ Joining Lists**

* Concatenation

```python
list1 = ["a", "b"]
list2 = ["c", "d"]
combined = list1 + list2  # ['a', 'b', 'c', 'd']
```

* Extending

```python
list1.extend(list2)
```

* Joining into string

```python
words = ["Hello", "World"]
sentence = " ".join(words)  # "Hello World"
```

* Separator can be any string

```python
"-".join(words)  # "Hello-World"
```

---

## **1️⃣2️⃣ Counting Elements**

* **List `.count()`**

```python
fruits = ["apple", "banana", "apple"]
print(fruits.count("apple"))  # 2
```

* **Manual counting with loop**

```python
count_dict = {}
for f in fruits:
    if f in count_dict:
        count_dict[f] += 1
    else:
        count_dict[f] = 1
```

* **Collections Counter**

```python
from collections import Counter
counter_fruits = Counter(fruits)
# Counter({'apple': 2, 'banana': 1})
```

* **Find top / least**

```python
top_seller = counter_fruits.most_common(1)[0]
```

* **Set for unique items**

```python
unique_fruits = set(fruits)
```

**Memory:** `.count()` scans the list every time. `Counter` stores counts in memory and is much faster for large lists.

---

## ✅ Summary of What You’ve Learned

* Creation, access, modification of lists ✅
* Loops, conditional operations ✅
* Sorting (basic & custom) ✅
* Summing & aggregating ✅
* Joining / combining lists ✅
* Counting elements ✅

**Blunt truth:** This is **all core Python list knowledge you’ll ever need for basic to intermediate work**. After this, we move to **tuples, sets, dictionaries**, which are crucial for real projects, databases, and data processing.

---

