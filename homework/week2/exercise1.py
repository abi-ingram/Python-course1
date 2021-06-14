# for number in range(0,10):
#     if (number % 3 == 0):
#         continue
#     else:
#         print(number)

for n in range(0,10):
    if (n % 3 == 0):
        continue
    else:
        print(n)

max_number = int(input("What is the max number?"))

for n in range(max_number):
    if (n % 3 == 0):
        continue
    else:
        print(n)