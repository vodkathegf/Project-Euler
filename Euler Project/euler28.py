def sum_of_diagonals_in_spiral(size):
    total_sum = 1  # starting from 1x1
    for n in range(3, size+1, 2):  # iterating odd numbers till the size
        # top-right
        total_sum += n**2
        # top-left
        total_sum += (n**2)-(n-1)
        # bottom-left
        total_sum += (n**2)-2*(n-1)
        # bottom-right
        total_sum += (n**2)-3*(n-1)
    return total_sum


result = sum_of_diagonals_in_spiral(1001)
print(result)
