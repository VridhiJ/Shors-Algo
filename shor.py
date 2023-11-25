# Finding Prime Factors of an integer using Shor's algorithm on classical computers. 
# Authors: Vridhi Jain and Sunil Jain; Creative Commons Attribution License CC-BY-3.0.
# This is an open access materia distributed under the terms of the Creative Commons Attribution License CC-BY-3.0, which permits unrestricted use, distribution, and reproduction in any medium, provided the original author and source are credited.  

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_prime_factors(num):
    prime_factors = []
    for i in range(2, num + 1):
        if num % i == 0 and is_prime(i):
            prime_factors.append(i)
    return prime_factors

def find_r_values(g, n, num_values):
    r_values = []
    r = 1

    while len(r_values) < num_values:
        # Check if (g^r)/n leaves remainder 1
        if (g ** r) % n == 1:
            r_values.append(r)

        r += 1

    return r_values

def find_prime_factors_for_r(g, n, r_values):
    prime_factors = []
    
    for r in r_values:
        # Check if ((g^(r/2) + 1) or (g^(r/2) - 1)) is a multiple of a prime factor of n
        factors = find_prime_factors(n)

        for factor in factors:
            candidate1 = (g ** (r // 2) + 1) // factor
            candidate2 = (g ** (r // 2) - 1) // factor

            if (g ** (r // 2) + 1) % factor == 0 or (g ** (r // 2) - 1) % factor == 0:
                prime_factors.append(factor)

    return prime_factors

# Example usage and logic: Assume n = p*q (where p and q are prime); asuume a number g which is coprime with n; In the equation g^r = m*n+1, find r such that g^r/n leaves remainder 1.
g_value = 5  # Replace with your desired value for g
n_value = 999999  # Replace with your desired value for n
num_values_to_find = 2  # Replace with the number of r values you want to find

r_values = find_r_values(g_value, n_value, num_values_to_find)
calculated_prime_factors = find_prime_factors_for_r(g_value, n_value, r_values)

print(f"Prime factors of n ({n_value}) such that ((g^(r/2)+1) or (g^(r/2)-1)) is a multiple of one of them:")
print(calculated_prime_factors, r_values)
