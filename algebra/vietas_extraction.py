#Extracts the sum and product from a quadratic!
def vieta_quadratic(a, b, c):
    sum_of_roots = -b / a
    product_of_roots = c / a
    return sum_of_roots, product_of_roots


#REAL AMC 12 EXAMPLE
# Problem: Find the sum and product of the roots for 2x^2 - 12x + 10 = 0
a, b, c = 2, -12, 10

r_sum, r_prod = vieta_quadratic(a, b, c)

#Test Result
print("Sum of roots (r1 + r2):", r_sum)
print("Product of roots (r1 * r2):", r_prod)
