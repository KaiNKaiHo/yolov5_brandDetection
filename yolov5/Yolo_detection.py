import numpy as np
# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Numpy array

newHeight = np.array(height)
newWeight = np.array(weight)

dot = np.dot(newHeight, newWeight)
point = newHeight * newWeight

sum = sum(point)

print(dot)
print(sum)
newWeight *=  2.2

print(newWeight)

