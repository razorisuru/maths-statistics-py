import numpy

# creating an empty list
nos = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    nos.append(ele) # adding the element
      
print("Numbers are - ", nos)

mean = numpy.mean(nos)
median = numpy.median(nos)
variance = numpy.var(nos)
sd = numpy.std(nos)
cv = ((sd/mean)*100)

#converting ints to floats (2f)

variancef = f'{variance:.2f}'
cvf = f'{cv:.2f}'
sdf = f'{sd:.2f}'


print("Mean               - ", mean)
print("Median             - ", median)
print("Variance           - ", variancef)
print("Standard Deviation - ", sdf)
print("Coefficient        - ", cvf,'%')

input('Press Enter To Exit')

