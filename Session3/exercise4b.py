counter = 0
total_sum = 0 
while counter <= 500:
    if counter % 3 == 0:
        print(f'adding {counter} to current sum {total_sum} to make {counter + total_sum}.')
        total_sum = total_sum + counter 
    counter = counter + 1
print(f'Total sum is {total_sum}.')