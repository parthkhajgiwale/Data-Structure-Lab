marks=[]
print("Fundamentals of Data Structures Marks")
n=int(input("Enter No. Of Students: "))

def read():
	for i in range(0,n):
		num=int(input("Enter Marks:"))
		marks.append(num)
def display():
	print(marks)
def main():
	read()
	display()
def avg():
	sum=0
	present=0
	for  i in range(0,n):
		if(marks[i]>=0):
			sum+=marks[i]
			present+=1
	avg=sum/present
	print("Average Marks of Class: ",avg)
	print("Absent Students: ",n-present)
def max_score():
	max=0
	for i in range(0,n):
		if((marks[i]>=0) and (marks[i]>max)):
			max=marks[i]
	print("Maximum Mark : ",max)
def min_score():
	min_score=[]
	for i in marks:
		if(i>=0):
			min_score.append(i)
	print("Minimum Mark : ", min(min_score))
def frequent_score():
	max=0
	hf_value=0
	for i in marks:
		frequency=marks.count(i)
		if frequency>max and i>=0:
			max=frequency
			hf_value=i
	print("Mark with Highest Frequency: ",hf_value )


main()
avg()
max_score()
min_score()
frequent_score()
