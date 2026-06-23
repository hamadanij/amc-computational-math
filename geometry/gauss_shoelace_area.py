def get_triangle_area(p1, p2, p3):
    # Breaks up points into simple x and y coordinates!
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # First we multiply down-right diagonals and add them
    down_diagonals = (x1 * y2) + (x2 * y3) + (x3 * y1)

    # Multiply up-right diagonals and add them
    up_diagonals = (y1 * x2) + (y2 * x3) + (y3 * x1)

    # Step 3: Find the difference, make it positive, and divide by 2
    shoelace_determinant = down_diagonals - up_diagonals
    area = 0.5 * abs(shoelace_determinant)
    
    return area


# --- Example Use (Works for ANY set of points) ---
if __name__ == "__main__":
    point_A = (0, 0)
    point_B = (4, 0)
    point_C = (0, 3)

    area = get_triangle_area(point_A, point_B, point_C)
    
    print("The area of the triangle is:")
    print(area)
