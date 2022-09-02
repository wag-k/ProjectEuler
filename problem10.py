def get_primes_generator_with_eratosthenes(upper_limit: int) -> iter:
    """Get prime numbers with sieve of Erastosthenes below `upper_limit`(included `uppper_limit`)

    Args:
        upper_limit (int): max number

    Returns:
        iter: prime numbers below `upper_limit`
    """
    sieve = [True for n in range(0, upper_limit+1)]
    
    for current_number in range(2, upper_limit+1):
        if(sieve[current_number] == False):
            continue
        yield current_number
        for sieved_number in range(current_number, upper_limit+1, current_number):
            sieve[sieved_number] = False

def solve_priblem10():
    upper_limit = 2000000
    prime_generator = get_primes_generator_with_eratosthenes(upper_limit)
    primes = list(prime_generator)
    return sum(primes)
    

if __name__ == "__main__":
    print(solve_priblem10())