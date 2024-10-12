def choose():
    color = input("red or blue: ")
    
    if color == "blue":
        return "Same"
    
    elif color == "red":
        return "Cool"

result = choose()
print(result)
