import numpy as np

a = np.array([[1, 2, 3], [7, 8, 9]])
print(a)

# How to get the number of dimension of the array
print(a.ndim)

# How to get the shape (rows and columns of the array)
print(a.shape)

# How to get the data type of the array
# and also how to specify the type when we create a brand new array
print(a.dtype)
b = np.array([[1, 2, 3], [7, 8, 9]], dtype="int16")
print(b)
print(b.dtype)

# How to get specific elements from an array [r, c]
c = np.array([[1, 2, 3, 4, 5], [7, 8, 9, 10, 11]])
print(c[0, :]) #How to get the first row
print(c[ : ,0]) #How to get the first column

c[0,3] = 50 #Hpw to change a specific element within an array
print(c)

d = np.array([[[1, 2, 3, 4, 5], [7, 8, 9, 10, 11]], #How to get elements into a 3d array
             [[12, 13, 14, 15, 16], [17, 18, 19, 20, 21]]])
print(d)
print(d[1, : ,2])

#How to initialize an array

zero = np.zeros((5,4,3))
print(zero)

one = np.ones((2,2,3))
print(one)

eye = np.eye(4) #A matrix whose diagonal is made of 1s
print(eye)

full = np.full((2,3), 99)
print(full)

full_like = np.full_like(d, 5) #How to initialize a matrix based on the shape of a previous one
print(full_like)

random = np.random.rand(2,3) #How to initialize an array with random numbers between 0 and 1
print(random)

randint = np.random.randint(7, size=(4,5)) #how to initialize an array with random numbers
print(randint)

exe = np.ones((5,5))
exe[1, 1:4]=0
exe[3, 1:4]=0
exe[2, 1:4]=0
exe[2,2]=9
print(exe)

#How to copy an array
z = np.array([[1,2,3], [4, 5, 6]])
print(z)
s = z.copy()
print(s)

#Operations with arrays

aa = np.array([[1, 2, 3], [4, 5, 6]])
bb = np.array([[1, 2, 3], [4, 5, 6]])

print(aa +bb)
print(aa * bb)
print(aa / bb)

#cc = np.matmul(aa, bb)

#Statistic with numpy

print(np.max(aa))
print(np.min(aa))
print(np.sum(aa, axis=0))

#How to mess with the shape of an array

before = np.array([[1, 2, 3], [4, 5, 6]])
before_1 = np.array([[1, 2, 3], [4, 5, 6]])
after = before.reshape(6,1) #when you get an error is because there is a mismatch between the before and the after
print(after)

stack = np.vstack([before, before_1])
ostack = np.hstack([before, before_1])
print(stack)
print(ostack)

new_type = before.astype(float)
print(new_type)

#Boolean masking

new = np.random.randint(10, 1000, size=(2,8))
print(new)
print(new[new > 500])
new_1 = np.any(new >500, axis=0)
print(new_1)

last = np.arange(5,1500,2)
print(last)










