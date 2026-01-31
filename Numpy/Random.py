import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(<value>) is used to store the random values permanently without changing everytime
np.random.seed(10)

# np.random.rand(size of array) used to generate the random values and generates the array of values in float
print(np.random.rand(5))

# np.random.randint(low(default = 0),high(must mention),size) used to generate array of random values in int
print(np.random.randint(10))

# Normal Distribution -> np.random.normal(loc(average),scale(standard deviation),size of array)
print(np.random.normal(loc=50,scale=10,size=10))

# Uniform Distribution -> np.random.uniform(low,high,size)
print(np.random.uniform(5,15,5))

# MATPLOT
data = np.random.normal(loc=50,scale=10,size=1000)
plt.hist(data,bins=30,density=True,alpha=0.6,color='b')
plt.xlabel("value")
plt.ylabel("frequency")
plt.title("Normal Distribution Mean=50, STD=10, SAMPLE=1000")
plt.show()