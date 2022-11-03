import numpy

# creating an empty list
nos = []
  
# number of elements as input
n = int(input("Enter number of elements : "))
  
# iterating till the range
for i in range(0, n):
    ele = int(input())
  
    nos.append(ele) # adding the element
      
print("Statics are - ", nos)

mean = numpy.mean(nos)
median = numpy.median(nos)
variance = numpy.var(nos)
sd = numpy.std(nos)
cv = ((sd/mean)*100)


print("Mean - ", mean)
print("Median - ", median)
print("Variance - ", variance)
print("Standard Deviation - ", sd)
print("Coefficient - ", cv)

input('Press Enter To Exit')

