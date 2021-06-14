# def hello(name):
#     print(f"Hello, {name}")

# hello("Abi")

# new_name = "Ryan"

# hello(new_name)

def is_even( num ):
    if num % 2 == 0:
        return True
    else:
        return False


my_num = int(input('Give me an integer! '))

if is_even(my_num):
    word = 'yes'
else: 
    word = 'no'

print(f"Is {my_num} even? {word}!")
