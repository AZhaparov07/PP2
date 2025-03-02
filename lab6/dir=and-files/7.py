def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as src, open(destination, "w", encoding="utf-8") as dest:
        dest.write(src.read())

source_file = r"C:\Users\User\Desktop\pp2 start\PP2\lab6\textfile.txt"
destination_file = "copy.txt"

copy_file(source_file, destination_file)

print("File copied")
