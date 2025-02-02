import math
def volofspher():
    print("Write a radius: ")
    radius = int(input())
    return (4/3)*(math.pi)*(radius**3)
print(volofspher())