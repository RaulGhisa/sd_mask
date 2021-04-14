import numpy as np

a = np.load("train_indices.npy")
b = np.load("test_indices.npy")

print(a[100:200])
print(b[100:200])
