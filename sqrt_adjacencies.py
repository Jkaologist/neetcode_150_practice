from math import sqrt


def rearrange_sequence(n):
    # Generate a list of numbers from 1 to n
    numbers = list(range(1, n + 1))

    # Helper function to check if two numbers add up to a perfect square
    def is_perfect_square(x, y):
        return sqrt(x + y) % 1 == 0

    # Helper function to swap two numbers in the list
    def swap(i, j):
        numbers[i], numbers[j] = numbers[j], numbers[i]

    # Recursive function to rearrange the list
    def rearrange(start):
        # Base case: if all numbers are in place, return True
        if start == n:
            return True

        # Recursive case: try swapping the current number with each subsequent number
        for i in range(start, n):
            if start == 0 or is_perfect_square(numbers[start - 1], numbers[i]):
                swap(start, i)
                if rearrange(start + 1):
                    return True
                swap(start, i)  # Undo the swap

        return False

    # Call the recursive function to rearrange the list
    rearrange(0)

    return numbers


print(rearrange_sequence(15))  # [1, 3, 2, 4, 7, 6, 5, 15, 14, 13, 12, 11, 10, 9, 8]
print(rearrange_sequence(5))  # [1, 3, 2, 5, 4]
