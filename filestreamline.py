import os
try:
    from pathlib import Path
except:
    os.system('python -m pip install pathlib')
    from pathlib import Path

# Define file categories and their extensions
subcategory = {
    'DOCUMENTS': ['.pdf', '.txt', '.doc', '.rtf', '.pptx', '.docx', '.odt'],
    'AUDIO': ['.mp3', '.m4b', '.m4a', '.webvtt', '.cea-608', '.cea-708', '.dfxp', '.sami', '.scc', '.srt', '.ttml', '.3gpp'],
    'VIDEOS': ['.mov', '.avi', '.mp4', '.3gp', '.ogg', '.oga', '.ogv', '.ogx', '.wmv', '.webm', '.flv', '.mxf', '.mpeg-2', '.ts', '.wav', '.vob'],
    'IMAGES': ['.jpg', '.jpeg', '.raw', '.png', '.tiff', '.gif'],
    'PROGRAMMING FILES': ['.htm', '.html', '.cpp', '.c', '.py', '.css', '.java']
}

def find_the_category(extension):
    """Find the category for a given file extension."""
    extension = extension.lower()
    for category, extensions in subcategory.items():
        if extension in extensions:
            return category
    return 'MISC'

def organize_dir(directory_path):
    """Organize files in the given directory into categorized folders."""
    directory_path = Path(directory_path)
    
    if not directory_path.is_dir():
        print(f"The path '{directory_path}' is not a valid directory.")
        return
    
    for file in directory_path.iterdir():
        if file.is_file():
            file_type = file.suffix.lower()
            category = find_the_category(file_type)
            category_dir = directory_path / category
            
            if not category_dir.exists():
                category_dir.mkdir()
            
            file.rename(category_dir / file.name)

if __name__ == "__main__":
    user_path = input("Enter the directory path to organize: ")
    organize_dir(user_path)
