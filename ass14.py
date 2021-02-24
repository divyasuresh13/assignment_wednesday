list1=[1,2,3,4]
list2=[10,20,30,40]
for x,y in zip(list1,list2[::-1]):
	print(x,y)