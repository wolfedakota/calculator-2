"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
while True:
    input_string = input("Give operation : ")
    if input_string == "q":
        break
    else:
        tokens = input_string.split(' ')
        if tokens[0] == 'pow':
            print(power(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == 'add':
            print(add(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == 'subtract':
            print(subtract(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == 'multiply':
            print(multiply(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == 'divide':
            print(divide(float(tokens[1]), float(tokens[2])))
        elif tokens[0] == 'square':
            print(square(float(tokens[1])))
        elif tokens[0] == 'cube':
            print(cube(float(tokens[1])))
        elif tokens[0] == 'mod':
            print(mod(float(tokens[1]), float(tokens[2])))


        ### cube and square verify function's signature 
    
    
