import numpy as np
x = np.array([1,2,3])
print(x.__class__)

print(x.shape)
print(x.ndim)

W = np.array([[1,2,3],[4,5,6]])
print(W.shape)
print(W.ndim)

W = np.array([[1,2,3],[4,5,6]])
X = np.array([[0,1,2],[3,4,5]])
print(W+X)
print(W*X)

# 벡터의 내적 
a = np.array([1,2,3])
b = np.array([4,5,6])
print(np.dot(a,b))

# 행렬의 곱
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(np.matmul(A,B))
