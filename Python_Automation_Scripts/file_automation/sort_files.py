import os
import shutil

def sort_files(folder):
    for file in os.listdir(folder):
        path = os.path.join(folder, file)

        if os.path.isfile(path):
            ext = file.split(".")[-1]
            dest = os.path.join(folder, ext)

            os.makedirs(dest, exist_ok=True)
            shutil.move(path, dest)

    print("Files sorted successfully!")

# Example
sort_files("C:/Users/User/Downloads")
