# 🐍 Python OS Module – Basics

This project demonstrates essential operations using Python's built-in **os module**, focusing on directory and file management.

---

## 📌 Overview

This project includes basic examples of how to:

* Create folders
* Check if folders exist
* Create nested folder structures
* List contents inside a folder
* Identify files vs directories
* Count files inside a directory
* Display folder structure in a tree-style format

These operations are foundational for automation, DevOps scripting, and managing files programmatically.

---

## 🧰 OS Module Functions Used

| Function           | Description                                   |
| ------------------ | --------------------------------------------- |
| `os.makedirs()`    | Creates directories (supports nested folders) |
| `os.path.exists()` | Checks if a path exists                       |
| `os.listdir()`     | Lists items inside a directory                |
| `os.path.isfile()` | Checks if a path is a file                    |
| `os.path.isdir()`  | Checks if a path is a folder                  |
| `os.remove()`      | Removes a file                                |
| `os.unlink()`      | Same as remove (file deletion)                |
| `os.rmdir()`       | Removes an **empty** directory                |

---

## 📁 Folder Structure Example

Your script automatically creates:

```
log/
├── error/
├── debug/
└── info/
```

Each folder can contain files and the program counts and displays them.

---

## 🧪 File Counting Function

The project includes a helper function to count files inside a directory:

```python
count_files_in_folder(folder_path)
```

This counts **only files**, not subdirectories.

---

## ▶️ How to Run

1. Save the script as a `.py` file.
2. Run it with:

```bash
python your_script.py
```

3. The script will:

   * Create necessary folders
   * Check their existence
   * Count files in each folder
   * Print a visual directory tree with file counts

---

## ⭐ Why Learn the OS Module?

Understanding the OS module helps with:

* Automation and scripting
* DevOps workflows
* Log management
* File backups and cleanup scripts
* Building custom utilities

It is one of the most important modules for system-level Python scripting.

---

## 🚀 Future Enhancements

You can continue this project by adding:

* Recursive file counting
* File creation/deletion utilities
* Move/Copy operations (using `shutil`)
* Log rotation scripts
* A CLI-based folder manager tool

---

Feel free to expand this README as your project grows!
