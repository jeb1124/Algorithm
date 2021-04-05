Python 3.6.1 (v3.6.1:69c0db5, Mar 21 2017, 17:54:52) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def solution(answers):
	a1=[1,2,3,4,5]
	a2=[2,1,2,3,2,4,2,5]
	a3=[3,3,1,1,2,2,4,4,5,5]
	first=0
	second=0
	third=0
	for number in range(len(answers)):
		if answers[number]==a1[number%5]:
			first+=1
		if answers[number]==a2[number%8]:
			second+=1
		if answers[number]==a3[number%10]:
			third+=1
	top_answer=[first,second,third]
	for person,score in enumerate(top_answer):
		if score==max(top_answer):
			answer.append(person+1)
	return answer
