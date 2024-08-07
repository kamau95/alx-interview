#!/usr/bin/python3
def pascal_triangle(n):
        """
    Generates Pascal's Triangle up to a specified number of rows.

    Parameters:
        n (int): The number of rows in Pascal's Triangle to generate.

    Returns:
        list: A list of lists where each inner list represents a row in Pascal's
        Triangle. Returns an empty list if n <= 0.
    """
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
