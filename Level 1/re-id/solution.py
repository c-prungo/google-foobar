def solution(i):

    # using this length as it creates a prime sequence of length 10,000
    prime_sequence = get_prime_sequence(20232)
    return prime_sequence[i:i+5]

# using sieve of Eratosthenes method to get a sequence of prime numbers
# https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
def get_prime_sequence(n):

    prime_sequence = ""

    primes_table = [True for i in range(n+1)] 
    p_num = 2

    # apply Eratosthenes sieve to tabulate primes up to number n
    while (p_num**2 <= n):
        # if a prime is identified, iterate through all of its products and set them to false (as they are divisible by p_num on principle)
        if (primes_table[p_num] == True):
            for i in range(p_num**2, n+1, p_num):
                primes_table[i] = False
        p_num += 1

    # use table to generate prime_sequence
    for p in range(2, n): 
        if primes_table[p]: 
            prime_sequence += str(p)

    return prime_sequence