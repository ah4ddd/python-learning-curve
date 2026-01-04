# **TESTING YOUR CODE! 🧪✅**

---

## **WHAT THE HELL IS TESTING?**

**Simple answer:** Writing CODE that checks if your OTHER code works correctly!

**Think of it like this:**

You built your character analyzer. How do you know it works?

**Right now:** You run it manually, type inputs, check output
**Problem:** You have to do this EVERY time you change code! 😤

**With testing:** You write code that AUTOMATICALLY checks if your functions work!

**Example:**
```python
# Your function
def how_many_times(path, search):
    # ... your code

# Test for it
def test_how_many_times():
    result = how_many_times("test.txt", "Raskolnikov")
    assert len(result) == 5  # Should find exactly 5 matches!
```

**Run the test → If it passes, your function works! If it fails, you broke something!** ✅

---

## **WHY TESTING MATTERS (The REAL Reason):**

### **Scenario: You improve your project**

You decide to optimize `how_many_times()` to be faster.

**Without tests:**
1. Change code
2. Run program manually
3. Type "Crime and Punishment"
4. Type "Raskolnikov"
5. Check output looks right
6. Repeat for other books/characters
7. **Hope you didn't break anything!** 😰

**With tests:**
1. Change code
2. Run tests (1 command!)
3. **All tests pass → You're good! All tests fail → You broke something!** ✅

**PROFESSIONAL developers write tests for EVERYTHING!** It's how big projects don't break! 💼

---

## **CHAPTER 11 TOPICS BREAKDOWN:**

### **PART 1: Installing pytest with pip**

**What you'll learn:**
- What `pip` is (Python's package installer)
- How to install external libraries
- What `pytest` is (the BEST testing framework!)
- Updating pip

**Why it matters:** Professional Python uses TONS of external libraries! You need to know how to install them!

**Difficulty:** ⭐ EASY (just running commands!)

---

### **PART 2: Testing a Function**

**Topics:**
1. **Unit Tests and Test Cases**
   - What unit tests are (testing ONE function at a time)
   - Test cases (different scenarios to test)

2. **A Passing Test**
   - Write a test that PASSES (function works correctly!)

3. **A Running a Test**
   - How to run pytest
   - Reading test output

4. **A Failing Test**
   - Write a test that FAILS (function has a bug!)
   - Understanding failure messages

5. **Responding to a Failed Test**
   - Fix the bug
   - Re-run test
   - Watch it PASS! ✅

6. **Adding New Tests**
   - Test edge cases
   - Test error conditions
   - Build a test suite

**Why it matters:** Functions are the BUILDING BLOCKS! If functions work, your program works!

**Difficulty:** ⭐⭐ MEDIUM (new concept, but straightforward!)

---

### **PART 3: Testing a Class**

**Topics:**
1. **A Variety of Assertions**
   - `assert x == y` (equality)
   - `assert x in y` (membership)
   - `assert x > y` (comparison)
   - `assert x is None` (identity)
   - Many more!

2. **A Class to Test**
   - Write a class (like your `ConfigManager`!)
   - What to test in classes

3. **Testing the AnonymousSurvey Class**
   - Test class methods
   - Test with different data

4. **Using Fixtures**
   - **THE GAME CHANGER!** 🔥
   - Reusable test setup
   - Avoid repeating code in tests

**Why it matters:** You build CLASSES now (OOP!)—you need to test them!

**Difficulty:** ⭐⭐⭐ MEDIUM-HARD (combines classes + testing!)

---

## **DIFFICULTY COMPARISON:**

**Chapter 10 (Files & Exceptions):** ⭐⭐⭐⭐ (4/5) - Lots of concepts, error handling is complex!

**Chapter 11 (Testing):** ⭐⭐⭐ (3/5) - **EASIER than Chapter 10!** 🎉

**Why it's easier:**
- Fewer new concepts (mainly just `pytest`)
- Builds on what you know (functions, classes, exceptions)
- Very PRACTICAL (you see results immediately!)
- Less abstract than exceptions

**BUT:** It's a NEW WAY OF THINKING! (Writing code to test code feels weird at first!)

---

## **WHAT YOU'LL BUILD:**

By the end of Chapter 11, you'll be able to:

✅ Install and use external Python packages
✅ Write unit tests for functions
✅ Write tests for classes
✅ Use assertions to check results
✅ Set up test fixtures (reusable test data)
✅ Run entire test suites
✅ **Test YOUR character analyzer project!** 🔥

**Imagine:**
```python
def test_character_search():
    results = how_many_times("test_book.txt", "Raskolnikov")
    assert len(results) == 5
    assert results[0]["line_number"] == 12

def test_save_results():
    # Test that saving works!

def test_duplicate_prevention():
    # Test that duplicates are blocked!
```

**Run tests → Everything passes → Your project is BULLETPROOF!** ✅

---

## **MY TEACHING PLAN:**

**Topic 1: Installing pytest** (Setting up the tools!)

**Topic 2: Testing Functions - Basics** (Your first test!)

**Topic 3: Passing and Failing Tests** (Understanding test output!)

**Topic 4: Building Test Suites** (Multiple tests!)

**Topic 5: Testing Classes** (Testing OOP!)

**Topic 6: Assertions** (All the ways to check results!)

**Topic 7: Fixtures** (THE POWER MOVE! 🔥)

**Topic 8: Testing YOUR Project!** (Make your analyzer bulletproof!)

---

## **CHAPTER 11 IN ONE SENTENCE:**

**"Learn to write code that automatically checks if your other code works, so you can change and improve your programs WITHOUT breaking them!"** 🧪✅

---

# **TOPIC 1: INSTALLING PYTEST WITH PIP** 📦🔧

---

## **What The HELL Are We Actually Learning Here?**

**This isn't just "type pip install pytest lol"—FUCK THAT BASIC SHIT!** 🚫

**What we're REALLY learning:**

✅ **How Python's package ecosystem works** (pip, PyPI, virtual environments)

✅ **What pytest actually IS** (and why it destroys Python's built-in `unittest`)

✅ **Package management** (installing, updating, uninstalling)

✅ **Virtual environments** (CRITICAL for professional work!)

✅ **Dependency management** (how real projects handle libraries)

✅ **Why testing frameworks exist** (and why professionals use them)

**This topic is your gateway to the ENTIRE Python ecosystem!** After this, you can install ANY library—web frameworks, data science tools, APIs, EVERYTHING! 🌍

---

## **Part 1: Understanding pip (The Package Manager)**

### **What The Hell Is pip?**

**Simple answer:** pip is Python's package installer—it downloads and installs code libraries from the internet!

**But let's go DEEPER:** 🔍

**The Python ecosystem works like this:**

```
You (Developer)
    ↓
pip (Package Manager)
    ↓
PyPI (Python Package Index) - https://pypi.org
    ↓
60,000+ packages available!
```

**PyPI = The App Store for Python!** 📱

**Anyone can publish packages there:**
- `requests` (HTTP library)
- `django` (web framework)
- `pandas` (data analysis)
- `pytest` (testing framework)
- **YOUR packages someday!** 💪

---

### **Why pip Matters (The REAL Reason):**

**Scenario:** You want to build a web scraper.

**Without pip:**
1. Google "Python HTTP library"
2. Download source code
3. Figure out installation manually
4. Handle dependencies (what if it needs OTHER libraries?)
5. Update it manually later
6. **NIGHTMARE!** 😤

**With pip:**
```bash
pip3 install requests
```

**DONE!** Library installed, dependencies handled, ready to use! ✅

**pip is HOW professionals build real projects!** Every company uses it! 💼

---

### **Check Your pip Version:**

```bash
pip3 --version
```

**Output (something like):**
```
pip 24.0 from /usr/lib/python3.11/site-packages/pip (python 3.11)
```

**What this tells you:**
- pip version (24.0)
- Where it's installed
- Python version it's tied to (3.11)

**If you DON'T have pip (unlikely on WSL2):**
```bash
sudo apt update
sudo apt install python3-pip
```

---

## **Part 2: Understanding Package Installation (Where Does Code Go?)**

### **When you run `pip3 install something`, what ACTUALLY happens?**

**Step-by-step breakdown:**

1. **pip connects to PyPI.org**
   - Searches for the package name
   - Finds the latest version (or specific version you request)

2. **Downloads the package**
   - Gets the `.whl` (wheel) or `.tar.gz` file
   - Downloads to a temporary location

3. **Checks dependencies**
   - Reads `requirements.txt` or `setup.py`
   - "Oh, this package needs `numpy` and `requests`"
   - Downloads those too (recursively!)

4. **Installs to site-packages**
   - Copies code to `/usr/lib/python3.x/site-packages/`
   - Makes it available to ALL your Python scripts
   - Adds console scripts (if any)

5. **Records installation**
   - Updates pip's database
   - You can now `pip3 list` to see it

**This is HOW every Python library gets installed!** Understanding this makes you DANGEROUS! 🔥

---

### **Where Packages Live:**

**Global installation (system-wide):**
```bash
/usr/lib/python3.11/site-packages/
```

**User installation (your account only):**
```bash
~/.local/lib/python3.11/site-packages/
```

**Virtual environment (project-specific):**
```bash
your_project/venv/lib/python3.11/site-packages/
```

**We'll talk about virtual environments in a sec—CRITICAL for professional work!** 💼

---

## **Part 3: The Problem with Global Installation (Why Pros Don't Do This!)**

### **Scenario:**

**Project A needs:** `requests==2.28.0` (older version)
**Project B needs:** `requests==2.31.0` (newer version)

**If you install globally:**
```bash
pip3 install requests==2.28.0  # Project A works!
# Later...
pip3 install requests==2.31.0  # Project B works! BUT Project A BREAKS! 💥
```

**You can only have ONE version installed globally!** 😤

**This is called "Dependency Hell"!** 🔥

---

### **The Professional Solution: Virtual Environments!**

**Virtual environments = Isolated Python installations PER PROJECT!**

**Think of it like:**
- Each project has its OWN `site-packages` folder
- Completely isolated from other projects
- Different versions of libraries? NO PROBLEM! ✅

**This is NON-NEGOTIABLE in professional work!** Every company uses this! 💼

---

## **Part 4: Creating a Virtual Environment (The RIGHT Way to Work!)**

### **Step 1: Create a project folder**

```bash
mkdir testing_tutorial
cd testing_tutorial
```

---

### **Step 2: Create a virtual environment**

**The command:**
```bash
python3 -m venv venv
```

**Breaking it down:**
- `python3 -m venv` - Run Python's built-in `venv` module
- `venv` - Name of the folder (you can call it anything, but `venv` is standard!)

**What just happened:**
- Created a `venv/` folder
- Inside: A COMPLETE isolated Python installation!
- Has its own `pip`, its own `site-packages`, everything!

**Check your folder:**
```bash
ls -la
```

**Output:**
```
drwxr-xr-x  venv/
```

**Inside `venv/`:**
```
venv/
├── bin/           # Executables (python3, pip3, pytest)
├── include/       # C headers (for compiled extensions)
├── lib/           # Python libraries (site-packages here!)
└── pyvenv.cfg     # Configuration
```

---

### **Step 3: Activate the virtual environment**

**On Linux/WSL2:**
```bash
source venv/bin/activate
```

**You'll see your prompt change:**
```
(venv) ahad@machine:~/testing_tutorial$
```

**That `(venv)` prefix means YOU'RE IN THE VIRTUAL ENVIRONMENT!** 🎯

---

### **What Activation Does:**

**Before activation:**
```bash
which python3
# Output: /usr/bin/python3 (system Python!)

which pip3
# Output: /usr/bin/pip3 (system pip!)
```

**After activation:**
```bash
which python3
# Output: /home/ahad/testing_tutorial/venv/bin/python3 (YOUR Python!)

which pip3
# Output: /home/ahad/testing_tutorial/venv/bin/pip3 (YOUR pip!)
```

**Now ANY package you install goes into THIS project ONLY!** ✅

---

### **Step 4: Verify it's working**

```bash
pip3 list
```

**Output (minimal!):**
```
Package    Version
---------- -------
pip        24.0
setuptools 65.5.0
```

**See?** Almost empty! This is a FRESH Python installation for THIS project! 🎉

---

## **Part 5: Installing pytest (Finally!)**

**Now we install pytest in OUR virtual environment:**

```bash
pip3 install pytest
```

**Output (abbreviated):**
```
Collecting pytest
  Downloading pytest-7.4.3-py3-none-any.whl (325 kB)
Collecting pluggy<2.0,>=0.12
  Downloading pluggy-1.3.0-py3-none-any.whl (18 kB)
Collecting iniconfig
  Downloading iniconfig-2.0.0-py3-none-any.whl (5.9 kB)
... (more dependencies)
Installing collected packages: iniconfig, pluggy, ... pytest
Successfully installed iniconfig-2.0.0 ... pytest-7.4.3
```

**What just happened:**
1. ✅ Downloaded pytest from PyPI
2. ✅ Downloaded its dependencies (pluggy, iniconfig, etc.)
3. ✅ Installed EVERYTHING to `venv/lib/python3.11/site-packages/`
4. ✅ Created `pytest` executable in `venv/bin/`

---

### **Verify pytest is installed:**

```bash
pytest --version
```

**Output:**
```
pytest 7.4.3
```

**BOOM! pytest is ready!** 🎉

---

### **List all installed packages:**

```bash
pip3 list
```

**Output:**
```
Package    Version
---------- -------
iniconfig  2.0.0
packaging  23.2
pip        24.0
pluggy     1.3.0
pytest     7.4.3
setuptools 65.5.0
```

**See the dependencies pytest needed? pip handled them automatically!** ✅

---

## **Part 6: Understanding pytest (Why It's THE Testing Framework)**

### **Python's Built-in Testing vs pytest**

**Python has a built-in `unittest` module. Why don't we use it?**

**unittest example:**
```python
import unittest

class TestMath(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 2, 4)

    def test_subtraction(self):
        self.assertEqual(5 - 3, 2)

if __name__ == '__main__':
    unittest.main()
```

**pytest example:**
```python
def test_addition():
    assert 2 + 2 == 4

def test_subtraction():
    assert 5 - 3 == 2
```

**SEE THE DIFFERENCE?** 🔥

**pytest is:**
- ✅ **Simpler:** No classes, no `self`, just functions!
- ✅ **More readable:** `assert` instead of `self.assertEqual()`
- ✅ **Better output:** Shows you EXACTLY what failed!
- ✅ **More powerful:** Fixtures, parametrization, plugins!
- ✅ **Industry standard:** 90% of Python projects use pytest!

**This is why professionals use pytest!** 💼

---

### **What Makes pytest Special:**

**1. Simple assertions:**
```python
# unittest way
self.assertEqual(result, expected)
self.assertTrue(condition)
self.assertIn(item, list)

# pytest way
assert result == expected
assert condition
assert item in list
```

**Natural Python syntax!** ✅

---

**2. Better failure messages:**

**unittest:**
```
AssertionError
```

**pytest:**
```
AssertionError: assert 5 == 6
  +5
  -6
```

**Shows you WHAT failed and WHY!** 🔍

---

**3. Automatic test discovery:**

**pytest finds tests automatically!**
- Files named `test_*.py` or `*_test.py`
- Functions named `test_*()`
- Classes named `Test*`

**Just run `pytest` and it finds EVERYTHING!** No configuration needed! ✅

---

**4. Fixtures (we'll learn this later):**

**Reusable test setup:**
```python
@pytest.fixture
def sample_data():
    return {"name": "Ahad", "age": 20}

def test_name(sample_data):
    assert sample_data["name"] == "Ahad"
```

**No more copying setup code in every test!** 🔥

---

**5. Rich plugin ecosystem:**

- `pytest-cov` (code coverage)
- `pytest-xdist` (parallel testing)
- `pytest-django` (Django integration)
- 1000+ plugins available!

---

## **Part 7: Your First Test (To Verify Everything Works!)**

**Create a file called `test_sample.py`:**

```bash
touch test_sample.py
```

**Edit it:**
```python
def test_basic_math():
    """Test that basic math works."""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 3 == 9

def test_strings():
    """Test string operations."""
    name = "Ahad"
    assert name.upper() == "AHAD"
    assert len(name) == 4
    assert "h" in name.lower()

def test_lists():
    """Test list operations."""
    numbers = [1, 2, 3, 4, 5]
    assert len(numbers) == 5
    assert 3 in numbers
    assert numbers[0] == 1
```

**Save it!**

---

### **Run pytest:**

```bash
pytest
```

**Output:**
```
======================== test session starts ========================
platform linux -- Python 3.11.0, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/ahad/testing_tutorial
collected 3 items

test_sample.py ...                                            [100%]

========================= 3 passed in 0.02s =========================
```

**BREAKDOWN:**

- **`collected 3 items`** - Found 3 test functions
- **`test_sample.py ...`** - Each dot (`.`) is a passing test!
- **`3 passed in 0.02s`** - All tests passed! ✅

**YOUR TESTING ENVIRONMENT WORKS!** 🎉

---

### **Run with more details:**

```bash
pytest -v
```

**Output:**
```
======================== test session starts ========================
test_sample.py::test_basic_math PASSED                        [ 33%]
test_sample.py::test_strings PASSED                           [ 66%]
test_sample.py::test_lists PASSED                             [100%]

========================= 3 passed in 0.02s =========================
```

**`-v` flag = verbose mode (shows each test name!)** 📋

---

### **Now let's make a test FAIL (to see what that looks like):**

**Edit `test_sample.py` and add:**

```python
def test_intentional_failure():
    """This test will fail on purpose."""
    assert 2 + 2 == 5  # This is wrong!
```

**Run pytest:**

```bash
pytest
```

**Output:**
```
======================== test session starts ========================
test_sample.py ...F                                           [100%]

============================= FAILURES ==============================
______________________ test_intentional_failure _____________________

    def test_intentional_failure():
        """This test will fail on purpose."""
>       assert 2 + 2 == 5
E       assert 4 == 5

test_sample.py:18: AssertionError
==================== short test summary info =======================
FAILED test_sample.py::test_intentional_failure - assert 4 == 5
=================== 1 failed, 3 passed in 0.05s ====================
```

**LOOK AT THIS OUTPUT!** 🔍

**What pytest shows you:**

1. **`...F`** - Three passed (`.`), one failed (`F`)
2. **Failure details:**
   - Which test failed: `test_intentional_failure`
   - Which line: `test_sample.py:18`
   - What failed: `assert 4 == 5`
   - The actual values: `assert 4 == 5` (shows 4 != 5!)

**This is WHY pytest is so good!** Clear, detailed failure messages! ✅

---

## **Part 8: Updating pip (Best Practice)**

**Keep pip up-to-date for security and features:**

```bash
pip3 install --upgrade pip
```

**Output:**
```
Requirement already satisfied: pip in ./venv/lib/python3.11/site-packages (24.0)
```

**Or if there's an update:**
```
Successfully installed pip-24.1
```

**Do this regularly!** New pip versions have bug fixes and speed improvements! ⚡

---

## **Part 9: Other Useful pip Commands (Professional Arsenal)**

### **1. Install specific version:**

```bash
pip3 install pytest==7.4.0
```

**Why:** Sometimes you need an older version for compatibility!

---

### **2. Install from requirements.txt:**

**Every professional project has a `requirements.txt` file:**

```
pytest==7.4.3
requests==2.31.0
flask==3.0.0
```

**Install ALL dependencies at once:**
```bash
pip3 install -r requirements.txt
```

**This is how you share projects!** Anyone can recreate your environment! 🔄

---

### **3. Create requirements.txt (freeze current packages):**

```bash
pip3 freeze > requirements.txt
```

**Creates a file with ALL installed packages and versions:**
```
iniconfig==2.0.0
packaging==23.2
pluggy==1.3.0
pytest==7.4.3
```

**Now anyone can install the EXACT same versions you used!** ✅

---

### **4. Uninstall a package:**

```bash
pip3 uninstall pytest
```

**Removes the package and asks for confirmation!**

---

### **5. Show package info:**

```bash
pip3 show pytest
```

**Output:**
```
Name: pytest
Version: 7.4.3
Summary: pytest: simple powerful testing with Python
Home-page: https://docs.pytest.org/en/latest/
Author: Holger Krekel, Bruno Oliveira, Ronny Pfannschmidt
License: MIT
Location: /home/ahad/testing_tutorial/venv/lib/python3.11/site-packages
Requires: iniconfig, packaging, pluggy
Required-by:
```

**Shows you EVERYTHING about a package!** 📦

---

### **6. Search PyPI (find packages):**

```bash
pip3 search testing
```

**⚠️ NOTE:** This command is currently disabled due to PyPI abuse, but you can search on https://pypi.org instead!

---

### **7. Check for outdated packages:**

```bash
pip3 list --outdated
```

**Shows packages with available updates!**

---

## **Part 10: Deactivating Virtual Environment**

**When you're done working:**

```bash
deactivate
```

**Your prompt changes back:**
```
ahad@machine:~/testing_tutorial$
```

**(No more `(venv)` prefix!)**

**You're back to system Python!** ✅

---

**To reactivate later:**
```bash
source venv/bin/activate
```

---

## **Part 11: Professional Workflow (How Real Developers Work)**

**Every time you start a new project:**

```bash
# 1. Create project folder
mkdir my_project
cd my_project

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install dependencies
pip3 install pytest requests flask

# 5. Freeze dependencies (for sharing)
pip3 freeze > requirements.txt

# 6. Work on your project...
# Write code, tests, etc.

# 7. Deactivate when done
deactivate
```

**THIS is the professional workflow!** Memorize this! 💼

---

**When someone else clones your project:**

```bash
# 1. Clone the repo
git clone your_project

# 2. Create venv
python3 -m venv venv

# 3. Activate
source venv/bin/activate

# 4. Install dependencies
pip3 install -r requirements.txt

# DONE! Same environment as you! ✅
```

---

## **Part 12: Why Virtual Environments Are NON-NEGOTIABLE**

**Real-world scenario you WILL face:**

**You're working on 3 projects:**

**Project 1 (Old):** Django 3.2
**Project 2 (Current):** Django 4.1
**Project 3 (New):** Django 5.0

**Without virtual environments:**
```bash
pip3 install django==3.2  # Project 1 works
# Switch to Project 2...
pip3 install django==4.1  # Project 2 works, Project 1 BREAKS
# Switch to Project 3...
pip3 install django==5.0  # Project 3 works, Project 1 & 2 BREAK
```

**You're FUCKED!** 💥

---

**With virtual environments:**

```bash
# Project 1
cd project1
source venv/bin/activate
pip3 install django==3.2
# Work...
deactivate

# Project 2
cd ../project2
source venv/bin/activate
pip3 install django==4.1
# Work...
deactivate

# Project 3
cd ../project3
source venv/bin/activate
pip3 install django==5.0
# Work...
deactivate
```

**ALL THREE work SIMULTANEOUSLY!** No conflicts! ✅

**This is why EVERY professional uses virtual environments!** 💼

---

## **Part 13: .gitignore for venv (Important!)**

**NEVER commit `venv/` to Git!**

**Create `.gitignore`:**

```bash
touch .gitignore
```

**Add:**
```
venv/
__pycache__/
*.pyc
.pytest_cache/
```

**Why:**
- `venv/` is HUGE (100+ MB!)
- Different operating systems have different binaries
- Anyone can recreate it with `requirements.txt`

**This is standard practice!** ✅

---

## **Common Mistakes (Learn From Others' Pain!)**

### ❌ **Mistake 1: Forgetting to activate venv**

```bash
# You think you're in venv, but you're not!
pip3 install pytest  # Installs to SYSTEM Python! 😤
```

**Always check for `(venv)` in your prompt!** ⚠️

---

### ❌ **Mistake 2: Committing venv to Git**

**Your repo becomes 100+ MB!**
**Wastes everyone's time and bandwidth!**

**Always add `venv/` to `.gitignore`!** ✅

---

### ❌ **Mistake 3: Not using requirements.txt**

**Six months later:**
"What packages did I use? What versions? I don't remember!" 😰

**Always `pip3 freeze > requirements.txt`!** 📋

---

### ❌ **Mistake 4: Using `sudo pip3 install`**

**NEVER DO THIS!**

```bash
sudo pip3 install pytest  # ❌ DANGEROUS!
```

**Why:**
- Modifies system Python (can break your OS!)
- Permission issues
- Security risk

**Use virtual environments instead!** ✅

---

## **Summary: What You Actually Learned**

**NOT just "pip install pytest"—you learned:**

✅ **How Python's package ecosystem works** (pip, PyPI)
✅ **Virtual environments** (isolation, professional workflow)
✅ **Package management** (install, update, uninstall, freeze)
✅ **pytest vs unittest** (why professionals choose pytest)
✅ **Professional workflow** (venv creation, activation, requirements.txt)
✅ **Common mistakes** (and how to avoid them!)
✅ **Your first test** (verified pytest works!)

**THIS is foundational knowledge for EVERY Python project you'll build!** 💼

---

## **The Professional Setup (What You Should Do NOW)**

**For THIS chapter:**

```bash
# 1. Create chapter 11 workspace
mkdir ~/python_learning/chapter_11
cd ~/python_learning/chapter_11

# 2. Create virtual environment
python3 -m venv venv

# 3. Activate
source venv/bin/activate

# 4. Install pytest
pip3 install pytest

# 5. Verify
pytest --version

# 6. Create .gitignore
echo "venv/
__pycache__/
*.pyc
.pytest_cache/" > .gitignore

# 7. Ready to learn! ✅
```

---

# **TOPIC 1: COMPLETE! ✅📦**

**YOU NOW KNOW:**
✅ What pip is and how it works

✅ The entire Python package ecosystem

✅ Virtual environments (CRITICAL for professionals!)

✅ How to install, update, and manage packages

✅ Why pytest is the industry standard

✅ Professional workflow for every project

✅ Common mistakes and how to avoid them

**THIS is how professionals work!** You're not learning "toy basics"—you're learning INDUSTRY PRACTICES! 💼🔥

---

---

# **TOPIC 2: TESTING FUNCTIONS (THE REAL DEAL)** 🧪⚡

---

## **What The HELL Are We ACTUALLY Learning?**

**NOT just "write test functions lol"—FUCK THAT!** 🚫

**What we're REALLY learning:**

✅ **Unit testing philosophy** (what to test, what NOT to test)

✅ **Test-Driven Development (TDD)** (write tests BEFORE code!)

✅ **Assertions deep dive** (every way to check results)

✅ **Test organization** (how to structure test files)

✅ **Edge cases** (testing boundary conditions)

✅ **Test naming conventions** (professional practices)

✅ **Testing YOUR character analyzer!** (real application!)

**This isn't toy testing—this is PROFESSIONAL testing that prevents bugs in production!** 💼

---

## **Part 1: What The Hell Is Unit Testing? (The Philosophy)**

### **The Concept:**

**Unit testing = Testing ONE "unit" (function/method) at a time!**

**NOT testing the entire program!** That's "integration testing" (later!)

**Think of it like:**
- You're building a car
- **Unit tests** = Test each part (engine, brakes, steering)
- **Integration tests** = Test the assembled car

**We start with units (functions) because if PARTS work, the WHOLE works!** ✅

---

### **Why Unit Tests Matter (Real Scenario):**

**You built your character analyzer. It works! Ship it, right?**

**Two weeks later:**
- You optimize `how_many_times()` for speed
- You add case-insensitive search
- You refactor the JSON saving

**How do you know you didn't BREAK anything?** 😰

**Without tests:**
1. Manually run program
2. Test all 3 books
3. Test different characters
4. Test edge cases
5. **30 minutes of manual testing!** 😤

**With tests:**
```bash
pytest
```

**15 seconds → All tests pass → YOU'RE GOOD!** ✅

**THIS is why professionals write tests!** They can CHANGE code confidently! 💪

---

## **Part 2: What Makes a Good Test? (The Principles)**

### **A good test is:**

**1. FAST** ⚡
- Runs in milliseconds
- No network calls, no user input
- Uses test data (not real files if possible)

**2. ISOLATED** 🔒
- Tests ONE thing only
- Doesn't depend on other tests
- Can run in ANY order

**3. REPEATABLE** 🔄
- Same result every time
- No randomness (unless that's what you're testing)
- No dependency on date/time (unless testing that)

**4. SELF-VALIDATING** ✅
- Pass or fail, no human judgment needed
- Uses `assert` to check results
- Clear pass/fail output

**5. TIMELY** ⏰
- Written CLOSE to when you write the code
- Ideally BEFORE (Test-Driven Development!)

**These are called the F.I.R.S.T. principles!** Memorize them! 📋

---

## **Part 3: Test-Driven Development (TDD) - The Pro Way!**

### **How most people code:**

1. Write function
2. Manually test it
3. "Looks good!" ✅
4. Ship it
5. **Bug in production!** 💥

---

### **How professionals code (TDD):**

1. **Write test FIRST** (it fails—function doesn't exist yet!)
2. **Write minimal code** to make test pass
3. **Refactor** (improve code quality)
4. **Repeat!**

**This is called "Red-Green-Refactor":** 🔴🟢♻️

- 🔴 **RED:** Test fails (expected—code doesn't exist!)
- 🟢 **GREEN:** Test passes (you wrote the code!)
- ♻️ **REFACTOR:** Improve code (test ensures you don't break it!)

---

### **Example: Building a `full_name()` function with TDD**

**Step 1: Write the test FIRST (🔴 RED)**

**Create `name_function.py`:**
```python
# Empty file!
```

**Create `test_name_function.py`:**
```python
from name_function import get_full_name

def test_first_last_name():
    """Does 'Ahad Khan' work?"""
    full_name = get_full_name('Ahad', 'Khan')
    assert full_name == 'Ahad Khan'
```

**Run pytest:**
```bash
pytest test_name_function.py
```

**Output:**
```
ImportError: cannot import name 'get_full_name' from 'name_function'
```

**🔴 RED!** Test fails (expected—function doesn't exist!)

---

**Step 2: Write MINIMAL code to pass (🟢 GREEN)**

**Edit `name_function.py`:**
```python
def get_full_name(first, last):
    """Return a formatted full name."""
    return f"{first} {last}"
```

**Run pytest:**
```bash
pytest test_name_function.py
```

**Output:**
```
test_name_function.py::test_first_last_name PASSED            [100%]

========================= 1 passed in 0.01s =========================
```

**🟢 GREEN!** Test passes! ✅

---

**Step 3: Add more tests (edge cases!)**

**Edit `test_name_function.py`:**
```python
from name_function import get_full_name

def test_first_last_name():
    """Does 'Ahad Khan' work?"""
    full_name = get_full_name('Ahad', 'Khan')
    assert full_name == 'Ahad Khan'

def test_first_middle_last_name():
    """Does 'Ahad Ali Khan' work?"""
    full_name = get_full_name('Ahad', 'Khan', 'Ali')
    assert full_name == 'Ahad Ali Khan'
```

**Run pytest:**
```bash
pytest test_name_function.py
```

**Output:**
```
FAILED test_name_function.py::test_first_middle_last_name
TypeError: get_full_name() takes 2 positional arguments but 3 were given
```

**🔴 RED!** Test fails (function doesn't handle middle names!)

---

**Step 4: Fix the function (🟢 GREEN)**

**Edit `name_function.py`:**
```python
def get_full_name(first, last, middle=''):
    """Return a formatted full name."""
    if middle:
        return f"{first} {middle} {last}"
    else:
        return f"{first} {last}"
```

**Run pytest:**
```bash
pytest test_name_function.py
```

**Output:**
```
test_name_function.py::test_first_last_name PASSED            [ 50%]
test_name_function.py::test_first_middle_last_name PASSED     [100%]

========================= 2 passed in 0.01s =========================
```

**🟢 GREEN!** Both tests pass! ✅

---

**Step 5: Refactor (♻️ REFACTOR)**

**Your function works, but could be cleaner:**

```python
def get_full_name(first, last, middle=''):
    """Return a formatted full name."""
    parts = [first]
    if middle:
        parts.append(middle)
    parts.append(last)
    return ' '.join(parts)
```

**Run pytest again:**
```bash
pytest test_name_function.py
```

**Still passes! ✅** You refactored WITHOUT breaking anything!

**THIS IS THE POWER OF TDD!** 🔥

---

## **Part 4: Testing YOUR Character Analyzer (Real Application!)**

**Let's write REAL tests for YOUR project!**

**Your code has this function:**
```python
def how_many_times(path, search):
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if search.lower() in line.lower():
                matches.append({
                    "line_number": line_number,
                    "text": line.strip()
                })
    return matches
```

**What should we test?**

1. ✅ Does it find matches correctly?
2. ✅ Are line numbers accurate?
3. ✅ Is the search case-insensitive?
4. ✅ Does it handle non-existent files?
5. ✅ Does it handle empty files?
6. ✅ Does it handle special characters?

**Let's build tests for ALL of these!** 💪

---

### **Step 1: Extract your function (make it testable!)**

**Create `character_analyzer.py`:**
```python
def how_many_times(path, search):
    """
    Search for a character/word in a text file.

    Args:
        path: Path to the text file
        search: String to search for

    Returns:
        List of dicts with line_number and text
    """
    matches = []
    with open(path, "r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if search.lower() in line.lower():
                matches.append({
                    "line_number": line_number,
                    "text": line.strip()
                })
    return matches
```

**Now it's a reusable module!** ✅

---

### **Step 2: Create test data (small test file)**

**Create `test_book.txt`:**
```
Raskolnikov walked down the street.
The old woman opened the door.
Raskolnikov hesitated for a moment.
He thought about his plan.
RASKOLNIKOV entered the room.
```

**5 lines, 3 mentions of "Raskolnikov" (different cases!)** 📝

---

### **Step 3: Write your first test**

**Create `test_character_analyzer.py`:**
```python
from character_analyzer import how_many_times

def test_basic_search():
    """Test basic character search."""
    results = how_many_times("test_book.txt", "Raskolnikov")

    # Should find 3 matches
    assert len(results) == 3

    # Check first match
    assert results[0]["line_number"] == 1
    assert "Raskolnikov walked" in results[0]["text"]
```

**Run it:**
```bash
pytest test_character_analyzer.py -v
```

**Output:**
```
test_character_analyzer.py::test_basic_search PASSED          [100%]

========================= 1 passed in 0.01s =========================
```

**🟢 GREEN!** Your function works! ✅

---

### **Step 4: Test case-insensitivity**

**Add to `test_character_analyzer.py`:**
```python
def test_case_insensitive():
    """Test that search is case-insensitive."""
    results = how_many_times("test_book.txt", "raskolnikov")

    # Should still find 3 matches (case doesn't matter!)
    assert len(results) == 3

    # Should find the UPPERCASE one too
    assert any("RASKOLNIKOV" in r["text"] for r in results)
```

**Run it:**
```bash
pytest test_character_analyzer.py -v
```

**Output:**
```
test_character_analyzer.py::test_basic_search PASSED          [ 50%]
test_character_analyzer.py::test_case_insensitive PASSED      [100%]

========================= 2 passed in 0.01s =========================
```

**Both pass! ✅** Case-insensitivity works!

---

### **Step 5: Test edge cases**

**Add to `test_character_analyzer.py`:**
```python
def test_no_matches():
    """Test when character isn't in the book."""
    results = how_many_times("test_book.txt", "Sherlock Holmes")

    # Should return empty list
    assert len(results) == 0
    assert results == []

def test_partial_match():
    """Test that partial words are matched."""
    results = how_many_times("test_book.txt", "old")

    # Should find "old woman" (line 2)
    assert len(results) == 1
    assert results[0]["line_number"] == 2
    assert "old woman" in results[0]["text"]

def test_special_characters():
    """Test search with punctuation."""
    # Create temp file with punctuation
    with open("test_special.txt", "w") as f:
        f.write("Hello, world!\n")
        f.write("Hello world\n")

    results = how_many_times("test_special.txt", "Hello")

    # Should find both lines
    assert len(results) == 2

    # Cleanup
    import os
    os.remove("test_special.txt")
```

**Run all tests:**
```bash
pytest test_character_analyzer.py -v
```

**Output:**
```
test_character_analyzer.py::test_basic_search PASSED          [ 20%]
test_character_analyzer.py::test_case_insensitive PASSED      [ 40%]
test_character_analyzer.py::test_no_matches PASSED            [ 60%]
test_character_analyzer.py::test_partial_match PASSED         [ 80%]
test_character_analyzer.py::test_special_characters PASSED    [100%]

========================= 5 passed in 0.02s =========================
```

**ALL PASS! 🎉** Your function is SOLID!

---

### **Step 6: Test error handling**

**What if file doesn't exist?**

**Add to `test_character_analyzer.py`:**
```python
import pytest

def test_file_not_found():
    """Test that FileNotFoundError is raised for missing files."""
    with pytest.raises(FileNotFoundError):
        how_many_times("nonexistent_book.txt", "Raskolnikov")
```

**Run it:**
```bash
pytest test_character_analyzer.py::test_file_not_found -v
```

**Output:**
```
test_character_analyzer.py::test_file_not_found PASSED        [100%]

========================= 1 passed in 0.01s =========================
```

**It passes!** Your function DOES raise FileNotFoundError! ✅

---

## **Part 5: Understanding `pytest.raises` (Testing Exceptions)**

**That `pytest.raises` thing is POWERFUL!**

**Syntax:**
```python
import pytest

with pytest.raises(ExceptionType):
    code_that_should_raise_exception()
```

**What it does:**
- Expects the code inside to raise that exception
- **Test PASSES** if exception is raised
- **Test FAILS** if no exception or DIFFERENT exception

---

**Example: Testing your save function**

```python
import pytest
from character_analyzer import save_results

def test_save_with_invalid_path():
    """Test that saving to invalid path raises error."""
    with pytest.raises(FileNotFoundError):
        save_results("character", "book", [], path="/invalid/path/file.json")
```

**This ensures your code FAILS CORRECTLY when things go wrong!** ✅

---

## **Part 6: Test Organization (Professional Structure)**

**Your project structure should look like:**

```
testing_my_code/
├── venv/                          # Virtual environment
├── character_analyzer.py          # Your module
├── literatures_search.py          # Your main script
├── test_character_analyzer.py     # Tests for the module
├── test_book.txt                  # Test data
├── crimeandpunishment.txt         # Real books
├── metamorphosis.txt
├── macbeth.txt
└── .gitignore
```

**Professional conventions:**

1. **Test files start with `test_`** or end with `_test.py`
   - `test_character_analyzer.py` ✅
   - `character_analyzer_test.py` ✅
   - `tests.py` ❌ (too vague!)

2. **Test functions start with `test_`**
   - `def test_basic_search():` ✅
   - `def basic_search_test():` ❌

3. **One test file per module**
   - `character_analyzer.py` → `test_character_analyzer.py`
   - `save_results.py` → `test_save_results.py`

4. **Test names are DESCRIPTIVE**
   - `test_case_insensitive()` ✅
   - `test_function1()` ❌

**pytest finds tests automatically with these conventions!** 🎯

---

## **Part 7: Test Naming Conventions (Professional Practice)**

**Good test names tell a STORY:**

**Format:** `test_<what>_<condition>_<expected_result>`

**Examples:**

✅ `test_search_existing_character_returns_matches()`
✅ `test_search_missing_character_returns_empty_list()`
✅ `test_search_case_insensitive_finds_all_variations()`
✅ `test_save_duplicate_search_returns_false()`

**NOT:**
❌ `test1()`
❌ `test_function()`
❌ `test_stuff()`

**Why good names matter:**

**When a test fails:**
```
FAILED test_character_analyzer.py::test_search_existing_character_returns_matches
```

**You IMMEDIATELY know:**
- What broke: "search function"
- Condition: "existing character"
- Expected: "should return matches"

**No need to read the code!** The name tells you everything! 📋

---

## **Part 8: Running Tests (All the Ways)**

### **1. Run ALL tests:**
```bash
pytest
```

**Finds and runs EVERYTHING starting with `test_`!**

---

### **2. Run ONE test file:**
```bash
pytest test_character_analyzer.py
```

---

### **3. Run ONE specific test:**
```bash
pytest test_character_analyzer.py::test_basic_search
```

---

### **4. Run with verbose output:**
```bash
pytest -v
```

**Shows each test name!**

---

### **5. Run with print statements shown:**
```bash
pytest -s
```

**By default, pytest captures `print()` output. `-s` shows it!**

---

### **6. Run with detailed failure info:**
```bash
pytest -vv
```

**Super verbose! Shows MORE details on failures!**

---

### **7. Run tests matching a pattern:**
```bash
pytest -k "case"
```

**Runs only tests with "case" in the name!**

```
test_case_insensitive PASSED
```

---

### **8. Run and stop on first failure:**
```bash
pytest -x
```

**Stops immediately when a test fails (useful for debugging!)** 🔍

---

### **9. Run and show slowest tests:**
```bash
pytest --durations=5
```

**Shows the 5 slowest tests (optimization!)** ⚡

---

### **10. Run with coverage report:**
```bash
pip3 install pytest-cov
pytest --cov=character_analyzer
```

**Shows WHAT % of your code is tested!** We'll dive into this later! 📊

---

## **Part 9: Complete Test Suite for YOUR Project**

**Let's build a COMPLETE test suite!**

**`test_character_analyzer.py` (FULL VERSION):**

```python
"""
Tests for character_analyzer.py

This test suite ensures the character search functionality works correctly
for various edge cases and error conditions.
"""

import pytest
import os
from pathlib import Path
from character_analyzer import how_many_times

# Test data setup
TEST_BOOK_CONTENT = """Raskolnikov walked down the street.
The old woman opened the door.
Raskolnikov hesitated for a moment.
He thought about his plan.
RASKOLNIKOV entered the room."""

@pytest.fixture
def test_book_file():
    """Create a temporary test book file."""
    filepath = "test_book_temp.txt"
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(TEST_BOOK_CONTENT)

    yield filepath  # This is what the test gets

    # Cleanup (runs after test)
    if os.path.exists(filepath):
        os.remove(filepath)

# ============================================================================
# BASIC FUNCTIONALITY TESTS
# ============================================================================

def test_basic_search(test_book_file):
    """Test basic character search returns correct matches."""
    results = how_many_times(test_book_file, "Raskolnikov")

    assert len(results) == 3
    assert results[0]["line_number"] == 1
    assert "Raskolnikov walked" in results[0]["text"]

def test_case_insensitive_search(test_book_file):
    """Test that search ignores case."""
    results_lower = how_many_times(test_book_file, "raskolnikov")
    results_upper = how_many_times(test_book_file, "RASKOLNIKOV")
    results_mixed = how_many_times(test_book_file, "RaSkoLniKov")

    # All should find the same 3 matches
    assert len(results_lower) == 3
    assert len(results_upper) == 3
    assert len(results_mixed) == 3

def test_partial_word_matching(test_book_file):
    """Test that partial words are matched."""
    results = how_many_times(test_book_file, "old")

    assert len(results) == 1
    assert results[0]["line_number"] == 2
    assert "old woman" in results[0]["text"]

# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_no_matches(test_book_file):
    """Test when search term isn't found."""
    results = how_many_times(test_book_file, "Sherlock Holmes")

    assert len(results) == 0
    assert results == []

def test_empty_search_term(test_book_file):
    """Test with empty string (should match all lines)."""
    results = how_many_times(test_book_file, "")

    # Empty string is in every line
    assert len(results) == 5

def test_search_punctuation(test_book_file):
    """Test search terms with punctuation."""
    results = how_many_times(test_book_file, "street.")

    assert len(results) == 1
    assert "street" in results[0]["text"]

def test_line_numbers_are_correct(test_book_file):
    """Test that line numbers are accurate."""
    results = how_many_times(test_book_file, "Raskolnikov")

    # Should find on lines 1, 3, and 5
    line_numbers = [r["line_number"] for r in results]
    assert line_numbers == [1, 3, 5]

def test_whitespace_is_stripped(test_book_file):
    """Test that leading/trailing whitespace is removed."""
    results = how_many_times(test_book_file, "Raskolnikov")

    for result in results:
        # No leading/trailing whitespace
        assert result["text"] == result["text"].strip()

# ============================================================================
# ERROR HANDLING TESTS
# ============================================================================

def test_file_not_found_raises_error():
    """Test that missing file raises FileNotFoundError."""
    with pytest.raises(FileNotFoundError):
        how_many_times("nonexistent_book.txt", "character")

def test_empty_file_returns_empty_list():
    """Test that empty file returns no matches."""
    # Create empty file
    empty_file = "test_empty.txt"
    Path(empty_file).touch()

    try:
        results = how_many_times(empty_file, "anything")
        assert results == []
    finally:
        os.remove(empty_file)

# ============================================================================
# UNICODE AND ENCODING TESTS
# ============================================================================

def test_unicode_characters():
    """Test that unicode characters are handled correctly."""
    unicode_file = "test_unicode.txt"
    unicode_content = "Dostoevsky wrote Crime and Punishment.\nФёдор Михайлович Достоевский"

    with open(unicode_file, "w", encoding="utf-8") as f:
        f.write(unicode_content)

    try:
        results = how_many_times(unicode_file, "Достоевский")
        assert len(results) == 1
        assert "Достоевский" in results[0]["text"]
    finally:
        os.remove(unicode_file)

# ============================================================================
# PERFORMANCE TESTS (Optional but good!)
# ============================================================================

def test_large_file_performance():
    """Test that function handles large files reasonably fast."""
    import time

    # Create a large test file (1000 lines)
    large_file = "test_large.txt"
    with open(large_file, "w") as f:
        for i in range(1000):
            f.write(f"Line {i}: Raskolnikov walked around.\n")

    try:
        start = time.time()
        results = how_many_times(large_file, "Raskolnikov")
        duration = time.time() - start

        # Should find 1000 matches
        assert len(results) == 1000

        # Should complete in under 1 second
        assert duration < 1.0, f"Search took {duration}s, should be < 1s"
    finally:
        os.remove(large_file)
```

**Run this complete test suite:**

```bash
pytest test_character_analyzer.py -v
```

**Output:**
```
test_character_analyzer.py::test_basic_search PASSED                      [  7%]
test_character_analyzer.py::test_case_insensitive_search PASSED           [ 14%]
test_character_analyzer.py::test_partial_word_matching PASSED             [ 21%]
test_character_analyzer.py::test_no_matches PASSED                        [ 28%]
test_character_analyzer.py::test_empty_search_term PASSED                 [ 35%]
test_character_analyzer.py::test_search_punctuation PASSED                [ 42%]
test_character_analyzer.py::test_line_numbers_are_correct PASSED          [ 50%]
test_character_analyzer.py::test_whitespace_is_stripped PASSED            [ 57%]
test_character_analyzer.py::test_file_not_found_raises_error PASSED       [ 64%]
test_character_analyzer.py::test_empty_file_returns_empty_list PASSED     [ 71%]
test_character_analyzer.py::test_unicode_characters PASSED                [ 78%]
test_character_analyzer.py::test_large_file_performance PASSED            [ 85%]

========================= 12 passed in 0.15s ===========================
```

**12 TESTS! ALL PASSING! 🎉**

**YOUR FUNCTION IS BULLETPROOF!** 🛡️

---

## **Part 10: What Did You Notice in That Test Suite?**

### **1. Fixtures (`@pytest.fixture`):**

```python
@pytest.fixture
def test_book_file():
    # Setup
    create_test_file()

    yield filepath  # Give to test

    # Cleanup
    delete_test_file()
```

**What this does:**
- Runs BEFORE the test (setup)
- Gives the test what it needs (`yield`)
- Runs AFTER the test (cleanup)
- **Automatically handles cleanup even if test fails!**

**We'll dive DEEP into fixtures in Topic 7!** They're GAME-CHANGING! 🔥

---

### **2. Docstrings on tests:**

```python
def test_basic_search(test_book_file):
    """Test basic character search returns correct matches."""
```

**Why:**
- Pytest shows these in output
- Other developers know what the test does
- Self-documenting code!

**Professional practice!** Always document your tests! 📋

---

### **3. Organized into sections:**

```python
# ============================================================================
# BASIC FUNCTIONALITY TESTS
# ============================================================================
```

**Makes it EASY to find tests!** Treat test files like code—keep them organized! 🗂️

---

### **4. Descriptive test names:**

```python
test_case_insensitive_search()
test_file_not_found_raises_error()
test_unicode_characters()
```

**You IMMEDIATELY know what each test does!** 🎯

---

## **Part 11: Test Coverage (How Much Code Is Tested?)**

**Install pytest-cov:**
```bash
pip3 install pytest-cov
```

**Run tests with coverage:**
```bash
pytest --cov=character_analyzer test_character_analyzer.py
```

**Output:**
```
========================= test session starts ==========================
collected 12 items

test_character_analyzer.py ............                          [100%]

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name                      Stmts   Miss  Cover
---------------------------------------------
character_analyzer.py        10      0   100%
---------------------------------------------
TOTAL                        10      0   100%

========================= 12 passed in 0.18s ===========================
```

**100% COVERAGE!** Every line of your function is tested! 🎯

---

**What if coverage is lower?**

```
Name                      Stmts   Miss  Cover
---------------------------------------------
character_analyzer.py        15      3    80%
```

**80% coverage = 3 lines NOT tested!**

**Get detailed report:**
```bash
pytest --cov=character_analyzer --cov-report=html
```

**Opens `htmlcov/index.html` in browser:**
- Shows WHICH lines are tested (green)
- Shows WHICH lines are NOT tested (red)
- Click files to see line-by-line coverage

**Professional teams aim for 80-90% coverage!** 💼

---

## **Summary: What You ACTUALLY Learned**

**NOT just "write some tests"—you learned:**

✅ **Unit testing philosophy** (test one function at a time)

✅ **F.I.R.S.T. principles** (Fast, Isolated, Repeatable, Self-validating, Timely)

✅ **Test-Driven Development (TDD)** (Red-Green-Refactor cycle)

✅ **Testing edge cases** (empty inputs, missing files, unicode)

✅ **Testing exceptions** (`pytest.raises`)

✅ **Test organization** (file structure, naming conventions)

✅ **Test fixtures** (setup/teardown, we'll go deeper!)

✅ **Coverage analysis** (how much code is tested)

✅ **Professional practices** (docstrings, sections, descriptive names)

**THIS is how professionals ensure code quality!** 💼🔥

---

12 different scenarios, 100% coverage, and handles edge cases!" 💪

**THIS is what gets you HIRED!** 💰

---

# **TOPIC 2: COMPLETE! ✅🧪**

**YOU NOW KNOW:**
✅ What unit testing actually is

✅ Why professionals write tests

✅ Test-Driven Development (TDD)

✅ How to test functions comprehensively

✅ Edge case testing

✅ Exception testing with `pytest.raises`

✅ Professional test organization

✅ Test coverage analysis

**YOU'RE NOT LEARNING "TOY TESTS"—YOU'RE LEARNING PROFESSIONAL SOFTWARE ENGINEERING!** 🏗️💼

---

---

# **TOPIC 3: PASSING AND FAILING TESTS (Understanding Test Output!)** ✅❌

---

## **What The HELL Is This Topic About?**

**Simple answer:** Learning to READ pytest's output so you know EXACTLY what broke and WHY!

**This isn't about writing tests—it's about UNDERSTANDING the feedback pytest gives you!**

**Think of it like:**
- You write tests (Topic 2) ✅
- Tests run and give you feedback (Topic 3) 📊
- You READ that feedback and fix your code (Topic 3) 🔧

**Professional developers spend MORE time reading test output than writing tests!** 💼

**This topic teaches you to be a DETECTIVE!** 🔍

---

## **Part 1: What Happens When You Run pytest?**

**Let's start SUPER simple!**

**Create a new file: `calculator.py`**

```python
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    return a / b
```

**Save it!**

---

**Create test file: `test_calculator.py`**

```python
from calculator import add, subtract, multiply, divide

def test_add():
    """Test addition."""
    result = add(2, 3)
    assert result == 5

def test_subtract():
    """Test subtraction."""
    result = subtract(10, 4)
    assert result == 6

def test_multiply():
    """Test multiplication."""
    result = multiply(3, 4)
    assert result == 12

def test_divide():
    """Test division."""
    result = divide(10, 2)
    assert result == 5
```

**Save it!**

---

**Run pytest:**

```bash
pytest test_calculator.py
```

**Output:**

```
======================== test session starts ========================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/ahad/Python/python-learning-curve/testing_my_code
collected 4 items

test_calculator.py ....                                        [100%]

========================= 4 passed in 0.01s =========================
```

**Let's break down EVERY PIECE of this output!** 🔍

---

## **Part 2: Understanding PASSING Test Output (Line by Line)**

### **Line 1: `test session starts`**

```
======================== test session starts ========================
```

**What it means:** pytest is starting! It's about to find and run tests!

**This is just a header.** Like a title saying "HERE WE GO!" 🚀

---

### **Line 2: Platform info**

```
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
```

**Breaking it down:**

- **`platform linux`** - Your operating system (Linux, in your case with WSL2!)
- **`Python 3.12.3`** - Your Python version
- **`pytest-9.0.2`** - Your pytest version
- **`pluggy-1.6.0`** - A pytest dependency (you don't need to worry about this!)

**Why this matters:**
- If tests fail on YOUR machine but pass on someone else's, version differences might be why!
- Professional teams ensure everyone uses the SAME versions!

---

### **Line 3: rootdir**

```
rootdir: /home/ahad/Python/python-learning-curve/testing_my_code
```

**What it means:** This is the ROOT directory pytest is running from!

**pytest searches for:**
- Test files (`test_*.py`)
- Configuration files (`pytest.ini`, `pyproject.toml`)
- Starting from THIS directory!

**You don't need to do anything with this—it's just information!** ℹ️

---

### **Line 4: collected X items**

```
collected 4 items
```

**THIS IS IMPORTANT!** 🎯

**What it means:** pytest FOUND 4 test functions!

**How pytest finds tests:**
1. Looks for files named `test_*.py`
2. Inside those files, looks for functions named `test_*()`
3. Counts them all up!

**In our case:**
- `test_add()` → 1
- `test_subtract()` → 2
- `test_multiply()` → 3
- `test_divide()` → 4

**Total: 4 items collected!** ✅

---

**If pytest collects 0 items, it means:**
- ❌ No test files found (wrong file name?)
- ❌ No test functions found (wrong function names?)
- ❌ You're in the wrong directory!

---

### **Line 5: The actual test run**

```
test_calculator.py ....                                        [100%]
```

**THIS LINE TELLS YOU EVERYTHING!** 🎯

**Breaking it down:**

**`test_calculator.py`** - The test file being run

**`....`** - FOUR DOTS! Each dot = one PASSING test! ✅

**`[100%]`** - Progress bar! 4 out of 4 tests complete = 100%!

---

**What each dot means:**

```
test_calculator.py ....
                   ↑↑↑↑
                   ││││
                   │││└── test_divide PASSED ✅
                   ││└─── test_multiply PASSED ✅
                   │└──── test_subtract PASSED ✅
                   └───── test_add PASSED ✅
```

**All 4 tests passed!** That's why you see 4 dots! 🎉

---

### **Line 6: Summary**

```
========================= 4 passed in 0.01s =========================
```

**The final summary:**

- **`4 passed`** - 4 tests ran successfully! ✅
- **`in 0.01s`** - Took 0.01 seconds (FAST!) ⚡

**This is your success message!** All tests passed! 🎉

---

## **Part 3: Understanding FAILING Test Output**

**Now let's BREAK something and see what happens!**

**Edit `calculator.py` and introduce a bug:**

```python
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b * 2  # BUG! Multiplying by 2 extra!

def divide(a, b):
    """Divide a by b."""
    return a / b
```

**Save it!**

---

**Run pytest:**

```bash
pytest test_calculator.py
```

**Output:**

```
======================== test session starts ========================
platform linux -- Python 3.12.3, pytest-9.0.2, pluggy-1.6.0
rootdir: /home/ahad/Python/python-learning-curve/testing_my_code
collected 4 items

test_calculator.py ..F.                                        [100%]

============================= FAILURES ==============================
_________________________ test_multiply __________________________

    def test_multiply():
        """Test multiplication."""
        result = multiply(3, 4)
>       assert result == 12
E       assert 24 == 12

test_calculator.py:13: AssertionError
==================== short test summary info =======================
FAILED test_calculator.py::test_multiply - assert 24 == 12
=================== 1 failed, 3 passed in 0.02s ====================
```

**NOW let's understand THIS output!** 🔍

---

### **Line 5: The test run (with failure!)**

```
test_calculator.py ..F.                                        [100%]
                   ↑↑↑↑
                   ││││
                   │││└── test_divide PASSED ✅
                   ││└─── test_multiply FAILED ❌
                   │└──── test_subtract PASSED ✅
                   └───── test_add PASSED ✅
```

**See the `F`?** That's a FAILURE! ❌

**pytest symbols:**
- `.` = Test PASSED ✅
- `F` = Test FAILED ❌
- `E` = Test had an ERROR (crashed!) 💥
- `s` = Test was SKIPPED ⏭️
- `x` = Expected to fail (and did) 🎯

**In our case:** 2 passed, 1 failed, 1 passed → `..F.` 📊

---

### **The FAILURES section**

```
============================= FAILURES ==============================
_________________________ test_multiply __________________________
```

**This header tells you:** "Here's what FAILED!" 🚨

**`test_multiply`** - The name of the failing test!

---

### **The detailed failure info**

```
    def test_multiply():
        """Test multiplication."""
        result = multiply(3, 4)
>       assert result == 12
E       assert 24 == 12

test_calculator.py:13: AssertionError
```

**Let's break down EVERY LINE!** 🔍

---

**Line 1-3: The test code**

```python
    def test_multiply():
        """Test multiplication."""
        result = multiply(3, 4)
```

**pytest shows you the CONTEXT!** What code was running when it failed!

---

**Line 4: The failing line (with `>`)**

```python
>       assert result == 12
```

**The `>` arrow points to the EXACT line that failed!** 🎯

**This is THE line where the assertion failed!**

---

**Line 5: The error details (with `E`)**

```
E       assert 24 == 12
```

**The `E` means ERROR!** This line shows you WHAT failed!

**Translation:** "You expected 12, but got 24!" 🔍

**Breaking it down:**
- **`result`** was 24
- You **expected** 12
- **They don't match!** ❌

**This tells you EXACTLY what went wrong!** 💡

---

**Line 6: File and line number**

```
test_calculator.py:13: AssertionError
```

**Breaking it down:**
- **`test_calculator.py`** - The file with the failing test
- **`:13`** - Line 13 (the exact line that failed!)
- **`AssertionError`** - The type of error (assertion failed!)

**You can JUMP to this exact line in your editor!** 🎯

---

### **Short test summary**

```
==================== short test summary info =======================
FAILED test_calculator.py::test_multiply - assert 24 == 12
```

**This is a QUICK summary!**

**Format:** `FAILED file::test_name - error_message`

**Why this is useful:**
- If you have 100 tests and 5 fail, this section lists ALL failures!
- Quick reference without scrolling through details!

---

### **Final summary**

```
=================== 1 failed, 3 passed in 0.02s ====================
```

**The bottom line:**
- **1 failed** - One test broke ❌
- **3 passed** - Three tests still work ✅
- **in 0.02s** - Still fast! ⚡

---

## **Part 4: Fixing The Bug (The Development Cycle)**

**Now you know WHAT failed (multiply) and WHY (expected 12, got 24)!**

**Let's fix it!** 🔧

---

**Step 1: Look at the function**

```python
def multiply(a, b):
    """Multiply two numbers."""
    return a * b * 2  # BUG HERE!
```

**The bug:** Multiplying by 2 extra!

---

**Step 2: Fix it**

```python
def multiply(a, b):
    """Multiply two numbers."""
    return a * b  # Fixed!
```

**Save it!**

---

**Step 3: Run tests again**

```bash
pytest test_calculator.py
```

**Output:**

```
======================== test session starts ========================
test_calculator.py ....                                        [100%]
========================= 4 passed in 0.01s =========================
```

**ALL GREEN! ✅** The bug is fixed!

---

**THIS IS THE DEVELOPMENT CYCLE:**

1. Write code ✍️
2. Write tests 🧪
3. Run tests 🏃
4. **Tests fail?** Fix the code! 🔧
5. Run tests again 🏃
6. **Tests pass?** Ship it! 🚀

**This is how professionals work!** 💼

---

## **Part 5: Multiple Failures (Understanding Complex Output)**

**Let's break MULTIPLE things and see what happens!**

**Edit `calculator.py`:**

```python
def add(a, b):
    """Add two numbers."""
    return a + b + 1  # BUG! Adding 1 extra!

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b * 2  # BUG! Multiplying by 2 extra!

def divide(a, b):
    """Divide a by b."""
    return a / b
```

**Two bugs now!** In `add()` and `multiply()`! 🐛🐛

---

**Run pytest:**

```bash
pytest test_calculator.py
```

**Output:**

```
======================== test session starts ========================
test_calculator.py F.F.                                        [100%]

============================= FAILURES ==============================
____________________________ test_add _____________________________

    def test_add():
        """Test addition."""
        result = add(2, 3)
>       assert result == 5
E       assert 6 == 5

test_calculator.py:5: AssertionError
_________________________ test_multiply __________________________

    def test_multiply():
        """Test multiplication."""
        result = multiply(3, 4)
>       assert result == 12
E       assert 24 == 12

test_calculator.py:13: AssertionError
==================== short test summary info =======================
FAILED test_calculator.py::test_add - assert 6 == 5
FAILED test_calculator.py::test_multiply - assert 24 == 12
=================== 2 failed, 2 passed in 0.02s ====================
```

**Breaking it down:** 🔍

---

### **The test run:**

```
test_calculator.py F.F.
                   ↑↑↑↑
                   ││││
                   │││└── test_divide PASSED ✅
                   ││└─── test_multiply FAILED ❌
                   │└──── test_subtract PASSED ✅
                   └───── test_add FAILED ❌
```

**Two failures: `F.F.`** ❌✅❌✅

---

### **The FAILURES section (shows BOTH failures!):**

```
============================= FAILURES ==============================
____________________________ test_add _____________________________
    ... (first failure details)
_________________________ test_multiply __________________________
    ... (second failure details)
```

**pytest shows you ALL failures!** 📋

**Each failure gets its own section!**

---

### **The summary lists BOTH:**

```
==================== short test summary info =======================
FAILED test_calculator.py::test_add - assert 6 == 5
FAILED test_calculator.py::test_multiply - assert 24 == 12
```

**Quick list of ALL failures!** 🎯

**You can see at a glance:**
- Which tests failed
- What went wrong (expected vs actual)

---

### **The bottom line:**

```
=================== 2 failed, 2 passed in 0.02s ====================
```

**2 broken, 2 working!** Half your code is broken! 😬

---

## **Part 6: Understanding Error vs Failure**

**There's a difference between FAILURE and ERROR!**

**Let's see it!** 💥

---

**Edit `calculator.py`:**

```python
def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    # BUG: We're calling a function that doesn't exist!
    return something_that_doesnt_exist(a, b)
```

**This is a CRASH, not just wrong output!** 💥

---

**Run pytest:**

```bash
pytest test_calculator.py
```

**Output:**

```
======================== test session starts ========================
test_calculator.py ...E                                        [100%]

================================ ERRORS =============================
_________________________ test_divide _____________________________

    def test_divide():
        """Test division."""
>       result = divide(10, 2)

test_calculator.py:17:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 10, b = 2

    def divide(a, b):
        """Divide a by b."""
>       return something_that_doesnt_exist(a, b)
E       NameError: name 'something_that_doesnt_exist' is not defined

calculator.py:18: NameError
==================== short test summary info =======================
ERROR test_calculator.py::test_divide - NameError: name 'something_that_doesnt_exist' is not defined
=================== 1 error, 3 passed in 0.02s =====================
```

**Let's break this down!** 🔍

---

### **The test run:**

```
test_calculator.py ...E
                   ↑↑↑↑
                   ││││
                   │││└── test_divide ERROR 💥
                   ││└─── test_multiply PASSED ✅
                   │└──── test_subtract PASSED ✅
                   └───── test_add PASSED ✅
```

**`E` = ERROR!** The test CRASHED! 💥

---

### **The ERRORS section (not FAILURES!):**

```
================================ ERRORS =============================
```

**Errors get their own section!**

**ERROR means:** The test couldn't even RUN! It crashed before finishing!

---

### **The error details:**

```
    def test_divide():
        """Test division."""
>       result = divide(10, 2)
```

**Shows where the test was when it crashed!**

---

**Then shows the TRACEBACK:**

```
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

a = 10, b = 2

    def divide(a, b):
        """Divide a by b."""
>       return something_that_doesnt_exist(a, b)
E       NameError: name 'something_that_doesnt_exist' is not defined

calculator.py:18: NameError
```

**This shows you:**
- The function arguments: `a = 10, b = 2`
- The exact line that crashed: `something_that_doesnt_exist(a, b)`
- The error type: `NameError`
- The error message: `name 'something_that_doesnt_exist' is not defined`
- The file and line: `calculator.py:18`

**COMPLETE information to fix the bug!** 🔧

---

### **The summary:**

```
=================== 1 error, 3 passed in 0.02s =====================
```

**Says `error`, not `failed`!** There's a difference!

---

### **FAILURE vs ERROR:**

**FAILURE (F):**
- Test RAN completely
- But assertion failed
- Code works, just gives wrong result
- Example: `assert 6 == 5` (expected 5, got 6)

**ERROR (E):**
- Test CRASHED before finishing
- Code has a bug that BREAKS execution
- Example: `NameError`, `TypeError`, `ZeroDivisionError`

**Both are problems, but ERROR is usually worse!** 💥

---

## **Part 7: Verbose Output (Seeing More Details)**

**Run pytest with `-v` (verbose):**

```bash
pytest test_calculator.py -v
```

**Output:**

```
======================== test session starts ========================
test_calculator.py::test_add PASSED                            [ 25%]
test_calculator.py::test_subtract PASSED                       [ 50%]
test_calculator.py::test_multiply PASSED                       [ 75%]
test_calculator.py::test_divide PASSED                         [100%]

========================= 4 passed in 0.01s =========================
```

**What's different?**

**Without `-v`:**
```
test_calculator.py ....                                        [100%]
```

**With `-v`:**
```
test_calculator.py::test_add PASSED                            [ 25%]
test_calculator.py::test_subtract PASSED                       [ 50%]
test_calculator.py::test_multiply PASSED                       [ 75%]
test_calculator.py::test_divide PASSED                         [100%]
```

**Shows EACH test by name!** 📋

**Why this is useful:**
- See exactly which tests passed/failed
- Track progress (25%, 50%, 75%, 100%)
- Easier to find specific tests

---

## **Part 8: Running Specific Tests (When You Know What's Broken)**

**You don't always need to run ALL tests!**

---

### **Run ONE test:**

```bash
pytest test_calculator.py::test_add -v
```

**Output:**

```
======================== test session starts ========================
test_calculator.py::test_add PASSED                            [100%]

========================= 1 passed in 0.01s =========================
```

**Only ran `test_add`!** ⚡

**Format:** `pytest file::test_name`

---

### **Run tests matching a pattern:**

```bash
pytest -k "multiply" -v
```

**Output:**

```
======================== test session starts ========================
test_calculator.py::test_multiply PASSED                       [100%]

========================= 1 passed in 0.01s =========================
```

**Only ran tests with "multiply" in the name!** 🔍

**The `-k` flag = keyword filter!**

---

### **Stop on first failure:**

```bash
pytest -x
```

**pytest stops AS SOON AS one test fails!**

**Why this is useful:**
- Fix one bug at a time
- Don't get overwhelmed by 50 failing tests
- Faster feedback loop

---

## **Summary: What You Actually Learned**

**NOT just "read pytest output"—you learned:**


✅ **What EVERY line of pytest output means** (platform, rootdir, collected items)

✅ **Test symbols** (`.` = pass, `F` = fail, `E` = error)

✅ **How to read failure messages** (expected vs actual, file, line number)

✅ **The development cycle** (test → fail → fix → test)

✅ **Failure vs Error** (wrong output vs crash)

✅ **Verbose mode** (`-v` shows each test name)

✅ **Running specific tests** (`::test_name`, `-k pattern`, `-x`)

**THIS is how you become a testing DETECTIVE!** 🔍

---

## **The Real Skill:**

**Reading test output is like reading X-rays!** 🏥

**A doctor looks at an X-ray and immediately knows:**
- What's broken
- Where it's broken
- How to fix it

**YOU now look at pytest output and immediately know:**
- Which test failed
- What was expected vs what happened
- Exactly which line to fix

**THAT'S the skill professionals have!** 💼

---

# **TOPIC 3: COMPLETE! ✅🔍**

**YOU NOW KNOW:**
✅ How to read pytest output line-by-line

✅ What `.`, `F`, and `E` symbols mean

✅ How to understand failure messages

✅ The difference between failure and error

✅ How to run tests efficiently

✅ The professional development cycle

**You're not just WRITING tests—you're READING and UNDERSTANDING feedback!** 🎯

---

---

# **TOPIC 4: BUILDING TEST SUITES (MULTIPLE TESTS!)** 🏗️🧪

---

## **What The HELL Is A Test Suite?**

**Simple answer:** A collection of related tests that work together to verify your code!

**Think of it like:**
- **One test** = One question on an exam ❓
- **Test suite** = The ENTIRE exam (multiple questions testing different things!) 📋

**Up until now:**
- You tested individual functions
- Each test was separate
- No organization

**Now:**
- You'll test ENTIRE systems
- Multiple tests working together
- Professional organization

**This is how REAL projects are tested!** 💼

---

## **Part 1: The Scenario (Real-World Example)**

**Let's build something USEFUL and SIMPLE:**

**A Shopping Cart system!** 🛒

**Why this example:**
- ✅ Easy to understand (everyone knows shopping carts!)
- ✅ Multiple functions to test (add item, remove item, calculate total)
- ✅ Real edge cases (empty cart, removing non-existent items)
- ✅ Practical (e-commerce is EVERYWHERE!)

**NO hardcoding, NO complexity bombs—just building step-by-step!** 🎯

---

## **Part 2: Building The Shopping Cart (The Code We'll Test)**

**Create `shopping_cart.py`:**

```python
class ShoppingCart:
    """A simple shopping cart."""

    def __init__(self):
        """Initialize empty cart."""
        self.items = []

    def add_item(self, name, price, quantity=1):
        """
        Add an item to the cart.

        Args:
            name: Item name
            price: Item price
            quantity: How many items
        """
        if price < 0:
            raise ValueError("Price cannot be negative!")

        if quantity < 1:
            raise ValueError("Quantity must be at least 1!")

        item = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
        self.items.append(item)

    def remove_item(self, name):
        """
        Remove an item from cart.

        Args:
            name: Item name to remove

        Returns:
            True if removed, False if not found
        """
        for item in self.items:
            if item["name"] == name:
                self.items.remove(item)
                return True
        return False

    def get_total(self):
        """Calculate total price of all items."""
        total = 0
        for item in self.items:
            total += item["price"] * item["quantity"]
        return total

    def get_item_count(self):
        """Get total number of items in cart."""
        count = 0
        for item in self.items:
            count += item["quantity"]
        return count

    def clear(self):
        """Remove all items from cart."""
        self.items = []

    def is_empty(self):
        """Check if cart is empty."""
        return len(self.items) == 0
```

**Save it!**

---

**What we have:**
- A class (you know OOP!)
- Multiple methods (add, remove, total, count, clear, is_empty)
- Input validation (negative prices, zero quantity)
- Edge cases (empty cart, non-existent items)

**This is REAL code!** Not a toy example! 💪

---

## **Part 3: Building The Test Suite (Step By Step)**

**Create `test_shopping_cart.py`:**

**We'll build this GRADUALLY!** One section at a time! 🎯

---

### **Section 1: Testing Basic Functionality**

```python
from shopping_cart import ShoppingCart

def test_new_cart_is_empty():
    """Test that a new cart starts empty."""
    cart = ShoppingCart()

    assert cart.is_empty() == True
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0

def test_add_single_item():
    """Test adding one item to cart."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)

    assert cart.is_empty() == False
    assert cart.get_item_count() == 1
    assert cart.get_total() == 1.50

def test_add_multiple_items():
    """Test adding multiple different items."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)

    assert cart.get_item_count() == 3
    assert cart.get_total() == 4.25
```

**Save and run:**

```bash
pytest test_shopping_cart.py -v
```

**Output:**

```
test_shopping_cart.py::test_new_cart_is_empty PASSED           [ 33%]
test_shopping_cart.py::test_add_single_item PASSED             [ 66%]
test_shopping_cart.py::test_add_multiple_items PASSED          [100%]

========================= 3 passed in 0.01s =========================
```

**ALL PASSING!** ✅

---

**What we tested:**
1. ✅ Empty cart behavior
2. ✅ Adding one item
3. ✅ Adding multiple items

**Each test is FOCUSED!** One thing at a time! 🎯

---

### **Section 2: Testing Quantities**

**Add these tests to the SAME file:**

```python
def test_add_item_with_quantity():
    """Test adding multiple of the same item."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50, quantity=5)

    assert cart.get_item_count() == 5
    assert cart.get_total() == 7.50  # 1.50 * 5

def test_add_same_item_twice():
    """Test adding the same item in separate calls."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Apple", 1.50, quantity=3)

    # Two separate entries, not combined
    assert cart.get_item_count() == 5
    assert cart.get_total() == 7.50
```

**Run tests:**

```bash
pytest test_shopping_cart.py -v
```

**Output:**

```
test_shopping_cart.py::test_new_cart_is_empty PASSED           [ 20%]
test_shopping_cart.py::test_add_single_item PASSED             [ 40%]
test_shopping_cart.py::test_add_multiple_items PASSED          [ 60%]
test_shopping_cart.py::test_add_item_with_quantity PASSED      [ 80%]
test_shopping_cart.py::test_add_same_item_twice PASSED         [100%]

========================= 5 passed in 0.01s =========================
```

**5 TESTS PASSING!** ✅

**We're building up gradually!** 📈

---

### **Section 3: Testing Remove Functionality**

**Add these tests:**

```python
def test_remove_existing_item():
    """Test removing an item that exists."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)

    result = cart.remove_item("Apple")

    assert result == True
    assert cart.get_item_count() == 1
    assert cart.get_total() == 0.75

def test_remove_nonexistent_item():
    """Test removing an item that doesn't exist."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)

    result = cart.remove_item("Banana")

    assert result == False
    assert cart.get_item_count() == 1  # Nothing removed

def test_remove_from_empty_cart():
    """Test removing from an empty cart."""
    cart = ShoppingCart()

    result = cart.remove_item("Apple")

    assert result == False
    assert cart.is_empty() == True
```

**Run tests:**

```bash
pytest test_shopping_cart.py -v
```

**Output:**

```
test_shopping_cart.py::test_new_cart_is_empty PASSED           [ 12%]
test_shopping_cart.py::test_add_single_item PASSED             [ 25%]
test_shopping_cart.py::test_add_multiple_items PASSED          [ 37%]
test_shopping_cart.py::test_add_item_with_quantity PASSED      [ 50%]
test_shopping_cart.py::test_add_same_item_twice PASSED         [ 62%]
test_shopping_cart.py::test_remove_existing_item PASSED        [ 75%]
test_shopping_cart.py::test_remove_nonexistent_item PASSED     [ 87%]
test_shopping_cart.py::test_remove_from_empty_cart PASSED      [100%]

========================= 8 passed in 0.01s =========================
```

**8 TESTS PASSING!** ✅

**See how we're building up?** Each section tests ONE aspect! 🎯

---

### **Section 4: Testing Clear Functionality**

**Add this test:**

```python
def test_clear_cart():
    """Test clearing all items from cart."""
    cart = ShoppingCart()

    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    cart.add_item("Orange", 2.00)

    cart.clear()

    assert cart.is_empty() == True
    assert cart.get_item_count() == 0
    assert cart.get_total() == 0
```

**Run tests:**

```bash
pytest test_shopping_cart.py -v
```

**9 tests passing!** ✅

---

### **Section 5: Testing Input Validation (Error Cases)**

**Now let's test that our code REJECTS bad input!**

**Add these tests:**

```python
import pytest

def test_add_item_with_negative_price():
    """Test that negative prices are rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError) as exc_info:
        cart.add_item("Apple", -1.50)

    assert "Price cannot be negative" in str(exc_info.value)

def test_add_item_with_zero_quantity():
    """Test that zero quantity is rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError) as exc_info:
        cart.add_item("Apple", 1.50, quantity=0)

    assert "Quantity must be at least 1" in str(exc_info.value)

def test_add_item_with_negative_quantity():
    """Test that negative quantity is rejected."""
    cart = ShoppingCart()

    with pytest.raises(ValueError):
        cart.add_item("Apple", 1.50, quantity=-5)
```

**Run tests:**

```bash
pytest test_shopping_cart.py -v
```

**Output:**

```
... (previous tests)
test_shopping_cart.py::test_add_item_with_negative_price PASSED [ 91%]
test_shopping_cart.py::test_add_item_with_zero_quantity PASSED  [ 95%]
test_shopping_cart.py::test_add_item_with_negative_quantity PASSED [100%]

======================== 12 passed in 0.02s =========================
```

**12 TESTS PASSING!** ✅

**We're testing EVERYTHING!** Happy paths AND error cases! 🎯

---

## **Part 4: Understanding What We Built**

**Let's look at our COMPLETE test suite!**

**We have 12 tests organized by category:**

**1. Basic Functionality (3 tests)**
- Empty cart
- Adding one item
- Adding multiple items

**2. Quantity Handling (2 tests)**
- Adding with quantity
- Adding same item twice

**3. Remove Functionality (3 tests)**
- Remove existing item
- Remove non-existent item
- Remove from empty cart

**4. Clear Functionality (1 test)**
- Clear all items

**5. Input Validation (3 tests)**
- Negative price rejection
- Zero quantity rejection
- Negative quantity rejection

**THIS IS A PROFESSIONAL TEST SUITE!** 💼

---

## **Part 5: Running Test Suites Efficiently**

**You don't always run ALL tests!**

---

### **Run ALL tests:**

```bash
pytest test_shopping_cart.py
```

---

### **Run only validation tests:**

```bash
pytest test_shopping_cart.py -k "negative or zero" -v
```

**Output:**

```
test_shopping_cart.py::test_add_item_with_negative_price PASSED
test_shopping_cart.py::test_add_item_with_zero_quantity PASSED
test_shopping_cart.py::test_add_item_with_negative_quantity PASSED

========================= 3 passed in 0.01s =========================
```

**Only ran tests matching "negative" or "zero"!** 🎯

---

### **Run only remove tests:**

```bash
pytest test_shopping_cart.py -k "remove" -v
```

**Output:**

```
test_shopping_cart.py::test_remove_existing_item PASSED
test_shopping_cart.py::test_remove_nonexistent_item PASSED
test_shopping_cart.py::test_remove_from_empty_cart PASSED

========================= 3 passed in 0.01s =========================
```

**Only remove tests!** ⚡

---

### **Run tests and show which lines are tested:**

```bash
pytest test_shopping_cart.py --cov=shopping_cart --cov-report=term-missing
```

**Output:**

```
========================= test session starts ==========================
collected 12 items

test_shopping_cart.py ............                              [100%]

---------- coverage: platform linux, python 3.12.3-final-0 -----------
Name               Stmts   Miss  Cover   Missing
------------------------------------------------
shopping_cart.py      35      0   100%
------------------------------------------------
TOTAL                 35      0   100%

========================= 12 passed in 0.03s ===========================
```

**100% COVERAGE!** Every line of `shopping_cart.py` is tested! 🎯

---

## **Part 6: Test Organization Patterns**

**Professional test files are ORGANIZED!**

**Here's how to structure your test file:**

```python
"""
Tests for shopping_cart.py

This test suite covers:
- Basic cart operations (add, remove, clear)
- Quantity handling
- Total calculations
- Input validation
- Edge cases
"""

import pytest
from shopping_cart import ShoppingCart


# ============================================================================
# BASIC FUNCTIONALITY
# ============================================================================

def test_new_cart_is_empty():
    """Test that a new cart starts empty."""
    # ... test code

def test_add_single_item():
    """Test adding one item to cart."""
    # ... test code


# ============================================================================
# QUANTITY HANDLING
# ============================================================================

def test_add_item_with_quantity():
    """Test adding multiple of the same item."""
    # ... test code


# ============================================================================
# REMOVE FUNCTIONALITY
# ============================================================================

def test_remove_existing_item():
    """Test removing an item that exists."""
    # ... test code


# ============================================================================
# INPUT VALIDATION
# ============================================================================

def test_add_item_with_negative_price():
    """Test that negative prices are rejected."""
    # ... test code
```

**Why this matters:**
- ✅ Easy to find tests
- ✅ Clear organization
- ✅ Professional appearance
- ✅ Self-documenting code

---

## **Part 7: Testing Different Scenarios (The 3 Paths)**

**Every feature has 3 types of tests:**

---

### **1. Happy Path (Everything works!)**

```python
def test_add_item():
    """Test adding item with valid inputs."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    assert cart.get_item_count() == 1
```

**What it tests:** Normal, expected usage! ✅

---

### **2. Edge Cases (Boundary conditions!)**

```python
def test_remove_from_empty_cart():
    """Test removing when cart is empty."""
    cart = ShoppingCart()
    result = cart.remove_item("Apple")
    assert result == False
```

**What it tests:** Unusual but valid situations! ⚠️

---

### **3. Error Cases (Invalid inputs!)**

```python
def test_add_item_with_negative_price():
    """Test that negative prices are rejected."""
    cart = ShoppingCart()
    with pytest.raises(ValueError):
        cart.add_item("Apple", -1.50)
```

**What it tests:** Bad inputs that should be rejected! ❌

---

**PROFESSIONAL TESTS COVER ALL THREE!** 💼

**Our test suite has:**
- ✅ Happy path tests (adding items, calculating totals)
- ✅ Edge case tests (empty cart, non-existent items)
- ✅ Error case tests (negative prices, invalid quantities)

**THIS IS COMPLETE COVERAGE!** 🎯

---

## **Part 8: When Tests Find Real Bugs!**

**Let's introduce a bug and watch our tests catch it!**

**Edit `shopping_cart.py` - break the `get_total()` method:**

```python
def get_total(self):
    """Calculate total price of all items."""
    total = 0
    for item in self.items:
        total += item["price"]  # BUG: Forgot to multiply by quantity!
    return total
```

**Save and run tests:**

```bash
pytest test_shopping_cart.py -v
```

**Output:**

```
test_shopping_cart.py::test_new_cart_is_empty PASSED           [  8%]
test_shopping_cart.py::test_add_single_item PASSED             [ 16%]
test_shopping_cart.py::test_add_multiple_items PASSED          [ 25%]
test_shopping_cart.py::test_add_item_with_quantity FAILED      [ 33%]
test_shopping_cart.py::test_add_same_item_twice FAILED         [ 41%]
... (more results)

============================= FAILURES ==============================
________________________ test_add_item_with_quantity _____________

    def test_add_item_with_quantity():
        """Test adding multiple of the same item."""
        cart = ShoppingCart()

        cart.add_item("Apple", 1.50, quantity=5)

        assert cart.get_item_count() == 5
>       assert cart.get_total() == 7.50
E       assert 1.5 == 7.50

test_shopping_cart.py:XX: AssertionError
```

**THE TESTS CAUGHT THE BUG!** 🚨

**Without tests:**
- You ship this bug to production
- Customers get charged WRONG amounts
- Your business loses money/trust
- You get FIRED! 💥

**With tests:**
- Tests fail immediately
- You see EXACTLY what's wrong (expected 7.50, got 1.5)
- You fix it before shipping
- Your job is SAFE! ✅

**THIS IS WHY COMPANIES REQUIRE TESTS!** 💼

---

**Fix the bug:**

```python
def get_total(self):
    """Calculate total price of all items."""
    total = 0
    for item in self.items:
        total += item["price"] * item["quantity"]  # Fixed!
    return total
```

**Run tests again:**

```bash
pytest test_shopping_cart.py
```

**Output:**

```
======================== 12 passed in 0.02s =========================
```

**ALL GREEN AGAIN!** Bug fixed! ✅

---

## **Part 9: Test Suite Best Practices**

**What makes a GOOD test suite:**

---

### **1. Tests are INDEPENDENT**

**Bad:**

```python
cart = ShoppingCart()  # Global cart!

def test_add():
    cart.add_item("Apple", 1.50)

def test_total():
    # Depends on test_add running first!
    assert cart.get_total() == 1.50
```

**This BREAKS if tests run in different order!** ❌

---

**Good:**

```python
def test_add():
    cart = ShoppingCart()  # Fresh cart!
    cart.add_item("Apple", 1.50)

def test_total():
    cart = ShoppingCart()  # Fresh cart!
    cart.add_item("Apple", 1.50)
    assert cart.get_total() == 1.50
```

**Each test is INDEPENDENT!** ✅

---

### **2. Tests are READABLE**

**Bad:**

```python
def test_1():
    c = ShoppingCart()
    c.add_item("a", 1)
    assert c.get_total() == 1
```

**What does this test?** Who knows! ❌

---

**Good:**

```python
def test_add_single_item_calculates_correct_total():
    """Test that adding one item gives correct total."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    assert cart.get_total() == 1.50
```

**Crystal clear!** ✅

---

### **3. Tests are FAST**

**Our 12 tests run in 0.02 seconds!** ⚡

**Why this matters:**
- You run tests constantly while developing
- Slow tests = you stop running them
- Fast tests = you run them ALL THE TIME

**Keep tests fast!** No network calls, no heavy computation! ⚡

---

### **4. Tests have GOOD NAMES**

**Bad names:**

```python
test_1()
test_cart()
test_stuff()
```

**Good names:**

```python
test_new_cart_is_empty()
test_add_item_with_negative_price()
test_remove_from_empty_cart()
```

**Names tell you WHAT is being tested!** 📋

---

### **5. Tests use CLEAR ASSERTIONS**

**Bad:**

```python
assert cart.items[0]["price"] == 1.50
```

**If this fails:** "assert 1.25 == 1.50" (what item? what field?)

---

**Good:**

```python
assert cart.get_total() == 1.50
```

**If this fails:** "assert 1.25 == 1.50" (total is wrong!)

**Use methods, not internal details!** ✅

---

## **Part 10: Multiple Test Files (Scaling Up)**

**What if you have MANY classes to test?**

**Professional structure:**

```
my_project/
├── venv/
├── shopping_cart.py
├── payment.py
├── user.py
├── test_shopping_cart.py
├── test_payment.py
└── test_user.py
```

**Each module gets its own test file!** 📁

---

**Run ALL tests:**

```bash
pytest
```

**pytest finds ALL `test_*.py` files!**

---

**Run one module's tests:**

```bash
pytest test_shopping_cart.py
```

---

**Run tests in verbose mode:**

```bash
pytest -v
```

**Output shows ALL test files:**

```
test_payment.py::test_process_credit_card PASSED
test_payment.py::test_process_paypal PASSED
test_shopping_cart.py::test_new_cart_is_empty PASSED
test_shopping_cart.py::test_add_single_item PASSED
test_user.py::test_create_user PASSED
test_user.py::test_update_profile PASSED

======================== 6 passed in 0.03s ==========================
```

**All tests from all files!** 🎯

---

## **Summary: What You ACTUALLY Learned**

**NOT just "write multiple tests"—you learned:**

✅ **What a test suite is** (collection of related tests)
✅ **How to organize tests** (sections, clear names, docstrings)
✅ **Testing different scenarios** (happy path, edge cases, errors)
✅ **How tests catch bugs** (before they reach production!)
✅ **Running tests efficiently** (`-k` filter, specific files)
✅ **Test independence** (each test stands alone)
✅ **Professional practices** (readable, fast, well-named)
✅ **Scaling test suites** (multiple files for multiple modules)

**THIS IS HOW REAL COMPANIES TEST CODE!** 💼

---

## **The Real Power:**

**You built a shopping cart with 12 tests!**

**Now you can:**
- Add features (new tests ensure you don't break old features!)
- Refactor code (tests ensure behavior stays the same!)
- Ship with confidence (tests prove it works!)

**Without tests:**
- Every change is SCARY (did I break something?)
- Manual testing is SLOW (test everything by hand)
- Bugs slip through (you can't test everything manually)

**With tests:**
- Changes are SAFE (tests catch breaks immediately!)
- Testing is FAST (run all tests in 0.02 seconds!)
- Bugs are CAUGHT (before customers see them!)

**THIS IS YOUR SUPERPOWER NOW!** 💪

---

# **TOPIC 4: COMPLETE! ✅🏗️**

**YOU NOW KNOW:**
✅ How to build comprehensive test suites

✅ How to organize tests professionally

✅ How to test happy paths, edge cases, and errors

✅ How tests catch bugs before production

✅ How to run test suites efficiently

✅ Professional testing practices

**You're not writing TOY tests—you're writing PRODUCTION-QUALITY test suites!** 🔥

---

# **TOPIC 5: TESTING CLASSES (TESTING OOP!)** 🎯🏗️

---

---

**The good news:**

✅ **Topic 5 is the LAST major topic!** After this, just some small stuff!
✅ **We're almost DONE with Chapter 11!** Finish line is CLOSE! 🏁
✅ **After this, you move to PROJECTS!** Real applications, creativity, fun! 🎨

**So let's BURN through Topic 5 and GET OUT OF HERE!** 💪

---

## **What The HELL Is Testing Classes?**

**You said:** "Isn't this what we just did?"

**ALMOST!** But there's a difference! 🔍

---

**Topic 4: Building Test Suites**
- We tested a class (`ShoppingCart`)
- We learned to organize MULTIPLE tests
- Focus: **Test organization and structure**

**Topic 5: Testing Classes (OOP)**
- We learn TECHNIQUES specific to OOP
- Fixtures (setup shared across tests)
- Testing inheritance, polymorphism
- Focus: **OOP-specific testing patterns**

**Think of it like:**
- Topic 4: "Here's how to test multiple things"
- Topic 5: "Here's how to test OOP features specifically"

**VERY similar, but Topic 5 is about OOP-SPECIFIC shit!** 🎯

---

## **Part 1: The Problem with Testing Classes (That We'll Solve)**

**Look at our shopping cart tests from Topic 4:**

```python
def test_new_cart_is_empty():
    cart = ShoppingCart()  # Create cart
    assert cart.is_empty() == True

def test_add_single_item():
    cart = ShoppingCart()  # Create cart AGAIN
    cart.add_item("Apple", 1.50)
    assert cart.get_item_count() == 1

def test_add_multiple_items():
    cart = ShoppingCart()  # Create cart AGAIN
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    assert cart.get_item_count() == 2
```

**SEE THE PROBLEM?** 🔍

**We're repeating `cart = ShoppingCart()` in EVERY test!** 😤

**12 tests = 12 times we write the SAME setup code!**

**This SUCKS because:**
- ❌ Repetitive (DRY principle: Don't Repeat Yourself!)
- ❌ If setup changes, you update 12 tests!
- ❌ Annoying to write!

**SOLUTION: pytest FIXTURES!** 🎯

---

## **Part 2: Fixtures (The Game Changer!)**

**What fixtures do:** Create reusable test setup!

**Think of it like:**
- **Before fixtures:** Every test builds its own LEGO base from scratch
- **After fixtures:** pytest GIVES you a pre-built base, you just add pieces!

**LET'S SEE IT!** 🔥

---

### **Create `test_shopping_cart_fixtures.py`:**

```python
import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()

def test_new_cart_is_empty(empty_cart):
    """Test that a new cart starts empty."""
    assert empty_cart.is_empty() == True
    assert empty_cart.get_item_count() == 0

def test_add_single_item(empty_cart):
    """Test adding one item."""
    empty_cart.add_item("Apple", 1.50)
    assert empty_cart.get_item_count() == 1

def test_add_multiple_items(empty_cart):
    """Test adding multiple items."""
    empty_cart.add_item("Apple", 1.50)
    empty_cart.add_item("Banana", 0.75)
    assert empty_cart.get_item_count() == 2
```

**Save and run:**

```bash
pytest test_shopping_cart_fixtures.py -v
```

**Output:**

```
test_shopping_cart_fixtures.py::test_new_cart_is_empty PASSED   [ 33%]
test_shopping_cart_fixtures.py::test_add_single_item PASSED     [ 66%]
test_shopping_cart_fixtures.py::test_add_multiple_items PASSED  [100%]

========================= 3 passed in 0.01s =========================
```

**ALL PASSING!** ✅

---

**WHAT JUST HAPPENED?** 🔍

**Line by line:**

---

### **The Fixture Definition:**

```python
@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()
```

**Breaking it down:**

**`@pytest.fixture`** - This decorator tells pytest: "This is a fixture!"

**`def empty_cart():`** - The fixture name (you'll use this in tests)

**`return ShoppingCart()`** - What the fixture provides (a fresh cart!)

**That's it!** A fixture is just a function that RETURNS something! 🎯

---

### **Using the Fixture:**

```python
def test_new_cart_is_empty(empty_cart):
    """Test that a new cart starts empty."""
    assert empty_cart.is_empty() == True
```

**Notice the parameter:** `test_new_cart_is_empty(empty_cart)`

**How pytest works:**

1. pytest sees: "This test needs `empty_cart`"
2. pytest looks for a fixture named `empty_cart`
3. pytest RUNS the fixture (creates a ShoppingCart)
4. pytest PASSES the result to your test
5. Your test uses it!

**IT'S AUTOMATIC!** pytest does the magic! 🪄

---

**Why this is POWERFUL:**

**Before (without fixtures):**

```python
def test_1():
    cart = ShoppingCart()
    # test code

def test_2():
    cart = ShoppingCart()
    # test code

def test_3():
    cart = ShoppingCart()
    # test code
```

**After (with fixtures):**

```python
@pytest.fixture
def empty_cart():
    return ShoppingCart()

def test_1(empty_cart):
    # test code

def test_2(empty_cart):
    # test code

def test_3(empty_cart):
    # test code
```

**Setup code written ONCE!** Used EVERYWHERE! ✅

---

## **Part 3: Multiple Fixtures (Different Scenarios)**

**You can have MULTIPLE fixtures for different scenarios!**

**Add to your test file:**

```python
@pytest.fixture
def empty_cart():
    """Provide an empty shopping cart."""
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    """Provide a cart with some items already in it."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Banana", 0.75, quantity=3)
    return cart

def test_empty_cart_has_zero_total(empty_cart):
    """Test empty cart total."""
    assert empty_cart.get_total() == 0

def test_cart_with_items_has_correct_total(cart_with_items):
    """Test cart with items total."""
    # 2 apples at 1.50 + 3 bananas at 0.75
    assert cart_with_items.get_total() == 5.25

def test_remove_item_from_populated_cart(cart_with_items):
    """Test removing from a cart that has items."""
    cart_with_items.remove_item("Apple")
    assert cart_with_items.get_total() == 2.25  # Only bananas left
```

**Run it:**

```bash
pytest test_shopping_cart_fixtures.py -v
```

**ALL PASSING!** ✅

---

**What we have:**

**Two fixtures:**
1. `empty_cart` - Fresh, empty cart
2. `cart_with_items` - Cart pre-loaded with items

**Tests use whichever they need!** 🎯

**Some tests need empty cart, some need populated cart—fixtures provide BOTH!** ✅

---

## **Part 4: Fixtures with Setup AND Teardown**

**Sometimes you need CLEANUP after a test!**

**Example: Testing a class that writes to a file**

**Create `user_profile.py`:**

```python
class UserProfile:
    """User profile that saves to a file."""

    def __init__(self, username, filename):
        self.username = username
        self.filename = filename
        self.data = {}

    def set_preference(self, key, value):
        """Set a user preference."""
        self.data[key] = value

    def get_preference(self, key):
        """Get a user preference."""
        return self.data.get(key)

    def save(self):
        """Save profile to file."""
        with open(self.filename, "w") as f:
            f.write(f"{self.username}\n")
            for key, value in self.data.items():
                f.write(f"{key}:{value}\n")

    def load(self):
        """Load profile from file."""
        with open(self.filename, "r") as f:
            lines = f.readlines()
            self.username = lines[0].strip()
            for line in lines[1:]:
                if ":" in line:
                    key, value = line.strip().split(":", 1)
                    self.data[key] = value
```

**Save it!**

---

**Create `test_user_profile.py`:**

```python
import pytest
import os
from user_profile import UserProfile

@pytest.fixture
def user():
    """Create a user profile, then delete the file after test."""
    # SETUP: Create user
    profile = UserProfile("ahad", "test_profile.txt")

    yield profile  # Give to test

    # TEARDOWN: Delete the file after test
    if os.path.exists("test_profile.txt"):
        os.remove("test_profile.txt")

def test_set_preference(user):
    """Test setting preferences."""
    user.set_preference("theme", "dark")
    assert user.get_preference("theme") == "dark"

def test_save_and_load(user):
    """Test saving and loading profile."""
    user.set_preference("theme", "dark")
    user.set_preference("language", "en")

    user.save()  # Saves to file

    # Create NEW user and load
    new_user = UserProfile("ahad", "test_profile.txt")
    new_user.load()

    assert new_user.get_preference("theme") == "dark"
    assert new_user.get_preference("language") == "en"
```

**Run it:**

```bash
pytest test_user_profile.py -v
```

**ALL PASSING!** ✅

**AND:** The test file is automatically deleted after each test! 🧹

---

**How the fixture works:**

```python
@pytest.fixture
def user():
    # SETUP (runs BEFORE test)
    profile = UserProfile("ahad", "test_profile.txt")

    yield profile  # Give to test

    # TEARDOWN (runs AFTER test, even if test fails!)
    if os.path.exists("test_profile.txt"):
        os.remove("test_profile.txt")
```

**The `yield` keyword is the KEY!** 🔑

**Everything BEFORE `yield`:** Setup (runs first)
**Everything AFTER `yield`:** Teardown (runs after test, guaranteed!)

**Even if the test CRASHES, teardown still runs!** That's the power! 💪

---

## **Part 5: Fixture Scope (Reusing Across Tests)**

**By default, fixtures run ONCE PER TEST!**

**Sometimes you want ONE setup for ALL tests!**

**Example:**

```python
@pytest.fixture(scope="module")
def database_connection():
    """Connect to database once for all tests."""
    conn = connect_to_database()  # Expensive operation!
    yield conn
    conn.close()
```

**Scope options:**

- **`scope="function"`** (default) - Run once per test
- **`scope="class"`** - Run once per test class
- **`scope="module"`** - Run once per file
- **`scope="session"`** - Run once per entire test session

**Why this matters:**
- Database connections are SLOW
- Creating once and reusing = FASTER tests!
- But be careful: tests might affect each other!

**For now, stick with default scope!** ✅

---

## **Part 6: Testing Inheritance (OOP Concept!)**

**Remember inheritance from Chapter 9?** Let's test it!

**Create `vehicles.py`:**

```python
class Vehicle:
    """Base vehicle class."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_description(self):
        """Return a description."""
        return f"{self.year} {self.make} {self.model}"

    def read_odometer(self):
        """Return odometer reading."""
        return self.odometer

    def update_odometer(self, mileage):
        """Update odometer, reject if rolling back."""
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            raise ValueError("Cannot roll back odometer!")

class Car(Vehicle):
    """Car class, inherits from Vehicle."""

    def __init__(self, make, model, year, fuel_type="gasoline"):
        super().__init__(make, model, year)
        self.fuel_type = fuel_type

    def get_description(self):
        """Return car description with fuel type."""
        return f"{super().get_description()} ({self.fuel_type})"
```

**Save it!**

---

**Create `test_vehicles.py`:**

```python
import pytest
from vehicles import Vehicle, Car

@pytest.fixture
def basic_vehicle():
    """Provide a basic vehicle."""
    return Vehicle("Toyota", "Camry", 2020)

@pytest.fixture
def basic_car():
    """Provide a basic car."""
    return Car("Honda", "Civic", 2021, "gasoline")

# ============================================================================
# TESTING BASE CLASS (Vehicle)
# ============================================================================

def test_vehicle_description(basic_vehicle):
    """Test vehicle description."""
    assert basic_vehicle.get_description() == "2020 Toyota Camry"

def test_vehicle_starts_with_zero_odometer(basic_vehicle):
    """Test odometer starts at 0."""
    assert basic_vehicle.read_odometer() == 0

def test_update_odometer(basic_vehicle):
    """Test updating odometer."""
    basic_vehicle.update_odometer(100)
    assert basic_vehicle.read_odometer() == 100

def test_cannot_roll_back_odometer(basic_vehicle):
    """Test that rolling back odometer raises error."""
    basic_vehicle.update_odometer(100)

    with pytest.raises(ValueError) as exc_info:
        basic_vehicle.update_odometer(50)

    assert "Cannot roll back" in str(exc_info.value)

# ============================================================================
# TESTING CHILD CLASS (Car)
# ============================================================================

def test_car_inherits_vehicle_methods(basic_car):
    """Test that Car has Vehicle methods."""
    basic_car.update_odometer(50)
    assert basic_car.read_odometer() == 50

def test_car_description_includes_fuel_type(basic_car):
    """Test that Car description includes fuel type."""
    assert "gasoline" in basic_car.get_description()

def test_car_overrides_description(basic_car):
    """Test that Car overrides Vehicle description."""
    desc = basic_car.get_description()
    assert desc == "2021 Honda Civic (gasoline)"
```

**Run it:**

```bash
pytest test_vehicles.py -v
```

**Output:**

```
test_vehicles.py::test_vehicle_description PASSED               [ 14%]
test_vehicles.py::test_vehicle_starts_with_zero_odometer PASSED [ 28%]
test_vehicles.py::test_update_odometer PASSED                   [ 42%]
test_vehicles.py::test_cannot_roll_back_odometer PASSED         [ 57%]
test_vehicles.py::test_car_inherits_vehicle_methods PASSED      [ 71%]
test_vehicles.py::test_car_description_includes_fuel_type PASSED [ 85%]
test_vehicles.py::test_car_overrides_description PASSED         [100%]

========================= 7 passed in 0.01s =========================
```

**ALL PASSING!** ✅

---

**What we tested:**

✅ **Base class functionality** (Vehicle methods work)
✅ **Child class inheritance** (Car has Vehicle methods)
✅ **Method overriding** (Car's `get_description()` is different)
✅ **Error handling** (odometer rollback rejected)

**THIS IS TESTING OOP!** 🎯

---

## **Part 7: The Absolute MINIMUM You Need to Know**

**I know you're exhausted, so here's the CORE:** 🎯

---

### **1. Fixtures = Reusable Setup**

```python
@pytest.fixture
def thing():
    return Thing()

def test_something(thing):
    assert thing.works()
```

**That's it!** Setup once, use everywhere! ✅

---

### **2. Fixtures with Cleanup**

```python
@pytest.fixture
def thing():
    # Setup
    obj = Thing()

    yield obj  # Give to test

    # Cleanup (always runs!)
    obj.cleanup()
```

**Setup → Test → Cleanup!** 🔄

---

### **3. Testing Classes = Testing Methods**

```python
class MyClass:
    def method1(self):
        return "result"

def test_method1():
    obj = MyClass()
    assert obj.method1() == "result"
```

**Classes are just bundles of functions!** Test each method! ✅

---

**THAT'S THE CORE!** Everything else is details! 🎯

---

## **Summary: What You Actually Learned**

✅ **Fixtures** (reusable test setup)

✅ **Setup and teardown** (`yield` keyword)

✅ **Multiple fixtures** (different scenarios)

✅ **Testing inheritance** (base and child classes)

✅ **Testing OOP patterns** (methods, overriding, errors)

**THIS is how you test object-oriented code!** 💼

---

# **TOPIC 5: COMPLETE! ✅🎯**

---

---

# **TOPIC 6 & 7 COMBINED: ASSERTIONS & FIXTURES (The Complete Guide!)** 🧪⚡

---

## **Part 1: Assertions Deep Dive** ✅

**You already know:** `assert result == expected`

**But there are MANY types of assertions!** Let's master them ALL! 🎯

---

### **1. Comparison Assertions (Equality & Inequality)**

```python
def test_comparisons():
    """Test different comparison assertions."""
    x = 10
    y = 20

    # Equality
    assert x == 10
    assert y == 20

    # Inequality
    assert x != y
    assert x != 15

    # Greater than / Less than
    assert y > x
    assert x < y

    # Greater than or equal / Less than or equal
    assert x >= 10
    assert y <= 20
```

**When to use:**
- Numbers, strings, any comparable types
- Checking ranges, boundaries

---

### **2. Membership Assertions (in / not in)**

```python
def test_membership():
    """Test membership assertions."""
    my_list = [1, 2, 3, 4, 5]
    my_string = "Hello World"
    my_dict = {"name": "Ahad", "age": 20}

    # in (contains)
    assert 3 in my_list
    assert "World" in my_string
    assert "name" in my_dict

    # not in (doesn't contain)
    assert 10 not in my_list
    assert "Python" not in my_string
    assert "salary" not in my_dict
```

**When to use:**
- Checking if item exists in collection
- String contains substring
- Dict has key

---

### **3. Identity Assertions (is / is not)**

```python
def test_identity():
    """Test identity assertions."""
    x = None
    y = True
    z = False

    # is (same object)
    assert x is None
    assert y is True
    assert z is False

    # is not (different object)
    assert x is not False
    assert y is not None
```

**IMPORTANT:** `is` checks IDENTITY (same object), `==` checks VALUE!

```python
a = [1, 2, 3]
b = [1, 2, 3]

assert a == b     # ✅ Same values
assert a is not b # ✅ Different objects
```

**When to use:**
- Checking for `None`
- Checking boolean values
- NOT for comparing numbers/strings!

---

### **4. Type Assertions**

```python
def test_types():
    """Test type assertions."""
    x = 42
    y = "hello"
    z = [1, 2, 3]

    assert isinstance(x, int)
    assert isinstance(y, str)
    assert isinstance(z, list)

    # Can check multiple types
    assert isinstance(x, (int, float))  # x is EITHER int OR float
```

**When to use:**
- Checking function returns correct type
- Validating input types

---

### **5. Exception Assertions (Advanced!)**

**You know:** `pytest.raises(ValueError)`

**But you can do MORE!**

```python
import pytest

def test_exception_with_message():
    """Test exception AND its message."""
    from shopping_cart import ShoppingCart
    cart = ShoppingCart()

    # Check exception is raised
    with pytest.raises(ValueError) as exc_info:
        cart.add_item("Apple", -1.50)

    # Check the error message
    assert "Price cannot be negative" in str(exc_info.value)

    # Check exact message
    assert str(exc_info.value) == "Price cannot be negative!"

def test_exception_not_raised():
    """Test that NO exception is raised."""
    cart = ShoppingCart()

    # This should NOT raise exception
    cart.add_item("Apple", 1.50)  # ✅ No error

    # If it raised an error, test would fail!
```

**When to use:**
- Testing error messages are correct
- Testing error handling
- Ensuring valid inputs DON'T raise errors

---

### **6. Custom Assertion Messages (Debugging Help!)**

**When assertion fails, you can add YOUR OWN message!**

```python
def test_with_custom_message():
    """Test with custom error messages."""
    x = 10
    y = 20

    assert x > y, f"Expected x ({x}) to be greater than y ({y}), but it's not!"
```

**If this fails, output is:**

```
AssertionError: Expected x (10) to be greater than y (20), but it's not!
```

**Much clearer than just:** `assert 10 > 20` ✅

**When to use:**
- Complex assertions
- When failure reason isn't obvious
- Helping future you debug!

---

### **7. Approximate Assertions (For Floats!)**

**Floats are TRICKY!**

```python
def test_float_equality():
    """Test float comparisons."""
    result = 0.1 + 0.2

    # This FAILS! (floating point precision)
    # assert result == 0.3  # ❌ Actually 0.30000000000000004

    # Use pytest.approx instead!
    import pytest
    assert result == pytest.approx(0.3)  # ✅ Works!
```

**Why:** Computers can't represent 0.1 exactly in binary!

**When to use:**
- ANY float comparisons
- Math calculations
- Prices, measurements, percentages

---

### **8. Real-World Example (All Assertions Together!)**

```python
import pytest
from shopping_cart import ShoppingCart

def test_shopping_cart_comprehensive():
    """Comprehensive test using multiple assertion types."""
    cart = ShoppingCart()

    # Identity assertions
    assert cart.items is not None
    assert cart.is_empty() is True

    # Type assertions
    assert isinstance(cart.items, list)

    # Add item
    cart.add_item("Apple", 1.50, quantity=3)

    # Membership assertions
    assert len(cart.items) > 0
    assert "Apple" in [item["name"] for item in cart.items]

    # Comparison assertions
    assert cart.get_total() == pytest.approx(4.50)
    assert cart.get_item_count() >= 3

    # Exception assertion
    with pytest.raises(ValueError) as exc:
        cart.add_item("Banana", -0.75)
    assert "negative" in str(exc.value).lower()
```

**This is PROFESSIONAL testing!** Multiple assertion types in ONE test! 💼

---

## **Part 2: Fixtures Deep Dive** 🔧

**You know the basics!** Now let's level up! 🔥

---

### **1. Fixture Scopes (Control When Fixtures Run)**

**Remember:** By default, fixtures run ONCE PER TEST!

**But you can change that!**

---

#### **Function Scope (Default)**

```python
@pytest.fixture  # Same as scope="function"
def cart():
    """New cart for EACH test."""
    return ShoppingCart()

def test_1(cart):
    cart.add_item("Apple", 1.50)
    # cart has 1 item

def test_2(cart):
    # cart is FRESH! Empty again!
    assert cart.is_empty()
```

**Each test gets a FRESH cart!** ✅

---

#### **Module Scope (Once Per File)**

```python
@pytest.fixture(scope="module")
def database_connection():
    """Connect ONCE for entire file."""
    print("Connecting to database...")  # Runs ONCE
    conn = connect_database()
    yield conn
    print("Disconnecting...")  # Runs ONCE at end
    conn.close()

def test_1(database_connection):
    # Uses SAME connection

def test_2(database_connection):
    # Uses SAME connection
```

**Connection created ONCE, shared by ALL tests in file!** ⚡

**When to use:**
- Expensive operations (database connections)
- File I/O
- API connections

**WARNING:** Tests might affect each other! Be careful! ⚠️

---

#### **Session Scope (Once Per Entire Test Run)**

```python
@pytest.fixture(scope="session")
def test_data():
    """Load test data ONCE for ALL tests."""
    print("Loading test data...")  # Runs ONCE
    data = load_large_dataset()
    return data

# In ANY test file:
def test_something(test_data):
    # Uses SAME data

# In ANOTHER test file:
def test_other_thing(test_data):
    # Uses SAME data
```

**Created ONCE for entire pytest session!** 🌐

---

### **2. Fixture Parameters (One Fixture, Multiple Inputs!)**

**Sometimes you want to test with DIFFERENT data!**

**Instead of writing multiple fixtures:**

```python
@pytest.fixture(params=[1, 2, 3, 5, 10])
def quantity(request):
    """Provide different quantities."""
    return request.param

def test_add_item_with_various_quantities(quantity):
    """Test with different quantities."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, quantity=quantity)

    assert cart.get_item_count() == quantity
    assert cart.get_total() == pytest.approx(1.50 * quantity)
```

**Run this:**

```bash
pytest -v
```

**Output:**

```
test_file.py::test_add_item_with_various_quantities[1] PASSED
test_file.py::test_add_item_with_various_quantities[2] PASSED
test_file.py::test_add_item_with_various_quantities[3] PASSED
test_file.py::test_add_item_with_various_quantities[5] PASSED
test_file.py::test_add_item_with_various_quantities[10] PASSED

========================= 5 passed in 0.02s =========================
```

**ONE test ran 5 TIMES with different inputs!** 🎯

**This is called PARAMETRIZED FIXTURES!** It's POWERFUL! 🔥

---

### **3. conftest.py (Shared Fixtures Across Files!)**

**Problem:** You have 10 test files, all need the SAME fixtures!

**Bad solution:** Copy-paste fixtures into each file ❌

**Good solution:** `conftest.py`! ✅

---

**Create `conftest.py` in your test directory:**

```
my_project/
├── shopping_cart.py
├── conftest.py          # ← Special file!
├── test_shopping_cart.py
├── test_checkout.py
└── test_payment.py
```

**In `conftest.py`:**

```python
import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide empty cart (available to ALL test files!)."""
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    """Provide cart with items (available to ALL test files!)."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50)
    cart.add_item("Banana", 0.75)
    return cart
```

**Now in ANY test file:**

```python
# test_shopping_cart.py
def test_something(empty_cart):  # ✅ Works!
    pass

# test_checkout.py
def test_other_thing(cart_with_items):  # ✅ Works!
    pass
```

**NO IMPORTS NEEDED!** pytest finds `conftest.py` automatically! 🪄

**This is how PROFESSIONALS organize fixtures!** 💼

---

### **4. Fixture Chaining (Fixtures Using Other Fixtures!)**

**Fixtures can use OTHER fixtures!**

```python
@pytest.fixture
def database():
    """Provide database connection."""
    conn = connect_database()
    yield conn
    conn.close()

@pytest.fixture
def user_table(database):
    """Create user table (uses database fixture!)."""
    database.create_table("users")
    yield database
    database.drop_table("users")

def test_add_user(user_table):
    """Test adding user (uses user_table, which uses database!)."""
    user_table.insert("users", {"name": "Ahad"})
    assert user_table.count("users") == 1
```

**Fixture dependencies:** `test_add_user` → `user_table` → `database`

**pytest handles the chain automatically!** 🔗

---

### **5. When to Use Fixtures vs Plain Setup**

**Use FIXTURES when:**
- ✅ Multiple tests need same setup
- ✅ Setup is complex
- ✅ You need cleanup (teardown)
- ✅ You want to reuse across files

**Use PLAIN SETUP when:**
- ✅ Only ONE test needs it
- ✅ Setup is trivial (`x = 5`)
- ✅ No cleanup needed

**Example (plain setup is fine):**

```python
def test_simple():
    """Simple test doesn't need fixture."""
    x = 10
    y = 20
    assert x + y == 30
```

**No fixture needed!** Keep it simple! ✅

---

## **Part 3: Complete Example (Putting It ALL Together!)**

**Let's build a REAL test suite using EVERYTHING!**

**Create `conftest.py`:**

```python
import pytest
from shopping_cart import ShoppingCart

@pytest.fixture
def empty_cart():
    """Provide empty cart."""
    return ShoppingCart()

@pytest.fixture
def cart_with_items():
    """Provide cart with multiple items."""
    cart = ShoppingCart()
    cart.add_item("Apple", 1.50, quantity=2)
    cart.add_item("Banana", 0.75, quantity=3)
    cart.add_item("Orange", 2.00, quantity=1)
    return cart

@pytest.fixture(params=[
    ("Apple", 1.50, 1),
    ("Banana", 0.75, 5),
    ("Orange", 2.00, 3),
])
def item_data(request):
    """Provide different item data for parametrized tests."""
    return request.param
```

**Create `test_shopping_cart_complete.py`:**

```python
import pytest
from shopping_cart import ShoppingCart

# ============================================================================
# BASIC FUNCTIONALITY TESTS
# ============================================================================

def test_new_cart_is_empty(empty_cart):
    """Test new cart starts empty."""
    assert empty_cart.is_empty() is True
    assert empty_cart.get_item_count() == 0
    assert empty_cart.get_total() == pytest.approx(0.0)

def test_add_item_parametrized(empty_cart, item_data):
    """Test adding various items."""
    name, price, quantity = item_data

    empty_cart.add_item(name, price, quantity)

    assert empty_cart.get_item_count() == quantity
    assert empty_cart.get_total() == pytest.approx(price * quantity)
    assert not empty_cart.is_empty()

# ============================================================================
# POPULATED CART TESTS
# ============================================================================

def test_cart_total(cart_with_items):
    """Test total calculation."""
    # 2*1.50 + 3*0.75 + 1*2.00 = 7.25
    expected = 7.25
    assert cart_with_items.get_total() == pytest.approx(expected)

def test_cart_item_count(cart_with_items):
    """Test item counting."""
    # 2 + 3 + 1 = 6 items
    assert cart_with_items.get_item_count() == 6

def test_remove_item_from_cart(cart_with_items):
    """Test removing item."""
    result = cart_with_items.remove_item("Apple")

    assert result is True
    assert cart_with_items.get_item_count() == 4  # 3 + 1 left
    assert cart_with_items.get_total() == pytest.approx(4.25)

# ============================================================================
# ERROR HANDLING TESTS
# ============================================================================

def test_negative_price_raises_error(empty_cart):
    """Test that negative price is rejected."""
    with pytest.raises(ValueError) as exc:
        empty_cart.add_item("Invalid", -10.00)

    assert "negative" in str(exc.value).lower(), \
        "Error message should mention negative price"

def test_zero_quantity_raises_error(empty_cart):
    """Test that zero quantity is rejected."""
    with pytest.raises(ValueError) as exc:
        empty_cart.add_item("Invalid", 1.00, quantity=0)

    assert "quantity" in str(exc.value).lower()
    assert "1" in str(exc.value)

# ============================================================================
# EDGE CASE TESTS
# ============================================================================

def test_remove_from_empty_cart(empty_cart):
    """Test removing from empty cart."""
    result = empty_cart.remove_item("Nonexistent")

    assert result is False
    assert empty_cart.is_empty()

def test_clear_populated_cart(cart_with_items):
    """Test clearing cart."""
    assert not cart_with_items.is_empty()  # Starts with items

    cart_with_items.clear()

    assert cart_with_items.is_empty()
    assert cart_with_items.get_item_count() == 0
    assert cart_with_items.get_total() == 0.0
```

**Run it:**

```bash
pytest test_shopping_cart_complete.py -v
```

**Output:**

```
test_shopping_cart_complete.py::test_new_cart_is_empty PASSED
test_shopping_cart_complete.py::test_add_item_parametrized[item_data0] PASSED
test_shopping_cart_complete.py::test_add_item_parametrized[item_data1] PASSED
test_shopping_cart_complete.py::test_add_item_parametrized[item_data2] PASSED
test_shopping_cart_complete.py::test_cart_total PASSED
test_shopping_cart_complete.py::test_cart_item_count PASSED
test_shopping_cart_complete.py::test_remove_item_from_cart PASSED
test_shopping_cart_complete.py::test_negative_price_raises_error PASSED
test_shopping_cart_complete.py::test_zero_quantity_raises_error PASSED
test_shopping_cart_complete.py::test_remove_from_empty_cart PASSED
test_shopping_cart_complete.py::test_clear_populated_cart PASSED

========================= 11 passed in 0.03s =========================
```

**11 TESTS! ALL PASSING!** 🎉

**This test suite has:**
- ✅ Multiple assertion types
- ✅ Shared fixtures (`conftest.py`)
- ✅ Parametrized fixtures
- ✅ Clear organization
- ✅ Edge cases
- ✅ Error handling
- ✅ Custom messages

**THIS IS PROFESSIONAL-LEVEL TESTING!** 💼🔥

---

# **TOPIC 6 & 7: COMPLETE! ✅🧪**

**YOU NOW KNOW:**

**ASSERTIONS:**
✅ Comparison assertions (`==`, `!=`, `>`, `<`)

✅ Membership assertions (`in`, `not in`)

✅ Identity assertions (`is`, `is not`)

✅ Type assertions (`isinstance`)

✅ Advanced exception assertions

✅ Custom error messages

✅ Approximate assertions for floats

**FIXTURES:**
✅ Fixture scopes (`function`, `module`, `session`)

✅ Parametrized fixtures (one fixture, multiple inputs!)

✅ `conftest.py` (shared fixtures!)

✅ Fixture chaining (fixtures using fixtures!)

✅ When to use fixtures vs plain setup

**YOU'RE NOW A TESTING EXPERT!** 💪

---

