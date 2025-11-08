"""
Lab 3: OS Module for File System Operations
============================================
Objective: Master file and directory operations using the os module

Topics Covered:
- Directory operations (create, list, remove, change)
- File operations (create, rename, delete, check existence)
- Path operations (join, split, absolute paths)
- Environment variables
- File metadata (size, modification time, permissions)
"""

import os
from datetime import datetime

# ========================================
# Exercise 1: Working with Directories
# ========================================
print("=" * 50)
print("Exercise 1: Directory Operations")
print("=" * 50)

# TODO: Get current working directory
current_dir = os.getcwd()
print(f"Current directory: {current_dir}")

# TODO: Create a new directory
test_dir = "test_deployment"
if not os.path.exists(test_dir):
    os.mkdir(test_dir)
    print(f"Created directory: {test_dir}")
else:
    print(f"Directory already exists: {test_dir}")

# TODO: Create nested directories
nested_dir = os.path.join(test_deployment", "logs", "2024", "january")
os.makedirs(nested_dir, exist_ok=True)
print(f"Created nested directories: {nested_dir}")

# TODO: List directory contents
print(f"\nContents of current directory:")
items = os.listdir(".")
for item in items[:10]:  # Show first 10 items
    item_path = os.path.join(".", item)
    item_type = "DIR" if os.path.isdir(item_path) else "FILE"
    print(f"  [{item_type}] {item}")

# TODO: Check if path exists and its type
paths_to_check = ["test_deployment", "nonexistent_file.txt", "."]

print(f"\nChecking paths:")
for path in paths_to_check:
    if os.path.exists(path):
        if os.path.isfile(path):
            print(f"  {path} - File exists")
        elif os.path.isdir(path):
            print(f"  {path} - Directory exists")
    else:
        print(f"  {path} - Does not exist")

print()

# ========================================
# Exercise 2: File Operations
# ========================================
print("=" * 50)
print("Exercise 2: File Operations")
print("=" * 50)

# TODO: Create a test file
config_file = os.path.join("test_deployment", "app.config")
with open(config_file, "w") as f:
    f.write("# Application Configuration\n")
    f.write("PORT=8080\n")
    f.write("HOST=localhost\n")
print(f"Created file: {config_file}")

# TODO: Create a log file
log_file = os.path.join("test_deployment", "logs", "2024", "january", "app.log")
with open(log_file, "w") as f:
    f.write("2024-01-15 10:00:00 INFO Application started\n")
    f.write("2024-01-15 10:01:00 INFO Server listening on port 8080\n")
print(f"Created log file: {log_file}")

# TODO: Rename a file
old_name = config_file
new_name = os.path.join("test_deployment", "application.config")
os.rename(old_name, new_name)
print(f"Renamed: {old_name} -> {new_name}")

# TODO: Get file information
if os.path.exists(new_name):
    file_size = os.path.getsize(new_name)
    mod_time = os.path.getmtime(new_name)
    mod_time_readable = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')

    print(f"\nFile information for {new_name}:")
    print(f"  Size: {file_size} bytes")
    print(f"  Modified: {mod_time_readable}")

print()

# ========================================
# Exercise 3: Path Operations
# ========================================
print("=" * 50)
print("Exercise 3: Path Operations")
print("=" * 50)

# TODO: Join paths correctly (cross-platform)
base_path = "/var/log"
app_name = "myapp"
log_filename = "application.log"

full_path = os.path.join(base_path, app_name, log_filename)
print(f"Joined path: {full_path}")

# TODO: Split path into components
directory, filename = os.path.split(full_path)
print(f"Directory: {directory}")
print(f"Filename: {filename}")

# TODO: Split filename and extension
name, extension = os.path.splitext(filename)
print(f"Name: {name}")
print(f"Extension: {extension}")

# TODO: Get absolute path
relative_path = "test_deployment"
absolute_path = os.path.abspath(relative_path)
print(f"\nRelative path: {relative_path}")
print(f"Absolute path: {absolute_path}")

# TODO: Get base name and directory name
sample_path = "/home/user/projects/app/main.py"
print(f"\nSample path: {sample_path}")
print(f"Base name: {os.path.basename(sample_path)}")
print(f"Directory name: {os.path.dirname(sample_path)}")

# TODO: Normalize path
messy_path = "/home/user/../user/./projects//app/main.py"
clean_path = os.path.normpath(messy_path)
print(f"\nMessy path: {messy_path}")
print(f"Normalized: {clean_path}")

print()

# ========================================
# Exercise 4: Environment Variables
# ========================================
print("=" * 50)
print("Exercise 4: Environment Variables")
print("=" * 50)

# TODO: Get environment variable
home_dir = os.environ.get("HOME") or os.environ.get("USERPROFILE")
print(f"Home directory: {home_dir}")

user = os.environ.get("USER") or os.environ.get("USERNAME")
print(f"Current user: {user}")

# TODO: Get with default value
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
print(f"\nDatabase configuration:")
print(f"  Host: {db_host}")
print(f"  Port: {db_port}")

# TODO: Set environment variable (for current process only)
os.environ["APP_ENV"] = "development"
os.environ["LOG_LEVEL"] = "DEBUG"

print(f"\nSet environment variables:")
print(f"  APP_ENV: {os.environ.get('APP_ENV')}")
print(f"  LOG_LEVEL: {os.environ.get('LOG_LEVEL')}")

# TODO: List all environment variables (first 5)
print(f"\nFirst 5 environment variables:")
for i, (key, value) in enumerate(os.environ.items()):
    if i >= 5:
        break
    print(f"  {key}={value[:50]}...")  # Truncate long values

print()

# ========================================
# Exercise 5: Walking Directory Tree
# ========================================
print("=" * 50)
print("Exercise 5: Walking Directory Tree")
print("=" * 50)

# TODO: Walk through directory tree
print(f"Directory tree of test_deployment:")
for root, dirs, files in os.walk("test_deployment"):
    # Calculate indentation level
    level = root.replace("test_deployment", "").count(os.sep)
    indent = "  " * level
    print(f"{indent}{os.path.basename(root)}/")

    # Print files with extra indentation
    sub_indent = "  " * (level + 1)
    for file in files:
        file_path = os.path.join(root, file)
        file_size = os.path.getsize(file_path)
        print(f"{sub_indent}{file} ({file_size} bytes)")

print()

# ========================================
# Exercise 6: Real DevOps Scenario - Log File Management
# ========================================
print("=" * 50)
print("Exercise 6: Real DevOps Scenario - Log Management")
print("=" * 50)

# TODO: Create a log directory structure
log_base = "test_deployment/logs"

services = ["nginx", "app", "database"]
log_types = ["access", "error"]

print("Creating log directory structure:")
for service in services:
    for log_type in log_types:
        log_dir = os.path.join(log_base, service, log_type)
        os.makedirs(log_dir, exist_ok=True)
        print(f"  Created: {log_dir}")

        # Create a sample log file
        log_file = os.path.join(log_dir, f"{service}_{log_type}.log")
        with open(log_file, "w") as f:
            f.write(f"# {service} {log_type} log\n")
            f.write(f"2024-01-15 10:00:00 Sample log entry\n")

# TODO: Find all .log files
print(f"\nAll .log files in {log_base}:")
log_files = []
for root, dirs, files in os.walk(log_base):
    for file in files:
        if file.endswith(".log"):
            full_path = os.path.join(root, file)
            log_files.append(full_path)
            file_size = os.path.getsize(full_path)
            print(f"  {full_path} ({file_size} bytes)")

print(f"\nTotal log files found: {len(log_files)}")

print()

# ========================================
# Exercise 7: File Permissions and Metadata
# ========================================
print("=" * 50)
print("Exercise 7: File Permissions and Metadata")
print("=" * 50)

# Create a test script
script_file = os.path.join("test_deployment", "deploy.sh")
with open(script_file, "w") as f:
    f.write("#!/bin/bash\n")
    f.write("echo 'Deployment script'\n")

print(f"Created script: {script_file}")

# TODO: Get file stats
stats = os.stat(script_file)
print(f"\nFile statistics:")
print(f"  Size: {stats.st_size} bytes")
print(f"  Created: {datetime.fromtimestamp(stats.st_ctime).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Modified: {datetime.fromtimestamp(stats.st_mtime).strftime('%Y-%m-%d %H:%M:%S')}")
print(f"  Accessed: {datetime.fromtimestamp(stats.st_atime).strftime('%Y-%m-%d %H:%M:%S')}")

# TODO: Make file executable (Unix-like systems)
if os.name != 'nt':  # Not Windows
    os.chmod(script_file, 0o755)
    print(f"Made {script_file} executable")

print()

# ========================================
# Exercise 8: Practical Task - Backup System
# ========================================
print("=" * 50)
print("Exercise 8: Simple Backup System")
print("=" * 50)

# TODO: Create backup directory structure
backup_base = "test_deployment/backups"
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
backup_dir = os.path.join(backup_base, timestamp)

os.makedirs(backup_dir, exist_ok=True)
print(f"Created backup directory: {backup_dir}")

# TODO: Copy configuration files to backup
config_source = os.path.join("test_deployment", "application.config")
if os.path.exists(config_source):
    import shutil
    config_backup = os.path.join(backup_dir, "application.config")
    shutil.copy2(config_source, config_backup)
    print(f"Backed up: {config_source} -> {config_backup}")

# TODO: List all backups
print(f"\nAll backups:")
if os.path.exists(backup_base):
    backups = sorted(os.listdir(backup_base), reverse=True)
    for backup in backups:
        backup_path = os.path.join(backup_base, backup)
        if os.path.isdir(backup_path):
            backup_size = sum(
                os.path.getsize(os.path.join(backup_path, f))
                for f in os.listdir(backup_path)
                if os.path.isfile(os.path.join(backup_path, f))
            )
            print(f"  {backup} ({backup_size} bytes)")

print("\n" + "=" * 50)
print("Lab 3 Complete!")
print("=" * 50)

# Cleanup
print("\nCleaning up test files...")
import shutil
if os.path.exists("test_deployment"):
    shutil.rmtree("test_deployment")
    print("Removed test_deployment directory")

# ========================================
# Your Tasks:
# ========================================
"""
1. Create a directory structure for a web application:
   - app/static/css
   - app/static/js
   - app/templates
   - app/logs

2. Write code to find all Python files (.py) in the current directory and subdirectories

3. Create a function that checks if a directory exists, if not, creates it

4. Get the size of all files in a directory and calculate total size

5. Read the PATH environment variable and print each path on a new line

6. Create a script that organizes files by extension:
   - Create folders for each extension found
   - Move files to their respective folders

7. Write code to find the largest file in a directory

8. Create a backup system that:
   - Creates timestamped backup folders
   - Copies all .config files to the backup folder
   - Lists all available backups sorted by date
"""
