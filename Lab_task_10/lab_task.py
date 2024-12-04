import numpy as np

score = [85, 90, 78, 92, 88]
scores = np.array(score)
print(scores)
new = scores.astype(float)
print(new.dtype)

score2 = scores.copy()
score2 = score2 + 5
print(score2)

x = np.where(scores > 85)
print(x)
print()

print(scores.shape)
print(scores.ndim)
print(scores.size)
print(scores.itemsize)
print(scores.dtype)
print(np.sort(scores))
print(scores.max())
print(scores.min())
print(scores.sum())
print(scores.mean())

print(scores[::2])
print(scores[-3:-1])
print(scores[1:4])