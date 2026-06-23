def math_factorial(n):
    # Calculates n! (Example: 4! = 4 * 3 * 2 * 1 = 24)
    product = 1
    for i in range(1, n + 1):
        product = product * i
    return product

def n_choose_r(n, r):
    # Calculates combinations of choosing r items out of n total items
    # Formula: n! / (r! * (n - r)!)
    top = math_factorial(n)
    bottom = math_factorial(r) * math_factorial(n - r)
    return top // bottom

if __name__ == "__main__":
    # Test 1: Calculate 5 factorial (5!)
    print("5 factorial is:")
    print(math_factorial(5))
    
    # Test 2: AMC 12 Example - Ways to choose 2 lines out of 5 total lines
    print("5 choose 2 is:")
    print(n_choose_r(5, 2))
