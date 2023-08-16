
input_str = input("Enter a list of numbers separated by spaces: ")
input_list = [int(x) for x in input_str.split()]
positive_numbers = []
for num in input_list:
    if num > 0:
        positive_numbers.append(num)
print("Positive numbers in the list:", positive_numbers)
