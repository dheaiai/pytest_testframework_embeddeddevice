# Create a utility module for file handling functions
file_utils_path = "/mnt/data/file_utils.py"

file_utils_code = '''import os
import json
import shutil

def create_directory(path):
    """Creates a directory if it doesn't exist."""
    os.makedirs(path, exist_ok=True)

def read_file(file_path):
    """Reads a file and returns its content."""
    with open(file_path, 'r') as f:
        return f.read()

def write_file(file_path, content):
    """Writes content to a file."""
    with open(file_path, 'w') as f:
        f.write(content)

def copy_file(src, dst):
    """Copies a file from src to dst."""
    shutil.copy2(src, dst)

def delete_file(file_path):
    """Deletes a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)

def read_json(file_path):
    """Reads a JSON file and returns the data."""
    with open(file_path, 'r') as f:
        return json.load(f)

def write_json(file_path, data):
    """Writes data to a JSON file."""
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)

# Example usage
if __name__ == "__main__":
    test_path = "test_dir"
    test_file = os.path.join(test_path, "example.txt")

    create_directory(test_path)
    write_file(test_file, "Hello, World!")
    print("File content:", read_file(test_file))
    copy_file(test_file, os.path.join(test_path, "copy.txt"))
    delete_file(test_file)
'''

# Write the file
with open(file_utils_path, "w") as f:
    f.write(file_utils_code)

file_utils_path
