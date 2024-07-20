#Exercise 1
hours = int(input('Enter number of hours you worked this week:'))
normal_rate = 51.45
overload_rate = 88.9
thrd_hours = 35

if hours > thrd_hours:
    pay = (thrd_hours * normal_rate) + ((hours - thrd_hours) *overload_rate)
else:
    pay = hours * normal_rate
print(f'This weekly payment is: {pay}')

#Exercise 2
number = [-2, 3, 9, 1, 5, 7, 2, 11, 0, 3, 12, 3, 15, 10]
temp_largest = numbers[0]
print('Before', temp_largest)
for number in numbers:
    if number > temp_largest:
        temp_largest = number
    print(number, temp_largest)
print(f'The largest number is: {temp_largest}')

#Exercise 3
for i in range(1, 4):
    for j in range(i,4):
        print(i,j)
