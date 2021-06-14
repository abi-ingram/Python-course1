def my_maths_function(int1, int2, math_function):
    if type(int1) != int or type(int2) != int:
        print('First 2 arguments must be integers!')
        return

    if math_function.lower() == "add":
        return int1 + int2
    elif math_function.lower() == "subtract":
        return int1 - int2
    elif math_function.lower() == "divide":
        return int1 / int2
    elif math_function.lower() == "multiply":
        return int1 * int2
    else:
        print("Choose add, subtract, divide or multiply")

print(my_maths_function('a', 4, "add"))
print(my_maths_function(12, 3, "subtract"))
print(my_maths_function(10, 2, "divide"))
print(my_maths_function(20, 10, "multiply"))