x = int(input("Number of heads: "))
y = int(input("Numbers of legs: "))
def solve(numheads, numlegs):
    # x + y = numheads -> x = numheads - y
    # 2x + 4y = numlegs -> 2numheads - 2y + 4y = numlegs - > 2numheads + 2y = numlegs -> y = (numlegs - 2numheads)/2 
    rabit = int((numlegs-2*numheads)/2) 
    chicken = int(35 - rabit)
    print(f"amount of chicken: {chicken} and amount of rabits: {rabit}")
solve(x,y)