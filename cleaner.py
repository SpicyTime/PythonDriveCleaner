#!/usr/bin/env python3
import os
import shutil
file_types: set = set() 
file_categories = {
    "image": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".webp", ".svg"],
    "document": [".txt", ".pdf", ".doc", ".docx", ".gdoc", ".odt", ".rtf", ".md"],
    "audio": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "video": [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".webm"],
    "code": [".py", ".js", ".html", ".css", ".cpp", ".c", ".java", ".json", ".xml", ".sh", ".bat", ".php"],
    "archive": [".zip", ".rar", ".7z", ".tar", ".gz", ".iso"],
    "data": [".csv", ".tsv", ".xlsx", ".xls", ".db", ".sqlite", ".parquet", ".yml", ".yaml"],
    "executable": [".exe", ".msi", ".apk", ".app", ".bin", ".sh", ".bat"],
    "font": [".ttf", ".otf", ".woff", ".woff2"],
    "system": [".dll", ".sys", ".ini", ".bak", ".tmp", ".log"]
}
def get_folder_category_name(category):
    return category.capitalize() + 's'

def categorize_file(file_name) -> str:
    _, ext = os.path.splitext(file_name)
    ext = ext.lower()
    for category, extensions in file_categories.items():
        if ext in extensions:
            return category
    return "unknown"
def add_category(category):
    folder_name = get_folder_category_name(category)
    os.makedirs(folder_name, exist_ok=True)
def organize():
    dir: list = os.listdir(os.curdir)
    for file in dir:
        print(file)
        category: str = categorize_file(file)
        if os.path.isdir(file):
            print(file, "Is directory")
            continue
        category_folder_name: str = get_folder_category_name(category)
        print(category_folder_name)
        if not category_folder_name in dir:
            add_category(category)
        ext:str = file.rsplit(".", 1)[1]

        ext_folder_name = ext + "_files"
        ext_folder_path = os.path.join(category_folder_name, ext_folder_name)
        if not ext_folder_name in category_folder_name:
            os.makedirs(ext_folder_path, exist_ok=True)
        shutil.move(file, os.path.join(ext_folder_path, file))
        
organize()