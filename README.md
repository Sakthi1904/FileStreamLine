# FileStreamline

**FileStreamline** is a powerful and intuitive tool designed to help you organize files in your directory into neatly categorized folders. By automatically sorting files based on their extensions, FileStreamline streamlines your workflow and ensures your files are always in order.

## Features

- **Automatic File Categorization**: Organizes files into predefined categories such as Documents, Audio, Videos, Images, and Programming Files.
- **Customizable Categories**: Easily modify or extend the file categories and their associated extensions to suit your needs.
- **User-Friendly Interface**: Simple command-line interface to input the directory path and start the organization process.
- **Efficient Organization**: Quickly moves files into the appropriate folders without manual intervention.

## Installation

FileStreamline is designed to be run in a Python environment. Follow these steps to get started:

1. **Clone the Repository:**
    ```sh
    git clone https://github.com/Sakthi1904/filestreamline.git
    ```

2. **Navigate to the Project Directory:**
    ```sh
    cd filestreamline
    ```

3. **Ensure Dependencies Are Installed:**
    FileStreamline relies on Python's `pathlib` module, which is included in the Python standard library. Make sure you have Python 3.4 or later installed.

## Usage

1. **Run the Script:**
    ```sh
    python filestreamline.py
    ```

2. **Enter the Directory Path:**
    When prompted, enter the full path to the directory you want to organize.

## Error Handling

The script includes basic error handling:

- **Invalid Directory:** If the provided path is not a valid directory, a message will be displayed.
- **File Operations:** Handles common file operation issues such as missing files or inaccessible directories.

## Customization
- **Modify Categories:** You can edit the `subcategory` dictionary in the script to change file categories or add new extensions.


**Happy Organizing!**
