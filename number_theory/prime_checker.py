def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime
        
    for i in range(2, n):
        if n % i == 0:
            return False  # Found a divisor, so it's not prime
            
    return True  # No divisors found, so our number is prime!
