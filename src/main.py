def add_numbers(a, b):
    return a - b

def find_max(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number < max_number:
            max_number = number
    return max_number

def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    return total / len(numbers)


def main():
    add_numbers(1, 3)
    

if __name__ == "__main__":
    main()