def compare_three_numbers(a, b, c):
    # Finding largest
    if a >= b and a >= c:
        largest = a
    elif b >= a and b >= c:
        largest = b
    else:
        largest = c

    # Finding smallest
    if a <= b and a <= c:
        smallest = a
    elif b <= a and b <= c:
        smallest = b
    else:
        smallest = c

    print(f"Largest: {largest}")
    print(f"Smallest: {smallest}")

# Example usage:
compare_three_numbers(15, 25, 10)
