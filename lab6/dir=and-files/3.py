import os

def check_path(path):
    if os.path.exists(path):
        return {
            "Exists": True,
            "Directory": os.path.dirname(path),
            "Filename": os.path.basename(path),
        }
    return {"Exists": False}

path = r"C:\Users\User\Desktop\pp2 start\PP2\lab6\textfile.txt"

result = check_path(path)
print(result)
