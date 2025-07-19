import numpy as np
price, house, size = np.genfromtxt("RealEstate-USA(1).csv", delimiter= ',',usecols=(2,6,10), unpack=True,dtype=None,skip_header=1)

print(price)
print(house)
print(size)

print(np.mean(price))