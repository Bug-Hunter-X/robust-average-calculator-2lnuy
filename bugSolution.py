def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    if all(x == 0 for x in numbers):
        return 0 #Handle list with only zeros
    return sum(numbers) / len(numbers)

# Example usage:
my_numbers = [10, 20, 30, 40, 50]
average = calculate_average(my_numbers)
print(f"The average is: {average}")

my_empty_list = []
average_empty = calculate_average(my_empty_list) 
print(f"The average of an empty list is: {average_empty}")

my_numbers_with_zero = [10,0,0, 0, 50]
average_with_zero = calculate_average(my_numbers_with_zero) 
print(f"The average with zeros is: {average_with_zero}")

my_zeros_list = [0,0,0,0,0]
average_all_zeros = calculate_average(my_zeros_list)
print(f"The average of all zeros is: {average_all_zeros}") 