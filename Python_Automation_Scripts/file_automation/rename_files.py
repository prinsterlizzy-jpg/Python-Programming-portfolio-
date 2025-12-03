import os

def rename_files(folder, prefix):
    files = os.listdir(folder)

    for index, file in enumerate(files):
        ext = file.split(".")[-1]
        new_name = f"{prefix}_{index}.{ext}"
        os.rename(
            os.path.join(folder, file),
            os.path.join(folder, new_name)
        )

    print("Renamed successfully!")

# Example
rename_files("C:/Users/User/Documents/images", "photo")
