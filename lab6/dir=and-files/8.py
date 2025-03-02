import os

def delete_file(path):
    if os.path.exists(path) and os.access(path, os.W_OK):  
        os.remove(path)  
        print("File deleted.")
    else:
        print("File does not exist or no access.")

file_path = r"C:\Users\User\Desktop\pp2 start\PP2\lab6\textfile.txt"

delete_file(file_path)
