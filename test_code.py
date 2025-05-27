# test_code.py
def calculate_average(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)

result = calculate_average([1, 2, 3, 0])
print(result)
