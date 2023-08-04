import numpy as np


arr_2d = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
slice_2d = (slice(0, 2), slice(0, 2))

print(arr_2d, end="\n\n")

print(arr_2d[slice_2d], end="\n\n")

arr_2d[slice_2d] = 5

print(arr_2d[slice_2d], end="\n\n")
print(arr_2d)
