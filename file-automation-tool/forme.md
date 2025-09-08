
---

## **Step 0: Setup**

1. Create a folder on your desktop or anywhere, call it `my_folder`.
2. Put some random files there: `example.txt`, `photo.jpg`, `report.pdf`, `music.mp3`, `notes.docx`.
3. In the same location, create your Python script: `file_organizer.py`.

---

## **Step 1: Import Modules**

```python
import os
import shutil
```

**Explanation:**

* `import os` → This lets Python **talk to your operating system**. You can list files, check if something exists, create folders, etc.
* `import shutil` → This is like a **superpowered hand**. You can move files, copy them, delete them easily.

Think:
`os = look & inspect`
`shutil = grab & move`

---

## **Step 2: Define Your Folder Path**

```python
folder_path = "./my_folder"  # Change this to your folder
```

* `folder_path` → variable storing where your messy files live.
* `"./my_folder"` → means the folder named `my_folder` in the **same directory as your script**.
* You can change it if your folder is somewhere else: `"C:/Users/Ahad/Desktop/my_folder"`

---

## **Step 3: Organize Files by Type**

```python
def organize_files(path):
    for filename in os.listdir(path):  # Step 1
        file_path = os.path.join(path, filename)  # Step 2
        if os.path.isfile(file_path):  # Step 3
            ext = filename.split('.')[-1]  # Step 4
            ext_folder = os.path.join(path, ext)  # Step 5
            if not os.path.exists(ext_folder):  # Step 6
                os.makedirs(ext_folder)  # Step 7
            shutil.move(file_path, os.path.join(ext_folder, filename))  # Step 8
```

**Line by line:**

1. `for filename in os.listdir(path):` → lists everything in `my_folder` and goes **one by one**.
2. `file_path = os.path.join(path, filename)` → combines folder path + filename → full path (`./my_folder/example.txt`).
3. `if os.path.isfile(file_path):` → ignore subfolders, **only process files**.
4. `ext = filename.split('.')[-1]` → get the file extension (`txt`, `jpg`, etc.).
5. `ext_folder = os.path.join(path, ext)` → new folder path for that type (`./my_folder/txt`).
6. `if not os.path.exists(ext_folder):` → check if the folder already exists.
7. `os.makedirs(ext_folder)` → if it doesn’t exist, create it.
8. `shutil.move(file_path, os.path.join(ext_folder, filename))` → **move file** into its new folder.

✅ Result: messy folder → files automatically sorted into `txt/`, `jpg/`, `pdf/`, etc.

---

## **Step 4: Rename Files in Batch**

```python
def rename_files(path, prefix):
    for count, filename in enumerate(os.listdir(path), 1):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            ext = filename.split('.')[-1]
            new_name = f"{prefix}_{count}.{ext}"
            new_path = os.path.join(path, new_name)
            os.rename(file_path, new_path)
```

**Explanation:**

* `enumerate(..., 1)` → gives **numbers starting from 1** automatically.
* `f"{prefix}_{count}.{ext}"` → new name pattern, e.g., `project_1.txt`, `project_2.jpg`.
* `os.rename(file_path, new_path)` → **renames the file** in place.

💡 This is super practical: imagine you have 100 photos from your phone. This will **rename all of them in seconds**.

---

## **Step 5: Backup Files**

```python
def backup_files(path, backup_folder):
    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            shutil.copy(file_path, os.path.join(backup_folder, filename))
```

**Explanation:**

* Check if `backup_folder` exists, if not, create it.
* Go through all files in `path`.
* Copy each file into `backup_folder`.
* Safety net → if something goes wrong, you don’t lose your files.

---

## **Step 6: Running Everything**

```python
organize_files(folder_path)  # Step 1
rename_files(folder_path, "project")  # Step 2
backup_files(folder_path, "./backup")  # Step 3
print("Files organized, renamed, and backed up! ✅")  # Final message
```

* **Step 1:** Sort all files into folders by type.
* **Step 2:** Rename all files in the main folder.
* **Step 3:** Make backup in `./backup`.
* **Step 4:** Print confirmation to terminal.

💥 When you run this in terminal (`python3 file_organizer.py`) → you see folders appear, files moved, renamed, and copied. Instant gratification.

---

### **Step 7: How to Execute**

1. Make folder inside script folder:

   ```bash
   mkdir my_folder
   ```
2. Add some dummy files:

   ```bash
   touch test.txt photo.jpg music.mp3
   ```
3. Run the script:

   ```bash
   python3 fat.py
   ```

4. ✅ Watch the magic → new folders (`txt/`, `jpg/`, `mp3/`) appear, files move inside them.

---
   ```
4. Watch the magic → messy files **organized automatically**.

---

### **Step 8: What You Learn**

1. **os & shutil** → interacting with system & files.
2. **loops** → iterate over items.
3. **if statements** → check conditions (file exists, folder exists).
4. **functions** → reusable chunks of code (`organize_files`, `rename_files`, `backup_files`).
5. **string manipulation** → `split`, f-strings, formatting.
6. **automation logic** → real-world useful scripts.
7. **debugging basics** → if file doesn’t move, you’ll see errors → fix it.

---

