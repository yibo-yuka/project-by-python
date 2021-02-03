import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x+y)
print(np.add(x,y))
print(x + 10)

print(x - y)
print(np.subtract(x, y))
print(x - [1,2])

print(x * y)
print(np.multiply(x, y))

print(x / y)
print(np.divide(x, y))

print(x**2)
print(np.sqrt(x))

print(x.dot(y))        #[1*5+2*7=19 1*6+2*8=22][3*5+4*7=43 3*6+4*8=50] 
print(np.dot(x, y))    #[跟以上一樣,真的矩陣乘法]