import numpy as np

price, size = np.genfromtxt(r"C:\Users\Rukham Ijaz\Downloads\Documents\GitHub\desktop-tutorial\RealEstate-USA.csv", delimiter=',',usecols=(2, 10), unpack=True,dtype=None,skip_header=1,invalid_raise=False)

print(size)
print(price)

#Statistic operation
print("price mean:",np.mean(price))
print("price average:",np.average(price))
print("price median:",np.median(price))
print("price max:",np.max(price))
print("price min:",np.min(price))

#Math operation
print("price square:",np.square(price))
print("price sqrt:",np.sqrt(price))
print("price power:",np.power(price,price))
print("price abs:",np.abs(price))

#perform basic arrithmatic operations
addition = price + size
subtraction = price - size
multiplication = price * size
division = price / size

print("calculate addition:,",addition)
print("calculate subtraction:",subtraction)
print("calculate multiplication:",multiplication)
print("calculate division:",division)

#Trignometric function
pricePie = (price/np.pi) +1
sin_values = np.sin(pricePie)
cosine_values = np.cos(pricePie)
tangent_values = np.tan(pricePie)

print("price -div -pie - sin values:",sin_values)
print("price - div - pie - cosine values:", cosine_values)
print("price - div - pie - tangent values:",tangent_values)

#calculate the natural logarithm and base_10 logarithm
log_array = np.log(pricePie)
log10_array = np.log10(pricePie)

print("price - div - pie - natural logarithm values:",log_array)
print("price - div - pie - base 10 logarithm values:",log10_array)

# Calculate the hyperbolic sine of each element
sinh_values = np.sinh(pricePie)
print("price - div - pie - hyperbolic sine :",sinh_values)

# Calculate the hyperbolic cosh() of each element
cosh_values = np.cosh(pricePie)
print("price - div - pie - hyperbolic cosine values:",cosh_values)

#calculate the hyperbolic tangent of each element
tanh_values = np.tanh(pricePie)
print("price - div - pie - hyperbolic tangent values:",tanh_values)

#calculate the inverse hyperbolic sine of each element
asinh_values = np.arcsinh(pricePie)
print("price - div - pie - inverse hyperbolic sine values:",asinh_values)

#calculate the inverse hyperbolic cosine of each element
acosh_values = np.arccosh(pricePie)
print("price - div - pie - inverse hyperbolic cosine values:",acosh_values)

#2 dimension array
D2sizeprice = np.array([size,price])
print("price plus size - 2 dimension array:",D2sizeprice)
print("price plus size - 2 dimension array- dimension:",D2sizeprice.ndim)
print("price plus size - 2 dimension array-total number of element:",D2sizeprice.size)
print("price plus size - 2 dimension array -give siza of array in each dimension:",D2sizeprice.shape)
print("price plus size - 2 dimension array - data type:",D2sizeprice.dtype)

#Slicing array
D2sizepriceslice = D2sizeprice[0:5:1]
print(D2sizepriceslice)

#indexing array
D2sizepricesliceitemonly = D2sizeprice[0:3]
print(D2sizepricesliceitemonly)

#if you don't need index values
for elem in np.nditer(D2sizeprice):
    print(elem)

#if you need index
for index, elem in np.ndenumerate(D2sizeprice):
    print(index,elem)