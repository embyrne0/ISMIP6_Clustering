''' 
File for importing/selecting your data files
''' 

# importing 
import os
import tkinter as tk
from tkinter import filedialog

def select_directory():
    # Create a Tkinter root window
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    # Open a file dialog window and ask the user to select a directory
    directory = filedialog.askdirectory(title="Select Directory")

    # Check if a directory was selected
    if directory:
        print(f"Selected directory: {directory}")
        # Check if the selected directory exists
        if os.path.exists(directory) and os.path.isdir(directory):
            print(f"The folder at '{directory}' exists.")
        else:
            print(f"The folder at '{directory}' does not exist or is not a directory.")
    else:
        print("No directory selected.")

# If this script is executed directly, call the function
if __name__ == "__main__":
    select_directory()