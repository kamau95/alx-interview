"""
#!/usr/bin/python3
def pascal_triangle(n):
    Generates Pascal's Triangle up to a specified number of rows.

    Parameters:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        list: A list of lists where each inner
        list represents a row in Pascal's
        Triangle. Returns an empty list if n <= 0.

    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element is always 1
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # Last element is always 1
        triangle.append(row)

    return triangle
    """


def pascal_triangle(n):
    """returns a list of lists of numbers
    representing the pascal triangle"""
    if n <= 0:
        return []

    pascal_triangle = [0] * n

    for i in range(n):
        # define a row and fill first and last idx with 1
        new_row = [0] * (i+1)
        new_row[0] = 1
        new_row[len(new_row) - 1] = 1

        for j in range(1, i):
            if j > 0 and j < len(new_row):
                a = pascal_triangle[i - 1][j]
                b = pascal_triangle[i - 1][j - 1]
                new_row[j] = a + b

        pascal_triangle[i] = new_row

    return pascal_triangle
