# Problem 50

from os import sys, path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from common import *

primes = list(primesLessThan(1000000))
len_primes = len(primes)

longest_sum = 0
prime = 0

for i in range(len_primes, 1, -1):

    current_prime = primes[i-1]
    
    primes_less = primes[0:(i-1)]
    len_primes_less = len(primes_less)

    longest_sum_temp = 0

    current_start = 0
    while current_start < (len_primes_less - 1):
        
        len_current_sum = 0
        current_sum = 0
        current_i = current_start
        
        while current_sum < current_prime:
            current_sum += primes_less[current_i]
            current_i += 1
            len_current_sum += 1
        
        if current_sum == current_prime:
            if len_current_sum > longest_sum_temp:
                longest_sum_temp = len_current_sum
        
        current_start += 1

    if longest_sum_temp > longest_sum:
        longest_sum = longest_sum_temp
        prime = current_prime

print prime, longest_sum
