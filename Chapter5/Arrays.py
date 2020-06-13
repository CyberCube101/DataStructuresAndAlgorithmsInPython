import sys
from array import array

list_primes = [2, 3, 5, 7, 11, 13, 17, 19]

print("The number of bytes required is {}".format(sys.getsizeof(list_primes)))

array_primes = array('i', [2, 3, 5, 7, 11, 13, 17, 19])
print("The number of bytes required is {}".format(sys.getsizeof('')))


