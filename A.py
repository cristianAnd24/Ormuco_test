def lines_overlap(line1, line2):
    x1, x2 = line1
    x3, x4 = line2

    # Check if lines do not overlap
    if x2 < x3 or x1 > x4:
        return False

    return True

# Test the function with your examples
print(lines_overlap((1,5), (2,6)))  # True
print(lines_overlap((1,5), (6,8)))  # False
