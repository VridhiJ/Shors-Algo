def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

# Example
number = 987654321987654321
result = prime_factors(number)
print(f"Prime factors of {number}: {result}")
