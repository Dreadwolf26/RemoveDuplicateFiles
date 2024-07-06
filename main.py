import os
import zipfile
import tkinter as tk
from tkinter import filedialog

def list_files_in_zip(zip_filepath):
    """List all files in a zip archive."""
    with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
        return zip_ref.namelist()

def file_exists_in_directory(directory, filepath):
    """Check if a file exists in the directory."""
    return os.path.exists(os.path.join(directory, filepath))

def find_and_delete_duplicate_zips(directory):
    """Find and delete zip files if their contents exist in the directory."""
    for dirpath, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith('.zip'):
                zip_filepath = os.path.join(dirpath, filename)
                try:
                    zip_contents = list_files_in_zip(zip_filepath)
                    all_files_exist = all(file_exists_in_directory(dirpath, file) for file in zip_contents)
                    if all_files_exist:
                        os.remove(zip_filepath)
                        print(f"Deleted zip file: {zip_filepath}")
                except (OSError, zipfile.BadZipFile) as e:
                    print(f"Error processing {zip_filepath}: {e}")

def select_directory():
    """Open a file dialog to select a directory."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    directory = filedialog.askdirectory(title="Select Directory to Scan for Duplicates")
    return directory

if __name__ == "__main__":
    directory = select_directory()
    if directory:
        find_and_delete_duplicate_zips(directory)
        print("Duplicate zip files removed if their contents exist in the directory.")
    else:
        print("No directory selected.")
