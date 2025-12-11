import os
import shutil

ext_map = {
    "images": [".png", ".jpg"],
    "docs": [".pdf", ".txt", ".docx"],
    "videos": [".mp4", ".mkv"],
    "zips": [".zip", ".rar"]
}

path = "./"

for file in os.listdir(path):
    for folder, exts in ext_map.items():
        if any(file.endswith(e) for e in exts):
            os.makedirs(folder, exist_ok=True)
            shutil.move(file, folder)
            print("Moved:", file)
