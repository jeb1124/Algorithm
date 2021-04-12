Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def sol(bridge_length, weight, truck_weights):
	time = 0
	q = [0] * bridge_length
	
	while q:
	time += 1
	q.pop(0)
	if truck_weights:
		if sum(q) + truck_weights[0] <= weight:
			q.append(truck_weights.pop(0))
		else:
			q.append(0)
	return time
