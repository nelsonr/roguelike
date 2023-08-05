import numpy as np


# arr_2d = np.array(((1, 2, 3), (4, 5, 6), (7, 8, 9)))
# slice_2d = (slice(0, 2), slice(0, 2))

# print(arr_2d, end="\n\n")

# print(arr_2d[slice_2d], end="\n\n")

# arr_2d[slice_2d] = 5

# print(arr_2d[slice_2d], end="\n\n")
# print(arr_2d)

# hello = "Hello World"
# hello_chars = [c for c in hello]

# print(hello_chars)

coordinate_pairs = (
    (10, 20),
    (30, 10),
    (8, 20)
)

coordinates_check = [pair == (10, 20) for pair in coordinate_pairs]

print(coordinates_check)
print(any(coordinates_check))
