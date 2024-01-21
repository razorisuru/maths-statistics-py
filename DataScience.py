import numpy

# creating an empty list
nos = [78,74,82,66,94,71,64,88,55,80,91,74,82,75,96,78,84,79,71,83]
    
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

