def FtoC():
    F = float(input("Write a  temperature: "))
    return (5/9) * (F - 32)
print("Equivalent centigrade temperature: ", round(FtoC(),2))
