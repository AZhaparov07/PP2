import os

def list_contents(path):
    items = os.listdir(path)
    directories = [i for i in items if os.path.isdir(os.path.join(path, i))]
    files = [i for i in items if os.path.isfile(os.path.join(path, i))]
    print(items)
    print(directories)
    print(files)

path = "C:/Users"

list_contents(path)

