def write_list_to_file(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        file.writelines("\n".join(data))

my_list = ["Apple", "Banana", "Cherry"]

file_path = r"C:\Users\User\Desktop\pp2 start\PP2\lab6\textfile.txt"

write_list_to_file(file_path, my_list)

print("Task is done")
