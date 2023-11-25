import math

def estimate_primes(x):
    if x < 2:
        return 0
    
    estimated_primes = x / math.log(x)
    return round(estimated_primes)

# Example
number_to_estimate = 123456789
estimated_count = estimate_primes(number_to_estimate)

print(f"Estimated number of primes up to {number_to_estimate}: {estimated_count}")

