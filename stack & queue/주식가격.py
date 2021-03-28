Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from collections import deque
>>> def solution(prices):
	answer=[]
	prices = depue(prices)
	while prices:
		c = prices.popleft()

		count = 0
		for i in prices:
			if c > i:
				count += 1
				break
			count += 1
		answer.append(count)
	return answer
