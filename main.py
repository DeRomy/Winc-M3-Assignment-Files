import os
import shutil


__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"


current_dir = os.path.dirname(__file__)
cache_path = os.path.join(current_dir, "cache")
zip_path = os.path.join(current_dir, "data.zip")


# Vraag 1
def clean_cache():
    if os.path.exists(cache_path):
        shutil.rmtree(cache_path)
    os.mkdir(cache_path)


# Vraag 2
def cache_zip(zip, cache):
    shutil.unpack_archive(zip, cache)


# Vraag 3
def cached_files():
    files = os.listdir(cache_path)
    file_paths = []
    for file in files:
        file_path = os.path.join(cache_path, file)
        file_paths.append(file_path)
    return file_paths


# Vraag 4
def find_password(cached_files):
    for file in cached_files:
        with open(file, "r") as f:
            lines = f.readlines()
            for line in lines:
                if "password" in line:
                    password_line = line
    password = password_line[password_line.find(" ") + 1 : password_line.rfind("\n")]
    return password


if __name__ == "__main__":
    clean_cache()
    cache_zip(zip_path, cache_path)
    print(find_password(cached_files()))
