def product_except_self(nums):
    n = len(nums)
    left_products = [1] * n
    right_products = [1] * n
    output = []

    # Calculate the product of all elements to the left of each element
    for i in range(1, n):
        left_products[i] = left_products[i - 1] * nums[i - 1]
    print(left_products)

    # Calculate the product of all elements to the right of each element
    for i in range(n - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]
    print(right_products)

    # Calculate the product excluding the current value to write to output list
    for i in range(n):
        output.append(left_products[i] * right_products[i])

    return output


print(product_except_self([1, 2, 3, 4, 5]))
