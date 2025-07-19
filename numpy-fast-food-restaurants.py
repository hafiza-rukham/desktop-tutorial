import numpy as np
latitude,longitude,postalCode = np.genfromtxt('FastFoodRestaurants.csv', delimiter=',', usecols=(4,5,7), unpack=True, dtype=None,skip_header=1,invalid_raise= False)

print(latitude)
print(longitude)
print(postalCode)

print(np.mean(postalCode))
