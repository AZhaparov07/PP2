def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as file:
        return sum(1 for _ in file)

file_path = r"C:\Users\User\Desktop\pp2 start\PP2\lab6\textfile.txt"

lines = count_lines(file_path)
print(f"Number of lines: {lines}")
#sum(1 for _ in file) 
#sum(len(line) for line in file) 
#sum(len(line.split()) for line in file) 