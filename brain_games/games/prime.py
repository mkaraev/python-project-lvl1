import random

DESCRIPTION = "Answer \'yes\' if given number is prime. " \
              "Otherwise answer \'no\'."

MAX_NUM = 1000
primes = None


def generate_question_answer_pair():
    nums = [_generate_random_prime(), random.randint(0, 1000)]
    random_number = random.choice(nums)
    answer = "yes" if random_number in primes else "no"
    return f"Question: {random_number}", answer


def _generate_random_prime():
    global primes
    if not primes:
        _sieve()
    return random.choice(primes)


def _sieve():
    global primes
    is_prime = [True for i in range(MAX_NUM)]
    is_prime[0] = False
    is_prime[1] = False

    p = 2
    while p ** 2 <= MAX_NUM:
        if is_prime[p]:
            for i in range(p ** 2, MAX_NUM, p):
                is_prime[i] = False
        p += 1
    primes = [i for i in range(MAX_NUM) if is_prime[i]]
