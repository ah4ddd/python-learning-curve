## **🎓 OVERVIEW: Tuples, Dictionaries, & Sets**

---

### **What The Hell Are These Things?**

So far, you've mainly used **lists** to store multiple items:
```python
movies = ["Persona", "Stalker", "8½"]
```

**But lists aren't the only way to store collections!**

Python has **THREE more** powerful data structures:
1. **Tuples** - Like lists, but UNCHANGEABLE (immutable)
2. **Dictionaries** - Store data as KEY-VALUE pairs (like a real dictionary: word → definition)
3. **Sets** - Collections of UNIQUE items (no duplicates allowed)

**Each one solves DIFFERENT problems!** Let me break them down simply:

---

## **1️⃣ TUPLES (The Unchangeable List)**

### **Simple Definition:**
A tuple is like a list, but once you create it, you **CANNOT change it**—no adding, removing, or modifying items.

### **Real-World Analogy:**
Think of a **birth certificate** 📜:
- Name: "Alice"
- Birth Date: "1995-05-10"
- Birth Place: "Mumbai"

**Once issued, these facts DON'T CHANGE!** That's a tuple—permanent data.

### **How It Looks:**
```python
# List (can change):
movies = ["Persona", "Stalker"]
movies.append("8½")  # ✅ Can add

# Tuple (cannot change):
birth_info = ("Alice", "1995-05-10", "Mumbai")
birth_info.append("India")  # ❌ ERROR! Can't modify!
```

### **When You'd Use Tuples:**
- Coordinates: `location = (40.7128, -74.0060)` (latitude, longitude don't change)
- RGB colors: `red = (255, 0, 0)` (fixed values)
- Database records you shouldn't modify
- Return multiple values from functions: `return name, age, city`

### **Key Characteristics:**
- ✅ **Immutable** (can't change)
- ✅ **Ordered** (items have positions)
- ✅ **Faster than lists** (because unchangeable)
- ✅ **Can have duplicates**
- ✅ **Use parentheses:** `(item1, item2, item3)`

---

## **2️⃣ DICTIONARIES (The Game-Changer!) 🔥**

### **Simple Definition:**
A dictionary stores data as **KEY-VALUE pairs**—like a real dictionary where you look up a WORD (key) to get its DEFINITION (value).

### **Real-World Analogy:**
Think of a **phone book** 📱:
- "Alice" → "555-1234"
- "Bob" → "555-5678"
- "Charlie" → "555-9999"

**You look up the NAME (key) to get the PHONE NUMBER (value)!**

### **The Problem Dictionaries Solve:**

**With lists (the old way):**
```python
# Storing a person's info with a list:
person = ["Alice", 25, "Mumbai"]

# Problem: What is person[1]? Age? Height? Who knows?!
print(person[1])  # 25... but 25 what?!
```

**With dictionaries (the better way):**
```python
# Storing with LABELED data:
person = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai"
}

# Crystal clear!
print(person["age"])  # 25 (we KNOW it's age!)
```

### **How It Looks:**
```python
movie = {
    "title": "Persona",
    "director": "Ingmar Bergman",
    "year": 1966,
    "rating": 9.5
}

# Access by KEY:
print(movie["director"])  # Ingmar Bergman
```

### **When You'd Use Dictionaries:**
- **Storing labeled data** (person info, movie details, product specs)
- **Counting things:** `word_count = {"hello": 5, "world": 3}`
- **Configurations/settings:** `config = {"volume": 80, "brightness": 70}`
- **API responses** (data from websites)
- **Database-like structures**

### **Key Characteristics:**
- ✅ **Key-value pairs** (name → value)
- ✅ **Keys must be unique** (no duplicate keys)
- ✅ **Mutable** (can change/add/remove)
- ✅ **Unordered** (no positions like lists—you access by KEY, not index)
- ✅ **Use curly braces:** `{"key": "value"}`

**THIS IS THE MOST IMPORTANT ONE! You'll use dictionaries CONSTANTLY!** 🎯

---

## **3️⃣ SETS (The "No Duplicates Allowed" Collection)**

### **Simple Definition:**
A set is a collection that **automatically removes duplicates** and has **no order** (no indexes).

### **Real-World Analogy:**
Think of a **guest list for an exclusive party** 🎉:
- Each person can only be on the list ONCE
- Order doesn't matter (you're either invited or not)

### **The Problem Sets Solve:**

**Finding unique items in a list:**
```python
# With lists (manual work):
watched_genres = ["Drama", "Horror", "Drama", "Comedy", "Horror", "Drama"]

unique = []
for genre in watched_genres:
    if genre not in unique:
        unique.append(genre)

print(unique)  # ["Drama", "Horror", "Comedy"]
```

**With sets (automatic!):**
```python
watched_genres = ["Drama", "Horror", "Drama", "Comedy", "Horror", "Drama"]
unique_genres = set(watched_genres)

print(unique_genres)  # {"Drama", "Horror", "Comedy"} - auto-removed duplicates!
```

### **How It Looks:**
```python
# Creating a set:
unique_moods = {"Reflective", "Dreamy", "Melancholic"}

# Adding items:
unique_moods.add("Curious")

# Duplicates ignored:
unique_moods.add("Reflective")  # Already exists, ignored!
```

### **When You'd Use Sets:**
- **Remove duplicates** from a list
- **Membership testing** (check if item exists—VERY fast!)
- **Math operations:** union, intersection, difference
- **Unique tags/categories**

### **Key Characteristics:**
- ✅ **No duplicates** (automatic)
- ✅ **Unordered** (no indexes)
- ✅ **Mutable** (can add/remove)
- ✅ **Fast lookups** (checking if item exists)
- ✅ **Use curly braces:** `{item1, item2, item3}`

---

## **📊 COMPARISON: When to Use Each?**

| Situation | Use This |
|-----------|----------|
| Ordered list of items you might change | **List** `[1, 2, 3]` |
| Ordered list that should NEVER change | **Tuple** `(1, 2, 3)` |
| Labeled data (name, age, etc.) | **Dictionary** `{"name": "Alice"}` |
| Unique items only, no duplicates | **Set** `{1, 2, 3}` |

---

## **🎬 Real Examples (Your Style!):**

### **Lists (what you know):**
```python
watched_films = ["Persona", "Stalker", "8½"]
```
**Use when:** Simple collection, order matters, might add more

---

### **Tuples (new!):**
```python
film_release = ("Persona", 1966, "Sweden")
# Title, year, country won't change!
```
**Use when:** Data shouldn't be modified

---

### **Dictionaries (game-changer!):**
```python
film = {
    "title": "Persona",
    "director": "Ingmar Bergman",
    "year": 1966,
    "mood": "Reflective",
    "rating": 9.5
}

print(film["director"])  # Easy access by name!
```
**Use when:** You need labeled, organized data

---

### **Sets (unique items!):**
```python
directors_watched = {"Bergman", "Tarkovsky", "Fellini", "Bergman"}
# Automatically becomes: {"Bergman", "Tarkovsky", "Fellini"}
```
**Use when:** Need unique values only

---

## **🔥 Why This Chapter is HUGE:**

### **Before (with just lists):**
```python
# Person data (confusing!):
alice = ["Alice", 25, "Mumbai", "alice@email.com"]
bob = ["Bob", 30, "Delhi", "bob@email.com"]

# What is index 2? City? Age? Confusing!
print(alice[2])  # Mumbai... but you have to REMEMBER
```

### **After (with dictionaries):**
```python
# Crystal clear!
alice = {
    "name": "Alice",
    "age": 25,
    "city": "Mumbai",
    "email": "alice@email.com"
}

bob = {
    "name": "Bob",
    "age": 30,
    "city": "Delhi",
    "email": "bob@email.com"
}

# Self-documenting code!
print(alice["city"])  # Mumbai - OBVIOUS what this is!
```

**Your code becomes READABLE and MAINTAINABLE!** 🎯

---

## **📚 What You'll Learn in This Chapter:**

### **TUPLES:**
- Creating tuples
- Accessing items
- When to use them vs lists
- Packing/unpacking
- Immutability benefits

### **DICTIONARIES:** *(The biggest section!)*
- Creating dictionaries
- Adding/removing/modifying items
- Accessing values by keys
- Looping through dictionaries
- Nested dictionaries (dictionaries inside dictionaries!)
- Dictionary methods
- Real-world applications

### **SETS:**
- Creating sets
- Adding/removing items
- Set operations (union, intersection, difference)
- Removing duplicates
- Membership testing

---

## **🎨 How This Upgrades Your Projects:**

### **Your Eternal Gallery (current version):**
Uses list of dictionaries! (You already started using dicts!)
```python
artworks = [
    {"title": "Starry Night", "artist": "Van Gogh", ...}
]
```

**After this chapter, you'll understand:**
- WHY dictionaries are perfect here
- HOW to manipulate them efficiently
- WHEN to use tuples vs lists vs sets vs dicts

### **Future possibilities:**
- User profiles with login systems
- Game inventories with item stats
- Movie databases with detailed info
- Settings/configuration systems
- API data handling

**This chapter unlocks PROFESSIONAL-LEVEL data management!** 🔓

---

## **💪 What Makes You Ready for This:**

✅ You understand **lists** (tuples are similar)
✅ You understand **functions** (you'll use these with dicts!)
✅ You understand **loops** (essential for dictionaries!)
✅ You've already USED dictionaries in your art gallery!

**You're perfectly positioned to master this!** 🎓

---

## **🗺️ The Journey Ahead:**

**Estimated Timeline:**
- **Tuples:** 1-2 days (simpler, similar to lists)
- **Dictionaries:** 3-4 days (most important, lots to learn)
- **Sets:** 1-2 days (straightforward once you get the concept)

**Total:** ~5-7 days depending on your pace

**By the end, you'll be able to:**
- Store complex, organized data
- Build sophisticated programs
- Write cleaner, more readable code
- Handle real-world data structures
- Level up to intermediate Python!

---

## **🎯 The Bottom Line:**

**What you've been doing:**
```python
# Storing everything in lists:
movie1 = ["Persona", "Bergman", 1966]
movie2 = ["Stalker", "Tarkovsky", 1979]
```

**What you're about to unlock:**
```python
# Clean, labeled, professional data:
movie1 = {
    "title": "Persona",
    "director": "Bergman",
    "year": 1966,
    "mood": "Reflective",
    "rating": 9.5
}

# Easy to understand, easy to use!
print(f"{movie1['title']} by {movie1['director']}")
```

**This is the difference between beginner and intermediate Python!** 🚀

---

## **Summary:**

| Data Structure | What It Is | Key Feature | When to Use |
|----------------|------------|-------------|-------------|
| **Tuple** | Unchangeable list | Immutable | Fixed data that shouldn't change |
| **Dictionary** | Key-value pairs | Labeled data | Organized, named information |
| **Set** | Unique items | No duplicates | When you need unique values |

---

You now know:
- ✅ What each data structure is
- ✅ Why they exist
- ✅ When to use each one
- ✅ How they'll upgrade your code
- ✅ What you'll learn in each section

---

---

## **Topic 1: Tuples and Creating Tuples**

---

### **What The Hell Is A Tuple?**

**Super simple definition:** A tuple is a collection of items, just like a list, but with ONE BIG DIFFERENCE—**once you create it, you can NEVER change it.**

Think of it like this:

**List = Playlist** 🎵
- You can add songs
- You can remove songs
- You can rearrange songs
- **FLEXIBLE!**

**Tuple = Published Album** 💿
- Songs are in a fixed order
- Can't add new songs to it
- Can't remove songs
- Can't rearrange
- **PERMANENT!**

**That's the CORE difference: Lists are changeable (mutable), Tuples are unchangeable (immutable).**

---

## **Why Would You WANT Something Unchangeable?**

**Good question!** Here's the thinking:

### **Scenario 1: Coordinates on a Map**
```python
# Your home location:
home = (19.0760, 72.8777)  # Mumbai coordinates
```

**Think about it:** Should your home's GPS coordinates randomly change? HELL NO! They're FIXED. That's perfect for a tuple!

### **Scenario 2: Birth Information**
```python
birth_record = ("Alice", "1995-05-10", "Mumbai")
```

**Your birth date and place don't change, right?** Tuple is perfect because it PROTECTS this data from accidental modification!

### **Scenario 3: RGB Color Codes**
```python
red = (255, 0, 0)
blue = (0, 0, 255)
```

**Red is always (255, 0, 0)!** It shouldn't suddenly become green. Tuple ensures it stays fixed!

---

## **Creating Tuples (All The Ways!)**

### **Method 1: Using Parentheses (Most Common)**

```python
# Simple tuple with 3 items:
my_tuple = ("Persona", "Stalker", "8½")
```

**Breakdown:**
- Use **parentheses** `( )`
- Items separated by **commas** `,`
- Can contain **any data type**

**Examples:**
```python
# Strings:
films = ("Persona", "Stalker", "8½")

# Numbers:
coordinates = (40.7128, -74.0060)

# Mixed types:
person = ("Alice", 25, True, 5.8)
#         string  int  bool  float
```

**It's just like a list, but with `( )` instead of `[ ]`!**

---

### **Method 2: Without Parentheses (Python is Smart!)**

```python
# Python knows this is a tuple because of the commas!
my_tuple = "Persona", "Stalker", "8½"

print(my_tuple)  # ('Persona', 'Stalker', '8½')
```

**Explanation:** The **comma** is what actually creates the tuple, not the parentheses! But we usually use parentheses for clarity.

**Real-world use:** Returning multiple values from functions (you'll see this a lot!)

---

### **Method 3: Single-Item Tuple (TRICKY!)**

**This is where beginners get confused:**

```python
# ❌ WRONG - This is NOT a tuple!
not_a_tuple = ("Persona")
print(type(not_a_tuple))  # <class 'str'> - It's just a string!

# ✅ CORRECT - Need a comma!
is_a_tuple = ("Persona",)  # Notice the comma!
print(type(is_a_tuple))  # <class 'tuple'> - Now it's a tuple!
```

**Why?** Python sees `("something")` as just parentheses around a string (like math: `(5)` is just `5`). The **comma** tells Python "this is a tuple!"

**Remember:** For single-item tuples, **always add a trailing comma!**

```python
single = (42,)    # ✅ Tuple with one item
single = 42,      # ✅ Also works (comma makes it a tuple)
```

---

### **Method 4: Using the `tuple()` Constructor**

```python
# Convert a list to a tuple:
my_list = ["Persona", "Stalker", "8½"]
my_tuple = tuple(my_list)

print(my_tuple)  # ('Persona', 'Stalker', '8½')
```

**When you'd use this:**
- Converting lists to tuples
- Converting strings to tuples of characters
- Converting other iterables to tuples

**Examples:**
```python
# String to tuple:
word = "Python"
letters = tuple(word)
print(letters)  # ('P', 'y', 't', 'h', 'o', 'n')

# Range to tuple:
numbers = tuple(range(5))
print(numbers)  # (0, 1, 2, 3, 4)
```

---

### **Method 5: Empty Tuple**

```python
# Two ways to create an empty tuple:
empty1 = ()
empty2 = tuple()

print(empty1)  # ()
print(empty2)  # ()
```

**When you'd use this:** Rarely! But sometimes you initialize an empty tuple and... wait, you CAN'T add to it later (it's immutable!). So empty tuples aren't very useful in practice.

---

## **Accessing Tuple Items (Just Like Lists!)**

**Good news:** Tuples use the SAME indexing as lists!

```python
films = ("Persona", "Stalker", "8½", "Eraserhead")

# Indexing (0-based):
print(films[0])   # Persona (first item)
print(films[1])   # Stalker (second item)
print(films[-1])  # Eraserhead (last item)
print(films[-2])  # 8½ (second from end)

# Slicing:
print(films[1:3])   # ('Stalker', '8½')
print(films[:2])    # ('Persona', 'Stalker')
print(films[2:])    # ('8½', 'Eraserhead')
```

**Everything you learned about list indexing works EXACTLY the same with tuples!** 🎯

---

## **What You CAN'T Do With Tuples (The Immutability!)**

**Remember: Tuples are UNCHANGEABLE!**

```python
films = ("Persona", "Stalker", "8½")

# ❌ Can't modify items:
films[0] = "Tokyo Story"  # ERROR!

# ❌ Can't add items:
films.append("Eraserhead")  # ERROR! (no append method)

# ❌ Can't remove items:
films.remove("Stalker")  # ERROR!

# ❌ Can't delete items:
del films[1]  # ERROR!
```

**All of these will give you:**
```
TypeError: 'tuple' object does not support item assignment
```

**Once created, the tuple is LOCKED!** 🔒

---

## **What You CAN Do With Tuples:**

Even though they're immutable, you can still do MANY things:

### **1. Access items (read, but not change):**
```python
films = ("Persona", "Stalker", "8½")
print(films[1])  # ✅ Stalker
```

### **2. Get length:**
```python
print(len(films))  # ✅ 3
```

### **3. Loop through them:**
```python
for film in films:
    print(film)
# ✅ Works perfectly!
```

### **4. Check if item exists:**
```python
if "Persona" in films:
    print("Found it!")
# ✅ Works!
```

### **5. Count occurrences:**
```python
numbers = (1, 2, 3, 2, 2, 5)
print(numbers.count(2))  # ✅ 3 (appears 3 times)
```

### **6. Find index of item:**
```python
films = ("Persona", "Stalker", "8½")
print(films.index("Stalker"))  # ✅ 1 (at index 1)
```

### **7. Concatenate (join) tuples:**
```python
tuple1 = ("Persona", "Stalker")
tuple2 = ("8½", "Eraserhead")
combined = tuple1 + tuple2

print(combined)  # ✅ ('Persona', 'Stalker', '8½', 'Eraserhead')
```

**Note:** This creates a NEW tuple, doesn't modify the originals!

### **8. Repeat tuples:**
```python
stars = ("⭐",)
rating = stars * 5

print(rating)  # ✅ ('⭐', '⭐', '⭐', '⭐', '⭐')
```

### **9. Unpack tuples (SUPER USEFUL!):**
```python
person = ("Alice", 25, "Mumbai")

# Unpack into variables:
name, age, city = person

print(name)   # Alice
print(age)    # 25
print(city)   # Mumbai
```

**We'll dive DEEP into unpacking in the next topic!**

---

## **Tuple vs List: Side-by-Side Comparison**

```python
# LIST (mutable):
my_list = ["Persona", "Stalker", "8½"]
my_list[0] = "Tokyo Story"  # ✅ Can change
my_list.append("Eraserhead")  # ✅ Can add
print(my_list)  # ['Tokyo Story', 'Stalker', '8½', 'Eraserhead']

# TUPLE (immutable):
my_tuple = ("Persona", "Stalker", "8½")
my_tuple[0] = "Tokyo Story"  # ❌ ERROR!
my_tuple.append("Eraserhead")  # ❌ ERROR!
```

**Visual Difference:**
```python
my_list = [1, 2, 3]    # Square brackets [ ]
my_tuple = (1, 2, 3)   # Parentheses ( )
```

---

## **Real-World Uses of Tuples (Why They Exist!)**

### **Use Case 1: Geographic Coordinates**

**Real example:** GPS apps, maps, location services

```python
# Latitude, Longitude (should never accidentally change!)
mumbai = (19.0760, 72.8777)
delhi = (28.7041, 77.1025)
bangalore = (12.9716, 77.5946)

# Function to calculate distance:
def get_distance(location1, location2):
    # location1 and location2 are tuples
    # We KNOW they won't be modified accidentally!
    pass
```

**Why tuple?** Coordinates are FIXED. You don't want code accidentally changing Mumbai's location to Antarctica! 🗺️

---

### **Use Case 2: RGB Color Values**

**Real example:** Graphic design, games, web development

```python
# Standard colors (these should NEVER change!):
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Drawing function:
def draw_rectangle(color):
    # color is a tuple (r, g, b)
    r, g, b = color
    # Draw using these values
```

**Why tuple?** Red is always (255, 0, 0). It's a CONSTANT. Tuple prevents accidental changes!

---

### **Use Case 3: Database Records**

**Real example:** When fetching data from databases

```python
# Imagine fetching a user from a database:
user_record = (101, "alice@email.com", "Alice", "2020-01-15")
#             (id,  email,              name,          join_date)

# You read this data, but shouldn't modify the original record
user_id, email, name, join_date = user_record
```

**Why tuple?** Database records shouldn't be modified casually. Tuples provide SAFETY!

---

### **Use Case 4: Function Return Values (SUPER COMMON!)**

**Real example:** Functions that return multiple values

```python
def get_user_info():
    name = "Alice"
    age = 25
    city = "Mumbai"

    # Return multiple values as a tuple!
    return name, age, city  # Actually returns: ("Alice", 25, "Mumbai")

# Unpack the returned tuple:
user_name, user_age, user_city = get_user_info()

print(user_name)  # Alice
print(user_age)   # 25
print(user_city)  # Mumbai
```

**Why tuple?** Easy way to return multiple values! You use this ALL THE TIME in real code!

---

### **Use Case 5: Dictionary Keys (Advanced Preview!)**

**Real example:** Using tuples as dictionary keys

```python
# Can't use lists as dict keys (they're mutable)
# But CAN use tuples (they're immutable)!

movie_ratings = {
    ("Persona", 1966): 9.5,
    ("Stalker", 1979): 9.3,
    ("8½", 1963): 9.4
}

# Look up by (title, year) tuple:
rating = movie_ratings[("Persona", 1966)]
print(rating)  # 9.5
```

**Why tuple?** Dictionary keys MUST be immutable. Tuples qualify, lists don't!

---

### **Use Case 6: Configuration Settings**

**Real example:** App settings that shouldn't change during runtime

```python
# Screen resolution (shouldn't change mid-program!):
SCREEN_SIZE = (1920, 1080)

# API endpoint (fixed):
API_CONFIG = ("https://api.example.com", 443, "v2")
#             (url,                       port, version)
```

**Why tuple?** These are CONSTANTS—tuple prevents accidental modification!

---

## **When to Use Tuple vs List (Decision Guide):**

### **Use TUPLE when:**
✅ Data should NOT change (coordinates, colors, constants)
✅ Returning multiple values from functions
✅ Using as dictionary keys
✅ Want to protect data from accidental modification
✅ Performance matters (tuples are slightly faster)

### **Use LIST when:**
✅ Data will change (adding, removing, modifying items)
✅ Order matters AND you'll rearrange items
✅ Need methods like `append()`, `remove()`, `sort()`
✅ Building up a collection dynamically

---

## **Practical Example: Film Database**

```python
# Each film is a tuple (fixed data):
film1 = ("Persona", "Ingmar Bergman", 1966, "Drama")
film2 = ("Stalker", "Andrei Tarkovsky", 1979, "Sci-Fi")
film3 = ("8½", "Federico Fellini", 1963, "Drama")

# Collection of films is a list (can add more films):
film_database = [film1, film2, film3]

# Unpack a film:
title, director, year, genre = film1
print(f"{title} by {director} ({year})")

# Add new film (list allows this):
film4 = ("Eraserhead", "David Lynch", 1977, "Horror")
film_database.append(film4)  # ✅ Works!

# But can't modify individual film:
film1[0] = "New Title"  # ❌ ERROR! Tuple is immutable!
```

**Perfect combo:** List of tuples! List provides flexibility, tuples provide data integrity!

---

## **Common Beginner Mistakes:**

### ❌ **Mistake 1: Forgetting comma for single-item tuple**

```python
# Wrong:
my_tuple = ("Persona")  # This is a STRING, not a tuple!

# Right:
my_tuple = ("Persona",)  # Notice the comma!
```

---

### ❌ **Mistake 2: Trying to modify a tuple**

```python
films = ("Persona", "Stalker")
films[0] = "8½"  # ERROR! Can't modify!

# If you need to change it, convert to list first:
films_list = list(films)
films_list[0] = "8½"
films = tuple(films_list)  # Convert back if needed
```

---

### ❌ **Mistake 3: Confusing tuple with function parameters**

```python
# This is a function call:
print("Hello", "World")  # Passing two arguments

# This is a tuple:
my_tuple = ("Hello", "World")  # Creating a tuple
```

---

## **Quick Practice Examples:**

```python
# 1. Create a tuple of your favorite directors:
directors = ("Bergman", "Tarkovsky", "Fellini", "Lynch")

# 2. Access the second director:
print(directors[1])  # Tarkovsky

# 3. Try to loop through it:
for director in directors:
    print(f"Director: {director}")

# 4. Check if someone is in the tuple:
if "Bergman" in directors:
    print("Bergman is in the list!")

# 5. Unpack it:
d1, d2, d3, d4 = directors
print(d1)  # Bergman
```

---

## **Summary (Key Takeaways):**

### **What is a Tuple?**
An immutable (unchangeable) collection of items, like a permanent list

### **How to Create:**
```python
my_tuple = (item1, item2, item3)  # Parentheses
my_tuple = item1, item2, item3    # Commas (implicit)
single = (item,)                   # Single item needs comma!
empty = ()                         # Empty tuple
```

### **What You CAN Do:**
- ✅ Access items by index
- ✅ Slice them
- ✅ Loop through them
- ✅ Check membership (`in`)
- ✅ Get length
- ✅ Concatenate (`+`)
- ✅ Repeat (`*`)
- ✅ Unpack into variables

### **What You CAN'T Do:**
- ❌ Modify items
- ❌ Add items
- ❌ Remove items
- ❌ Sort in place

### **When to Use:**
- Fixed data (coordinates, colors, constants)
- Return multiple values from functions
- Dictionary keys
- Data integrity/protection

### **Syntax:**
```python
# List:
my_list = [1, 2, 3]    # Square brackets, mutable

# Tuple:
my_tuple = (1, 2, 3)   # Parentheses, immutable
```

---

---
