Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from itertools import permutations
>>> def is_prime(n):
	if n<2:
		return False
	for i in range(2, n):
		if n%i==0:
			return False
	return True

>>> def solution(numbers):
	answer=set()
	for i in range(1, len(numbers)+1):
		n_list = list(''.join(tup) for tup in permutations(numbers, i))
		for n in n_list(int(n)):
			if is_prime(int(n)):
				answer.add(int(n))
	return len(answer)
