def compare_two_numbers(a, b):
    if a > b:
        largest = a
        smallest = b
    elif b > a:
        largest = b
        smallest = a
    else:
        largest = smallest = a  # or b, since they are equal

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")

# Example usage:
compare_two_numbers(10, 20)
