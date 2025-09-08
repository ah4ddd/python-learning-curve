### **File organizer Automated**
## 1. Imports

```python
import os
import shutil
```

* **`import os`** → “Hey Python, I want to talk to the **Operating System**. I want to check files, folders, paths, etc.”

  * Functions like `os.listdir()`, `os.path.join()`, `os.makedirs()` are all in `os`.
  * Think of `os` as a **toolkit to manage files/folders**.

* **`import shutil`** → “Python, I want to **move or copy files** easily.”

  * `shutil.move()` → move file from place A → B
  * `shutil.copy()` → copy file from place A → B
  * This library doesn’t create files; it just moves or copies **existing ones**.

---

## 2. Defining folder path

```python
folder_path = "./my_folder"
```

* `folder_path` is a **variable**. Think of it as a **sticky note that remembers where your folder is**.

* `"./my_folder"` → `./` = current folder, `my_folder` = folder name.

* Example: if your terminal is in `/home/ahad/project/`, then this points to `/home/ahad/project/my_folder`.

* ⚡ Important: **This folder must exist already**. Python won’t magically create `my_folder` for you unless you code it.

---

## 3. Function: Backup Files

```python
def backup_files(path, backup_folder):
```

* `def` → defines a **function** (a reusable block of code).
* `backup_files` → name of the function. You call it later with: `backup_files(folder_path, "./backup")`.
* `path` → temporary name for your folder (here, it will be `"./my_folder"`).
* `backup_folder` → temporary name for the folder where backup will go (here, `"./backup"`).

```python
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
```

* `os.path.exists(backup_folder)` → checks: does a folder/file with this name already exist?
* `not` → “if it does **not** exist”
* `os.makedirs()` → **make the folder** (create directory).
* **So:** If backup folder doesn’t exist, it is created. ✅

```python
    for root, _, files in os.walk(path):
```

* `os.walk(path)` → **walks through every folder/subfolder** starting from `path`.

* Returns **3 things** each time:

  1. `root` → current folder path being looked at
  2. `_` → list of subfolders inside this folder (we don’t use it here, so we write `_`)
  3. `files` → list of all files inside `root`

* Example: if my\_folder has:

```
my_folder/
├── file1.txt
├── file2.pdf
└── images/
    └── photo.jpg
```

* First iteration:

  * root = `my_folder/`
  * files = `['file1.txt', 'file2.pdf']`
* Second iteration:

  * root = `my_folder/images/`
  * files = `['photo.jpg']`

```python
        for filename in files:
            file_path = os.path.join(root, filename)
```

* Loop through **every file** in current folder (`files`).
* `os.path.join(root, filename)` → makes the **full path** to that file.

  * Example: `root = my_folder/images/`, `filename = photo.jpg` → `file_path = my_folder/images/photo.jpg`

```python
            shutil.copy(file_path, os.path.join(backup_folder, filename))
```

* `shutil.copy()` → make a **copy** of the file.
* `os.path.join(backup_folder, filename)` → where the copy goes.
* Example: backup\_folder = `backup/` → `backup/photo.jpg` is created.
* **Important:** It doesn’t remove original file; original stays in `my_folder`.

✅ **Result:** All files from `my_folder` (and subfolders) are copied into `backup/`.

---

## 4. Function: Organize Files

```python
def organize_files(path):
    for filename in os.listdir(path):
```

* `os.listdir(path)` → returns **all items (files + folders)** inside `path` (not recursive).
* Example: `my_folder/` contains `['file1.txt', 'file2.pdf', 'images']`.

```python
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
```

* `os.path.isfile(file_path)` → True if this is a **file**, not a folder.
* ⚡ Only files will be moved; folders are ignored.

```python
            ext = filename.split('.')[-1]
```

* `filename.split('.')` → splits the file name by `.`
* `[-1]` → take the **last part**, which is the file extension
* Example:

  * `example.txt` → `['example', 'txt']` → `ext = 'txt'`
  * `report.final.pdf` → `['report', 'final', 'pdf']` → `ext = 'pdf'`

```python
            ext_folder = os.path.join(path, ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
```

* Create a folder named after the extension if it doesn’t exist.
* Example: `my_folder/txt/` or `my_folder/pdf/`

```python
            shutil.move(file_path, os.path.join(ext_folder, filename))
```

* Move the file into the folder corresponding to its extension.
* Original file is **removed** from `my_folder` and now lives inside the new folder.

✅ **Result:** Files are sorted by type inside folders.

---

## 5. Function: Rename Files Recursively

```python
def rename_files_recursive(path, prefix):
    count = 1
```

* Start counting files at 1.
* `prefix` = string that will start the filename (`"project"`).

```python
    for root, _, files in os.walk(path):
        for filename in files:
            ext = filename.split('.')[-1]
            old_path = os.path.join(root, filename)
            new_name = f"{prefix}_{count}.{ext}"
            new_path = os.path.join(root, new_name)
            os.rename(old_path, new_path)
            count += 1
```

* **Walk through all folders** recursively.
* For every file:

  1. Get its extension.
  2. Build a **new name**: `project_1.txt`, `project_2.pdf`, etc.
  3. `os.rename(old_path, new_path)` → actually renames the file.
  4. Increment `count` → next file will get `project_2`, then `project_3`.

✅ **Result:** All files inside organized folders get new sequential names.

---

## 6. Main Execution (The Engine)

```python
backup_files(folder_path, "./backup")
organize_files(folder_path)
rename_files_recursive(folder_path, "project")
```

* **Step 1:** Backup all files first → safety net.
* **Step 2:** Organize by type → txt/, pdf/, jpg/ folders created.
* **Step 3:** Rename → all files get sequential project\_\* names inside their folder.

```python
print("Files backed up, organized, and renamed! ✅")
```

* Confirms everything is done.

---

## ✅ Flow Example (Everything at Once)

Start:

```
my_folder/
├── example.txt
├── photo.jpg
├── report.pdf
```

Step 1 → Backup:

```
backup/
├── example.txt
├── photo.jpg
├── report.pdf
```

Step 2 → Organize:

```
my_folder/
├── txt/
│   └── example.txt
├── pdf/
│   └── report.pdf
├── jpg/
│   └── photo.jpg
```

Step 3 → Rename:

```
my_folder/
├── txt/
│   └── project_1.txt
├── pdf/
│   └── project_2.pdf
├── jpg/
│   └── project_3.jpg
```

---

### **How to Execute**

1. Make folder inside script folder:

   ```bash
   mkdir my_folder
   ```
2. Add some dummy files in my_folder:

   ```bash
   touch test.txt photo.jpg music.mp3
   ```
3. Run the script:

   ```bash
   python3 fat.py
   ```

4. Watch the magic → messy files > organized

---

## 🔑 Key Concepts You Must Internalize

1. **Variables** store info temporarily (`folder_path`, `count`, `filename`).
2. **`os.path.join()`** → safely joins folders + file names → cross-platform friendly.
3. **`os.walk()`** → loop through folder & subfolders recursively.
4. **`os.makedirs()`** → create folder if it doesn’t exist.
5. **`shutil.copy()`** → make a backup copy.
6. **`shutil.move()`** → physically move file from one folder → another.
7. **`os.rename()`** → rename file in place.
8. **Functions** → reusable chunks of code. You call them in the main program.
9. **Flow matters:** Backup → Organize → Rename. If you rename before backup, backups get renamed too.

---
