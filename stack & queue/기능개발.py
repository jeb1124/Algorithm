Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def solution(progress, speed):
	answer=[]
	day=0
	count=0
	while len(progress)!=0:
		if progress[0]+day*speed[0]>=100:
			progress.pop(0)
			speed.pop(0)
			count+=1
		else:
			if count>0:
				answer.append(count)
				count=0
				day+=1
	answer.append(count)
	return answer

>>> 
