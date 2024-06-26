import numpy as np

def sigmoid(x):
    return 1 / (1+np.exp(-x))

x = np.random.randn(10,2) # 2차원 데이터 10개가 미니배치로 처리
W1 = np.random.randn(2,4)
b1 = np.random.randn(4)
W2 = np.random.randn(4,3)
b2 = np.random.randn(3)

h = np.matmul(x,W1) + b1
a = sigmoid(h)
s = np.matmul(a,W2) + b2 # 출력은 3차원 데이터 10개